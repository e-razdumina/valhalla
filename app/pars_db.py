from pars_functions import vikings_tv_pars, norsemen_tv_pars_wiki, norsemen_nfl_wiki
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.flask_db
todos = db.valhalla

vikings_tv = vikings_tv_pars()
nors_tv = norsemen_tv_pars_wiki()
nors_team = norsemen_nfl_wiki()

info = [vikings_tv, nors_tv, nors_team]

for i in info:
    todos.insert_many(i)


