## Vote of Confidence: Assessing Statistical Signification of Trends in Voting Difficulty
This repository contains the work completed for the project **"Vote of Confidence"**, as part of the **UC Berkeley MIDS W203: Statistics for Data Science** course in Spring 2024.

### Overview
This project investigates whether Democratic or Republican voters experience more difficulty voting in the United States. With voting access being a critical and contested issue in recent years, this study aims to provide a data-driven perspective on voting challenges and their potential implications for voter turnout and election outcomes.

### Key Research Question:
- **Do Democratic voters or Republican voters experience more difficulty voting?**

By leveraging data from the 2022 American National Election Studies (ANES) Pilot Study, the analysis seeks to provide statistical evidence to address this question.

### Data and Methodology
#### Data Source:
- 2022 ANES Pilot Study: A nationally representative survey of U.S. citizens aged 18+ conducted between November 14 and November 22, 2022, with 1,585 respondents.
#### Key Variables:
1. Political Party Affiliation (pid_x):
    - Defined as "Democrat" or "Republican" based on explicit identification and party lean.
    - Excluded independents and missing responses.
2. Difficulty Voting (vharder0 through vharder11):
    - Captures binary responses to challenges faced while voting (e.g., long wait times, transportation issues).
    - Summed to generate a "difficulty score" for each respondent.

#### Methodology:
1. Data Cleaning:
    - Excluded respondents with missing or independent political affiliations.
    - Normalized binary difficulty fields to construct a "difficulty score."
2. Statistical Testing:
    - Conducted a two-sample t-test to compare difficulty scores between Democrats and Republicans.
    - Verified t-test assumptions: IID data, metric scale, and normality (via Central Limit Theorem).
3. Validation:
    - Ensured no multicollinearity among difficulty variables using a correlation matrix.

### Results
- **Key Findings**:
    - Democrats reported a higher average difficulty score (0.72) than Republicans (0.39).
    - The difference was statistically significant.
    - Cohen's d: Democrats' difficulty score was 0.296 standard deviations higher than Republicans'.
- **Limitations**:
    - "Difficulty score" does not account for varying severity of different voting challenges.
    - Sampling weights from the ANES dataset were not applied (per lab instructions).


### Tools and Technologies
- R programming language
- R libraries: tidyverse, magrittr, stats, dplyr, ggplot2, lmtest, sandwich, car, moments, effsize

### Authors
- Gia Nguyen
- Aman Kumar
- Ayodele Oyewole
- Assaph Aharoni