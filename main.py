import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from numpy import genfromtxt
from grapher import *
import config as cfg
graph = WeightedGraphProgram()
graph.input(cfg.FILE_PATH) #dua file vao input
graph.plot() #ve va hien thi do thi
graph.traversalDFS(0) #depth first search
print()
graph.traversalBFS(0) #breadth first search
print(graph.degreeVertices(3)) #tim va in ra so luong bac cua dinh dua vao ma tran
graph.shortestPath(0) #tim duong ngan nhat de di qua tat ca cac diem con lai
graph.generate2DRandom(3) #tao ra ma tran ngau nhien kich co nxn va ve do thi