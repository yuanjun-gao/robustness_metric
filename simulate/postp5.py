import numpy as np

f0 = open("traj0.txt", 'r')

n0 = 666

fout = open("traj5.txt", 'w')

for i in range(n0):
    line0 = f0.readline()
    data0 = line0.split(' ')
    x = float(data0[1]) + np.random.rand() * 0.5 - 0.25
    y = float(data0[2]) + np.random.rand() * 0.5 - 0.25
    z = float(data0[3]) + np.random.rand() * 0.5 - 0.25
    fout.write(data0[0] + " " + str(x) + " " + str(y) + " " + str(z) + " " + "1.0 0.0 0.0 0.0\n")

fout.close()