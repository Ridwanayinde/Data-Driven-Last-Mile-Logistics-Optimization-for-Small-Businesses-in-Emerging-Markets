# 🚀 Milestone 3 — Exploratory Data Analysis (EDA)

## 🧭 1. Project Overview

Small businesses in emerging markets often struggle with high delivery costs, long delays, and inefficient dispatch routing. These challenges are intensified by:

- Limited road infrastructure
- Dense, irregular urban layouts
- Unmapped informal areas
- Unpredictable demand patterns

This project aims to build a **data-driven geospatial framework** for optimizing last-mile logistics.

Using POIs, road networks, and clustering techniques, we analyze:

- Where demand is concentrated (hotspots)

- How POIs naturally form delivery zones

- How riders can be assigned to zones to minimize travel time and cost

This milestone (Milestone 3) focuses on **Exploratory Data Analysis (EDA)** — cleaning the data, visualizing it, identifying demand zones, and understanding spatial patterns relevant to routing optimization.

## 🗂️ 2. Dataset Description

📍 Spatial Layers Used

| Layer | Description |
|-------|-------------|
| 🗺️ **Boundary** | Administrative polygon defining the study area |
| 🚗 **Road Network** | Streets and paths used for routing and connectivity analysis |
| 🏘️ **Buildings** | Structural footprints within the region |
| 📌 **POIs (Points of Interest)** | Markets, schools, restaurants, shops, religious centers, and other key activity locations |

📊 Data Source

Extracted from OpenStreetMap (OSM) through the Overpass API.

Processed using GeoPandas, Shapely, Fiona, and Matplotlib.

## 🧹 3. Data Cleaning & Validation

Each spatial layer was validated to ensure geometries were usable for analysis and routing.

🔧 Key Cleaning Steps

- Check for missing geometries

- Remove nulls

- Fix invalid geometries using buffer(0)

- Standardize Coordinate Reference System (CRS)

- Repair self-intersections, spikes, overlaps

- Ensure polygons and lines conform to expected types

📐 CRS Standardization

All layers were projected to a local metric CRS (EPSG:3857) to support:

- Distance calculations

- Heatmaps

- Clustering

- Routing

## 🗺️ 4. Exploratory Data Analysis (EDA)

🧲 4.1 Boundary Visualization

Shows the overall shape and spatial context for routing.

🛣️ 4.2 Road Network Visualization

Important for:

- Identifying connectivity

- Understanding travel constraints

- Preparing for shortest-path algorithms

📌 4.3 POI Distribution Map

- Initial inspection of POIs shows:

- Dense clusters at commercial centers

- Spread-out residential or institutional POIs

- Hotspots that may require more riders

## 🔥 5. Heatmap Analysis (Demand Hotspots)

Heatmaps were used to understand where POIs are concentrated.
The colored regions (not the dots) indicate demand intensity.

**🔥 Interpretation:**

- Red = **High POI density → high demand zones**

- Light red = **Low POI density**

This helps identify:

- Business clusters

- Market centers

- High-traffic delivery areas

- Regions needing prioritized routing or more riders

Heatmaps provide a strong foundation for understanding **demand-driven logistics.**

## 🎯 6. Clustering Analysis (Delivery Zones)

KMeans clustering was applied to POI coordinates to create natural delivery zones.

**📌 Why clustering?**

- Riders stay **within a zone** instead of moving across town.

- Reduces travel distance and cost.

- Reduces delays.

- Helps balance workload between riders.

- Simplifies route optimization (TSP/VRP).

**🧠 How to interpret cluster labels (0–4):**

They represent **geographical regions**, not POI categories.

Example:

- Cluster 0 = area with many POIs in one neighborhood

- Cluster 1 = educational zone

- Cluster 2 = market zone

etc.

**🏷️ Optional (future step):**

Cluster labels can be automatically renamed using **dominant POI categories,** such as:

“Market Zone”

“Residential Zone”

“Recreation Zone”