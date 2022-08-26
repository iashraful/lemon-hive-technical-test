## Lemon Hive Technical Test Python

### How to run? (Docker)
* Copy the `credentials.json.example` to `credentials.json` (**If you want to call the API from postman/curl.**)
* Run `docker compose up --build -d`
* To run the tests you need to connect to the container. See the following commands
  * `docker compose exec api sh`
  * `pytest -v`
* Application is available at 8091 port.

### If you haven't docker then,
* Copy the `credentials.json.example` to `credentials.json` (**If you want to call the API from postman/curl.**)
* You need to create virtualenv using python 3.8+(Tested with 3.8, 3.9, 3.10)
* Active the venv and install `pip install -r requirements.txt`
* Run the app `flask --app main run --reload --host 0.0.0.0 --port 8091` (You are free to customize your port.)
* Run the test using `pytest -v`

**Thank you :)**