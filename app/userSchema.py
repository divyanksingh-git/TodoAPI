# Importing python dependencies
from pydantic import BaseModel

#Basic User authintication model
class AuthDetails(BaseModel):
    username: str
    password: str