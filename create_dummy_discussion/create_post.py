from .fetch_api import create_post, create_thread


def _post_post(token, post):
    if post.title:
        data = {
            "title": post.title,
            "body": post.body
        }
        create_thread(token, data)
    else:
        data = {
            "body": post.body,
            "in_reply_to_id": post.index
        }
        create_post(token, data)
    return


def create_post_main(user_list, post_list):
    for pi, post in post_list.items():
        token = user_list[post.user_id].token
        _post_post(token, post)

    return
