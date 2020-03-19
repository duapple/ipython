##------绘图1--------##
##绘图1##

import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

outfile_name_first = './acc/acc_'
txt_format = '.txt'
png_format = '.png'
pic_outfile_name1_first = './acc_pic/acc_'

num_l = 57
num_h = 65
x_len = 20
y_len = 10

for count in range(num_l, num_h, 1):
    count_str = str(count)
    outfile_name = outfile_name_first + count_str + txt_format
    pic_outfile_name1 = pic_outfile_name1_first + count_str + png_format
    
    with open(outfile_name, 'rt') as fin:
        cin = csv.reader(fin)
        acc = [row for row in cin]
        
    acc_x = acc[0]
    acc_y = acc[1]
    acc_z = acc[2]
    acc_svm = acc[3]
    
    data_len = len(acc_x)
    
    for i in range(0, data_len, 1):
        acc_x[i] = float(acc_x[i])
        acc_y[i] = float(acc_y[i])
        acc_z[i] = float(acc_z[i])
        acc_svm[i] = float(acc_svm[i])
        
    plt.figure(figsize = (x_len, y_len))
    #plt.axis([xmin,xmax,ymin,ymax])

    #刻度设置
    x_major_locator=MultipleLocator(data_len / 20)
    #把x轴的刻度间隔设置为1，并存在变量里
    y_major_locator=MultipleLocator(y_len * 2 / 10)
    #把y轴的刻度间隔设置为10，并存在变量里
    ax=plt.gca()
    #ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    #把x轴的主刻度设置为1的倍数
    ax.yaxis.set_major_locator(y_major_locator)
    #把y轴的主刻度设置为10的倍数

    #绘制整个曲线图
    plt.axis([0, data_len, -20, 20])
    plt.ylabel("acc$(g)$")
    plt.xlabel("t")
    time = range(0, data_len, 1)

    plt.plot(time, acc_x, label = "acc_x", color = 'red')
    plt.plot(time, acc_y, label = "acc_y", color = 'green')
    plt.plot(time, acc_z, label = "acc_z", color = 'blue')
    plt.plot(time, acc_svm, label = "acc_svm", color = 'black')

    plt.hlines(0.4, 0, data_len, linestyles = 'dashed', label = "", color = 'orange' )
    plt.hlines(-2, 0, data_len, linestyles = 'dashed', label = "", color = 'orange' )

    plt.legend()
    plt.savefig(pic_outfile_name1, dpi = 320)
    pic = plt.gcf()
    plt.close(pic)
