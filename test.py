import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt




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


if __name__ == "__main__":
    main()
