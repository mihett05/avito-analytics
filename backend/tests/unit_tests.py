import json

import requests

tests = [
    {
        "url": "http://localhost:5000/price/1/33/24",
        "method": requests.get,
        "body": {},
        "params": {},
        "awaited answer": {
            "price": 40,
            "matrix_id": 24,
            "location_id": 33,
            "category_id": 1
        }
    }
]


def run_tests():
    try:
        for test in tests:
            kwargs = {"url": test["url"], "params": test["params"]}
            if test["method"] != requests.get:
                kwargs["body"] = test["body"]

            result = test["method"](**kwargs).json()
            assert result == test["awaited answer"]

    except BaseException as err:
        print(err)


if __name__ == '__main__':
    run_tests()
