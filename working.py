from fastapi import FastAPI

app = FastAPI()

inventory = {
    1: {
        "name": "milk",
        "price": 5000,
        "brand": "peak"
    }
}
@app.get("/get_item/{item_id}")
def get_item(item_id: int):
    return inventory[item_id]

@app.get("/get_by_name")
def get_item(name: str):
    for item in inventory:
        if inventory[item]["name"] == name:
            return inventory[item]
    return {"Data": "Not found"}
