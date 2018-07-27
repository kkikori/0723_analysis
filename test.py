import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
from matplotlib.collections import LineCollection



def main():

    # X軸データ
    x = [dt.datetime(2010, 1, 1), dt.datetime(2010, 1, 2),
         dt.datetime(2010, 1, 3), dt.datetime(2010, 1, 4),
         dt.datetime(2010, 1, 5)]

    # Y軸データ
    y = [1, 3, 2, 4, 1]

    # データをセット
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)
    ax.plot(dt.datetime(2010,1,1,12,30),5,"o")

    days = mdates.DayLocator()  # every day
    daysFmt = mdates.DateFormatter('%m-%d')
    ax.xaxis.set_major_locator(days)
    ax.xaxis.set_major_formatter(daysFmt)
    fig.autofmt_xdate()
    plt.show()

def plottest():
    # Now do a second plot coloring the curve using a continuous colormap
    t = np.linspace(0, 10, 200)
    x = np.cos(np.pi * t)
    y = np.sin(t)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    lc = LineCollection(segments, cmap=plt.get_cmap('copper'),
                        norm=plt.Normalize(0, 10))
    lc.set_array(t)
    lc.set_linewidth(3)

    plt.figure()
    plt.gca().add_collection(lc)
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.show()

if __name__ == "__main__":
    #main()
    plottest()
