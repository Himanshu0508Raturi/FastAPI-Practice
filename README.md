# FastAPI Practice

A RESTful API built with FastAPI for managing product inventory.  This project demonstrates CRUD (Create, Read, Update, Delete) operations with SQLAlchemy ORM and database integration.

## 🚀 Features

- **Complete CRUD Operations**: Create, read, update, and delete products
- **Database Integration**: SQLAlchemy ORM for database operations
- **CORS Support**: Configured for cross-origin requests
- **Data Validation**: Pydantic models for request/response validation
- **Auto-generated Documentation**: Swagger UI and ReDoc available out of the box

## 📋 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message |
| GET | `/products` | Get all products |
| GET | `/product/{id}` | Get product by ID |
| POST | `/product` | Add a new product |
| PUT | `/product` | Update an existing product |
| DELETE | `/product` | Delete a product by ID |

## 🛠️ Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type annotations
- **Python 3.x**: Programming language

## 📦 Installation

1. Clone the repository: 
```bash
git clone https://github.com/Himanshu0508Raturi/FastAPI-Practice.git
cd FastAPI-Practice
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

4. Configure the database:
   - Open `dbconfig.py`
   - Update the `db_url` variable with your database connection string: 
   ```python
   db_url = "sqlite:///./products.db"  # For SQLite
   # or
   db_url = "postgresql://user:password@localhost/dbname"  # For PostgreSQL
   ```

## 🚀 Running the Application

Start the development server: 

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Access Interactive Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc


## 📂 Project Structure

```
FastAPI-Practice/
├── main. py           # FastAPI application and route definitions
├── models.py         # Pydantic models for data validation
├── db_models.py      # SQLAlchemy database models
├── dbconfig.py       # Database configuration
├── . gitignore        # Git ignore file
└── README.md         # Project documentation
```

## 🔧 Configuration

The application includes CORS middleware configured for:
- `http://localhost:3000`
- `http://localhost:5000`

To add more origins, update the `allow_origins` list in `main.py`.

## 📚 Product Model

```python
{
  "id": int,
  "name": str,
  "description": str,
  "price": float,
  "quantity": int
}
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  Feel free to check the issues page.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Himanshu Raturi**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/himanshu-raturi/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/Himanshu0508Raturi)

## ⭐ Show your support

Give a ⭐️ if this project helped you learn FastAPI!