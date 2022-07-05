import re
from dao import DAO
import os
from dao_db_users import DAO_db_users
from dao_db_community import DAO_db_community

from dao_csv import DAO_csv
from dao_json import DAO_json
from dao_api import DAO_api
from dao_linkedDataHub import DAO_linkedDataHub
import json

import requests
from requests.auth import HTTPBasicAuth

from bson.json_util import dumps, loads

from dao import DAO


def main():

    dao = DAO_db_users("localhost", 27018, "spice", "spicepassword")
    # dao = DAO_db_community("localhost", 27018, "spice", "XXX")

    dao.drop()
    user1 = {
        "userid": "001",
        "origin": "aaa",
        "source_id": "bbb",
        "age": "22",
        "gender": "F",
        "hobby": "bwm"
    }
    user2 = {
        "userid": "001",
        "origin": "aaa",
        "source_id": "bbb",
        "age": "19",
        "gender": "M",
        "religion": "AA"
    }
    correctResponse = {
        'userid': '001',
        'origin': 'aaa',
        'source_id': 'bbb',
        'hobby': 'bwm',
        'gender': 'M',
        'age': '19',
        'religion': 'AA',
        '_id': "xxx"
    }
    dao.insertUser(user1)
    print(dao.getUsers())
    dao.updateUser(user2)

    # print(dao.getUser("001"))
    print(dao.getUsers())


main()
