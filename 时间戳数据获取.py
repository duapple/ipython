##--------时间戳数据处理---------##
##数据处理##

import matplotlib.pyplot as plt
#from matplotlib.pyplot import MultipleLocator
import numpy as np
import csv

num_l = 1
num_h = 2

infile_name_first = './data_src/data'
outfile_name_first = './timestamp/timestamp_'
txt_format = '.txt'

for count in range (num_l, num_h, 1):
    count_str = str(count)
    infile_name = infile_name_first + count_str + txt_format
    outfile_name = outfile_name_first + count_str + txt_format
    
    with open(infile_name, 'rt') as fin:
        cin = csv.reader(fin)
        villains = [row for row in cin]
    
    time_l = ([f[0] for f in villains])
    time_h = ([f[1] for f in villains])

    data_len = len(villains)
    print(data_len)
    timestamp = []
    
    for i in range(0, data_len, 1):
        temp = bytes.fromhex(time_h[i] + time_l[i])
        tt = int.from_bytes(temp, byteorder='big', signed=False)
        timestamp.append(tt)

    with open(outfile_name, 'wt', newline = '') as fout:
        fout.write(str(timestamp))