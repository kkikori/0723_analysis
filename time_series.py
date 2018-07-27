import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cm as cm  # http://matplotlib.org/examples/color/colormaps_reference.html

import datetime as dt

FACILITATER_ID = 24
except_usr_name = ["unagi", "maguro", "saba", "iwashi", "aji", "shirauo", "facilitator", "structure_estimator"]
except_usr_id = [18, 19, 20, 21, 22, 23, 24, 25]
fn_path = "/Users/ida/Desktop/0723_resutls/time_series/"

start_time = "2018-07-23T07:20:00"
finish_time = "2018-07-23T08:20:00"

start_t = dt.datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S")
finish_t = dt.datetime.strptime(finish_time, "%Y-%m-%dT%H:%M:%S")


def _extract_time(pi_list, Post_list):
    post_num = 0

    x_times = []
    y_nums = []

    for pi in pi_list:
        if Post_list[pi].user_id in except_usr_id:
            continue
        x_times.append(Post_list[pi].created_at)
        y_nums.append(post_num)
        post_num += 1

    return x_times, y_nums


def _counter_post_per_thread(Thread_list, Post_list, group_n):
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

    minutes = mdates.MinuteLocator(interval=5)  # 5分間隔で描画
    timeFmt = mdates.DateFormatter('%H:%M')  # x軸の時刻表示フォーマットの設定
    ax.xaxis.set_major_locator(minutes)  # 上記の条件をグラフに設定
    ax.xaxis.set_major_formatter(timeFmt)  # 上記の条件をグラフに設定
    plt.xlim(start_t, finish_t)  # x軸の範囲を設定
    plt.ylim(0, 70)  # y軸の範囲を設定
    plt.title(group_n)
    # plt.legend(loc='upper left')  #データの名前を表示
    fig.autofmt_xdate()  # いい感じにx軸の時刻表示を調節
    plt.savefig(fn_path + group_n[0] + "_per_counter_post_no_legend" + ".png")
    plt.show()


def _counter_post_per_user(User_list, Post_list, group_n):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    sort_uilist = sorted(User_list.keys())
    for u_i in sort_uilist:
        if u_i in except_usr_id:
            continue
        user = User_list[u_i]
        print(" user", user.name, u_i)
        x_times, y_nums = _extract_time(user.pi_list, Post_list)
        if len(x_times) == 0:
            print("     this thread has not post from users.")
            continue
        if group_n == "ALPHA":
            ax.plot(x_times, y_nums, label=user.name, color=cm.spring((u_i - 1) / len(User_list)))
            ax.plot(x_times[-1], y_nums[-1], marker='o', color=cm.spring((u_i - 1) / len(User_list)))
        elif group_n == "BRAVO":
            ax.plot(x_times, y_nums, label=user.name, color=cm.summer((u_i - 1) / len(User_list)))
            ax.plot(x_times[-1], y_nums[-1], marker='o', color=cm.summer((u_i - 1) / len(User_list)))
        elif group_n == "CHARLIE":
            ax.plot(x_times, y_nums, label=user.name, color=cm.autumn((u_i - 1) / len(User_list)))
            ax.plot(x_times[-1], y_nums[-1], marker='o', color=cm.autumn((u_i - 1) / len(User_list)))
        else:
            ax.plot(x_times, y_nums, label=user.name, color=cm.winter((u_i - 1) / len(User_list)))
            ax.plot(x_times[-1], y_nums[-1], marker='o', color=cm.winter((u_i - 1) / len(User_list)))

    days = mdates.MinuteLocator(interval=5)
    daysFmt = mdates.DateFormatter('%H:%M')
    ax.xaxis.set_major_locator(days)
    ax.xaxis.set_major_formatter(daysFmt)
    plt.xlim(start_t, finish_t)
    plt.ylim(0, 40)
    plt.title(group_n)
    plt.legend(loc='upper left')
    fig.autofmt_xdate()
    plt.savefig(fn_path + group_n[0] + "_per_user_post_counter" + ".png")
    plt.show()


def time_series_analysis_main(Thread_list, Post_list, User_list, group_n):
    # _counter_post_per_thread(Thread_list, Post_list, group_n)

    _counter_post_per_user(User_list, Post_list, group_n)
