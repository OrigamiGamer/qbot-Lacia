import json
from pathlib import Path

# path
dir_config = Path(__file__).parent.joinpath(Path("config"))

path_apikey = dir_config.joinpath(Path("apikey.json"))

path_user_database = dir_config.joinpath(Path("user-database.json"))


# json
json_apikey: dict[str, str] = {}


# load config
with open(path_apikey, encoding="utf-8") as file_apikey:
    json_apikey = json.load(file_apikey)
