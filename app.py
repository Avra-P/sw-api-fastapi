import json
import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

logging.basicConfig(format='%(asctime)s - -%(levelname)s - %(message)s',
                    level=logging.INFO,
                    datefmt='%d-%b-%y %H:%M:%S:%f')

app = FastAPI()


@app.get('/')
def index():
    return {"This the Starwars API test project. Only  /people, /starships, /planets are supported"}


# Following classes demonstrate how a base model would look like for the 3 data categories the project supports
# Currently they are not in use.
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


# Handle the people related data and endpoints
with open('./resources/people.json', 'r') as f:
    people = json.load(f)['people']
    if people:
        logging.info("People data loaded from json file")
    else:
        logging.debug("Could not load people.json file.")  # not replicated


@app.get('/people')
def get_people():
    logging.debug("Could not return people data.")
    return people


@app.get('/people/{p_id}')
async def get_person(p_id: int):
    person = [p for p in people if p['id'] == p_id]
    logging.debug(f"Requesting person with if{p_id}")
    if len(person) <= 0:
        logging.debug(f"Planet with ID {p_id} not found")
        raise HTTPException(status_code=404, detail=f"person does not exist")
    else:
        logging.info(f"Planet with ID {p_id} found")
        return person[0]


# Handle the starship related data and endpoints
with open('./resources/starships.json', 'r') as f:
    starships = json.load(f)['starships']


@app.get('/starships')
def get_starships():
    return starships


@app.get('/starships/{s_id}')
async def get_starship(s_id: int):
    starship = [p for p in starships if p['id'] == s_id]
    logging.debug(f"Requesting starship with idf{s_id}")
    if len(starship) <= 0:
        logging.debug(f"Starship with ID {s_id} not found")
        raise HTTPException(status_code=404, detail=f"starship does not exist")
    else:
        logging.info(f"Starship with ID {s_id} found")
        return starships[0]


with open('./resources/planets.json', 'r') as f:
    planets = json.load(f)['planets']


@app.get('/planets')
def get_planets():
    return planets


@app.get('/planets/{p_id}')
async def get_planet(p_id: int):
    planet = [p for p in planets if p['id'] == p_id]
    logging.debug(f"Requesting planet with id{p_id}")
    if len(planet) <= 0:
        logging.debug(f"Planet with ID {p_id} not found")
        raise HTTPException(status_code=404, detail=f"planet does not exist")
    else:
        logging.info(f"Planet with ID {p_id} found")
        return planet[0]
