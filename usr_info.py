import numpy as np
import matplotlib.pyplot as plt

FACILITATER_ID = 24
except_usr_id = ["unagi", "maguro", "saba", "iwashi", "aji", "shirauo", "facilitator", "structure_estimator"]
fn_path = "/Users/ida/Desktop/0723_resutls/usrs/"


def _comment_nums(Usr_list, group_n):
    names_label = []
    coms = []
    for usr_i, usr in Usr_list.items():
        if usr.name in except_usr_id:
            continue
        names_label.append(usr.name)
        coms.append(len(usr.pi_list))

    plt.bar(list(range(len(coms))), coms, tick_label=names_label, align="center")
    plt.title(group_n)
    plt.ylim(0, 40)
    plt.xticks(list(range(len(coms))), names_label, rotation=30)
    plt.savefig(fn_path + group_n + ".png")
    plt.show()

    print("最大値,", max(coms))
    print("最小値,", min(coms))
    print("平均", sum(coms) / len(coms))
    print("平均")


def usr_analysis_main(Usr_list, group_n):
    _comment_nums(Usr_list, group_n)
