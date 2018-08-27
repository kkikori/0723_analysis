FACILITATER_ID = 24
except_usr_id = ["unagi", "maguro", "saba", "iwashi", "aji", "shirauo", "facilitator", "structure_estimator"]
fn_path = "/Users/ida/Desktop/0723_resutls/usrs/"


def _facilitator_has_reply(Post_list):
    interval_times = []
    for pi, post in Post_list.items():
        if not post.reply_to_id:
            continue
        rep_post = Post_list[post.reply_to_id]
        if rep_post.user_id != FACILITATER_ID:
            continue
        print("")

        rep_rep_post = Post_list[rep_post.reply_to_id]
        if rep_rep_post.user_id == post.user_id:
            interval_times.append(post.created_at - rep_rep_post.created_at)

    interval_seconds =[]
    for it in interval_times:
        print(it,it.total_seconds())
        interval_seconds.append(it.total_seconds())

    return interval_seconds


def _extract_interval_times(Post_list, user):
    pi_list = user.pi_list
    com_nums = len(pi_list)
    if com_nums <= 1:
        return None

    intervals = []

    for ti in range(1, com_nums):
        before_p = Post_list[pi_list[ti - 1]]
        after_p = Post_list[pi_list[ti]]
        intervals.append(after_p.created_at - before_p.created_at)

    interval_seconds = []
    for it in intervals:
        interval_seconds.append(it.total_seconds())
    return interval_seconds


def _user_intervals(Post_list, User_list):
    interval_times = []
    for user_id, user in User_list.items():
        if user.name in except_usr_id:
            continue
        intervals = _extract_interval_times(Post_list, user)
        if intervals:
            interval_times.extend(intervals)
    return interval_times


def post_interval_analysis_main(Post_list, User_list):

    facilitator_interval_times = _facilitator_has_reply(Post_list)
    total_interval_times = _user_intervals(Post_list, User_list)
    print("facilitator_interval_Times",facilitator_interval_times)
    print(total_interval_times)
