import fetch_api

def main():
    token = fetch_api.get_access_token("goat","test")
    fetch_api.create_thread(token, {"title":"好きな動物","body":"私はゴーストです．こんばんは．"})


if __name__ == "__main__":
    main()