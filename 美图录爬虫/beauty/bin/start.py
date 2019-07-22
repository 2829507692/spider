import os
import sys
path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(path)
from main import core
if __name__ == '__main__':
    core.main()