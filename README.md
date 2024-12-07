# Itamaraty Inventory

#### This is a small Rest api built with fast api(first time using it BTW) that parses the official Itamaraty(Brazilian external relations ministery) Inventory CSV file and adds it to a sqlite db allowing for searches trough REST endpoints

## How to use it
- Make sure you have python + pip installed
- then run 
    ` pip install -r requirements.txt `
- then set up a venv like: https://fastapi.tiangolo.com/virtual-environments/#activate-the-virtual-environment

- and then run ` fastapi dev main.py`

## How to use the endpoints
#### Currently there are 2 endpoints that matter in the API:

` /inventory/{item_id} `
Who is reponsible for returning one single item by its id or returning a 404

` {
    "result": {
        "archive_number":"7760","description":"Tapete Aubusson, estylo Luiz XIV, 1840, com 8,m.37 x 10,m.10.","conservation_status":"Usado","amount":"1","section":" Geral ","id":1,"origin":"Fab. Aubusson - Franï¿½a","obs":"em branco"
    }
} `

` /inventory/archive/{archive_number} `
Who is reponsible for returning a list of items that belong to the same archive_number

` {
    "result": [
    {"description":"Tapete Aubusson, estylo Luiz XIV, 1840, com 8,m.37 x 10,m.10.","archive_number":"7760","conservation_status":"Usado","section":" Geral ","id":1,"amount":"1","origin":"Fab. Aubusson - Franï¿½a","obs":"em branco"},

    {"description":"Cortinas cantoneiras, de Aubusson, de seda, estylo Regencia, fundo rosa e creme com flï¿½res.","archive_number":"7760","conservation_status":"Bom","section":" Geral  ","id":2,"amount":"8","origin":"Fab. Aubusson - Franï¿½a","obs":"Comprados em 1907"},
    
    {"description":"Cortinas Auusson, de seda, compostas de 2 pernas e 1 bando semelhantes aos ns. 2 a 9.","archive_number":"7760","conservation_status":"Bom","section":" Geral ","id":3,"amount":"4","origin":"Fab. Aubusson - Franï¿½a","obs":"em branco "},
    
    {"description":"Sanefas de imbuia dourada, estylo Luiz XIV.","archive_number":"7760","conservation_status":"Bom","section":" Geral ","id":4,"amount":"12","origin":"Leandro Martins & Cia. ","obs":"Copia da antiga."},
    
    {"description":"Espelhos, estylo Regencia, moldura de imbuia dourada, com 5,m.20 x 2,m.40.","archive_number":"7760","conservation_status":"Bom","section":" Geral ","id":5,"amount":"2","origin":"Leandro Martins & Cia. ","obs":"Copia da antiga "},
    
    {"description":"Lustres de bronze dourado com pingentes de crystal, e correntes com 12 mangas de crystal, estylo Regencia.","archive_number":"7760","conservation_status":"Bom","section":" Geral ","id":6,"amount":"4","origin":"Franï¿½a ","obs":"em branco "},
    
    {"description":"Sofï¿½s de imbuia dourada com Aubusson de seda, desenho  igual aos ns. 2 a 9 com 2,m.55 de assento e as iniciais R.E R.E. O madeiramento foi reformado em 1927. A tapeï¿½aria foi feita em 1907.","archive_number":"7760","conservation_status":"Usado","section":" Geral ","id":7,"amount":"2","origin":"Fab. Aubusson - Franï¿½a","obs":"em branco "},
    
    {"description":"Poltronas do mesmo grupo que os ns. 32 e 33. Com 0,m.75 de assento. ","archive_number":"7760","conservation_status":"Usado","section":" Geral ","id":8,"amount":"18","origin":"em branco ","obs":"em branco "},
    
    {"description":"Braï¿½adeiras de bronze dourada, estylo Regencia para vidraï¿½as e para bandeiras. ","archive_number":"7760","conservation_status":"Bom","section":" Geral ","id":9,"amount":"8","origin":"Paris ","obs":"em branco "},
    
    {"description":"Tapete Aubusson, estylo Luiz XIV, 1840, com 8,m.37 x 10,m.10.","archive_number":"7760","conservation_status":"Usado","section":" Geral ","id":1963,"amount":"1","origin":"Fab. Aubusson - Franï¿½a","obs":"em branco"},
    
    {"description":"Cortinas cantoneiras, de Aubusson, de seda, estylo Regencia, fundo rosa e creme com flï¿½res.","archive_number":"7760","conservation_status":"Bom","section":" Geral  ","id":1964,"amount":"8","origin":"Fab. Aubusson - Franï¿½a","obs":"Comprados em 1907"},
    
    {"description":"Cortinas Auusson, de seda, compostas de 2 pernas e 1 bando semelhantes aos ns. 2 a 9.","archive_number":"7760","conservation_status":"Bom","section":" Geral ","id":1965,"amount":"4","origin":"Fab. Aubusson - Franï¿½a","obs":"em branco "},
    
    {"description":"Sanefas de imbuia dourada, estylo Luiz XIV.","archive_number":"7760","conservation_status":"Bom","section":" Geral ","id":1966,"amount":"12","origin":"Leandro Martins & Cia. ","obs":"Copia da antiga."},
    
    {"description":"Espelhos, estylo Regencia, moldura de imbuia dourada, com 5,m.20 x 2,m.40.","archive_number":"7760","conservation_status":"Bom","section":" Geral ","id":1967,"amount":"2","origin":"Leandro Martins & Cia. ","obs":"Copia da antiga "},
    
    {"description":"Lustres de bronze dourado com pingentes de crystal, e correntes com 12 mangas de crystal, estylo Regencia.","archive_number":"7760","conservation_status":"Bom","section":" Geral ","id":1968,"amount":"4","origin":"Franï¿½a ","obs":"em branco "},
    
    {"description":"Sofï¿½s de imbuia dourada com Aubusson de seda, desenho  igual aos ns. 2 a 9 com 2,m.55 de assento e as iniciais R.E R.E. O madeiramento foi reformado em 1927. A tapeï¿½aria foi feita em 1907.","archive_number":"7760","conservation_status":"Usado","section":" Geral ","id":1969,"amount":"2","origin":"Fab. Aubusson - Franï¿½a","obs":"em branco "},
    
    {"description":"Poltronas do mesmo grupo que os ns. 32 e 33. Com 0,m.75 de assento. ","archive_number":"7760","conservation_status":"Usado","section":" Geral ","id":1970,"amount":"18","origin":"em branco ","obs":"em branco "},
    
    {"description":"Braï¿½adeiras de bronze dourada, estylo Regencia para vidraï¿½as e para bandeiras. ","archive_number":"7760","conservation_status":"Bom","section":" Geral ","id":1971,"amount":"8","origin":"Paris ","obs":"em branco "}
        ]   
    } `
