import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import datetime as dt

FACILITATER_ID = 24
except_usr_id = ["unagi", "maguro", "saba", "iwashi", "aji", "shirauo", "facilitator", "structure_estimator"]
except_usr_id = [18, 19, 20, 21, 22, 23, 24, 25]
fn_path = "/Users/ida/Desktop/0723_resutls/threads/"


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
        print(" title", thread.title,th_i)
        x_times, y_nums = _extract_time(thread.pi_list, Post_list)
        if len(x_times) == 0:
            print("     this thread has not post from users.")
            continue

        ax.plot(x_times, y_nums,)
    days = mdates.MinuteLocator(interval=5)
    daysFmt = mdates.DateFormatter('%H:%M')
    ax.xaxis.set_major_locator(days)
    ax.xaxis.set_major_formatter(daysFmt)
    fig.autofmt_xdate()
    plt.show()


def time_series_analysis_main(Thread_list, Post_list, group_n):
    _counter_post(Thread_list, Post_list, group_n)
