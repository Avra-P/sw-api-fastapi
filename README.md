# sw-api-fastapi
An attempt to implement a simplistic python server that exposes an API. It comes with its functional and performance test suites (ToDo).

It is my first project in Python for test automation, as well as the first project that application development is combined with creating a test automation suite.

## Prerequisites
- Python 3, version 3.8
- PIP managing python packages
- Venv for creating a separate virtual environment for the project. This is order to keep its own requirements independent of global python settings.

## Instructions
- Checkout project current git project.
<br>E.g. in a terminal `git clone git@github.com:Avra-P/sw-api-fastapi.git` or any command that works for you.
- Enter a terminal , navigating inside the `sw-api-fastapi` repo folder
- Install dependencies as saved in `requirements.txt`. 
<br>With `pip` CLI tool it could be `pip install -r requirements.txt`.

### Run server
- Run command `uvicorn app:app --reload` (reload parameter is optional)
- When server is launched on a localhost-url, click on localUrl/docs to see the api doc.
  <br>For some reason error handling information is not correct, but it would be interesting to find a way to fix it.(ToDo)

### Test execution
- For executing functional tests: While server is running , in a separate terminal activate project's virtual environment
```
➜  sw-api-fastapi git:(main) source ./venv/bin/activate # robot is a project dependency
(venv)➜  sw-api-fastapi git:(main) robot ./tests/functional/get_people.robot
```


## More info

- [Notes](./docs/notes.md): a file containing the detailed information and steps on how the project was developed.
- [References](./docs/notes.md#References): Section provides usefull links on tools' tutorials
- [Important missing features](./docs/notes.md#Important-missing-features): Section contains suggestions for missing functionalities that are important.
- [Improvements](./docs/notes.md#Improvements): Section contains more suggested improvements in order to have a complete solution that is properly tested.

