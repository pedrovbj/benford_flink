import re

def main():
    tempo = {}
    for i in [1,4,8,12,16]:
        for j in ["500k", "1m", "2m", "3m", "4m", "5m"]:
            filename = "nos/" + str(i) + "nos/tempo_" + j + "_" + str(i) + "_nos.txt"
            with open(filename) as f:
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


if __name__ == '__main__':
    main()
