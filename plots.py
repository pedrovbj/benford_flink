import re
from matplotlib import pyplot as plt
from math import log

def main():
    tempo = {}
    for i in [1,4,8,12,16]:
        for j in ["500k", "1m", "2m", "3m", "4m", "5m"]:
            filename = "nos/" + str(i) + "nos/tempo_" + j + "_" + str(i) + "_nos.txt"
            with open(filename, 'r') as f:
                print filename
                t_real = t_user = t_sys = 0.0
                for line in f:
                    m_real = re.match("real\t([0-9]+)m([0-9]+.[0-9]+)s", line)
                    m_user = re.match("user\t([0-9]+)m([0-9]+.[0-9]+)s", line)
                    m_sys = re.match("sys\t([0-9]+)m([0-9]+.[0-9]+)s", line)
                    if m_real:
                        print line[:-1], m_real.groups()
                        minutos, seg = m_real.groups()
                        t_real = 60*float(minutos)+float(seg)
                    if m_user:
                        print line[:-1], m_user.groups()
                        minutos, seg = m_user.groups()
                        t_user = 60*float(minutos)+float(seg)
                    if m_sys:
                        print line[:-1], m_sys.groups()
                        minutos, seg = m_sys.groups()
                        t_sys = 60*float(minutos)+float(seg)
                tempo[(i,j)] = [t_real, t_user, t_sys]
                print tempo[(i,j)]

    print "Real, N X t"
    for i in [1,4,8,12,16]:
        t = []
        for j in ["500k", "1m", "2m", "3m", "4m", "5m"]:
            t.append(tempo[(i,j)][0])
        plt.plot([0.5,1.0,2.0,3.0,4.0,5.0], t, label=str(i)+" node(s)")
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)
    plt.ylabel("Real execution time (t)")
    plt.xlabel("Input size (N)")
    plt.show()

    print "Efficiency X Number of nodes"
    for j in ["500k", "1m", "2m", "3m", "4m", "5m"]:
        e = []
        for i in [4,8,12,16]:
            e.append(tempo[(1,j)][0]/(i*tempo[(i,j)][0]))
        plt.plot([4,8,12,16], e, label=j)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=3, mode="expand", borderaxespad=0.)
    plt.ylabel("Efficiency (E)")
    plt.xlabel("Number of Nodes (p)")
    plt.show()


if __name__ == '__main__':
    main()
