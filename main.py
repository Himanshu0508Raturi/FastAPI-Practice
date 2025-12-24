from fastapi import FastAPI , Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from dbconfig import session , engine
from sqlalchemy.orm import Session
import db_models

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:3000" , "http://localhost:5000"],
    allow_methods = ["*"]
)


db_models.Base.metadata.create_all(bind = engine)  


products = [
Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

def init_db():
    db = session()
    count = db.query(db_models.Product).count
    if count == 0:
        for product in products:
            db.add(db_models.Product(**product.model_dump()))
    db.commit()

init_db()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
def greet():
    return "Welcome to homepage of fastapi"

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(db_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id: int , db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
        return db_product
    return "Product Not Found"

@app.post("/product")
def add_a_product(product: Product , db: Session = Depends(get_db)):
    db.add(db_models.Product(**product.model_dump()))
    db.commit()
    return product

@app.put("/product")
def update_product(newproduct: Product , db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == newproduct.id).first()
    if db_product:
        db_product.name = newproduct.name
        db_product.description = newproduct.description
        db_product.price = newproduct.price
        db_product.quantity = newproduct.quantity
        db.commit()
        return {
            "message" : "Updated Successfully."
        }
    else:
        return {
            "message" : "Product Not found."
        }

@app.delete("/product")
def delete_product(id: int , db: Session = Depends(get_db)):
    db_product = db.query(db_models.Product).filter(db_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return {
            "message" : "Deleted Successfully."
        }
    else:
        return {
            "message" : "Product Not found."
        }