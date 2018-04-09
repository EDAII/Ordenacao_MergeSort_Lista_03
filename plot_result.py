from matplotlib import pyplot as plt

execucao = [
    ( 1, 7.152557373046875e-07), ( 10001, 0.05105924606323242), ( 20001, 0.10591983795166016), ( 30001, 0.15982627868652344), ( 40001, 0.22411632537841797), ( 50001, 0.28085827827453613), ( 60001, 0.340287446975708), ( 70001, 0.4009556770324707), ( 80001, 0.4622457027435303), ( 90001, 0.5254421234130859), ( 100001, 0.5957679748535156), ( 110001, 0.6540353298187256), ( 120001, 0.7185814380645752), ( 130001, 0.7870070934295654), ( 140001, 0.8519728183746338), ( 150001, 0.9238865375518799), ( 160001, 0.9893262386322021), ( 170001, 1.0866141319274902), ( 180001, 1.1621215343475342), ( 190001, 1.213498592376709), ( 200001, 1.280517816543579), ( 210001, 1.353543996810913), ( 220001, 1.4402287006378174), ( 230001, 1.5028462409973145), ( 240001, 1.5759174823760986), ( 250001, 1.6480979919433594), ( 260001, 1.7134807109832764), ( 270001, 1.8197896480560303), ( 280001, 1.8745012283325195), ( 290001, 1.9390277862548828), ( 300001, 2.0083742141723633), ( 310001, 2.083195686340332), ( 320001, 2.165534734725952), ( 330001, 2.248835802078247), ( 340001, 2.3092470169067383), ( 350001, 2.393674612045288), ( 360001, 2.4771499633789062), ( 370001, 2.539548635482788), ( 380001, 2.590491771697998), ( 390001, 2.6646299362182617), ( 400001, 2.7618155479431152), ( 410001, 2.84002423286438), ( 420001, 2.9115004539489746), ( 430001, 2.9676966667175293), ( 440001, 3.0696089267730713), ( 450001, 3.1242072582244873), ( 460001, 3.2018206119537354), ( 470001, 3.275952100753784), ( 480001, 3.349316358566284), ( 490001, 3.4510483741760254), ( 500001, 3.5462570190429688), ( 510001, 3.5822906494140625), ( 520001, 3.691462516784668), ( 530001, 3.763415575027466), ( 540001, 3.822603702545166), ( 550001, 3.9110639095306396), ( 560001, 3.975893497467041), ( 570001, 4.062248945236206), ( 580001, 4.167872428894043), ( 590001, 4.25617790222168), ( 600001, 4.308430433273315), ( 610001, 4.382746934890747), ( 620001, 7.981959342956543), ( 630001, 4.565828323364258), ( 640001, 4.645046710968018), ( 650001, 4.7346272468566895), ( 660001, 4.779029130935669), ( 670001, 4.853346347808838), ( 680001, 4.952791213989258), ( 690001, 5.042264461517334), ( 700001, 5.100268840789795), ( 710001, 5.196674823760986), ( 720001, 5.25615930557251), ( 730001, 5.335631608963013), ( 740001, 5.442203760147095), ( 750001, 5.490103244781494), ( 760001, 5.6247429847717285), ( 770001, 5.674201965332031), ( 780001, 5.767033100128174), ( 790001, 5.876396179199219), ( 800001, 5.951265811920166), ( 810001, 6.020629644393921), ( 820001, 6.064042329788208), ( 830001, 6.138955354690552), ( 840001, 6.276117563247681), ( 850001, 6.372836112976074), ( 860001, 6.3755223751068115), ( 870001, 6.385838031768799), ( 880001, 6.510791063308716), ( 890001, 6.565899610519409), ( 900001, 6.594520807266235), ( 910001, 6.7384233474731445), ( 920001, 6.7581236362457275), ( 930001, 6.852382659912109), ( 940001, 6.9308342933654785), ( 950001, 7.0413453578948975), ( 960001, 7.0944390296936035), ( 970001, 7.172158479690552), ( 980001, 7.244277238845825), ( 990001, 7.365815877914429), ( 1740001, 14.6139500141), ( 1750001, 14.8542711735), ( 1760001, 14.7978348732), ( 1770001, 15.1199600697), ( 1780001, 15.9613618851), ( 1790001, 15.8576381207), ( 1800001, 18.6744630337), ( 1810001, 17.3739449978), ( 1820001, 16.3238298893), ( 1830001, 15.8971188068), ( 1840001, 15.494122982), ( 1850001, 15.591091156), ( 1860001, 15.6627049446), ( 1870001, 15.7935111523), ( 1880001, 15.836961031), ( 1890001, 15.9550499916), ( 1900001, 16.0238289833), ( 1910001, 16.1531500816), ( 1920001, 16.2282559872), ( 1930001, 16.3357150555), ( 1940001, 16.414716959), ( 1950001, 16.5336070061), ( 1960001, 16.7551300526), ( 1970001, 16.9126520157), ( 1980001, 14.1025710106), ( 1990001, 11.3969299793)
]

execucao_x = zip(*execucao)[0]

execucao_y = zip(*execucao)[1]


plt.plot(execucao_x[::2], execucao_y[::2], 'ro', execucao_x[1::2], execucao_y[1::2], 'go')
plt.axis([execucao_x[0], execucao_x[-1]*3, execucao_y[0], execucao_y[-1]*3])
plt.show()