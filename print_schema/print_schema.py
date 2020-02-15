"""

TODO:
    1. Add support for alphabetical arrangement
    2. Nested indent
    3. Add support for a collected Pyspark Row
"""

import json


def is_json(obj):
    """

    :param obj: Any Python object
    :return:    True if obj is a JSON object, else returns False
    """
    try:
        json_object = json.loads(obj)
    except ValueError as e:
        return False
    return True


def is_which_const(obj):
    """

    :param obj: A Python object
    :return:    Returns if the type of object is a string, integer, float, complex-number,
                tuple, ot boolean - considered constants
    """
    return type(obj) if type(obj) in [str, int, float, complex, tuple, bool] else None


# Considering only homogeneous list in the first iteration
def print_list(my_list, level=1, list_name=" list "):
    type_list = list(set([type(elt) for elt in my_list]))
    if len(type_list) == 1:
        print("|\t" * level + list_name + "\t - " + "list [{}] ".format(len(my_list)) \
              + str(type(my_list[0])))
        if type_list[0] is dict:
            print_dictionary(my_list[0], level + 1)
    elif len(type_list) > 1:
        print("|\t" * level + list_name + "\t - " + "list [{}] <heterogeneous list>". \
              format(len(my_list)))
    elif len(type_list) == 0:
        print("|\t" * level + list_name + "\t - " + "list [{}] <empty list>". \
              format(len(my_list)))
    else:
        print("|\t" * level + list_name + "\t - " + "list [{}] ".format(len(my_list)))


def print_dictionary(my_dict, level=1):
    for key, val in my_dict.items():
        const_type = is_which_const(val)
        if const_type:
            print("|\t" * level + str(key) + "\t - " + str(const_type))
        elif type(val) is dict:
            print("|\t" * level + str(key) + "\t - " + str(type(val)))
            print_dictionary(val, level + 1)
        elif type(val) is list:
            print_list(val, level, str(key))
        else:
            print("Not supported")


def print_json_str(my_json_string, level=1):
    json_dict = json.loads(my_json_string)
    print_dictionary(json_dict, 1)
    pass


def print_schema(obj):
    if type(obj) is dict:
        print_dictionary(obj, 1)
    elif type(obj) is list:
        print_list(obj, 1)
    elif is_json(obj):
        print_json_str(obj, 1)
    elif is_which_const(obj) is not None:
        print("Constant type: {}".format(is_which_const(obj)))
    else:
        print("Data-type not currently supported. Sorry!")
