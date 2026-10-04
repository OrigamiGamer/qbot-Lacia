import json

import config

# json
json_user_database: dict[str, dict[str, str]] = {}

with open(config.path_user_database, encoding="utf-8") as file_user_database:
    json_user_database = json.load(file_user_database)


def __save_user_database():
    with open(
        config.path_user_database, encoding="utf-8", mode="w"
    ) as file_user_database:
        json.dump(json_user_database, file_user_database)


def is_user_registered(uid: str) -> bool:
    return json_user_database.get(uid) != None


def set_user_name(uid: str, name: str) -> bool:
    if is_user_registered(uid=uid) == True:
        json_user_database[uid]["name"] = name
        __save_user_database()
        return True
    return False


def register_user(uid: str, name: str = "unknown"):
    json_user_database[uid] = dict[str, str]()
    json_user_database[uid]["name"] = name
    json_user_database[uid]["permission_level"] = "user"
    __save_user_database()


def get_user_info(uid: str, item: str) -> str:
    value: str = ""
    if is_user_registered(uid) == True and json_user_database[uid].get(item) != None:
        value = json_user_database[uid][item]
    return value
