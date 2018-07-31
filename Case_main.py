import sys
import json
from pathlib import Path
import analysis_preparate


#
def _preparate_file_paths():
    fn = Path("file_paths.json")
    if not fn.exists():
        sys.exit()
    group_file_paths = {}
    f = fn.open("r")
    jsonData = json.load(f)
    for group_n, group in jsonData.items():
        file_paths = {}
        for fn, fp in group.items():
            if not fp:
                file_paths[fn] = None
            else:
                file_paths[fn] = Path(fp)
        group_file_paths[group_n] = file_paths
    return group_file_paths


def main():
    group_files = _preparate_file_paths()
    group_names = sorted(group_files.keys())
    for group_n in group_names:
        print("-" * 15, "  ", group_n, "  ", "-" * 20)
        Thread_list, Post_list, Usr_list = analysis_preparate.data_load(group_files[group_n])


if __name__ == "__main__":
    main()
