# Multi-Agent orchestration AI Verification System

AIVerification System is an advanced automation solution built on **IBM Watsonx Orchestrate** and **IBM Code Engine**. It utilizes a multi-agent architecture to streamline and secure the customer document verification process.

## 🚀 Project Overview

The system is designed to automate the manual task of reviewing financial transfers and verifying supporting documents. By splitting the logic into two specialized agents, the system ensures high accuracy and modularity.

### 🤖 Multi-Agent Architecture

1.  **Agent-A (Customer Intake Agent)**
    - Responsible for initial customer data validation.
    - Handles identity verification and generates a unique `Transfer_ID`.
    - **Deployment:** Hosted as a microservice on IBM Code Engine.

2.  **Agent-B (Document Auditor Agent)**
    - Performs the core business logic: "The 7-File Rule".
    - Automatically counts and verifies the uploaded documents.
    - Updates the **Employee Portal** with a final decision (`DONE` / `NOT DONE`).
    - **Deployment:** Hosted as a microservice on IBM Code Engine.

## 🌐 Live Deployment (Endpoints)

The backend logic is fully operational and deployed as serverless applications:

- **Agent-A Endpoint:** `https://agent-a.25rq6jnf20iq.eu-gb.codeengine.appdomain.cloud`
- **Agent-B Endpoint:** `https://agent-b.25rq6jnf20iq.eu-gb.codeengine.appdomain.cloud`

## 🛠️ Tech Stack

- **Orchestration:** IBM Watsonx Orchestrate (Custom Skills).
- **Compute:** IBM Code Engine (Serverless Microservices).
- **Language:** Python 3.11
- **Communication:** RESTful APIs (JSON).

## 📋 Logic Implementation (The 7-File Rule)

The system enforces a strict verification policy. Agent-B evaluates the input array of files:
- **Files >= 7:** Status set to `DONE`, triggers payment confirmation.
- **Files < 7:** Status set to `NOT DONE`, provides a detailed reasoning report for the employee.

## 📂 Project Structure
├── agent_a.py # Backend logic for Agent-A 
├── agent_b.py # Backend logic for Agent-B (Document Audit) 
└── README.md # Documentation

## 🎯 Key Achievements
- **Seamless Integration:** Successfully bridged the gap between Watsonx AI and external cloud compute.
- **Scalability:** Deployed via Code Engine to handle variable traffic loads.
- **Clean Architecture:** Separated concerns between data entry and document auditing.

## challenges
-Faced some environment configuration challenges during final deployment, but the logic and microservices architecture are fully implemented and ready for scaling.