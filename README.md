# Website Visitor Counter (AWS Lambda + DynamoDB)

This project implements a simple **visitor counter** for wwww.yashas-dev.com using **AWS Lambda** (Python) and **Amazon DynamoDB**.  
Every time the function is invoked (via API Gateway), it increments a counter in DynamoDB and returns the updated visit count.

---

## 📌 Features
- **Serverless**: Powered by AWS Lambda
- **Persistent Counter**: Visit count stored in DynamoDB
- **Fast & Scalable**: Handles high traffic with low latency
- **Simple API**: Easily integrate with a frontend using API Gateway

---

## 🛠 Tech Stack
- **AWS Lambda** – Compute
- **Amazon DynamoDB** – NoSQL database to store visit counts
- **Amazon API Gateway** – Optional API endpoint
- **Python 3.13** – Lambda runtime
- **Boto3** – AWS SDK for Python

---
