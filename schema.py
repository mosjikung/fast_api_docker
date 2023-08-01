from typing import Generic, Optional, TypeVar, Dict ,List ,Any ,Tuple
from pydantic.generics import GenericModel
from pydantic import BaseModel, Field ,EmailStr 
from datetime import datetime

T = TypeVar("T")


class Parameter(BaseModel):
    data: Dict[str, str] = None


class RequestSchema(BaseModel):
    # parameter: Parameter = Field(...) #ดึงจาก Class Parameter
    parameter: Parameter = Field(
        {
            "data": {
                "username": "",
                "email": "",
                "phone_number": "",
                "password": "",
                "first_name": "",
                "last_name": "",
            }
        }
    )


class ResponseSchema(BaseModel):
    code: str
    status: str
    message: str
    result: Optional[T] = None


class UserSigupSchema(BaseModel):
    username: str
    email: str
    phone_number: str
    password: str
    first_name: str
    last_name: str


class UserSiginSchema(BaseModel):
    username: str
    password: str


class Userloginweb(BaseModel):
    email: str
    password: str


class UserBase(BaseModel):
    username: str
    email: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class Checkemail(BaseModel):
    email:str
    



class EmailSchema(BaseModel):
    email: List[EmailStr]
    body: Dict[str,Any]

class ChangePassword(BaseModel):
    token:str
    newpassword:str

class ChangePasswordLogin(BaseModel):
    oldpassword:str
    newpassword:str

class ChangePasswordResp(BaseModel):
    result:bool
    message:str

class UpdateMember(BaseModel):
    username:str
    email:str
    first_name:str
    last_name:str
    address:str
    phone_number:str
    country_id:int
    province:str
    district:str
    sub_district:str
    postal_code:str
    modified_by:int

class CustomException(Exception):
    http_code: int
    code: str
    message: str

    def __init__(self, http_code: int = None, code: str = None, message: str = None):
        self.http_code = http_code if http_code else 500
        self.code = code if code else str(self.http_code)
        self.message = message

class UploadFileResponse(BaseModel):
    bucket_name: str
    file_name: str
    url: str

class AuthModel(BaseModel):
    username: str
    password: str

class GoogleToken(BaseModel):
    token:str

class Check_email(BaseModel):
    email:str

class Check_register(BaseModel):
    email:str
    password:str
    name:str
    birth_date:Optional[str]=None

class Callback_token(BaseModel):
    token:str

class Insertscore(BaseModel):
    score:int





# หน้า schema คือ Request Body
