import sys
import json
from analysis_preparate import data_load

def _load_data(fn):
    if not fn.exists():
        print("[FILE ERROR]", fn, "is not found.")
        sys.exit()
    f = fn.open("r")
    jsonData = json.load(f)
    f.close()
    return jsonData

def analysis_main(file_paths):
    Threads_list, Post_list, Usr_list = data_load(file_paths)
