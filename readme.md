# FastAPI MySQL CRUD Application

This is a CRUD (Create, Read, Update, Delete) application built with FastAPI and MySQL.

## Project Structure

The project is structured as follows:

- `api`: Main directory containing the FastAPI application.
  - `app.py`: Entry point of the FastAPI application.
  - `controllers`: Directory containing controller modules for business logic.
    - `user_controller.py`: Controller for user-related operations.
  - `models`: Directory containing model classes for database interactions.
    - `user.py`: Model class for user entity.
  - `routers`: Directory containing route modules for HTTP routes.
    - `user_router.py`: Router module for user routes.
  - `mysql_connector.py`: MySQL connector module for database operations.

## Installation

To run the application, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/shivangkushwaha/fastapi-mysql-template