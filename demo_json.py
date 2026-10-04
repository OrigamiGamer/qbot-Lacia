import json
from typing import Any

json_personal_info: dict[str, Any] = json.loads(
    json.dumps(
        {"name": "unknown", "race": "精灵", "age": "1000"},
        ensure_ascii=False,
        indent=2,
    )
)

json_personal_info["name"] = "Alice"

print(json_personal_info["name"])
