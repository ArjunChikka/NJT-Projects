# config/config_template.py
#
# Copy this file to config.py and fill in your own values.

import os

# ─── DATA PATHS ───────────────────────────────────────────────────────────────

# Root data directory
DATA_DIR = os.path.join(os.getcwd(), "data")

# Raw GTFS directory
RAW_GTFS_DIR = os.path.join(DATA_DIR, "raw GTFS data")

# Ridership source file
RIDERSHIP_XLSX = os.path.join(DATA_DIR, "NJT 2019 Ridership.xlsx")

# GIS directory (for shapefiles, etc.)
GIS_DIR = os.path.join(DATA_DIR, "gis")
SHAPEFILE_PATH = os.path.join(GIS_DIR, "NJT_stations.shp")

# ─── SCRIPTS & NOTEBOOKS ───────────────────────────────────────────────────────

NOTEBOOKS_DIR = os.path.join(os.getcwd(), "notebooks")
SCRIPTS_DIR   = os.path.join(os.getcwd(), "scripts")

# ─── API KEYS ──────────────────────────────────────────────────────────────────

# Google Maps Directions API
GMAPS_API_KEY = "<YOUR_GOOGLE_MAPS_API_KEY>"

# Census API
CENSUS_API_KEY = "<YOUR_CENSUS_API_KEY>"

# Google Custom Search Engine (for station URL scraping)
GOOGLE_CSE_ID  = "<YOUR_GOOGLE_CSE_ID>"

# Open Service Route API key
OPEN_SERVICE_ROUTE_KEY = "<YOUR_OPEN_SERVICE_ROUTE_KEY>"
