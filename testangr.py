import angr
import angr
proj = angr.Project('/home/ckx/testangr/case1')

# get our state
state = proj.factory.entry_state()
simgr = proj.factory.simgr(state)
simgr.use_technique(angr.exploration_techniques.DFS())

# add a breakpoint. This breakpoint will drop into ipdb right before a memory write happens.
# s.inspect.b('mem_write')

# on the other hand, we can have a breakpoint trigger right *after* a memory write happens. 
# we can also have a callback function run instead of opening ipdb.
# def debug_func(state):
#     print("State %s is about to do a memory write!"%state)

# state.inspect.b('mem_write', when=angr.BP_BEFORE, action=debug_func)


def debug_func(state):
    print("State %s is about to do a memory write!"%state)


# simgr.
simgr.active[0].inspect.b('constraints', when=angr.BP_BEFORE, action=debug_func)
# state.inspect.b('constraints', when=angr.BP_BEFORE, action=debug_func)




simgr.run()




# # or, you can have it drop you in an embedded IPython!
# >>> s.inspect.b('mem_write', when=angr.BP_AFTER, action=angr.BP_IPYTHON)