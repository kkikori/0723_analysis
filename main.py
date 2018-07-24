import sys
import json
from pathlib import Path
from .analysis import analysis_main

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
            file_paths[fn] = Path(fp)
        group_file_paths[group_n] = file_paths
    return group_file_paths


def main():
    group_list = _preparate_file_paths()

    for group_n, group in group_list.items():
        analysis_main(group)


if __name__ == "__main__":
    main()
