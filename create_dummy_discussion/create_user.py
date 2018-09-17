from pathlib import Path
import simplejson as json
import fetch_api

def create_user_main(f_user):
    buta_token = fetch_api.get_access_token("buta", "test")

    f = f_user.open("r")
    jsonData = json.load(f)
    for user in jsonData:
        fetch_api.create_user(buta_token, user)


if __name__ == "__main__":
    f_user = Path("/Users/ida/Dropbox/AAAI/AAAI_dummy_useres.json")
    create_user_main(f_user)
