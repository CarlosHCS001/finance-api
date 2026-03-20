from pydantic import BaseModel, field_validator
import datetime

class TransactionCreate(BaseModel):
    description: str
    amount: float
    date: datetime.date
    category: str

    @field_validator('amount')
    @classmethod
    def amount_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('amount deve ser maior que zero')
        return v

class TransactionUpdate(BaseModel):
    description: str | None = None
    amount: float | None = None
    date: datetime.date | None = None
    category: str | None = None

    @field_validator('amount')
    @classmethod
    def amount_must_be_positive(cls, v):
        if v is not None and v <= 0:
            raise ValueError('amount deve ser maior que zero')
        return v

class TransactionResponse(TransactionCreate):
    id: int

    class Config:
        from_attributes = True