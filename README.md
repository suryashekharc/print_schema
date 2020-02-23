# print_schema

Ever had a complex Python object and wanted to easily see its structure?
print_schema makes it super easy to display the structure of complex dictionaries, JSONs, lists, etc

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

## Authors

* **Surya Shekhar Chakraborty**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This project started when I started looking for an equivalent of the printSchema function available in PySpark and Scala.