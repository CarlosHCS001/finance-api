from sqlalchemy import Column, Integer, String, Float, Date
from app.database import Base
import datetime

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    date = Column(Date, default=datetime.date.today)
    category = Column(String, nullable=False)