from matplotlib import pyplot as plt

execucao=[]
with open('valores.txt') as f:
    for i in f:
        e=i.split('\n')[0]
        if e:
            execucao.append((int(e.split(',')[0]), float(e.split(',')[1])))
execucao = sorted(execucao)

with open('valores.txt', 'w') as f:
    for l in execucao:
        f.write("{},{}\n".format(l[0], l[1]))

execucao_x = zip(*execucao)[0]
execucao_y = zip(*execucao)[1]

plt.axis([execucao_x[0], execucao_x[-1]*1.2, execucao_y[0], execucao_y[-1]*1.2])
time_wait = 5.0/len(execucao_x)

import time
start = time.time()
for i in range(len(execucao_x)):
    plt.scatter(execucao_x[i], execucao_y[i])
    # plt.scatter(execucao_x[i], execucao_y[i], s='array_like', c=plotable_item[(i%len_symbols)], maker=plotable_colors[(i%len_colors)])
    plt.pause(time_wait)
end = time.time()

print (end - start)
plt.show()
