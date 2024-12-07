from fastapi import FastAPI, HTTPException
from src.inventorysetup import parse_inventory_csv
from db.conn.conn import create_db_and_tables, session, SessionDep
from db.models.item import Item
from src.services.item import get_one_item, get_many_by_archive_number

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    items = parse_inventory_csv()
    
    with session:
        session.bulk_insert_mappings(Item, items)
        session.commit()
    return

@app.get("/")
async def root():
    return {"result": "Hello World"}

@app.get("/inventory/archive/{archive_number}")
async def get_items_archive_number(s: SessionDep, archive_number):
    return {
        "result": (await get_many_by_archive_number(s, archive_number)).get("ok")
    }

@app.get("/inventory/{item_id}")
async def get_item(s: SessionDep, item_id):
    result = await get_one_item(s, item_id)
    if(result.get("ok")):
        return {"result": result.get("ok")}
    raise HTTPException(status_code=result.get("code"), detail=result.get("message"))
    