
# Project Overview
This is a Serverless Web Application built using AWS services like Lambda , API Gateway, DynamoDB and other AWS serverless services.  
The project implements a Contact  page where users can submit their name, email, and message. Submissions are stored in DynamoDB, and all entries can be retrieved using GET operations.

 # Architecture & AWS Services Used

- AWS Lambda: Backend logic for GET and POST requests.
- API Gateway: Provides RESTful endpoints for the web application.
- DynamoDB: NoSQL database to store user messages.
- S3 / Hosting: Optional for hosting frontend HTML (if used separately).
- Serverless Approach: Fully managed, scalable, and cost-effective.

# Flow:
1. User submits the contact form.
2. API Gateway routes request to Lambda function.
3. Lambda stores the message in DynamoDB.
4. Lambda can also fetch all stored messages for display.

   
# Features:

- Submit a message using a Contact Us form.
- Retrieve all messages using GET API.
- Serverless architecture, no backend server management required.
- Real-time updates on the frontend after submission.
- Fully scalable using AWS services
