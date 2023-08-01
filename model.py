from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Date,
    PrimaryKeyConstraint,
    ForeignKey,
    UniqueConstraint,
    Text
)
from sqlalchemy.orm import relationship
from config import Base
import datetime



class Score(Base):
    __tablename__ = "score"
    id = Column(Integer, primary_key=True)
    score = Column(Integer)



    


    





# model คือตัวแทน Table
