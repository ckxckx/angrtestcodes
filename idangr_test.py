
#coding:utf-8
import angr
import angrdbg
from datetime import datetime
from angr.errors import SimProcedureArgumentError, SimProcedureError, SimSolverError
import idangr


if not idangr.is_initialized():
    idangr.init() #use local angrdbg
    # idangr.init(is_remote=False, host=None, port=None, use_pin=False)


    # idangr.init(is_remote=True, host="202.112.51.159", port=18812, use_pin=False)


import idc
# import angrdbg
import logging
import idaapi
from monkeyhex import *

from idaapi import *
import idc
import idaapi
logging.basicConfig
angr.manager.l.setLevel('DEBUG')

sym_mem_list=[]

sm = angrdbg.StateManager()
# sm = angrdbg.StateManager(check_dbg=True)

target_mem_addr = 0x402030
mem_size = 0x100
sm.sim(target_mem_addr,mem_size)

m = sm.simulation_manager()

re=m.explore(find = 0x400601)

s = re.found[0]
print(s.solver.constraints)