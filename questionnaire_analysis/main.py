import sys
from pathlib import Path
import csv
import numpy as np
from scipy import stats


# ただcsvを読み込むだけ
def read_data_from_csv(fn):
    print("fn", fn)
    datas = []
    if not fn.exists():
        print("[FILE ERROR]", fn, "is not found.")
        sys.exit()
    with fn.open("r") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            datas.append(row)

    return header, datas


def fairing_totalsums(datas, degree):
    datas_int = []
    for data in datas:
        li = [int(i) for i in data]
        datas_int.append(li)

    datas = np.array(datas_int)
    print(datas)
    if len(datas[:, 0]) % degree != 0:
        print("datas error")
        print(datas)
        print(datas[:, 0])
        sys.exit()

    faired_data = []

    for ri in range(len(datas[0])):
        print("ri", ri)
        row = datas[:, ri]
        print(row)
        faired_r = np.array([row[i:i + degree] for i in range(0, len(row), degree)])
        faired_data.append(faired_r.tolist())

    return faired_data


def krus(data):
    if len(data) == 2:
        result = stats.kruskal(data[0], data[1])
    elif len(data) == 3:
        result = stats.kruskal(data[0], data[1], data[2])
    elif len(data) == 4:
        result = stats.kruskal(data[0], data[1], data[2], data[3])
    elif len(data) == 5:
        result = stats.kruskal(data[0], data[1], data[2], data[3], data[4])
    elif len(data) == 6:
        result = stats.kruskal(data[0], data[1], data[2], data[3], data[4], data[5])
    elif len(data) == 7:
        result = stats.kruskal(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
    elif len(data) == 8:
        result = stats.kruskal(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
    else:
        print("data size bigger.")
        return None
    return result


def _faied(datas):
    r_datas = []
    for data in datas:
        kno = []
        for i, k in enumerate(data):

            for j in range(k):
                kno.append(i + 1)
        r_datas.append(kno)
    return r_datas


def main():
    # fn = Path("/Users/ida/Desktop/静大実験解析用/total_answers.csv")
    fn = Path("/Users/ida/Desktop/静大実験解析用/議論システムについて.csv")
    header, datas = read_data_from_csv(fn)
    print(header)
    faired_data = fairing_totalsums(datas, 5)
    print(faired_data[0])
    for k in range(len(faired_data)):
        print("\n")
        print(header[k])
        d = _faied(faired_data[k])
        # print(d)
        result = krus(d)
        # print(result)
        print(result.statistic, result.pvalue)

    x = [1, 1, 1, 1]
    y = [3, 9, 10, 4]
    z = [3, 8, 11, 3]
    result = krus([x, y, z])
    print(result)

    for k in range(len(faired_data)):
        print("\n" * 1)
        print(header[k])
        d_f = _faied(faired_data[k])
        a = d_f[0]

        b = d_f[1]
        c = d_f[2]
        d = d_f[3]
        a.extend(c)
        b.extend(d)
        # result = krus([a, b])
        # result = stats.ranksums(a, b)
        result = stats.ks_2samp(a, b)
        # print(result)
        print(result.statistic, result.pvalue)

    print("\"alfa and bravo\" vs　\"charlie and delta\" ")
    for k in range(len(faired_data)):
        print("\n" * 1)
        print(header[k])
        d_f = _faied(faired_data[k])
        alfa = d_f[0]

        bravo = d_f[1]
        charlie = d_f[2]
        delta = d_f[3]
        alfa.extend(bravo)
        charlie.extend(delta)
        # result = stats.ranksums(alfa, charlie)
        print(alfa, charlie)
        result = stats.ks_2samp(alfa, charlie)
        # print(result)
        print(result.statistic, result.pvalue)


if __name__ == "__main__":
    main()
