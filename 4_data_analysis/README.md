# 🗺️ Last-Mile Delivery Routing Project

This repository contains a workflow for **planning and visualizing last-mile delivery routes** using geospatial data, clustering, and routing algorithms. The project is organized into several steps, from building the road network graph to clustering Points of Interest (POIs) into delivery zones.

---

## 📂 Project Structure

1. **01_build_graph.ipynb**  
   - Builds the road network graph from OpenStreetMap or preprocessed data.  
   - Prepares a NetworkX graph that will be used for routing calculations.

2. **02_shortest_distance.ipynb**  
   - Computes shortest distances from each POI to relevant nodes in the road network.  
   - Prepares the data for efficient route generation.

3. **03_route_generation.ipynb**  
   - Generates delivery routes from starting points (centroids or hubs) to each POI.  
   - Visualizes routes on the map for initial inspection.

4. **04_clustering_and_zones.ipynb**  
   - Groups POIs into **delivery zones** using clustering techniques.  
   - Calculates **zone centroids** (central point of each cluster).  
   - Visualizes routes from centroids to POIs per zone with color-coded zones.  
   - Provides a visual map for easy inspection of zones, routes, and POIs.

---

## 🔜 Next Steps

- **05_evaluation.ipynb**  
  - Will evaluate the quality of the delivery zones and routes.  
  - Metrics may include total distance per zone, average distance from centroid to POIs, and zone compactness.  
  - Will help ensure zones are optimized for efficient last-mile delivery.

---

## 🖼️ Visualizations

- Maps showing routes from **zone centroids to POIs**.  
- Color-coded zones for easy inspection.  
- Zone centroids represented with stars (`*`).  
- Routes and POIs colored by zone for clarity.  

---

## ⚙️ Requirements

- Python 3.8+  
- Geospatial libraries: `geopandas`, `shapely`, `osmnx`  
- Network analysis: `networkx`  
- Visualization: `matplotlib`  
- Optional: `pyproj` for coordinate transformations

---

## 📌 Notes

- The workflow so far focuses on **building the graph, computing routes, and clustering POIs into delivery zones**.  
- Evaluation and further optimization (like vehicle routing or delivery scheduling) will be addressed in `05_evaluation.ipynb`.  

---

### 🏁 Summary

This project is a step-by-step pipeline for **last-mile delivery optimization**, starting from raw spatial data to **clustered delivery zones and visualized routes**. Future steps will focus on **evaluating and improving these delivery zones** for efficiency.
