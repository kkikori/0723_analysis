import fetch_api
import simplejson as json
import csv
from pathlib import Path


def _csv_convert(thread_data):
    posts_list = []
    header = ["post_id", "sentence_id", "parent_id", "user_id", "title", "body"]
    posts_list.append(header)
    for post in thread_data["posts"]:
        user_id = post["user"]
        user_id = user_id["id"]

        if post["in_reply_to"]:
            rp = post["in_reply_to_id"]
            rp = rp["Int64"]
            title = None
        else:
            rp = None
            title = thread_data["title"]

        for s in post["sentences"]:
            posts_list.append([post["id"], s["id"], rp, user_id, title, s["body"]])

    return posts_list


def jp_dadta_create():
    fn = Path("/Users/ida/Dropbox/AAAI/data_jp")

    token = fetch_api.get_access_token("goat", "test")
    # fetch_api.create_thread(token, {"title": "好きな動物", "body": "私はゴーストです．こんばんは．"})

    thi_list = fetch_api.get_thi_list(token)
    for thi in thi_list:
        thread_data = fetch_api.load_thread(token, thi)
        csv_data = _csv_convert(thread_data)

        fname = str(thi) + ".csv"
        f_save = fn /fname

        with f_save.open("w") as f:
            writer = csv.writer(f,lineterminator = "\n")
            writer.writerows(csv_data)
        f.close()


def main():
    fn = Path("/Users/ida/Dropbox/AAAI/data_jp")

    token = fetch_api.get_access_token("goat", "test")
    fetch_api.create_thread(token, {"title": "好きな動物", "body": "私はゴーストです．こんばんは．"})


if __name__ == "__main__":
    jp_dadta_create()
