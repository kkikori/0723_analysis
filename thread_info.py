import numpy as np
import matplotlib.pyplot as plt

FACILITATER_ID = 24
except_usr_id = ["unagi", "maguro", "saba", "iwashi", "aji", "shirauo", "facilitator", "structure_estimator"]
except_usr_id = [18, 19, 20, 21, 22, 23, 24, 25]
fn_path = "/Users/ida/Desktop/0723_resutls/threads/"


def _except_others(pi_list, Post_list):
    pi_except_other_list = []
    for pi in pi_list:
        if Post_list[pi].user_id in except_usr_id:
            continue
        pi_except_other_list.append(pi)
    return pi_except_other_list


def _comment_nums(Thread_list, Post_list, group_n):
    names_label = []
    coms = []
    for th_i, thread in Thread_list.items():
        names_label.append(thread.title)
        pi_except_other_list = _except_others(thread.pi_list, Post_list)
        coms.append(len(pi_except_other_list))

    coms = np.array(coms)
    plt.bar(list(range(len(coms))), coms, tick_label=names_label, align="center")
    plt.title(group_n)
    plt.ylim(0, 70)
    plt.xticks(list(range(len(coms))), names_label, rotation=70)
    plt.savefig(fn_path + group_n + "_comment_num" + ".png")
    plt.show()

    print("最大値,", coms.max())
    print("最小値,", coms.min())
    print("合計コメント数", coms.sum())
    print("スレッド数", len(coms))
    print("平均", coms.sum() / len(coms))
    print("分散", coms.var())
    coms = list(coms)
    coms.remove(0)
    print("coms",coms)
    try:
        coms.remove(0)
    except:
        print("")
    print(coms)
    print("平均,", sum(coms) / len(coms))


def thread_analysis_main(Thread_list, Post_list, group_n):
    _comment_nums(Thread_list, Post_list, group_n)
