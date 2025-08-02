# NJ Transit Ridership Modeling

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

**Author:** Arjun Chikkappa 
**Date:** 2025-07-31  

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/njt-ridership-model.git
   cd njt-ridership-model
   ```
2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate       # On macOS/Linux
   .\venv\Scripts\activate      # On Windows
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Set your API keys** as environment variables or in a `.env` file:
   ```bash
   export GOOGLE_API_KEY="your_google_api_key"
   export CENSUS_API_KEY="your_census_api_key"
   ```
2. **Place raw data files** in the `data/` directory:
   - `NJT 2019 Ridership.xlsx`
   - `stops.txt`
   - `stop_times.txt`
3. **Launch the notebooks** in sequence:
   ```bash
   jupyter lab notebooks/01_Stop_Data.ipynb
   jupyter lab notebooks/02_Isochrones_IntersectingData
   jupyter lab notebooks/03_Modeling.ipynb
   ```
   Or run the consolidated overview in `notebooks/Ridership_Modeling.ipynb`.

---

## Project Structure

```
NJT-Projects/
├── config/                            ← new
│   └── config_template.py
│
├── data/
│   ├── raw GTFS data/
│   │   ├── agency.txt
│   │   ├── calendar_dates.txt
│   │   ├── routes.txt
│   │   ├── shapes.txt
│   │   ├── stop_times.txt
│   │   ├── stops.txt
│   │   └── trips.txt
│   │
│   ├── Full_Station_Data.csv
│   ├── NJT 2019 Ridership.xlsx
│   └── Station_Characteristics_Final.csv
│
│   └── gis/                          ← new
│       ├── NJT_stations.shp
│       ├── NJT_stations.shx
│       ├── NJT_stations.dbf
│       ├── NJT_stations.prj
│       └── NJT_stations.qgz
│
├── notebooks/
│   ├── 01_Stop_Data.ipynb
│   └── 02_Isochrones_IntersectingData.ipynb
│
├── scripts/
│   └── census_data.py
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## Project Overview

This project builds a station-level ridership model for New Jersey Transit (NJT) by combining:

1. **Operational Data**  
   - **2019 weekday boardings** (`NJT 2019 Ridership.xlsx`, Sheet 2, cols B–E)  
   - **Service frequency/timepoint details** (`stop_times.txt`)  

2. **Geospatial & Amenity Features**  
   - **Station coordinates** ('stops.txt')  
   - **Parking capacity & WalkScore** (scraped in `Stop_Data.ipynb`)  
   - **Distance & transit travel times** to New York Penn (computed in `Stop_Data.ipynb`)  
   - **Walking & driving isochrones** (generated in `IsoChrones.ipynb`)  

3. **Demographic Enrichment**  
   - **U.S. Census ACS 5-year (2020)** block-group data via `scripts/census_data.py`  
   - **Socioeconomic metrics:** income, education, age  
   - **Transit-mode metrics:** public transit share, labor force participation  

4. **Modeling & Analysis**  
   - **Exploratory visualizations**  
   - **Regression models** to explain and predict ridership  

---

> **Tip:** Run each notebook in sequence (or import their outputs as DataFrames), and adjust file paths, API keys, or environment settings as needed.

---

## Contributing

1. Fork the repository  
2. Create your feature branch (`git checkout -b feature/foo`)  
3. Commit your changes (`git commit -am "Add foo"`)  
4. Push to the branch (`git push origin feature/foo`)  
5. Open a Pull Request  

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
