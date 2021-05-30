f = open("SUR5_Train.DAT")
data=[]
X=[]
y=[]
lines=f.readlines()
header=lines[0].split()
n=int(lines[1])
for line in lines[2:]:
    print(line)
    if '/' in line:
        spl= line.split()
        skip_samples=int(float(spl[0]))
        atomic=float(spl[1])
        beta=float(spl[2])
    else:
        dt=line.split()
        dose = float(dt[0])
        avg_life=float(dt[1])
        X.append([atomic,beta,dose])
        y.append(avg_life)
        to_append=[atomic,beta,dose,avg_life]
        data.append(to_append)
print(data)
