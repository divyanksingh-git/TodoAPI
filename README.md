# <u>TodoAPI</u>

**It is a basic To-do list API created in python using FastAPI**

### <u>Features included :</u>

- It is a REST API
- IT supports user authentication using JWT (JSON Web Tokens), only registered user will be able to create or update tasks
- It use FastAPI as its framework
- It uses Mongo db for storing data
- It has implementations of all the CRUD functionalities

### <u>API Endpoints :</u> 

1. /register : You can register new user.

![[pic/Pasted image 20230211194427.png]]

2. /login : login as a user and generate a authentication token.

![[pic/Pasted image 20230211194858.png]]

3. /all : Get all the todo tasks

![[pic/Pasted image 20230211195044.png]]

4. /get/{name} : Get the specific task using name

![[pic/Pasted image 20230211195438.png]]

5. /create : create the task and append it in todo list

 ![[pic/Pasted image 20230211195356.png]]

7. /update : update the specific task 

![[pic/Pasted image 20230211195534.png]]

8. /delete : delete a task

![[pic/Pasted image 20230211195612.png]]


### <u>How To Run:</u>

##### Windows :

1. Install all python dependencies using : pip install -r requirements.txt
2. Install mongodb and configure.
3. run API using : uvicorn app.app:app --reload

##### Linux and Mac :

1. Install all python dependencies using : pip3 install -r requirements.txt
2. Install mongodb and configure.
3. run : ./run.sh

### <u>Working Screenshots</u>

![[pic/Pasted image 20230211200525.png]]
![[pic/Pasted image 20230211200735.png]]
![[pic/Pasted image 20230211200846.png]]

### <u>Improvements that can be implemented :</u>

1. More user operations and a better user management system.
2. Persist users across sessions by implementing seperate user database.
3. Seperate Todo database for all users.

### <u>References</u>

1. https://fastapi.tiangolo.com/
2. https://www.mongodb.com/docs/
3. https://jwt.io/introduction
