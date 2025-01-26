## Honey, I Shrunk the Nuclear Family: Analyzing Family Size Over Time Using GSS Data
This repository contains the work completed for the project **"Honey, I Shrunk the Nuclear Family"**, as part of the **UC Berkeley MIDS W203: Statistics for Data Science** course in Spring 2024.

### Overview
This project explores changes in family size over time in the United States by analyzing data from the **General Social Survey (GSS)**. Using generational data and socioeconomic factors, we aim to understand how family structures have evolved, focusing on the number of siblings in families and other related characteristics.

### Key Questions Addressed:
1. How does family size vary with age, acting as a generational proxy?
2. How do socioeconomic factors like income, parental status, and cultural context influence family size?
3. What patterns emerge in the relationship between age and family size when accounting for other variables?

### Data and Methodology
#### Data Sources:
- **General Social Survey (2022)**: A cross-sectional survey of 3,544 adults in the US capturing demographic, behavioral, and attitudinal data.

#### Key Variables:
- **Dependent Variable**: Number of siblings (sibs)
- **Independent Variable**: Age (age), perceived income (incom16), parential socioeconomic index (masei10 and pasei10), and location characteristics (reg16 and res16).

#### Methodology
1. **Data Cleaning**: Removed outliers and missing responses. Applied transformations to variables (e.g., square root transformation for the dependent variable to handle heavy-tailed distribution).
2. **Modeling**: 
    - Performed OLS regression to analyze relationships between family size and independent variables.
    - Controlled for socioeconomic and cultural factors.
3. **Validation**: Split the data into exploration (30%) and validation (70%) sets.

### Results
- **Age-Family Size Relationship**:
    - A statistically significant positive relationship was observed between age and the number of siblings.
    - Generational changes show smaller family sizes for younger respondents.
- **Influence of Socioeconomic Factors**:
    - Higher parental socioeconomic index and income are associated with smaller family sizes.
    - Cultural and locational factors, such as growing up in the US versus overseas, significantly affect sibling count.
- **Model Fit**:
    - Base Model R^2: 0.025
    - Extended Model R^2: 0.083

### Discussion
#### Insights:
- Family size has declined across generations, with younger respondents reporting fewer siblings than older generations.
- Socioeconomic factors, particularly income and parental background, are critical determinants of family size.
- Cultural context plays a role, with differences observed between respondents raised in the US and those raised overseas.

#### Limitations:
- Generational Proxy: Using age as a proxy for generational trends may miss nuances in historical context.
- Perceived Variables: Recall bias may affect responses about income and family background.
- Fat Tails: Heavy-tailed data suggests further exploration of transformations for more robust modeling.

### Tools and Technologies
- R programming language
- R Libraries: tidyverse, magrittr, stats, dplyr, ggplot2, lmtest, sandwich, knitr, caret, stargazer, estimatr, car, moments, effsize
- Data Source: [General Social Survey (GSS)](https://gss.norc.org/us/en/gss/about-the-gss.html)

### Authors
- Gia Nguyen
- Aman Kumar
- Ayodele Oyewole
- Assaph Aharoni