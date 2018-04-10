
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

i_menor = 0
i_maior = 0
for i in range(len(execucao_x)-1):           
     if (execucao_x[i+1]-execucao_x[i]) > (execucao_x[i_maior]-execucao_x[i_menor]):
         i_menor=i
         i_maior=i+1
print (execucao_x[i_menor], execucao_x[i_maior])