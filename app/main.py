from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
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
    return {"message": "Finance API - Semana 2"}

@app.post("/transactions", response_model=schemas.TransactionResponse)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    db_transaction = models.Transaction(**transaction.model_dump())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@app.get("/transactions", response_model=list[schemas.TransactionResponse])
def get_transactions(db: Session = Depends(get_db)):
    return db.query(models.Transaction).all()



@app.put("/transactions/{transaction_id}", response_model=schemas.TransactionResponse)
def update_transaction(transaction_id: int, transaction: schemas.TransactionUpdate, db: Session = Depends(get_db)):
    db_transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    update_data = transaction.model_dump(exclude_none=True)
    for field, value in update_data.items():
        setattr(db_transaction, field, value)

    db.commit()
    db.refresh(db_transaction)
    return db_transaction


@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = db.query(models.Transaction).filter(models.Transaction.id == transaction_id).first()

    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transação não encontrada")

    db.delete(db_transaction)
    db.commit()
    return {"message": "Transação deletada com sucesso"}