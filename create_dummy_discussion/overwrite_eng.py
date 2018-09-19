from pathlib import Path
import csv, sys

import fetch_api


def data_load(f_n):
    if not f_n.exists():
        print("[FILE ERROR]", f_n, "is not found.")
        sys.exit()
    post_list = []
    with f_n.open("r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            post_list.append(row)

    return post_list


def overwrite_from_csv(fn, token):
    data = data_load(f_n=fn)

    for row in data:
        d = {}
        d["component_type"] = row[6]
        if row[7]:
            d["related_to_id"] = int(row[7])
        else:
            d["related_to_id"] = None
        print(row[1], row[5], row[6])
        fetch_api.updated_sentence(row[1], token, d)


def overwrite(token):
    updates = [["PREMISE", 33, 32], ["CLAIM", 24, 33], ["PREMISE", 33, 34]]
    for update in updates:
        d = {"component_type": update[0], "related_to_id": update[1]}
        fetch_api.updated_sentence(update[2], token, d)


def main():
    token = fetch_api.get_access_token("buta", "test")

    fn = Path("/Users/ida/Dropbox/AAAI/data_eng/1.csv")
    # overwrite_from_csv(fn, token)
    overwrite(token)


if __name__ == "__main__":
    main()
