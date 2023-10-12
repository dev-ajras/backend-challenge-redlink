import os
import json
from config import config
from src import init_app

configuration = config['development']
app = init_app(configuration)

db_file = 'db.json'
if not os.path.isfile(db_file):
    initial_data = {
        "users": []
    }
    with open(db_file, 'w') as file:
        json.dump(initial_data, file)

if __name__ == '__main__':
    app.run()