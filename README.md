
---
> **DON'T PUSH TO MAIN** 
# **Barazer Civic Platform Backend**

This backend powers the Barazer Civic Platform, designed to support the frontend applications in handling user authentication, forums, voting systems, USSD interactions, and AI-driven sentiment analysis. The backend is built using **FastAPI** and integrates with **Appwrite** for authentication and data storage.

## **Table of Contents**

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [API Endpoints](#api-endpoints)
- [Docker Setup](#docker-setup)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

---

## **Features**

- **User Authentication:** Uses Appwrite for secure and scalable user authentication.
- **Forum Management:** Allows users to post topics, comment, and participate in discussions.
- **Voting System:** Enables users to cast votes on various civic issues.
- **USSD Integration:** Offers USSD support for users without access to smartphones or the internet.
- **AI-Powered Sentiment Analysis:** Analyzes user feedback using Google Cloud Natural Language API to provide insights.

---

## **Tech Stack**

### **Backend**
- **FastAPI**: The primary backend framework.
- **Appwrite**: Handles authentication and data storage.
- **Google Cloud Natural Language API**: For sentiment analysis.
- **Africa's Talking**: For USSD integration.

### **DevOps**
- **Docker**: Containerization for easy deployment and scalability.

---

## **Project Structure**

```bash
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── auth/
│   │   ├── __init__.py
│   │   ├── endpoints.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── forums/
│   │   ├── __init__.py
│   │   ├── endpoints.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── voting/
│   │   ├── __init__.py
│   │   ├── endpoints.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── ussd/
│   │   ├── __init__.py
│   │   ├── endpoints.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── nlp/
│   │   ├── __init__.py
│   │   ├── endpoints.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── config.py
│   └── database.py
├── requirements.txt
├── Dockerfile
└── README.md

```

---

## **Setup & Installation**

### **Prerequisites**

- **Python 3.8+**
- **Pipenv**
- **Docker (optional, for containerized deployment)**

### **1. Clone the Repository**

```bash
git clone https://github.com/Barazer-Improving-Citizen-Engagement/backend-bar.git
cd backend-bar
```

### **2. Setup the Virtual Environment**

```bash
pipenv install --dev
pipenv shell
```

### **3. Install Dependencies**

```bash
pipenv install -r requirements.txt
```

### **4. Configure Environment Variables**

Create a `.env` file at the root of the project and add the following environment variables:

```bash
# Appwrite Configuration 
#you get a copy for testing
APPWRITE_ENDPOINT=https://[YOUR_APPWRITE_ENDPOINT]
APPWRITE_PROJECT_ID=[YOUR_PROJECT_ID]
APPWRITE_API_KEY=[YOUR_API_KEY]

# Google Cloud Configuration
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/google-cloud-service-account.json
```

### **5. Run the FastAPI Server**

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The backend server should now be running at `http://localhost:8000`.

---


## **API Endpoints**

The API is divided into several modules based on functionality: `Authentication`, `Forums`, `Voting`, `USSD`, and `NLP`. Each module contains specific endpoints to handle relevant operations and includes models, utilities, and routing logic.

### **Authentication Endpoints**

| Method | Endpoint          | Description                                      | Payload                                                    |
|--------|-------------------|--------------------------------------------------|------------------------------------------------------------|
| POST   | `/auth/register`   | Register a new user with email and password.     | `{ "email": "user@example.com", "password": "********" }`   |
| POST   | `/auth/login`      | Log in an existing user.                         | `{ "email": "user@example.com", "password": "********" }`   |
| GET    | `/auth/me`         | Retrieve current logged-in user's profile.       | `Authorization: Bearer <JWT-Token>`                         |
| POST   | `/auth/logout`     | Log out the current user.                        | `Authorization: Bearer <JWT-Token>`                         |

### **Forum Endpoints**

| Method | Endpoint            | Description                                      | Payload                                                            |
|--------|---------------------|--------------------------------------------------|--------------------------------------------------------------------|
| POST   | `/forums/create`     | Create a new forum thread.                       | `{ "title": "Topic Title", "content": "Detailed content..." }`      |
| GET    | `/forums/list`       | Retrieve a list of all forum threads.            | -                                                                  |
| GET    | `/forums/{thread_id}`| Get details of a specific forum thread.          | `thread_id` in URL                                                 |
| POST   | `/forums/{thread_id}/comment` | Add a comment to a specific thread.       | `{ "content": "Comment content..." }`                              |
| DELETE | `/forums/{thread_id}`| Delete a specific forum thread (admin only).     | `Authorization: Bearer <Admin-Token>`                              |

### **Voting Endpoints**

| Method | Endpoint             | Description                                      | Payload                                                             |
|--------|----------------------|--------------------------------------------------|---------------------------------------------------------------------|
| POST   | `/voting/cast`        | Cast a vote on a civic issue.                     | `{ "issue_id": "123", "vote": "yes" }`                              |
| GET    | `/voting/results`     | Retrieve voting results of all issues.           | -                                                                   |
| GET    | `/voting/results/{issue_id}` | Get results of a specific issue.           | `issue_id` in URL                                                   |

### **USSD Endpoints**

| Method | Endpoint             | Description                                      | Payload                                                             |
|--------|----------------------|--------------------------------------------------|---------------------------------------------------------------------|
| POST   | `/ussd/session`       | Handle a USSD session initiated by a user.       | `{ "phoneNumber": "+254712345678", "text": "1*2" }`                 |
| POST   | `/ussd/register`      | Register a new user through USSD.                | `{ "phoneNumber": "+254712345678", "name": "John Doe" }`            |
| POST   | `/ussd/vote`          | Cast a vote through USSD interaction.            | `{ "phoneNumber": "+254712345678", "issue_id": "123", "vote": "yes"}`|

### **NLP/Sentiment Analysis Endpoints**

| Method | Endpoint             | Description                                      | Payload                                                             |
|--------|----------------------|--------------------------------------------------|---------------------------------------------------------------------|
| POST   | `/nlp/analyze`        | Analyze user feedback and assess sentiment.      | `{ "text": "This policy is effective and fair..." }`                 |
| GET    | `/nlp/reports`        | Retrieve a list of sentiment analysis reports.   | -                                                                   |
| GET    | `/nlp/reports/{report_id}` | Get details of a specific sentiment report. | `report_id` in URL                                                  |

### **Response Format**

All endpoints will return a standardized JSON response structure, including `status`, `message`, and `data` fields, for consistent integration with the frontend.

```json
{
  "status": "success",
  "message": "Operation completed successfully",
  "data": {
    // ... relevant data
  }
}
```

### **Error Handling**

All errors are handled uniformly, returning an appropriate HTTP status code and an error message:

```json
{
  "status": "error",
  "message": "Invalid credentials or missing fields",
  "data": null
}
```

---


## **Docker Setup**

To containerize the application, follow these steps:

1. **Build the Docker Image:**

```bash
docker build -t barazer-backend .
```

2. **Run the Docker Container:**

```bash
docker run -d --name barazer-container -p 8000:8000 barazer-backend
```

The backend should now be running in a Docker container on `http://localhost:8000`.

---

## **Environment Variables**

Create a `.env` file at the root of the project with the following content:

```bash
# Appwrite Configuration
APPWRITE_ENDPOINT=https://[YOUR_APPWRITE_ENDPOINT]
APPWRITE_PROJECT_ID=[YOUR_PROJECT_ID]
APPWRITE_API_KEY=[YOUR_API_KEY]

# Google Cloud Configuration
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/google-cloud-service-account.json

# Africa's Talking Configuration
AFRICAS_TALKING_USERNAME=[YOUR_USERNAME]
AFRICAS_TALKING_API_KEY=[YOUR_API_KEY]
AFRICAS_TALKING_SHORTCODE=[YOUR_SHORTCODE]
```

Make sure you update these values based on your project settings and credentials.

---

## **Contributing**

1. Fork the repository.
2. Create a new feature branch.
3. Submit a pull request with clear documentation on your changes.

For detailed contribution guidelines, refer to the `CONTRIBUTING.md` file.

---

## **License**

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---
