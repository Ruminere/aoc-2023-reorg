import sys
sys.path.append('../')
from aoctools.aoc_functions import *
import itertools as it
import numpy as np
from collections import defaultdict, Counter, deque
import networkx as nx

def main():
    testing = 0
    filename = "actual" if not testing else "test"
    file = filename + ".in"

    ans1 = 1

    g = nx.Graph()
    with open(file) as fh:
        for line in fh:
            line = line.strip().split(": ")
            a = line[0]
            for b in line[1].split():
                g.add_edge(a,b)
    cuts = nx.minimum_edge_cut(g)
    g.remove_edges_from(cuts)
    ans1 = math.prod(len(i) for i in nx.connected_components(g))
    
    print("1:", ans1)
    print("2: N/A")

# ==================================================



# ==================================================

main()