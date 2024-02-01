# Lets Learn fastApi
# FastAPI CRUD Operations

This project demonstrates simple CRUD (Create, Read, Update, Delete) operations using FastAPI.

## Overview

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

This project showcases a basic API for managing posts. It includes endpoints for creating, retrieving, updating, and deleting posts.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/dev-Kevo/fastApi.git
    cd fastApi
    ```
2. Create a virtual Enviroment and activate:

    ```bash
    python -m venv <name_of_the_virtual_env>
    cd venv/Scripts
    ----> activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI application:

    ```bash
    uvicorn app.main:app --reload
    ```

2. Open your browser and navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the FastAPI Swagger documentation.

3. Explore and test the CRUD operations using the provided API endpoints.

## API Endpoints

### Create a Post

- **Endpoint:** `/create`
- **Method:** `POST`
- **Parameters:** `title`, `content`, `published`

### Read Post

- **Endpoint:** `/post/{id}`
- **Method:** `GET`

### Read Posts

- **Endpoint:** `/posts`
- **Method:** `GET`

### Update a Post

- **Endpoint:** `/update/{id}`
- **Method:** `PUT`
- **Parameters:** `id`, `title`, `content`, `published`

### Delete a Post

- **Endpoint:** `/delete/{id}`
- **Method:** `DELETE`
- **Parameters:** `id`

## Dependencies

- FastAPI: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- Uvicorn: [https://www.uvicorn.org/](https://www.uvicorn.org/)


