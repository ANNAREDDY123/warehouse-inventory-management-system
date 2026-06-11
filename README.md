# warehouse-inventory-management-system
FastAPI-based Warehouse Inventory Management System with JWT Authentication, Product Management, Supplier Management, Stock Tracking, SQLAlchemy, and SQLite.
# Warehouse Inventory Management System

## Features

- JWT Authentication
- Product Management
- Supplier Management
- Stock Management
- Inventory Tracking

## APIs

### Authentication

- POST /auth/register
- POST /auth/login

### Products

- POST /products
- GET /products
- GET /products/{id}
- PUT /products/{id}
- DELETE /products/{id}

### Suppliers

- POST /suppliers
- GET /suppliers

### Stock

- POST /stock/inward
- POST /stock/outward
- GET /stock/history

## Business Rules

- SKU unique
- Stock cannot become negative
- Product must exist
- Every stock movement tracked

## Run

py -m pip install -r requirements.txt
py -m uvicorn main:app --reload


Swagger:

http://127.0.0.1:8000/docs
