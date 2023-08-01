from fastapi import FastAPI
from fastapi import APIRouter, Depends 
from fastapi.middleware.cors import CORSMiddleware
from config import engine
from model import Score
import model
from sqlalchemy.orm import Session
from config import get_db
from schema import (
  
    Insertscore

)
from repository.repository import BaseRepo

# generate model to table postgresql
model.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:8080",
	"https://nrc-management.xcoshop.com",
    "https://nrc-oauth.xcoshop.com",
    "https://nrc-management-service.xcoshop.com",
    "https://nrc.xcoshop.com",
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/')
async def Home():
    return "Welcome Home"


@app.post("/pop")
async def pop(request:Insertscore,db: Session = Depends(get_db)):  # get_db->config.py
       update_data  = BaseRepo.update_score(db,
                                            Score,
                                            request.score)
       results_update = BaseRepo.update(db,update_data)

       if results_update == True:
              return "Save Complete"

@app.get("/pop_count")
async def pop_count(db: Session = Depends(get_db)):
       get_data = BaseRepo.get_score(db,
                                     Score)
       
       return get_data.score




