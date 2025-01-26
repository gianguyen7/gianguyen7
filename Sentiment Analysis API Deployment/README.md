## Sentiment Analysis API Deployment
This repository contains the work completed for the project **"Sentiment Analysis API Deployment"**, as part of the **UC Berkeley MIDS W255: Machine Learning Systems Engineering** course in Fall 2024.

### Overview
The Sentiment Analysis API is a tool that processes written text and identifies its sentiment. It is particularly useful for:

- Customer Feedback: Understanding customer satisfaction from reviews and comments.
- Market Research: Analyzing trends and public opinions on social media or surveys.
- Support Systems: Prioritizing responses based on the urgency or tone of customer messages.

### Project Flow
Once the project is complete, all the parts come together in the following workflow:
1. User Interaction
- A user (e.g., a business, developer, or researcher) submits text data to the Sentiment Analysis API via a simple interface or application.
2. API Processing
- The API receives the text input and processes it using a pre-trained sentiment analysis model (e.g., Hugging Face's DistilBERT).
- The model predicts whether the sentiment of the input is positive, negative, or neutral.
3. Deployment and Scalability

To ensure the API is robust and can handle many users at once:
- Docker: The API is packaged into a container for consistent and portable deployment across systems.
- Kubernetes: The containers are managed and scaled using Kubernetes to ensure the service can handle multiple requests efficiently.
- Azure Kubernetes Service (AKS): The API runs on AKS, providing high availability and reliability in the cloud.
- Redis: A caching system stores frequent queries and results, improving response times for repeated or similar inputs.
4. Monitoring and Optimization
- Grafana: Tracks the system’s performance, such as uptime, latency, and error rates, ensuring a smooth user experience.
- k6: Simulates heavy traffic to test and optimize the API’s ability to handle high demand.
5. Results Delivery
- The API returns the sentiment result (positive, negative, or neutral) in a user-friendly format.
- Developers can integrate this result into their applications, such as dashboards, customer service tools, or analytics platforms.

### Deployment Components
#### Technologies Used
1. Docker: Simplifies packaging and deployment.
2. Kubernetes: Ensures scalability and reliability.
3. Redis: Speeds up the system by caching frequent queries.
4. Azure Kubernetes Service (AKS): Provides a secure, cloud-based deployment environment.
5. Monitoring Tools:
    - Grafana: For tracking system performance.
    - k6: For load testing and optimization.

### Why This Matters
In today's data-driven world, understanding public sentiment is essential. This project helps:

- Businesses: Refine products and services based on customer feedback.
- Researchers: Analyze large datasets to uncover trends and insights.
- Developers: Integrate advanced sentiment analysis into their applications.

### Author
- Gia Nguyen