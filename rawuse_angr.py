import angr
import logging
import claripy
from termcolor import cprint
import ipdb

#新建符号对象，设置bit数目
arg1=claripy.BVS('arg1',16*8)
#设置hook instrument的逻辑，137是修改返回的值，64代表寄存器长度
# def calc_offset(state):
#     state.regs.rax=state.se.BVV(137,64)


logging.basicConfig=angr.manager.l.setLevel('DEBUG')

pro=angr.Project("./chall")
state=pro.factory.entry_state(args=['./chall',arg1])



simgr=pro.factory.simgr(state)


def dumpstates():
    for state in simgr.active:
        cprint(state,"yellow")

# print("the first step")
# simgr.step()

# dumpstates()


ts =None

for i in range(15):
    print("the next step")
    simgr.step()
    dumpstates()
    ts = simgr.active[0]
    print(ts.solver.constraints)
    if len(simgr.active)>1:
        print("i is %d" % i)
        break

# ipdb.set_trace()
# ipdb.run("b angr.state_plugins.symbolic_memory.SimSymbolicMemory._store")
for i in range(1):
    print("the next step")
    simgr.step()
    dumpstates()
    ts = simgr.active[0]
    print("what the fuck it is:")
    print(ts.solver.constraints)

    if len(simgr.active)>1:
        print("i is %d" % i)
        break


# for k in r
# simgr.step()

