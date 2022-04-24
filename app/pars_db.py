from pars_functions import vikings_tv_pars, norsemen_tv_pars_wiki, norsemen_nfl_wiki
from pymongo import MongoClient

client = MongoClient('localhost', 27017, tls=True)

db = client.flask_db
todos = db.valhalla

vikings_tv = todos.insert_many(vikings_tv_pars())
nors_tv = todos.insert_many(norsemen_tv_pars_wiki())
nors_team = todos.insert_many(norsemen_nfl_wiki())

