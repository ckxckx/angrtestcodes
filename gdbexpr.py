
import gdb
from angrgdb import *
import angr
gdb.execute("file case_expr")
gdb.execute("b main")
gdb.execute("r")

sm = StateManager()
sm.sim(key=0x402020,size=8)
m = sm.simulation_manager()
m.use_technique(angr.exploration_techniques.DFS())


# def debug_func(state):
#     print("State %s is about to do a memory write!"%state)

# m.state.inspect.b('constraints', when=angr.BP_BEFORE, action=debug_fun



def debug_func(state):
    print("=========")
    print("State %s "%state)
    print(state.inspect.expr)
    print(state.inspect.expr_result)
    print(type(state.inspect.expr))

    print(type(state.inspect))

m.active[0].inspect.b('expr', when=angr.BP_AFTER, action=debug_func)

# 需要暴露一个state的接口出来
re=m.explore(find=[0x4005ed])
# re=m.run()
print(re)
print(m)
print(m.found)
print(m.active[0].inspect.added_constraints)
print(m.active[0].solver)
print(m.active[0].solver.constraints)