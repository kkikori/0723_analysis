import sys
import json

sys.path.append('/Users/ida/github/AskingKalliopeia/src/')
import preparation

# 全部のデータを読み込む
def _load_json(fn):
    f_lists = list(fn.glob(""))
    datas = []
    for fn in f_lists:
        f = fn.open("r")
        jsonData = json.load(f)
        datas.append(jsonData)
        f.close()

    return datas


def data_load(file_paths):
    threads = _load_json(file_paths["THREADS"])
    users = _load_json(file_paths["USRS"])

    Threads_list, Post_list, Usr_list = preparation.preparate_main(file_paths,threads,users)


    return Threads_list, Post_list, Usr_list
