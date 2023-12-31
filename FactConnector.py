import requests
import json
from flask import Flask

app = Flask(__name__)


@app.route('/')
def fact_connection():
    response = requests.get("https://cat-fact.herokuapp.com/facts/")
    connection = response.json()
    fact_str = json.dumps(connection)
    fact_dict = json.loads(fact_str)

    for idx, fact_dict in enumerate(fact_dict, start=1):
        return fact_dict['text']

if __name__ == '__main__':
    app.run()
