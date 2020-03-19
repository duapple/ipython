##------绘图3---------##
##三轴和加速度图像##

import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import csv

outfile_name_first = './acc/acc_'
txt_format = '.txt'
png_format = '.png'
pic_outfile_name1_first = './acc_pic/accs_abs_'

num_l = 1
num_h = 8
x_len = 40
y_len = 25
pnum_max = 9

for n in range(num_l, num_h+1, 1):
    plt.figure(1, figsize = (x_len, y_len))
    pnum = 1
    pic_outfile_name1 = pic_outfile_name1_first + str(n) + png_format
    for count in range(8*(n-1)+1, 8*n+1, 1):
        count_str = str(count)
        outfile_name = outfile_name_first + count_str + txt_format

        with open(outfile_name, 'rt') as fin:
            cin = csv.reader(fin)
            acc = [row for row in cin]
        
        acc_x = acc[0]
        acc_y = acc[1]
        acc_z = acc[2]

        data_len = len(acc_x)

        for i in range(0, data_len, 1):
            acc_x[i] = float(acc_x[i])
            acc_y[i] = float(acc_y[i])
            acc_z[i] = float(acc_z[i])
            
        acc_svm_abs = []
        for k in range(0, data_len, 1):
            acc_svm_abs.append(abs(acc_x[k]) + abs(acc_y[k] + abs(acc_z[k])))

        ax1 = plt.subplot(4,2,pnum)
        pnum = pnum + 1
        #ax2 = plt.subplot(4,2,2)
        #ax3 = plt.subplot(4,2,3)
        #ax4 = plt.subplot(4,2,4)
        #ax5 = plt.subplot(4,2,5)
        #ax6 = plt.subplot(4,2,6)
        #ax7 = plt.subplot(4,2,7)
        #ax8 = plt.subplot(4,2,8)

        #刻度设置
        x_major_locator=MultipleLocator(data_len / 20)
        #把x轴的刻度间隔设置为1，并存在变量里
        y_major_locator=MultipleLocator(y_len * 2 / 10)
        #把y轴的刻度间隔设置为10，并存在变量里

        #ax为两条坐标轴的实例
        ax1.xaxis.set_major_locator(x_major_locator)
        #把x轴的主刻度设置为1的倍数
        ax1.yaxis.set_major_locator(y_major_locator)
        #把y轴的主刻度设置为10的倍数

        #绘制整个曲线图
        plt.axis([0, data_len, -40, 40])
        plt.ylabel("acc$(g)$")
        plt.xlabel("t")
        time = range(0, data_len, 1)
        
        plt.plot(time, acc_svm_abs, label = "acc_svm", color = 'black')

        plt.hlines(0.4, 0, data_len, linestyles = 'dashed', label = "", color = 'orange' )        
        plt.hlines(16, 0, data_len, linestyles = 'dashed', label = "", color = 'orange' )
        plt.hlines(1, 0, data_len, linestyles = 'dashed', label = "", color = 'orange' )

        plt.legend()

    plt.savefig(pic_outfile_name1, dpi = 320)
    #pic = plt.gcf()
    plt.close()