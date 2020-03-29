import time

from print_schema import print_schema, print_matrix


def run_matrix(my_arr=None):
    if my_arr is None:
        my_arr = [[11, 312, None, 2], [93, -45, 10], [-100.3, 8, 192, 5], [55, 1.5, 854, 6]]
    print("With index=False:")
    print_matrix(my_arr, index=False)
    print("With index=True:")
    print_matrix(my_arr)


def run_json(json_path="https://transit.land/api/v1/routes.geojson?"
                       "operated_by=o-d2g6-transmilenio~alimentadores&per_page=false"):
    import requests
    resp = requests.get(json_path)
    dat = resp.json()
    print_schema(dat, indent=6, dense=True)


def run_dict(my_dict=None):
    if my_dict is None:
        my_dict = {"bts": {"members": 7,
                           "bias": "Kim Tae-hyung",
                           "albums": {"first": "Dark & Wild",
                                      "peak_chart_position": {"Japan": 30, "Korea": 2},
                                      "favorite_songs": ["Blood Sweat and Tears", "Boy with luv"]},
                           "more_members_alive_than_dead": True,
                           (2, 3): "a random tuple"},
                   "beatles": {"members": 4,
                               "bias": "George Harrisom",
                               "albums": {"first": "Please Please Me",
                                          "peak_chart_position": {"UK": 1, "France": 5, "Germany": 5},
                                          "favorite_songs": ["Eleanor Rigby", "While My Guitar Gently Weeps"]},
                               "more_members_alive_than_dead": False,
                               (4, 5): "another random tuple"}}
    print_schema(my_dict)


def run_list(my_list=None):
    # TODO: Add support for list of dictionaries and other heterogeneous lists
    if my_list is None:
        my_list = [{"a": [3, 4]}, {"a": 7}, {"a": 6, "b": 4}]
    print_schema(my_list)


if __name__ == "__main__":
    print("Running dictionary...")
    run_dict()
    time.sleep(2)
    print("Running list...")
    run_list()
    time.sleep(2)
    print("Running matrix...")
    run_matrix()
    time.sleep(2)
    print("Running JSON... (this may take some time based on your internet connection)")
    run_json()
    print("Finished running all.")
