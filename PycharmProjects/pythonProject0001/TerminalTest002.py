import sys
from datetime import datetime
import os
from os.path import dirname
import shutil


today = datetime.now()

d3 = today.strftime("%m%d%Y%H%M%S")
args = sys.argv



x = dirname(args[0])
print(args[0])
ans = (x + "/" + args[1] + "_" + d3)
print(ans)
# os.mkdir(ans)
inp = x + "/" + args[1]

shutil.copy(inp, ans)