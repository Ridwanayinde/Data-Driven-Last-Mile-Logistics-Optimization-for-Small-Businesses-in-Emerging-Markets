# 📦 Milestone 2: Data Preparation

Project Title: Optimal Delivery Routing in Lagos

## 📝 1. Overview

The goal of this milestone is to prepare the geospatial data required for analyzing optimal delivery routes in Lagos. The raw datasets include administrative boundaries, road networks, buildings, and points of interest (POIs).

This step ensures the datasets are valid, consistent, and ready for network analysis in later milestones.

## 📂 2. Dataset Description

The raw datasets are stored in a GeoPackage (../1_dataset/raw/processed/lagos_data.gpkg):

| 🗂️ Layer Name | 📖 Description
|-------|--------
|lagos_boundaryshp__nga_admbnda_adm2_osgof_20170222 | Administrative boundary of Lagos at the LGA level
|roads_lagos| Road network including highways, streets, and minor roads
| buildings_lagos | Building footprints in Lagos
|pois_lagos | Points of interest (markets, schools, hospitals, etc.)
| buildings_clean | Cleaned and validated buildings layer
| roads_clean | Cleaned and simplified road network
| pois_clean | Cleaned POIs layer

## 🧹 3. Data Cleaning Steps

1. 📥 Loading Layers

- Layers loaded using GeoPandas (read_file)
- Inspected geometries and attributes  

2. ✅ Geometry Validation

- Checked geometry.is_valid

- Repaired invalid geometries with shapely.make_valid
 
3. 🔧 Column Selection

- Kept only relevant columns for routing:

  - Roads: geometry, highway
  - Buildings: geometry
  - POIs: geometry, type

4. 🌍 CRS Transformation

- Reprojected all layers to metric CRS (EPSG:4326) for accurate distance calculations.

5. 💾 Saving Clean Layers

- Exported cleaned datasets to a new GeoPackage for routing analysis

## 🌍 CRS Transformation

Reprojected all layers to metric CRS (EPSG:4326) for accurate distance calculations

- `validate_geometry.py` — checks for invalid geometries.  
- `generate_synthetic_points.py` — script to generate synthetic delivery points (to be used in Milestone 3).

**Example usage:**

```bash
python generate_synthetic_points.py --boundary ../1_dataset/raw/processed/lagos_dat.gpkg \
                                    --output data/processed/delivery_points.gpkg
