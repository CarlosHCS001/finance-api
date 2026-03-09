from pydantic import BaseModel
import datetime

class TransactionCreate(BaseModel):
    description: str
    amount: float
    date: datetime.date
    category: str

class TransactionResponse(TransactionCreate):
    id: int

    class Config:
        from_attributes = True