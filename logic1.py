from z3 import *

input=open("q3_input.txt",'r')
data=input.read().splitlines()
for i in range(len(data)):
    data[i]=data[i].split(" ")

candidates=[f'c{i}' for i in range(len(data))]
print(candidates)
solver=Solver()
slots={i: Int(i) for i in candidates}
print(slots)
print(data)

for i in range(len(candidates)):
    solver.add(slots[candidates[i]]>=0)
    solver.add(slots[candidates[i]]<len(data))

for i in range(len(data)):
    for j in range(len(data)):
        if data[i][j]=='0':
            solver.add(slots[candidates[j]] != i)

for i in candidates:
    for j in candidates:
        if i!=j:
            solver.add(slots[i]!=slots[j])

while solver.check()==sat:
    model=solver.model()
    allotment={i:model[slots[i]].as_long() for i in candidates}
    for i in allotment:
        print(i,allotment[i])
    config=And(1==1,1==1)
    for i in allotment:
        # print(i,slots[i],allotment[i])
        config=And(config,slots[i]==allotment[i])
    config=Not(config)
    # print(config)
    solver.add(config)
    print()