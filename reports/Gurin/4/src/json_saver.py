from json import dump

from const import JSON_BASE_FILENAME


def save_data_to_json(username: str, data: str) -> None:
    with open(username + "-" + JSON_BASE_FILENAME, "w", encoding="utf-8") as file:
        dump(data, file, ensure_ascii=False, indent=4)
