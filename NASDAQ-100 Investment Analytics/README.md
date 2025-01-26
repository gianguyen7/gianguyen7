## NASDAQ-100 Investment Analytics
This repository contains the work completed for the project **"NASDAQ-100 Investment Analytics"**, as part of the **UC Berkeley MIDS W205: Fundamentals of Data Engineering** course in Spring 2024.

### Overview
#### Objectives
- Identify clusters of companies with similar stock movement patterns.
- Provide actionable insights for investors through stock grouping and analytics.
- Demonstrate the advantages of NoSQL databases in stock market analytics.
#### Importance
- Traditional relational databases struggle with complex relationships, horizontal scaling, and dynamic data requirements in stock market analysis.
- NoSQL databases like Neo4j, MongoDB, and Redis provide flexibility, scalability, and real-time processing capabilities essential for financial analytics.

### Dataset
- Source: NASDAQ-100 stock price data (2011–2016).
- Size: 271,680 observations with 8 attributes:
    - Date, Open, High, Low, Close, Adjusted Close, Volume, and Stock Name.
#### Preprocessing Steps:
1. Filtered data from 2011–2016.
2. Removed missing values based on the NASDAQ-100 holiday calendar.
3. Added new features:
    - Price Change ($)
    - Price Change (%)
4. Standardized stock prices to account for individual distributions.

### Methodology
#### Correlation Techniques
1. Pearson Correlation with Exponential Weights:
    - Highlights recent trends for better sensitivity to short-term changes.
2. Cosine Similarity:
    - Captures directional changes in stock prices, robust to outliers.
#### NoSQL Database Implementations
1. Neo4j:
    - Louvain Modularity: Clustering stocks based on cosine similarity.
    - PageRank: Identifying influential stocks within sectors.
    - Betweenness Centrality: Highlighting stocks acting as intermediaries between sectors.
2. MongoDB:
    - Document-oriented structure for flexible financial data analysis.
    - Agile schema adaptation for dynamic datasets.
3. Redis:
    - Provides real-time performance for stock trading platforms.
    - Supports fast transactional operations essential for traders.

### Results
#### Clustering Insights
- Stocks grouped by sector exhibit distinct movement patterns, enabling market segmentation.
- Influential stocks (e.g., ANSS, COST) identified through PageRank analysis.
- Stocks with high betweenness centrality (e.g., MELI, HON) are potential indicators of market ripple effects.
##### Database Efficiency
- Neo4j: Excellent for analyzing interconnected data points and market visualization.
- MongoDB: Scalable and adaptable for diverse financial data formats.
- Redis: Unmatched in providing real-time stock prices and fast data processing.

### Challenges and Limitations
1. Computational Power:
    - Limited GPU access restricted data processing at scale.
2. Data Variety:
    - Dataset lacked sufficient diversity in industry-specific stock attributes.
3. Relational Database Constraints:
    - Inflexible schemas and horizontal scaling challenges hindered traditional database efficiency.

### Tools and Technologies
- Python programming language
- Databases: Neo4j, MongoDB, Redis
- Python Libraries: pandas, numpy, matplotlib, seaborn

### Authors
- Gia Nguyen
- Rini Gupta
- Bao Pham
- Jaekwang Shin