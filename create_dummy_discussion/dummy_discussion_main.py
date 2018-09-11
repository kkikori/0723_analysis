import csv
import sys
from pathlib import Path


def main():
    # data load
    f_n = Path("/Users/ida/Dropbox/AAAI_discussion_dummy.csv")
    if not f_n.exists():
        print("[FILE ERROR]", f_n, "is not found.")
        sys.exit()

    with f_n.open("r") as f:
        reader =


if __name__ == "__main__":
    main()
