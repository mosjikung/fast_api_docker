from typing import TypeVar, Generic, Optional
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import desc, null,or_ ,func , cast ,Date ,asc, not_

from datetime import datetime, timedelta
from jose import JWTError, jwt
from config import SECRET_KEY, ALGORITHM
from datetime import datetime, timedelta

from fastapi import Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials,OAuth2PasswordBearer
from fastapi import Request, HTTPException


from model import  Score

import pdb


T = TypeVar("T")


class BaseRepo:
    """
    CRUD
    C = Create
    R = Read
    U = update
    D = Delete
    """

    @staticmethod
    def get_score(db: Session, model: Generic[T]):
        sql =  db.query(model).filter(model.id == 1).first()
        return sql
    @staticmethod
    def update_score(db:Session, model:Generic[T],score:int):
        sql = db.query(model).first()
        sql.score = score
        return sql 





    
  

    @staticmethod
    def insert(db: Session, model: Generic[T]):
        db.add(model)
        db.commit()
        db.refresh(model)
        return True

    
    @staticmethod
    def update(db: Session, model: Generic[T]):
        db.commit()
        db.refresh(model)
        return True

    @staticmethod
    def delete(db: Session, model: Generic[T]):
        db.delete(model)
        db.commit()
        return True



    
    

   







