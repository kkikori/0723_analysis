from scipy import stats
import numpy as np
from collections import namedtuple
import warnings
from numpy import array, asarray, ma, zeros


def kruskal_calc(datas):
    hierarchy = len(datas[0])
    data_size = len(datas)
    datas = np.array(datas)

    # 各群の合計数
    gun_nums = [sum(data) for data in datas]
    #print("gun_nums", gun_nums)
    N = sum(gun_nums)

    # 列計
    line_sum = [sum(datas[:, i]) for i in range(hierarchy)]
    #print("line_num", line_sum)

    # 各カテゴリの中間順位(average_order)
    rui = 0
    ruikei = []
    for line in line_sum:
        rui += line
        ruikei.append(rui)
    #print("ruikei", ruikei)
    ruikei = np.array(ruikei)

    average_order = [(1 + ruikei[0]) / 2]
    for i in range(1, hierarchy):
        average_order.append((1 + ruikei[i - 1] + ruikei[i]) / 2)
    #print("average_order", average_order)

    # 順位和
    juniwa = []
    for data in datas:
        junis = []
        for i in range(hierarchy):
            junis.append(average_order[i] * data[i])
        juniwa.append(junis)
    RS = [sum(j) for j in juniwa]
    #print("juniwa", RS)

    # 修正項を求める
    syuseis = [(line * line * line) - line for line in line_sum]
    C = 1 - (sum(syuseis) / (N * N * N - N))
    #print("修正項：", C)

    # 検定統計量
    RS_2 = [RS[i] * RS[i] / gun_nums[i] for i in range(len(datas))]
    statistics = 2 * sum(RS_2) / (N * (N + 1)) - (N + 1) / 2
    statistics = statistics * (6 / C)
    print("  検定統計量", statistics)

    # 自由度
    jiyuudo = data_size - 1
    #print("  自由度", jiyuudo)

    # p値
    p = stats.chi2.sf(statistics, jiyuudo)
    print("  p値", p)


def kruskal_wallis(titles, datas, print_title=True):
    if not print_title:
        print("a")

    for title, data in zip(titles, datas):
        print(title)


def test():
    # http://halbau.world.coocan.jp/multigrp.html#kruskal
    x = [8, 10, 6, 1]
    y = [3, 9, 10, 4]
    z = [3, 8, 11, 3]
    kruskal_calc([x, y, z])


if __name__ == "__main__":
    test()
