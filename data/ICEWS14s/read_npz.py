# coding=utf-8
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# 加载npz文件
graph = np.load('graphs.npz')
print graph.files
# print graph['graph']

# 查看图
print len(graph['graph'])
# # print graph['graph']
# nx.draw(graph['graph'][2], with_labels=True)
# plt.show()

# 节点数
print graph['graph'][365].nodes()
