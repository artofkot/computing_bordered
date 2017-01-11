from basics import AttrDict, Generator, Bunch_of_arrows, debug
from right_a_module import Right_A_module
from left_a_module import Left_A_module

def dualization_right_to_left_A(Right_A):
    gen_by_name=AttrDict({})
    for gen in Right_A.genset:
        gen_by_name[gen.name+'*']=Generator(gen.name+'*')
        gen_by_name[gen.name+'*'].add_idems(gen.idem.right,0)

    left_a_arrows=Bunch_of_arrows([])
    for arrow in Right_A.right_a_arrows:
        left_a_arrows[(arrow[1],gen_by_name[arrow[2].name+'*'],gen_by_name[arrow[0].name+'*'])]+=1

    return Left_A_module(gen_by_name,left_a_arrows,Right_A.algebra,name=Right_A.name + '_dual')
