<h1 align="center">What's this?</h1>
<h3 align="center">This is just simple Django app that can help you log your weather data via REST API</h3>


<ol>
  <li><a href="#base-functionality">Base functionality</a></li>
  <li><a href="#setup">Setup</a></li>
  <li><a href="#usage-example">Usage example</a></li>
  <li><a href="#endpoints">Endpoints</a></li>
  <li><a href="#todos">TODOs</a></li>
</ol>



## Base functionality
* Djoser user login/registration
* Adding and managing your devices
* Logging data to DB via endpoint using given UUID as identifier
* Retrieving data from DB to plot/analyze/do whatever you want
* Exporting device data to CSV
* Axes login bruteforce protection 

## Setup
```
git clone git@github.com:hntirgeam/WIoT-Logger.git
cd smart-home-logger
python3 -m venv env
source env/bin/activate 
pip install -r requirements.txt
```
Now you will need to start PostgreSQL. For example you can run it in docker:
```
docker run -p 5435:5432 -e POSTGRES_USER=logger_drf -e POSTGRES_PASSWORD=logger_drf -e POSTGRES_DB=logger_drf -v $(pwd)/psql_volume:/var/lib/postgresql/data -d postgres:latest
```

```
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```
And it's done. 


## Usage example
I'm using this [sketch](https://github.com/hntirgeam/ESP8266-WIoT#wiring) on ESP8266 with connected MH-Z19b and BME280 sensors to it.
Every 10 seconds it sends data to endpoint and it logs it successfully.


## Endpoints

* `POST: auth/users/` - User registration. Accepts `{"username": username, "password": password}`
* `POST: auth/token/login/` - User login. Accepts `{"username": username, "password": password}`. Returns Token
* `GET: users/me/` - Returns some info and your devices. Needs auth_token headers! `{'Authorization': 'Token <token>'}` 
* `GET: devices/<int:pk>` - Returns device with entered id with all of its records. Needs auth_token headers! `{'Authorization': 'Token <token>'}`
* `POST: record/` - Creats new record for device. Accepts 
```
{
    "uuid": "received uuid when device was registered",
    "temp": Decimal with 8 point precision,
    "humidity": Decimal with 8 point precision,
    "pressure": Decimal with 8 point precision,
    "CO2": Decimal with 8 point precision,
    "eTVOC": Decimal with 8 point precision,
}
```
Everything except for UUID may be blank


## TODOs
- [x] Write .ino sketch for ESP8266
- [ ] Write semi-usable frontend for this project
- [ ] Dockerize everything 
- [ ] Tests? No way...
- [ ] Gunicorn..?










