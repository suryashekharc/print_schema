# print_schema

Ever had a complex Python object and wanted to easily see its structure?
**print_schema** makes it super easy to display the structure of complex dictionaries, JSONs, lists, etc
It differs from pprint in that this displays the structure rather than the object itself.

*New:* Use **print_matrix** to display a 2D array (list of lists) in the matrix form.

## Installing

You can download this package from pip:
```
pip install print_schema
```

### How to use this package

```
from print_schema import print_schema
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
print_schema(my_dict, indent=3, dense=False)
```

### Display a list of lists as a matrix
New in version 1.1
```
from print_schema import print_matrix
my_arr = [[11, 312, None, 2],
          [93, -45, 10],
          [-100.3, 8, 192, 5],
          [55, 1.5, 854, 6]]
print_matrix(my_arr, index=True)
```

## Author

* **Surya Shekhar Chakraborty**

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/suryashekharc/print_schema/blob/master/LICENSE) file for details

## Acknowledgments

This project started when I started looking for a native Python equivalent of PySpark/Scala's printSchema() and couldn't find any :)

Much thanks to my favorite after-hours colleague Puneet Jindal for all the help.
