from fastapi import FastAPI
from user_service import user_services
import requests

app = FastAPI()
# review the following lists
products = ['rice','shoes','shirts','pants','socks','hats','gloves','scarves','coats','jackets','sweaters','sweatshirts','shorts','skirts','dresses','suits','blazers','underwear','bras','socks','pajamas','robes','slippers','boots','sandals','sneakers','heels','flats','loafers','oxfords','pumps','t-shirts','polos','tank tops','blouses','tunics','cardigans','turtlenecks','vests','sweatpants','leggings','jeans','trousers','joggers','chinos','overalls','jumpsuits','rompers','swimsuits','cover-ups','sunglasses','eyeglasses','belts','hats','gloves','scarves','umbrellas','watches','bracelets','rings','earrings','necklaces','handbags','backpacks','clutches','briefcases','luggage','totes','wallets','crossbody bags','satchels','duffel bags','tote bags','shoulder bags','hobo bags','bucket bags','messenger bags','wristlets','baguettes','bowling bags','saddle bags','sunglasses','eyeglasses','belts','hats','gloves','scarves','umbrellas','watches','bracelets','rings','earrings','necklaces','handbags','backpacks','clutches','briefcases','luggage','totes','wallets','crossbody bags','satchels','duffel bags','tote bags','shoulder bags','hobo bags','bucket bags','messenger bags','wristlets','baguettes','bowling bags','saddle bags']

@app.get("/")
async def read_main():
    return {"message": "Hello World"}

@app.get("/items/{item_id}/{item_name}/{item_description}")
async def read_item(item_id: int, item_name: str, item_description: str):
    return {"id": item_id, "name": item_name, "desscription": item_description}


@app.get("/users")
def get_users():
    users = user_services.get_users_from_db()
    return users

@app.get("/get_activities")
def get_activities():
    response = requests.get('https://www.boredapi.com/api/activity')
    new_json = response.json()
    return new_json['activity']
