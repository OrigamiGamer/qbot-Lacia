import json
from pathlib import Path

# path
dir_config = Path(__file__).parent.joinpath(Path("config"))

path_apikey = dir_config.joinpath(Path("apikey.json"))

path_user_database = dir_config.joinpath(Path("user-database.json"))


# json
json_apikey: dict[str, str] = {}


# check and complete directories and config files
if dir_config.exists() == False:
    dir_config.mkdir(parents=True, exist_ok=True)

if path_apikey.exists() == False:
    with open(path_apikey, encoding="utf-8", mode="w") as file_apikey:
        __default_json_apikey: dict[str, str] = {"appid": "", "secret": ""}
        json.dump(__default_json_apikey, file_apikey)

if path_user_database.exists() == False:
    with open(path_user_database, encoding="utf-8", mode="w") as file_user_database:
        __default_json_user_database: dict[str, dict[str, str]] = {
            "uid": {"name": "unknown", "permission_level": "user"}
        }
        json.dump(__default_json_user_database, file_user_database)


# load config
with open(path_apikey, encoding="utf-8") as file_apikey:
    json_apikey = json.load(file_apikey)
