#Libraries
from collections import deque

#TQ=2
time_quantum = 2

class Prs:
    def __init__(self, name, AT, RT):
        self.name = name
        self.AT = AT
        self.RT = RT
        self.t_t = 0
        self.CPU = -1

    def __repr__(self):
        return self.name

#        Pid  AT  BT
p1 = Prs('P1', 0, 5)
p2 = Prs('P2', 1, 4)
p3 = Prs('P3', 2, 2)
p4 = Prs('P4', 4, 1)
P = [p1, p2, p3, p4]
end_times = {Prs.name: 0 for Prs in P}
WT = {Prs.name: 0 for Prs in P}
R_T = {Prs.name: 0 for Prs in P}
queue = deque()
run_prs = None  # Tracks running Prs in the CPU
P_s = 0  # Tracks the time running Prs spent in the CPU

for t in range(12):
    if t == 0:
        for p in P:
            if p.AT == 0:
                queue.append(p)

    if run_prs == None:
        if len(queue) > 0:
            run_prs = queue.popleft()
            if run_prs.CPU == -1:
                run_prs.CPU = t
            P_s = 0
    
    for p in P:
        if p.AT == t + 1:
            queue.append(p)
    
    if run_prs is not None:
        run_prs.t_t += 1
        P_s += 1
        if run_prs.RT == run_prs.t_t:
            end_times[str(run_prs)] = t + 1
            WT[str(run_prs)] = end_times[str(run_prs)] - run_prs.AT - run_prs.RT
            R_T[str(run_prs)] = run_prs.CPU - run_prs.AT
            run_prs = None
            P_s = 0
        elif P_s >= time_quantum:
            queue.append(run_prs)
            run_prs = None
            P_s = 0

print()
print("G A N T T-C H A R T")
print(end_times)  
print()

print("Prs\t AT\t BT\t TAT\t WT\t RT")
t_TAT = 0
t_WT = 0
t_RT = 0
for p in P:
    tat = end_times[p.name] - p.AT
    wt = WT[p.name]
    rt = R_T[p.name]
    t_TAT += tat
    t_WT += wt
    t_RT += rt
    print(p.name, "\t", p.AT, "\t", p.RT, "\t", tat, "\t", wt, "\t", rt)
m = len(P)
A_tat = t_TAT / m
A_wt = t_WT / m
A_rt = t_RT / m

#AvErAgE 
print("A tat: ", A_tat)
print("A wt: ", A_wt)
print("A rt: ", A_rt)
