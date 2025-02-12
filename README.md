# Receipt Processor & Rewards Calculator

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [Process a Receipt](#process-a-receipt)
  - [Get Reward Points](#get-reward-points)
- [Error Handling](#error-handling)
- [Docker Setup](#docker-setup)
- [Testing the API](#testing-the-api)

## Overview

This application processes receipts, assigns a unique ID to each receipt, and calculates reward points based on predefined rules and input data.

## Features

- Accepts receipts in JSON format, validates them, and assigns a unique ID.
- Calculates reward points based on receipt details.
- Provides API endpoints to submit receipts and retrieve points.
- Implements error handling for invalid data and missing receipts.
- Stateless in-memory storage.
- Application is build using **Python Flask** and can be easily deployed using **Docker**.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/manishptl/fetch-rewards-receipt-processor.git
   cd fetch-rewards-receipt-processor
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Running the Application

To start the server without **Docker** setup:

```sh
python app/server.py
```

## API Endpoints

### Process a Receipt

- **Endpoint:** `POST /receipts/process`
- **Request Body:** (Example)
  ```json
  {
    "retailer": "M&M Corner Market",
    "purchaseDate": "2022-03-20",
    "purchaseTime": "14:33",
    "items": [
      {
        "shortDescription": "Gatorade",
        "price": "2.25"
      },{
        "shortDescription": "Gatorade",
        "price": "2.25"
      },{
        "shortDescription": "Gatorade",
        "price": "2.25"
      },{
        "shortDescription": "Gatorade",
        "price": "2.25"
      }
    ],
    "total": "9.00"
  }
  ```
- **Response:**
  ```json
  { "id": "a572e126-481e-4de2-9fb9-224a20b4ad77" }
  ```

### Get Reward Points

- **Endpoint:** `GET /receipts/{id}/points`
- **Response:**
  ```json
  { "points": 109 }
  ```

## Error Handling

| Error Message                 | HTTP Code |
| ----------------------------- | --------- |
| The receipt is invalid.       | 400       |
| No receipt found for that ID. | 404       |
| Internal Server Error         | 500       |

## Docker Setup

1. Build the Docker image:
   ```sh
   docker build -t fetch-rewards-receipt-processor .
   ```
2. Run the container:
   ```sh
   docker run -p 5000:5000 fetch-rewards-receipt-processor
   ```

## Testing the API

- Use **Postman** or **cURL**:
  ```sh
  curl -X POST http://localhost:8080/receipts/process \
       -H "Content-Type: application/json" \
       -d '{"retailer": "Target", "purchaseDate": "2022-01-01", "purchaseTime": "13:01", "items": [{ "shortDescription": "Mountain Dew 12PK", "price": "6.49" },{ "shortDescription": "Emils Cheese Pizza", "price": "12.25" },{ "shortDescription": "Knorr Creamy Chicken", "price": "1.26" },{ "shortDescription": "Doritos Nacho Cheese", "price": "3.35" },{ "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00" }], "total": "35.35"}'
  ```


