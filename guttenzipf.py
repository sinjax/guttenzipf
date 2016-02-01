from urllib import request
import re
from itertools import groupby
from operator import itemgetter
from functools import reduce
from matplotlib import pyplot as plt
import numpy as np
import os

def count(obj1, obj2):
	return (obj1[0],obj1[1] + obj2[1])

root = "http://www.gutenberg.org"
book = "cache/epub/2600/pg2600.txt"
outfile = book
guttenfile = None

if not os.path.exists(outfile):

	if not os.path.exists(os.path.dirname(outfile)):
		os.makedirs(os.path.dirname(outfile))
	guttenfile = request.urlopen("/".join([root,book])).read().decode("utf-8")
	with open(outfile,"w") as f:
		f.write(guttenfile)
else:
	with open(outfile,"r") as f:
		guttenfile = f.read()


guttenfile = re.sub(
	r"[^\w\s.]", '', guttenfile, re.MULTILINE
)

guttenfile = guttenfile.replace("\n","").replace("\r","")

counts = [(len(a),1) for a in guttenfile.split(".") if len(a) != 0]
group_counts = [ reduce(count, group) for (_, group) in  groupby(sorted(counts), key=itemgetter(0))]
index = np.arange(len(group_counts))
vals = [x[1] for x in group_counts]

plt.bar(index,vals,0.35)
plt.title(book)
plt.savefig("guttenzipf.png")
plt.show()