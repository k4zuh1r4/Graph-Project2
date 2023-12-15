from collections import deque
import string
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import config as cfg
import sys
from numpy import genfromtxt, random
class  WeightedGraphProgram():
    def __init__(self):
        self.__matrix = []
        self.__edges = []
        self.__graph = nx.Graph()
        self.__searchRecordDFS = []
        self.__searchRecordBFS = []
        self.__convertedMatrix = []
    def input(self, filePath:string):
        self.__matrix = genfromtxt(filePath, delimiter = ',')
        self.__graph = nx.from_numpy_array(self.__matrix, create_using=nx.Graph)
        self.__searchRecordDFS = [False] * len(self.__matrix)
        self.__searchRecordBFS = [False] * len(self.__matrix)
        self.weightlessConvert()
    def weightlessConvert(self):
        self.__convertedMatrix = np.where(self.__matrix > 1, 1, self.__matrix)
        print(self.__convertedMatrix)
    def plot(self):
        layout = nx.spring_layout(self.__graph)
        nx.draw(self.__graph, layout, node_size= cfg.NODE_SIZE, with_labels=True, font_size=15)
        labels = nx.get_edge_attributes(self.__graph,'weight')
        nx.draw_networkx_edge_labels(self.__graph,pos=layout,edge_labels=labels)
        plt.show()
        self.clear()
    def clear(self):
        self.__graph.clear()
    def traversalDFS(self, node):
        self.__searchRecordDFS[node] = True
        print("DFS Visited node: ", node, " ")
        for i in range(len(self.__convertedMatrix[node])):
            if self.__convertedMatrix[node][i] >= 1 and not self.__searchRecordDFS[i]:
                self.traversalDFS(i)  
    def degreeVertices(self, vertex):
        if vertex < 0 or vertex >= len(self.__matrix):
            return "Invalid vertex"
        degree = 0
        for i in range(len(self.__matrix[vertex])):
            if self.__matrix[vertex][i] >= 1:
                degree += 1
        return degree
    def traversalBFS(self, vertex):
        queue = deque()
        queue.append(vertex)
        self.__searchRecordBFS[vertex] = True
        while queue:
            node = queue.popleft()
            print("BFS Visited node: ", node, " ")
            for i in range(len(self.__convertedMatrix)):
                if self.__convertedMatrix[node][i] and not self.__searchRecordBFS[i]:
                    queue.append(i)
                    self.__searchRecordBFS[i] = True
    def minDistance(self, dist, traversed):
        min = sys.maxsize
        for v in range(len(self.__matrix)):
            if dist[v] < min and traversed[v] == False:
                min = dist[v]
                minIndex = v
        return minIndex
    def shortestPath(self, src):
        dist = [1e7] * len(self.__matrix)
        dist[src] = 0
        traversed = [False] * len(self.__matrix)
        for damn in range(len(self.__matrix)):
            u = self.minDistance(dist, traversed)
            traversed[u] = True
            for v in range(len(self.__matrix)):
                if (self.__matrix[u][v] > 0 and
                   traversed[v] == False and
                   dist[v] > dist[u] + self.__matrix[u][v]):
                    dist[v] = dist[u] + self.__matrix[u][v]
        print("Nut \t Khoang cach tu nut da nhap")
        for node in range(len(self.__matrix)):
            print(node, "\t\t", dist[node])        
    def generate2DRandom(self,n):
        matrix = np.array([[random.randint(0, 100) for i in range(n)] for j in range(n)])
        for i in range(n):
            matrix[i][i] = 0
        graph = nx.from_numpy_array(matrix, create_using=nx.Graph)
        print(matrix)
        layout = nx.spring_layout(graph)
        nx.draw(graph, layout, node_size= cfg.NODE_SIZE, with_labels=True, font_size=15)
        labels = nx.get_edge_attributes(graph,'weight')
        nx.draw_networkx_edge_labels(graph,pos=layout,edge_labels=labels)
        plt.show()