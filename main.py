import sys
import json
from pathlib import Path
import analysis


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
    group_list = _preparate_file_paths()
    group_names = sorted(group_list.keys())

    for group_n in group_names:
        print("-" * 15, "  ", group_n, "  ", "-" * 20)
        analysis.analysis_main(group_n, group_list[group_n])

    # for group_n, group in group_list.items():
    #     print("-" * 15, "  ", group_n, "  ", "-" * 20)
    #     analysis.analysis_main(group_n,group)


if __name__ == "__main__":
    main()
