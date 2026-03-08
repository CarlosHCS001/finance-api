from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import Base
import app.models as models
import app.schemas as schemas
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependência de sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Finance API - Semana 1"}

@app.post("/transactions")
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = models.Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@app.get("/transactions")
def get_transactions(db: Session = Depends(get_db)):
    return db.query(models.Transaction).all()