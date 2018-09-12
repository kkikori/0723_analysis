import sys
from pathlib import Path

from .data_load import data_load
from .create_post import create_post_main


def main():
    # data load
    f_n = Path("/Users/ida/Dropbox/AAAI_discussion_dummy.csv")
    user_list, post_list = data_load(f_n)

    # post post
    create_post_main(user_list, post_list)


if __name__ == "__main__":
    main()
