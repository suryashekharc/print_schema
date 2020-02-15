import time

from print_schema import print_schema


def test_json(json_path="https://transit.land/api/v1/routes.geojson?"
                        "operated_by=o-d2g6-transmilenio~alimentadores&per_page=false"):
    import requests
    resp = requests.get(json_path)
    dat = resp.json()
    print_schema(dat)


def test_dict(my_dict=None):
    if my_dict is None:
        my_dict = {"first_dict":{"al": 2, "bravo": "bee",
                    "charlie": {"two": 3, 6: [3, 4, 5]}, (2, 3): "two-three"},
                   "second_dict":
                   {"definitions": {"address": {"type": "object", "properties": {
                       "street_address": {"type": "string"},
                       "city": {"type": "string"},
                       "state": {"type": "string"}
                   }, "required": ["street_address", "city", "state"]}}}}
    print_schema(my_dict)


def test_list(my_list=None):
    if my_list is None:
        my_list = [{"a": [3, 4]}, {"a": 7}, {"a": 6, "b": 4}]
    print_schema(my_list)


if __name__ == "__main__":
    print("Testing dictionary...")
    test_dict()
    time.sleep(2)
    print("Testing list...")
    test_list()
    time.sleep(2)
    print("Testing JSON... (this may take some time based on your internet connection")
    test_json()
    print("Tests finished running.")
