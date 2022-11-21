import json

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get('/')
def index():
    return {"This the Starwars API test project. Only  /people, /starships, /planets are supported"}


# Handle the people related data and endpoints
class Person(BaseModel):
    id: Optional[int] = None
    edited: str
    name: str
    created: str
    gender: str
    skin_color: str
    hair_color: str
    height: str
    eye_color: str
    mass: str
    homeworld: int
    birth_year: str
    starships: list


with open('./resources/people.json', 'r') as f:
    people = json.load(f)['people']


@app.get('/people')
def get_people():
    return people


@app.get('/people/{p_id}')
def get_person(p_id: int):
    person = [p for p in people if p['id'] == p_id]
    if len(person) > 0:
        return person[0]
    else:
        return HTTPException(status_code=404, detail=f"person with id:{p_id} does not exist")


# Handle the starship related data and endpoints
class Starship(BaseModel):
    id: Optional[int] = None
    model: str
    manufacturer: str
    cost_in_credits: str
    length: str
    max_atmosphering_speed: str
    crew: str
    passengers: str
    cargo_capacity: str
    consumables: str
    hyperdrive_rating: str
    MGLT: str
    starship_class: str
    pilots: list
    created: str
    edited: str


with open('./resources/starships.json', 'r') as f:
    starships = json.load(f)['starships']


@app.get('/starships')
def get_starships():
    return starships


@app.get('/starships/{s_id}')
def get_starship(s_id: int):
    # todo handle 404 error
    starship = [p for p in people if p['id'] == s_id]
    if len(starship) > 0:
        return starship[0]
    else:
        return HTTPException(status_code=404, detail=f"starship with id:{s_id} does not exist")


# Handle the planet related data and endpoints
class Planet(BaseModel):
    id: Optional[int] = None
    edited: str
    climate: str
    surface_water: str
    name: str
    diameter: str
    rotation_period: str
    created: str
    terrain: str
    gravity: str
    orbital_period: str
    population: str
    residents: list


with open('./resources/planets.json', 'r') as f:
    planets = json.load(f)['planets']


@app.get('/planets')
def get_planets():
    return planets


@app.get('/planets/{p_id}')
def get_planets(p_id: int):
    # todo handle 404 error
    planet = [p for p in planets if p['id'] == p_id]
    if len(planets) > 0:
        return planet[0]
    else:
        return HTTPException(status_code=404, detail=f"planet with id:{p_id} does not exist")
