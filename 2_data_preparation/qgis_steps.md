# 🗺️ QGIS Steps for Data Preparation

This document describes the steps taken in QGIS to prepare spatial data
for the Lagos Last-Mile Delivery Project.

## 1. 📂 Load Raw Data

- Loaded Lagos boundary shapefile/GeoPackage.

- Loaded raw OSM datasets: Roads, Buildings, POIs.

## 2. 🌐 Check CRS

- Ensured all layers are in the same CRS (EPSG:4326 or projected CRS for Lagos).

## 3. ✂️ Clip Layers to Lagos Boundary

- Used **Vector → Geoprocessing Tools → Clip**.

- Input layers clipped: Buildings, Roads, POIs.

- Clipping polygon: Lagos boundary layer.

- Saved outputs to `data/processed/` folder in GeoPackage format.

## 4. 🧹 Clean Layers

- Verified geometries were valid (no null geometries).

- Removed unnecessary attributes if needed (optional).

## 5. 💾 Save Processed Data

- All clipped layers (Buildings, Roads, POIs, and Boundary) were saved together in a single GeoPackage:

  - `1_dataset/raw/processed/lagos_data.gpkg`

**Note:** This file contains all processed layers and is ready for further analysis, including synthetic delivery point generation and routing experiments.
