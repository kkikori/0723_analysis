import sys
import csv
from collections import OrderedDict
from .DummyUserClass import DummyUser
from .DummyPostClass import DummyPost


def data_load(f_n):
    if not f_n.exists():
        print("[FILE ERROR]", f_n, "is not found.")
        sys.exit()

    users_list = {}
    post_list = OrderedDict()
    post_index = 0
    with f_n.open("r") as f:
        reader = csv.reader(f)
        header = next(reader)
        index_user = header.index("user_id")
        for row in reader:
            # 新規ユーザのリストへの追加
            if row[index_user] not in users_list.keys():
                newuser = DummyUser(row[index_user])
                users_list[row[index_user]] = newuser
            # 投稿リストへの追加
            newpost = DummyPost(row[0], row[1], row[2], row[3], \
                                row[4], row[5], row[6], post_index)
            post_list[row[0]] = newpost
            post_index += 1

    return users_list, post_list
