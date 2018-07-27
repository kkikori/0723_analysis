import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cm as cm  # http://matplotlib.org/examples/color/colormaps_reference.html

import datetime as dt

FACILITATER_ID = 24
except_usr_id = ["unagi", "maguro", "saba", "iwashi", "aji", "shirauo", "facilitator", "structure_estimator"]
except_usr_id = [18, 19, 20, 21, 22, 23, 24, 25]
fn_path = "/Users/ida/Desktop/0723_resutls/time_series/"

start_time = "2018-07-23T07:20:00"
finish_time = "2018-07-23T08:20:00"

start_t = dt.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
finish_t = dt.datetime.strptime(finish_time, "%Y-%m-%dT%H:%M:%S")


def _extract_time(thread_pi_list, Post_list):
    post_num = 0

    x_times = []
    y_nums = []

    for pi in thread_pi_list:
        if Post_list[pi].user_id in except_usr_id:
            continue
        x_times.append(Post_list[pi].created_at)
        y_nums.append(post_num)
        post_num += 1

    return x_times, y_nums


def _counter_post(Thread_list, Post_list, group_n):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    for th_i in range(1, len(Thread_list) + 1):
        thread = Thread_list[th_i]
        print(" title", thread.title, th_i)
        x_times, y_nums = _extract_time(thread.pi_list, Post_list)
        if len(x_times) == 0:
            print("     this thread has not post from users.")
            continue
        if group_n == "ALPHA":
            ax.plot(x_times, y_nums, label=th_i, color=cm.spring((th_i - 1) / len(Thread_list)))
        elif group_n == "BRAVO":
            ax.plot(x_times, y_nums, label=th_i, color=cm.summer((th_i - 1) / len(Thread_list)))
        elif group_n == "CHARLIE":
            ax.plot(x_times, y_nums, label=th_i, color=cm.autumn((th_i - 1) / len(Thread_list)))
        else:
            ax.plot(x_times, y_nums, label=th_i, color=cm.winter((th_i - 1) / len(Thread_list)))

    days = mdates.MinuteLocator(interval=5)
    daysFmt = mdates.DateFormatter('%H:%M')
    ax.xaxis.set_major_locator(days)
    ax.xaxis.set_major_formatter(daysFmt)
    plt.xlim(start_t, finish_t)
    plt.ylim(0, 70)
    plt.title(group_n)
    # plt.legend(loc='upper left')
    fig.autofmt_xdate()
    plt.savefig(fn_path + group_n[0] + "_per_counter_post_no_legend" + ".png")
    plt.show()


def time_series_analysis_main(Thread_list, Post_list, group_n):
    _counter_post(Thread_list, Post_list, group_n)
