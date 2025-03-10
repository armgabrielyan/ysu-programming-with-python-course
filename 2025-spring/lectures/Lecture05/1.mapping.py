from typing import Dict

# def get_value(d: Dict[str, int], key: str) -> int:
def get_value(d: dict[str, int], key: str) -> int:
    return d.get(key, 0)

mapping = {"apple": 10, "banana": 20}

get_value(mapping, "apple")
get_value(mapping, "orange")
