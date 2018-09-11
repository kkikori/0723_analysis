import sys
import csv
from .DummyUserClass import DummyUser


def data_load(f_n):
    if not f_n.exists():
        print("[FILE ERROR]", f_n, "is not found.")
        sys.exit()

    users_list = {}
    with f_n.open("r") as f:
        reader = csv.reader(f)
        header = next(reader)
        index_user = header.index("user_id")
        for row in reader:
            if row[index_user] not in users_list.keys():
                newuser = DummyUser(row[index_user])
                users_list[row[index_user]] = newuser

