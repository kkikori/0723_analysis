import sys
import csv
from collections import OrderedDict
import DummyUserClass
import DummyPostClass


def data_load(f_n):
    if not f_n.exists():
        print("[FILE ERROR]", f_n, "is not found.")
        sys.exit()

    users_list = {}
    post_list = OrderedDict()
    with f_n.open("r") as f:
        reader = csv.reader(f)
        header = next(reader)
        #index_user = header.index("user_id")
        for row in reader:
            # 新規ユーザのリストへの追加
            if row[2] not in users_list.keys():
                print(row[2])
                newuser = DummyUserClass.DummyUser(row[2])
                users_list[row[2]] = newuser
            # 投稿リストへの追加
            newpost = DummyPostClass.DummyPost(row[0], row[1], row[2], row[3], \
                                               row[4], row[5], row[6])
            post_list[row[0]] = newpost

    return users_list, post_list
