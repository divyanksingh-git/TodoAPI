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

![Pasted image 20230211194427](https://user-images.githubusercontent.com/26967154/218264994-1cf51742-a9cb-4b91-b7fb-32031bd1dd56.png)

2. /login : login as a user and generate a authentication token.

![Pasted image 20230211194858](https://user-images.githubusercontent.com/26967154/218265167-2c23a9f8-1688-4e9b-97f0-e20e5c2bb5cd.png)

3. /all : Get all the todo tasks

![Pasted image 20230211195044](https://user-images.githubusercontent.com/26967154/218265224-11e265bc-8b08-4955-8220-cb2ea61ed659.png)

4. /get/{name} : Get the specific task using name

![Pasted image 20230211195438](https://user-images.githubusercontent.com/26967154/218265236-319f2744-903e-4ad0-911a-61e90abbc48e.png)

5. /create : create the task and append it in todo list

![Pasted image 20230211195356](https://user-images.githubusercontent.com/26967154/218265247-5011a54f-3282-4e1e-b83a-554c05de4c08.png)

7. /update : update the specific task 

![Pasted image 20230211195534](https://user-images.githubusercontent.com/26967154/218265258-ce16101a-e562-4b3f-9774-cdc9529f1331.png)

8. /delete : delete a task

![Pasted image 20230211195612](https://user-images.githubusercontent.com/26967154/218265263-e43df92c-127e-4908-a623-0f97f2f63fdf.png)


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

![Pasted image 20230211200525](https://user-images.githubusercontent.com/26967154/218265273-59a87c18-d144-4c89-a240-a4dd6db5cd93.png)
![Pasted image 20230211200735](https://user-images.githubusercontent.com/26967154/218265295-9f7fa8b7-b171-4c2d-824d-59e387b68876.png)
![Pasted image 20230211200846](https://user-images.githubusercontent.com/26967154/218265328-03f629d1-d07c-4dbf-9748-59d6e124b2f8.png)

### <u>Improvements that can be implemented :</u>

1. More user operations and a better user management system.
2. Persist users across sessions by implementing seperate user database.
3. Seperate Todo database for all users.

### <u>References</u>

1. https://fastapi.tiangolo.com/
2. https://www.mongodb.com/docs/
3. https://jwt.io/introduction
