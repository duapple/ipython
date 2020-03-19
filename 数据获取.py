##加速度acc数据处理##
##数据处理##

import matplotlib.pyplot as plt
#from matplotlib.pyplot import MultipleLocator
import numpy as np
import csv

num_l = 57
num_h = 65

infile_name_first = './data_src/data'
outfile_name_first = './acc/acc_'
txt_format = '.txt'
png_format = '.png'

for count in range (num_l, num_h, 1):
    count_str = str(count)
    infile_name = infile_name_first + count_str + txt_format
    outfile_name = outfile_name_first + count_str + txt_format
    pic_outfile_name1 = infile_name_first + count_str + png_format
    
    with open(infile_name, 'rt') as fin:
        cin = csv.reader(fin)
        villains = [row for row in cin]
    
    acc1_l = ([f[2] for f in villains])
    acc1_h = ([f[3] for f in villains])
    acc2_l = ([f[4] for f in villains])
    acc2_h = ([f[5] for f in villains])
    acc3_l = ([f[6] for f in villains])
    acc3_h = ([f[7] for f in villains])

    data_len = len(villains)
    print(data_len)
    acc_x = []
    acc_y = []
    acc_z = []
    acc_svm = []
    
    for i in range(0, data_len, 1):
        temp = bytes.fromhex(acc1_h[i] + acc1_l[i])
        tt = int.from_bytes(temp, byteorder='big', signed=True)
        acc_x.append(tt / 1000)
        temp = bytes.fromhex(acc2_h[i] + acc2_l[i])
        tt = int.from_bytes(temp, byteorder='big', signed=True)
        acc_y.append(tt / 1000)
        temp = bytes.fromhex(acc3_h[i] + acc3_l[i])
        tt = int.from_bytes(temp, byteorder='big', signed=True)
        acc_z.append(tt / 1000)
        acc_svm.append(np.sqrt(pow(acc_x[i], 2) + pow(acc_y[i], 2) + pow(acc_z[i], 2)))
    
    accx = [acc_x, acc_y, acc_z, acc_svm]
    with open(outfile_name, 'wt', newline = '') as fout:
        writer = csv.writer(fout)
        writer.writerows(accx)