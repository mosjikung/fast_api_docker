from typing import Generic, Optional, TypeVar, Dict ,List ,Any ,Tuple
from pydantic.generics import GenericModel
from pydantic import BaseModel
from datetime import datetime

T = TypeVar("T")


class Parameter(BaseModel):
    data: Dict[str, str] = None



class Insertscore(BaseModel):
    score:int





# หน้า schema คือ Request Body
