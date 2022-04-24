# Understanding Valhalla

1. Clone Git repository
git clone https://github.com/e-razdumina/valhalla.git

2. Create db via pars_db.py
python pars_db.py
OR import
mongoimport -d flask_db -c valhalla db.json

3. Set the FLASK_ENV environment variable
export FLASK_APP=app

4. Go to local host
http://127.0.0.1:5000/
