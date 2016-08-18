#-*- coding: utf-8-unix; -*-
import os

base_path = 'partitions//'

algs = ['AL','CeL','CoL','KM','SL','SNN']
ns = ['one','two','three','four','five','six']

for i in range(6):
    path = base_path + ns[i] + '//'
    if not os.path.exists(path):
        os.makedirs(path)
    for a in range(i):
        
    
