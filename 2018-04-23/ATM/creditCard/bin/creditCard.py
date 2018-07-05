# Author： ninuxer
# Date： 2018/04/23 14:29
# File： creditCard.py


import os, sys


PROPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROPATH)

print(sys.path)

from core import main

if __name__ == '__main__':
    main.main()


