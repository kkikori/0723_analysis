import sys
import json
import analysis_preparate
import usr_info
import thread_info


def _load_data(fn):
    if not fn.exists():
        print("[FILE ERROR]", fn, "is not found.")
        sys.exit()
    f = fn.open("r")
    jsonData = json.load(f)
    f.close()
    return jsonData


def analysis_main(group_n, file_paths):
    Thread_list, Post_list, Usr_list = analysis_preparate.data_load(file_paths)
    # usr_info.usr_analysis_main(Usr_list, group_n)
    thread_info.thread_analysis_main(Thread_list, Post_list, group_n)
