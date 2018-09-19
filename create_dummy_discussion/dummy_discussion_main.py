import sys
from pathlib import Path

import create_post
import data_load


# 読み込んだデータをAPIを使って復元

def main():
    # posts data load
    f_n = Path("/Users/ida/Dropbox/AAAI/dummy_short.csv")
    user_list, post_list = data_load.data_load(f_n)

    # post post
    create_post.create_post_main(user_list, post_list)


if __name__ == "__main__":
    main()
