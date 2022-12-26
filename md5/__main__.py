import sys

from .md5 import md5

if __name__ == "__main__":
    print(md5(sys.argv[1]))