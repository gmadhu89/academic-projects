import os
import numpy as np
from os.path import abspath, exists
from scipy import sparse
import scipy
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
import argparse


def output_file(a, idx2name, c_idx):
    dirpath = os.getcwd()
    node_file = dirpath + '//nodes.csv'
    edge_file = dirpath + '//edges.csv'

    with open(edge_file, 'w') as fid:
        fid.write('Source\tTarget\n')
        for i in range(len(a)):
            fid.write(f'{a[i,0]}\t{a[i,1]}\n')

    with open(node_file, 'w') as fid:
        fid.write('Id\tLabel\tColor\n')
        for i in range(len(idx2name)):
            fid.write(f'{i}\t{idx2name[i]}\t{c_idx[i]}\n')

def read_team_name():
    # read inverse_teams.txt file
    f_path = abspath("Data/inverse_teams.txt")
    idx2name = []
    if exists(f_path):
        with open(f_path) as fid:
            for line in fid.readlines():
                name = line.split("\t", 1)[1]
                idx2name.append(name[:-1])
    return idx2name

def import_graph():
    # read the graph from 'play_graph.txt'
    f_path = abspath("Data/play_graph.txt")
    if exists(f_path):
        with open(f_path) as graph_file:
            lines = [line.split() for line in graph_file]
    return np.array(lines).astype(int)



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="sample command: python Spectral_Clustering_Clusters.py 10")
    parser.add_argument("k", help="Number of clusters")

    args = parser.parse_args()

# spectral clustering
    n =   321  # Total number of teams/nodes
    k = int(args.k)   # No. of clusters to group them into

# load the graph
    a = import_graph()

    i = a[:, 0]-1
    j = a[:, 1]-1
    v = np.ones((a.shape[0], 1)).flatten()

    A = sparse.coo_matrix((v, (i, j)), shape=(n, n))
    A = (A + np.transpose(A))/2
    A = sparse.csc_matrix.todense(A) # ## convert to dense matrix

    D = np.diag(1/np.sqrt(np.sum(A, axis=1)).A1)
    L = D @ A @ D
    L = np.array(L)

    v, x  = np.linalg.eig(L)
    idx_sorted = np.argsort(v)

    x = x[:, idx_sorted[-k:]].real.astype(np.float32) # Eigen vectors for the k largest eigen values

    x = x/np.repeat(np.sqrt(np.sum(x*x, axis=1).reshape(-1, 1)), k, axis=1)


# Implementing k-means to find the clusters
    kmeans = KMeans(n_clusters=k).fit(x)
#kmeans = KMeans(n_clusters=k, random_state=3425).fit(x)
    c_idx = kmeans.labels_

# show cluster
    idx2name = read_team_name()
    for i in range(k):
        print(f'Cluster {i+1}\n***************')
        idx = [index for index, t in enumerate(c_idx) if t == i]
        for index in idx:
            print(idx2name[index])
        print('\n')
