from collections import defaultdict

FACILITATER_ID = 24
except_usr_id = ["unagi", "maguro", "saba", "iwashi", "aji", "shirauo", "facilitator", "structure_estimator"]
fn_path = "/Users/ida/Desktop/0723_resutls/usrs/"


def _facilitator_self(facilitator, Post_list, User_list):
    print(facilitator.pi_list)
    print("コメント数", len(facilitator.pi_list))

    reply_to_usr = defaultdict(int)
    for pi in facilitator.pi_list:
        post = Post_list[pi]
        rep_post = Post_list[post.reply_to_id]
        reply_to_usr[rep_post.user_id] += 1

    for ui, num in reply_to_usr.items():
        usr = User_list[ui]
        print(ui, usr.name, usr.display_name, len(usr.pi_list), num)


def _usrs(User_list):
    for ui, usr in User_list.items():
        print(ui, usr.name, usr.display_name, len(usr.pi_list), len(usr.previousQ_list))


def _print_post(post):
    print("*" * 5, post.id, "(", post.user_id, ")", "*" * 10)
    for s in post.sentences:
        print(s.body)


def _facilitator_has_reply(Post_list):
    for pi, post in Post_list.items():
        if not post.reply_to_id:
            continue
        rep_post = Post_list[post.reply_to_id]
        if rep_post.user_id != FACILITATER_ID:
            continue
        print("")
        rep_rep_post = Post_list[rep_post.reply_to_id]

        _print_post(rep_rep_post)
        _print_post(rep_post)
        _print_post(post)


def facilitator_analysis_main(Thread_list, Post_list, User_list):
    # _facilitator_self(User_list[FACILITATER_ID], Post_list, User_list)
    # _usrs(User_list)
    _facilitator_has_reply(Post_list)
