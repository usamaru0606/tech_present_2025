from sqlalchemy import Column, String, Date, Integer, ForeignKey
from app.db.base_class import Base

class RecordTraining(Base):
    __tablename__ = "trainings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(36), ForeignKey("users.guid"), nullable=False, index=True)
    date = Column(Date, nullable=False)
    trainingMenu = Column(String, nullable=True)
    trainingTime = Column(String, nullable=True) 