#importing python dependencies
from fastapi import FastAPI, Depends, HTTPException

#importing user created file
from .userAuth import AuthHandler
from .userSchema import AuthDetails
from . import db
from . import modal

#initializing fastapi, authintication handler and user list
app = FastAPI()
auth_handler = AuthHandler()
users = []

# home route
@app.get('/')
def home():
    return{"data":"Todo API using FastAPI python"}

# User registration and login endpoint
@app.post('/register', status_code=201)
def register(auth_details: AuthDetails):
    if any(x['username'] == auth_details.username for x in users):
        raise HTTPException(status_code=400, detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    users.append({
        'username': auth_details.username,
        'password': hashed_password    
    })
    return


@app.post('/login')
def login(auth_details: AuthDetails):
    user = None
    for x in users:
        if x['username'] == auth_details.username:
            user = x
            break
    
    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(user['username'])
    return { 'token': token }


# Todo API endpoints
@app.get("/all")
def getAll(user = Depends(auth_handler.auth_wrapper)):
    data = db.getAll()
    return {'data':data}

@app.post("/create")
def create(data:modal.TODO,user = Depends(auth_handler.auth_wrapper)):
    id = db.create(data)
    return{"Inserted":True,"ID":id}

@app.get("/get/{name}")
def getTask(name:str,user = Depends(auth_handler.auth_wrapper)):
    data = db.getTask(name)
    return(data)

@app.delete("/delete")
def delete(name:str,user = Depends(auth_handler.auth_wrapper)):
    data = db.delete(name)
    return {"deleted":True,"coubt":data}

@app.put("/update")
def update(name:str,data:modal.TODO,user = Depends(auth_handler.auth_wrapper)):
    data = db.update(name,data)
    return{"updated":True,"count":data}
