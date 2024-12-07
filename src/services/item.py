from db.repository.item import get_item_by_id, get_items_by_archive_number

async def get_one_item(session, item_id):
    itemFound = session.exec(get_item_by_id(item_id)).all()
    if(len(itemFound) > 0):
        return { "ok":itemFound[0] }

    return { "code":404, "message":"Item not found"}

async def get_many_by_archive_number(session, archive_number):
    items = session.exec(get_items_by_archive_number(archive_number)).all()
    return { "ok":items }
