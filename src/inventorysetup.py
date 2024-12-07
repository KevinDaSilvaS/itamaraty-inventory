def parse_inventory_csv():
    f = open("inventory.csv", "r")
    f.readline() #discarding keys

    items = []
    while (True):
        line = f.readline()
        if (line == ''):
            break
        line = line.split(';')
        parsed_item = {
            "section":line[0],
            "location":line[1],
            "archive_number":line[2],
            "amount":line[5],
            "description":line[6],
            "origin":line[10],
            "conservation_status":line[13],
            "obs":line[14]
        }
        items.append(parsed_item)

    return items
