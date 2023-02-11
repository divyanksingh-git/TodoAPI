# Importing python dependencies
from pydantic import BaseModel

# Basic Todo Model 
class TODO(BaseModel):
    name: str
    description: str