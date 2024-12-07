from sqlmodel import select
from db.models.item import Item

def get_items_by_archive_number(archive_number):
    return select(Item).where(Item.archive_number == archive_number)

def get_item_by_id(id):
    return select(Item).where(Item.id == id)

def get_items():
    return select(Item)