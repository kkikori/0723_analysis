import sys
from pathlib import Path

from .data_load import data_load


def main():
    # data load
    f_n = Path("/Users/ida/Dropbox/AAAI_discussion_dummy.csv")
    user_list, post_list = data_load(f_n)


if __name__ == "__main__":
    main()
