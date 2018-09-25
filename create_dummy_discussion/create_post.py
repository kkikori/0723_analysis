import fetch_api


def _post_post(token, post):
    if not post.parent_id:
        print("    new thread is created")
        data = {
            "title": post.title,
            "body": post.body
        }
        print("        data", data)
        fetch_api.create_thread(token, data)
    else:
        print("    new post")
        data = {
            "body": post.body,
            "in_reply_to_id": post.parent_id
        }
        fetch_api.create_post(token, data)
    return

# dummy_discussion_mainから呼び出される
def create_post_main(user_list, post_list):
    print("create_post_main")
    for pi, post in post_list.items():
        print("pi", pi, post.user_id)
        token = user_list[post.user_id].token
        _post_post(token, post)

    return
