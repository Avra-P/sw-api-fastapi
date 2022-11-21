### Setup

- Setup my local environment. 
```
 # Create a virtual env with venv and activate it   
➜  python3 -m venv .venv     
➜  source ./.venv/bin/activate 

# store dependencies with pip
(venv) ➜  pip install fastapi
(venv) ➜  pip install "uvicorn[standard]"

# Export dependencies in python's requirements.txt file
pip3 freeze > requirements.txt
```
- Created a python module in [app.py](../app.py) 
- Run my instance using one of the requirements' packages
``` 
(.venv) ➜  sw-api-fastapi git:(main) ✗ uvicorn app:app 

INFO:     Started server process [56525]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```
Option `uvicorn app:app --reload` restartes the server after code changes.

- Copied the swapi data from [swapi GitHub repo resources folder](https://github.com/phalt/swapi/tree/master/resources/fixtures), 
into a [local folder](../resources), in order to keep them as an in-memory storage solution.
This is a quick and simplistic storage approach. 
<br>A much better solution would be to implement a relational database, using eg Flask or Django.
<br>In order to keep the data of a minimal size, the json files with people, planets and starships contain only 5 entries each, keeping those based on existing relationships with the people objects.

- Added 404 exception handling
- Added a logging mechanism

```
### Extract from info level log messages
22-Nov-22 01:37:38:f - -INFO - People data loaded from json file
INFO:     Started server process [58525]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:58073 - "GET /people HTTP/1.1" 200 OK
22-Nov-22 01:38:00:f - -INFO - Found the person with id 1
INFO:     127.0.0.1:58074 - "GET /people/1 HTTP/1.1" 200 OK

### Extract when requesting a non-existent people id
22-Nov-22 01:39:19:f - -WARNING - Requesting people with 6 not successful
INFO:     127.0.0.1:58076 - "GET /people/6 HTTP/1.1" 200 OK
```

## Instructions
- Run command
- When server is launched on a localhost-url, click on localUrl/docs to see the api doc. 
For some reason error handling information is not correct but it would be interesting to find a way to fix it.
- 

## References
- [Official FastAPI tutorial](https://github.com/phalt/swapi/tree/master/resources/fixtures)
- [swapi Github repo data](https://github.com/phalt/swapi/tree/master/resources/fixtures)
- [Logging in Python - RealPython](https://realpython.com/python-logging/)
- [Logging in Python 3 - Official docs](https://docs.python.org/3/howto/logging.html)