from fastapi import FastAPI
from pydantic import BaseModel
import file_handler

app = FastAPI()

class JobApplication(BaseModel):
    name: str
    company: str
    position: str
    status: str  
