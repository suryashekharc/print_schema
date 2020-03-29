import json


def is_json(obj: str) -> bool:
    """ Checks if an object is a valid JSON string

    :param obj: Any Python object
    :return:    True if obj is a JSON object, else returns False
    """
    try:
        json_object = json.loads(obj)
    except ValueError as e:
        return False
    return True


def is_which_const(obj):
    """ Checks if an object is a constant data-type

    :param obj: A Python object
    :return:    Returns if the type of object is a string, integer, float, complex-number,
                tuple, ot boolean - considered constants
    """
    return type(obj) if type(obj) in [str, int, float, complex, tuple, bool] else None


def _get_indent(level: int, indent: int = 4, dense: bool = False):
    """ Given a level and indent, return the preceding indent of an output row

    :param level:   Degree of nesting
    :param indent:  Number of whitespaces at every indent level
    :param dense:   True would print vertical lines at every level
    :return:        String of indent preceding the actual output
    """
    if not dense:
        one_tab = " " * indent
    else:
        one_tab = "|" + " " * (indent - 1)
    pre_str_indent = one_tab * level + "|- "
    return pre_str_indent


# Considering only homogeneous list in the first iteration
# TODO: Support list of dictionaries in a better way
def print_list(my_list: list, level: int = 1, indent: int = 4, dense: bool = False,
               list_name: str = " list ") -> None:
    """ Recursively prints the structure of a list and its length

    :param my_list:     List to print
    :param level:       Degree of nesting
    :param indent:      Number of whitespaces at every indent level
    :param dense:       True would print vertical lines at every level
    :param list_name:   Name of the list to print
    :return:            Prints the list recursively
    """
    type_list = list(set([type(elt) for elt in my_list]))
    if len(type_list) == 1:
        print(_get_indent(level, indent, dense) + list_name + "\t - " + "list [{}] ".format(len(my_list)) \
              + str(type(my_list[0])))
        if type_list[0] is dict:
            print_dictionary(my_list[0], level + 1, indent, dense)
    elif len(type_list) > 1:
        print(_get_indent(level, indent, dense) + list_name + "\t - " + "list [{}] <heterogeneous list>". \
              format(len(my_list)))
    elif len(type_list) == 0:
        print(_get_indent(level, indent, dense) + list_name + "\t - " + "list [{}] <empty list>". \
              format(len(my_list)))
    else:
        print(_get_indent(level, indent, dense) + list_name + "\t - " + "list [{}] ".format(len(my_list)))


def print_dictionary(my_dict: dict, level: int = 1, indent: int = 4, dense: bool = False) -> None:
    """ Recursively prints the structure of a dictionary and the types of the values of its keys

    :param my_dict:     Dictionary to print
    :param level:       Degree of nesting
    :param indent:      Number of whitespaces at every indent level
    :param dense:       True would print vertical lines at every level
    :return:            Prints the dictionary recursively
    """
    for key, val in my_dict.items():
        const_type = is_which_const(val)
        if const_type:
            print(_get_indent(level, indent, dense) + str(key) + "\t - " + str(const_type))
        elif type(val) is dict:
            print(_get_indent(level, indent, dense) + str(key) + "\t - " + str(type(val)))
            print_dictionary(val, level + 1, indent, dense)
        elif type(val) is list:
            print_list(val, level, indent, dense, str(key))
        else:
            print("Not supported")


def print_json_str(my_json_string: str, level: int = 1, indent: int = 4, dense: bool = False) -> None:
    json_dict = json.loads(my_json_string)
    print_dictionary(json_dict, level, indent, dense)


def print_schema(obj, indent: int = 4, dense: bool = False, level: int = 0) -> None:
    """ Prints the schema of a Python object

    :param obj:         Python object
    :param indent:      Number of whitespaces at every indent level
    :param dense:       True would print vertical lines at every level
    :param level:       Degree of nesting, initially it is 0
    :return:            Recursively prints the structure of the Python object
    """
    if type(obj) is dict:
        print_dictionary(obj, level, indent, dense)
    elif type(obj) is list:
        print_list(obj, level, indent, dense)
    elif is_json(obj):
        print_json_str(obj, level, indent, dense)
    elif is_which_const(obj) is not None:
        print("Constant type: {}".format(is_which_const(obj)))
    else:
        print("Data-type not currently supported. Sorry!")


def is_valid_matrix(array: list) -> bool:  # Returns False if array is not a list of lists
    if type(array) is not list:
        print("Error: array is not a list")
        return False
    for row in array:
        if type(row) is not list:
            print("Error: row in array is not a list")
            return False
    if len(array) < 1:
        return False
    return True


def print_matrix(array: list, index: bool = True) -> None:
    """ Pretty print a 2D array

    :param array: List of lists, the array to print
    :param index: Boolean, True will print array indices
    :return:      The array, displayed as a matrix
    """
    if not is_valid_matrix(array):
        return
    row_len = len(str(len(array)))  # If there are 6470 rows, row_len is 4
    max_space_len = max(max([len(str(item)) for row in array for item in row]), row_len)  # Used to fix indent spaces
    if not index:
        print('\n'.join([''.join(['{:>{}}'.format(str(item), max_space_len) for item in row])
                         for row in array]))
    else:
        print('{:{}} |'.format('', row_len), end='')
        for col_index in range(max([len(row) for row in array])):
            print('{:{}}'.format(col_index, max_space_len), end='')
        print()
        print('{:{}} |'.format('-' * row_len, row_len), end='')
        print('{:{}}'.format('-' * max_space_len, max_space_len) * max(
            [len(row) for row in array]))
        for row_index, row in enumerate(array):
            print('{:{}} |'.format(row_index, row_len), end='')
            for val in row:
                print('{:>{}}'.format(str(val), max_space_len), end='', sep=' ')
            print()
