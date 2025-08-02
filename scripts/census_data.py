import requests, pandas as pd
from config import CENSUS_API_KEY

# Function to get the list of counties in a state
def get_county_fips(state_fips):
    base_url = 'https://api.census.gov/data/2020/acs/acs5'
    params = {
        'get': 'NAME',
        'for': 'county:*',
        'in': f'state:{state_fips}',
        'key': CENSUS_API_KEY
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        counties = [row[2] for row in data[1:]]  # Extract the county FIPS codes (county FIPS code is the 3rd item in each row)
        return counties
    else:
        print(f"Error fetching counties: {response.status_code} - {response.text}")
        return []

# Function to get population, transportation, employment, income, education data, and employment density for all census block groups in New Jersey
def get_census_data(state_fips='34'):
    counties = get_county_fips(state_fips)
    all_data = []

    for county_fips in counties:
        print(f"Fetching data for county: {county_fips}")
        base_url = f'https://api.census.gov/data/2020/acs/acs5'

        # Define the parameters for the API request
        params = {
            'get': 'NAME,B01003_001E,B01002_001E,B08301_001E,B08301_010E,B19013_001E,B15003_001E,B15003_002E,B15003_017E,B15003_022E,B15003_025E,B23025_001E,B23025_002E,B23025_004E,B23025_005E',
            # B01003_001E: Total population
            # B01002_001E: Median age
            # B08301_001E: Total workers (commuters)
            # B08301_010E: Public transportation users
            # B19013_001E: Median household income
            # B15003_001E: Total population 25 years and over
            # B15003_002E: No schooling completed
            # B15003_017E: High school graduate (includes equivalency)
            # B15003_022E: Bachelor's degree
            # B15003_025E: Graduate or professional degree
            # B23025_001E: Population 16 years and over
            # B23025_002E: In labor force
            # B23025_004E: Employed
            # B23025_005E: Unemployed
            'for': 'block group:*',
            'in': f'state:{state_fips} county:{county_fips}',
            'key': CENSUS_API_KEY
        }

        # Make the request to the Census API
        response = requests.get(base_url, params=params)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            if len(data) > 1:
                all_data.extend(data[1:])  # Append the data excluding the header row
            else:
                print(f"No data found for county {county_fips}")
        else:
            print(f"Error fetching data for county {county_fips}: {response.status_code} - {response.text}")

    if all_data:
        # Convert the response data into a pandas DataFrame
        columns = ['NAME', 'Total_Population', 'Median_Age', 'Total_Workers', 'Public_Transit_Users',
                   'Median_Household_Income', 'Total_Pop_25_and_Over', 'No_Schooling_Completed',
                   'High_School_Graduate', 'Bachelors_Degree', 'Graduate_Professional_Degree',
                   'Population_16_and_Over', 'In_Labor_Force', 'Employed', 'Unemployed',
                   'state', 'county', 'tract', 'block group']
        df = pd.DataFrame(all_data, columns=columns)

        # Convert numeric columns to appropriate data types
        numeric_columns = ['Total_Population', 'Median_Age', 'Total_Workers', 'Public_Transit_Users',
                           'Median_Household_Income', 'Total_Pop_25_and_Over', 'No_Schooling_Completed',
                           'High_School_Graduate', 'Bachelors_Degree', 'Graduate_Professional_Degree',
                           'Population_16_and_Over', 'In_Labor_Force', 'Employed', 'Unemployed']
        df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

        # Add a full FIPS code column for easier merging with other datasets
        df['GEOID'] = (df['state'].astype(str) + df['county'].astype(str) + df['tract'].astype(str) + df['block group'].astype(str)).astype(str)

        # Calculate additional metrics
        df['Employment_Rate'] = (df['Employed'] / df['In_Labor_Force']) * 100
        df['Unemployment_Rate'] = (df['Unemployed'] / df['In_Labor_Force']) * 100
        df['Percent_Public_Transit_Users'] = (df['Public_Transit_Users'] / df['Total_Workers']) * 100
        df['Labor_Force_Participation_Rate'] = (df['In_Labor_Force'] / df['Population_16_and_Over']) * 100

        # Calculate employment density (Employed per square kilometer)
        # This assumes that you have an area field in square kilometers in the dataset
        if 'area_sq_km' in df.columns:
            df['Employment_Density'] = df['Employed'] / df['area_sq_km']
        else:
            print("Area in square kilometers is not available to calculate employment density.")

        return df
    else:
        print("No data was collected.")
        return None

# Fetch the census data for New Jersey census block groups
nj_census_data = get_census_data()

# Display the first few rows of the DataFrame
if nj_census_data is not None:
    print(nj_census_data.head())

nj_census_data['Percent_Bach_Degree'] = (nj_census_data['Bachelors_Degree']/nj_census_data['Total_Pop_25_and_Over'])*100
nj_census_data = nj_census_data.loc[:, ~nj_census_data.columns.str.contains('^Unnamed')]

nj_census_data.to_csv("nj_census_data.csv",index=False)