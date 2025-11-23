# 🚀 Data-Driven Last-Mile Logistics Optimization for Small Businesses in Emerging Markets

## 📌  Overview
  
This project explores how data engineering, predictive analytics, and intelligent dispatching
can dramatically improve last-mile delivery performance for small and medium-sized businesses
(SMEs) operating in emerging markets.

Using synthetic data, machine learning models, and algorithmic rider assignment, the system
demonstrates how technology can help reduce delivery delays, optimise routing decisions, and
improve customer experience in challenging logistics environments.

This project is developed as part of the MIT Emerging Talent Program, Milestone 1–5.

## 🧩 Motivation

During my undergraduate years, I founded Tomori Foods, a small food business serving customers in
Akure, Ondo State.

Our biggest challenge was not the food — it was logistics.

Every day we dealt with:

- Rider shortages

- Late deliveries

- Traffic uncertainties

- Drivers ignoring instructions or customer locations

- Customer complaints

- Loss of repeat customers due to inconsistent delivery performance

Recently, my Amir made a statement that perfectly captured the problem:

“Most Nigerian drivers are a menace to small-scale businesses.
Without wisdom and extraordinary endurance, a manager can lose customers and watch the business collapse.”

This project is inspired by that lived reality.

Small businesses in emerging markets suffer from unpredictable human factors, limited infrastructure,
and inefficient last-mile delivery processes.

This project attempts to address these issues through data-driven logistics intelligence.

## 🧠 Problem Statement

Small businesses in emerging markets rely heavily on riders/drivers for product delivery.

However:

- Delivery times are highly unpredictable

- Human behaviour introduces delays

- Routing decisions are made without data

- Customer satisfaction depends on the weakest link — the rider

- Managers lack tools to monitor performance or allocate riders efficiently

There is a need for a scalable, automated, predictive, and intelligent delivery management system.

## 🎯 Project Objectives

The project aims to:

  1. Generate synthetic customer orders and delivery events

  2. Predict demand zones and order surges

  3. Estimate delivery times using ML models

  4. Implement an intelligent rider assignment algorithm

  5. Analyze operational KPIs (delays, peak hours, zone traffic)

  6. Provide a foundation for a real-time dashboard

  7. Document insights using MIT milestone workflows

## System Architecture

Below is the high-level architecture of the platform:
![System Architecture](./documentation/guide/assets/system_architecture.png)

## Data Architecture

![Data Architecture](./documentation/guide/assets/data_architecture.png)

## 🔍 Features

✔ 1. **Synthetic Order Generation**

Creates realistic customer orders with:

- timestamps

- pickup and drop-off zones

- order type

- simulated delivery conditions
  
✔ 2. **Demand Zone Prediction**

- Identifies high-demand zones using:

- clustering

- historical patterns

- peak-hour analysis

✔ 3. **Delivery Time Prediction (ML Model)**

A machine learning model predicts:

- expected delivery time

- risk of delay

- zone-based arrival estimation

✔ 4. **Intelligent Rider Assignment**

- A rule-based (later ML-based) system that:

- selects the optimal rider

- balances workload

- reduces overall delay

- considers predicted travel time

✔ 5. **KPI Analysis (Dashboard Coming Soon)**

- Metrics include:

- average delivery time

- delay frequency

- peak demand windows

- rider utilization

## 🧱  Tech Stack

- Python

- Pandas, NumPy

- scikit-learn

- OpenStreetMap (OSM) data

- Matplotlib/Plotly

- Jupyter Notebook

- draw.io (architecture)

## 🧪 How to Run the Project

```bash
git clone https://github.com/Ridwanayinde/Data-Driven-Last-Mile-Logistics-Optimization-for-Small-Businesses-in-Emerging-Markets.git

cd Data-Driven-Last-Mile-Logistics-Optimization-for-Small-Businesses-in-Emerging-Markets

pip install -r requirements.txt

```

Run data generation:

```bash
 python generate_orders.py
```

Train ML model:

```bash

python train_model.py
```

Run rider assignment:

``` bash

python assign_riders.py

```

📁 Project Structure

```css

├── 0_domain_study/
├── 1_domain_study/
├── 1_dataset/
├── 2_data_preparation/
├── 3_data_exploration/
├── 4_data_analysis/
├── 5_communication_strategy/
│── 6_final_presentation/
│── documentation/
│   ├── guide/
├── README.md
└── retrospective.md (for MIT milestones)

```

## 📌 MIT Emerging Talent Workflow

- Project Structure

Milestone 0 - Project Structure

Milestone 1 (Problem Identification)

- Motivation
- Real-world problem
- Business context

Milestone 2 (Data Collection)

- Synthetic orders
- OSM data
- Rider data

Milestone 3 (Data Analysis)

- ML predictions
- Rider assignment
- KPI evaluation

Milestone 4 (Communicating Results)

- Public artefact (infographic/video/blog)

Milestone 5 (Final Presentation)

- Slide deck or showcase
- Retrospective reflections

## 🔮 Future Work

- Real-time dashboard with Streamlit

- Geospatial routing (OSRM, Mapbox, or GraphHopper)

- Neural network for delivery time prediction

- Reinforcement learning for rider dispatching

- Integration with mobile delivery apps

- Multi-objective optimization (distance vs time vs cost)