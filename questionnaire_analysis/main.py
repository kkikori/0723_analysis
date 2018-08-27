import sys
from pathlib import Path
import csv
import numpy as np
from scipy import stats
import kruskalWallis


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
    # print(datas)
    if len(datas[:, 0]) % degree != 0:
        print("datas error")
        print(datas)
        print(datas[:, 0])
        sys.exit()

    faired_data = []

    for ri in range(len(datas[0])):
        # print("ri", ri)
        row = datas[:, ri]
        # print(row)
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


def kruskal_test(faired_data, header):
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


def mykruskal_test(faired_data, headers):
    for name, data in zip(headers, faired_data):
        print(name)
        kruskalWallis.kruskal_calc(datas=data)


def tyottodake():
    facilitator = [125.026554, 97.181644, 697.227844, 98.644286, 163.747379, 605.660489, 266.94826, 188.205602]
    another1 = [686.008306, 125.026554, 402.93921, 416.649883, 122.744296, 139.065845, 244.424707, 150.819081,
                98.325025, 69.930234, 202.874023, 36.267543, 16.438056, 319.20989, 1014.49771, 408.328517, 49.188248,
                64.551585, 1217.457816, 32.615652, 43.525768, 32.606868, 81.109202, 29.827159, 34.212723, 135.260157,
                372.032036, 208.387268, 1126.552986, 85.947087, 182.977871, 117.079995, 554.245705, 258.08159,
                62.482412, 97.181644, 227.250909, 147.209862, 179.482336, 87.918184, 178.501611, 89.043653, 487.029963,
                212.844001, 290.046735, 278.575714, 391.224077, 1183.59784, 121.679844, 314.170049, 61.101235,
                187.977438, 186.953624, 651.411631, 45.816213, 236.186073, 124.533633, 88.780264, 122.548852, 194.40301,
                52.489398, 11.429153, 133.358698, 91.061485]
    another2 = [103.309756, 226.331738, 411.617791, 290.81757, 515.192378, 704.94598, 150.483711, 112.74876, 113.433513,
                100.355943, 319.635198, 126.693111, 179.342116, 150.81495, 785.973899, 1082.934535, 305.742838,
                828.300405, 552.545651, 2427.897746, 98.644286, 98.136656, 30.668678, 58.652262, 114.041296, 182.373361,
                212.28503, 274.719021, 191.267872, 93.583567, 192.545982, 74.402278, 113.263772, 195.854335, 123.210969,
                232.66412, 168.167047, 237.373326, 70.212814, 45.313135, 117.620776, 456.803575, 335.468341, 453.624039,
                417.495838, 301.17942, 282.294773, 241.487726, 183.609709, 158.728867, 182.667767, 550.480956,
                375.272602, 412.917028, 110.270909, 280.314067, 594.816423, 358.585554, 73.426647, 47.622259, 71.171907,
                205.637855, 92.19795, 20.061417, 96.895579, 216.134556, 163.747379, 484.357575, 95.610234, 142.153255,
                354.714946, 150.569046, 68.479102, 153.031271, 121.704009, 83.127302, 49.24621, 62.796561, 56.999845,
                68.409196, 46.411223, 894.58476, 124.515645, 81.296598, 55.226093, 393.042051, 134.453946, 242.506969,
                171.348382, 457.939176, 71.313492, 514.236211, 605.660489, 614.997248, 767.832871, 985.940869]

    print(len(another1),len(another2))
    another1.extend(another2)
    print(len(another1))
    result = krus([facilitator,another1])
    print(result)


def main():
    # データ読み込み
    fn = Path("/Users/ida/Desktop/静大実験解析用/total_answers.csv")
    # fn = Path("/Users/ida/Desktop/静大実験解析用/議論システムについて.csv")
    header, datas = read_data_from_csv(fn)
    # print(header)
    faired_data = fairing_totalsums(datas, 7)

    # kruskal_test(faired_data, header)
    mykruskal_test(faired_data, header)
    tyottodake()

if __name__ == "__main__":
    main()
