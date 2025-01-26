## Weather Impact Analysis on Formula 1 Driver Performance
This repository contains the work completed for the **"Weather Impact Analysis on Formula 1 Driver Performance"** project, conducted as part of the **UC Berkeley MIDS W200: Python for Data Science** course in Fall 2023.

### Overview
- Data Sources:
    - Ergast API: Provides comprehensive Formula 1 race and performance data.
    - Open-Meteo API: Supplies historical weather data for race locations.
- Analysis Questions:
    1. How do abnormal weather conditions affect driver standings at the end of races?
    2. Are specific drivers more prone to not finishing (DNF) in certain weather conditions?
    3. What patterns emerge in driver performance under various weather conditions?
- Results:
    - Detailed insights into how drivers and teams perform in abnormal vs. normal conditions.
    - Identification of drivers who excel in specific conditions (e.g., wet or hot races).
    - Analysis of team-level DNF trends across weather types.

### Project Structure
This repository contains six folders with detailed work, including data preprocessing, exploratory analysis, and results presentation. Below is a high-level breakdown of the project structure:

1. Data Preparation:
    - Preprocessing and merging of weather and race datasets.
    - Definition of "abnormal weather conditions" (e.g., high wind speeds, extreme temperatures).
2. Exploratory Data Analysis (EDA):
    - Insights into driver position changes and DNF rates.
    - Comparison of performances across teams and weather conditions.
3. Visualization:
    - Box plots, heatmaps, and bar charts highlighting key findings.
4. Conclusions:
    - Abnormal weather increases the DNF rate by 1%.
    - Drivers like Lewis Hamilton consistently perform well across weather conditions, while others (e.g., Kevin Magnussen) face higher challenges

### Tools and Technologies
- Python Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn
- APIs:
    - [Ergast Developer API](https://ergast.com/mrd/)
        - **NOTE:** The Ergast API is deprecated and will be removed in early 2025. The current drop-in replacement is called [Jolpica](https://github.com/jolpica/jolpica-f1).
    - [Open-Meteo API](https://open-meteo.com/)
- Collaboration: GitHub for version control

### Authors
- Gia Nguyen
- Cat Weiss
- Akin Akinlabi