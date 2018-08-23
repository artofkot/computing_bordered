# -*- coding: utf-8 -*- 
import sys
sys.path.append('../')
import cPickle as pickle

from algebraic_structures.basics import  *
from algebraic_structures.dualization import *
from algebraic_structures.algebra import *
from algebraic_structures.tensoring import *
from algebraic_structures.chain_complex import *
from algebraic_structures.dd_bimodule import *
from algebraic_structures.aa_bimodule import *
from algebraic_structures.da_bimodule import *
from algebraic_structures.right_a_module import *
from algebraic_structures.left_a_module import *
from algebraic_structures.algebra_simpler import *
from algebraic_structures.left_d_module import *
from algebraic_structures.right_d_module import *
from algebraic_structures.specific_algebras_modules_bimodules import *

#### modules over pil_A
def init_left_d_N_L0(pil_A):
    gen_by_name=AttrDict({
                "L0_i0": Generator("L0_i0"),
                "L0_i1": Generator("L0_i1"),
                "L0_j0": Generator("L0_j0"),
                "L0_j1": Generator("L0_j1"),
                })

    gen_by_name.L0_i0.add_idems(pil_A.idem_by_name.i0, 0)
    gen_by_name.L0_i1.add_idems(pil_A.idem_by_name.i1, 0)
    gen_by_name.L0_j0.add_idems(pil_A.idem_by_name.j0, 0)
    gen_by_name.L0_j1.add_idems(pil_A.idem_by_name.j1, 0)
    

    left_d_arrows=Bunch_of_arrows([
        (              gen_by_name.L0_i0,
           pil_A.gen_by_name.r0, gen_by_name.L0_j0),
        (              gen_by_name.L0_i0,
           pil_A.gen_by_name.et12, gen_by_name.L0_j1),
        (              gen_by_name.L0_i1,
           pil_A.gen_by_name.ks123, gen_by_name.L0_j1),
        (              gen_by_name.L0_i1,
           pil_A.gen_by_name.et23, gen_by_name.L0_j0),
                                    ])
    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="N_L0")
N_L0=init_left_d_N_L0(pil_A)
def init_left_d_N_L1(pil_A):
    gen_by_name=AttrDict({
                "L1_i1": Generator("L1_i1"),
                "L1_j2": Generator("L1_j2"),
                "L1_i2": Generator("L1_i2"),
                "L1_j1": Generator("L1_j1")

                })

    gen_by_name.L1_i1.add_idems(pil_A.idem_by_name.i1, 0)
    gen_by_name.L1_j2.add_idems(pil_A.idem_by_name.j2, 0)
    gen_by_name.L1_i2.add_idems(pil_A.idem_by_name.i2, 0)
    gen_by_name.L1_j1.add_idems(pil_A.idem_by_name.j1, 0)
    

    left_d_arrows=Bunch_of_arrows([
        (              gen_by_name.L1_i1,
           pil_A.gen_by_name.ks12, gen_by_name.L1_j2),

        (              gen_by_name.L1_i2,
             pil_A.gen_by_name.r2, gen_by_name.L1_j2),
        (              gen_by_name.L1_i2,
             pil_A.gen_by_name.ks23, gen_by_name.L1_j1),
        (              gen_by_name.L1_i1,
             pil_A.gen_by_name.et2, gen_by_name.L1_j1),
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="N_L1")
N_L1=init_left_d_N_L1(pil_A)
def init_Left_D_j1(pil_A):
    gen_by_name=AttrDict({
                "arc_j1": Generator("arc_j1"),
                })

    gen_by_name.arc_j1.add_idems(pil_A.idem_by_name.j1, 0)
    

    left_d_arrows=Bunch_of_arrows([])

    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="Left_D_j1")
Dj1=init_Left_D_j1(pil_A)
def init_Left_D_i1(pil_A):
    gen_by_name=AttrDict({
                "arc_i1": Generator("arc_i1"),
                })

    gen_by_name.arc_i1.add_idems(pil_A.idem_by_name.i1, 0)

    left_d_arrows=Bunch_of_arrows([])
    
    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="Left_D_i1")
Di1=init_Left_D_i1(pil_A)
def init_Left_D_i2(pil_A):
    gen_by_name=AttrDict({
                "arc_i2": Generator("arc_i2"),
                })

    gen_by_name.arc_i2.add_idems(pil_A.idem_by_name.i2, 0)

    left_d_arrows=Bunch_of_arrows([])
    
    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="Left_D_i2")
Di2=init_Left_D_i2(pil_A)
def init_Left_D_j2(pil_A):
    gen_by_name=AttrDict({
                "arc_j2": Generator("arc_j2"),
                })

    gen_by_name.arc_j2.add_idems(pil_A.idem_by_name.j2, 0)

    left_d_arrows=Bunch_of_arrows([])
    
    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="Left_D_j2")
Dj2=init_Left_D_j2(pil_A)
def init_Left_D_j0(pil_A):
    gen_by_name=AttrDict({
                "arc_j0": Generator("arc_j0"),
                })

    gen_by_name.arc_j0.add_idems(pil_A.idem_by_name.j0, 0)

    left_d_arrows=Bunch_of_arrows([])
    
    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="Left_D_j0")
Dj0=init_Left_D_j0(pil_A)
def init_Left_D_i0(pil_A):
    gen_by_name=AttrDict({
                "arc_i0": Generator("arc_i0"),
                })

    gen_by_name.arc_i0.add_idems(pil_A.idem_by_name.i0, 0)

    left_d_arrows=Bunch_of_arrows([])
    
    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="Left_D_i0")
Di0=init_Left_D_i0(pil_A)

def init_left_d_N_U0(pil_A):
    gen_by_name=AttrDict({
                "U0_i0": Generator("U0_i0"),
                "U0_i1": Generator("U0_i1"),
                "U0_j0": Generator("U0_j0"),
                "U0_j1": Generator("U0_j1"),
                })

    gen_by_name.U0_i0.add_idems(pil_A.idem_by_name.i0, 0)
    gen_by_name.U0_i1.add_idems(pil_A.idem_by_name.i1, 0)
    gen_by_name.U0_j0.add_idems(pil_A.idem_by_name.j0, 0)
    gen_by_name.U0_j1.add_idems(pil_A.idem_by_name.j1, 0)
    

    left_d_arrows=Bunch_of_arrows([
        (              gen_by_name.U0_i0,
           pil_A.gen_by_name.r0, gen_by_name.U0_j0),
        (              gen_by_name.U0_i0,
           pil_A.gen_by_name.et1, gen_by_name.U0_i1),
        (              gen_by_name.U0_i1,
           pil_A.gen_by_name.ks123, gen_by_name.U0_j1),
        (              gen_by_name.U0_j1,
           pil_A.gen_by_name.et3, gen_by_name.U0_j0),
                                    ])
    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="N_U0")
N_U0=init_left_d_N_U0(pil_A)
def init_left_d_N_U1(pil_A):
    gen_by_name=AttrDict({
                "U1_i1": Generator("U1_i1"),
                "U1_j2": Generator("U1_j2"),
                "U1_i2": Generator("U1_i2"),
                "U1_j1": Generator("U1_j1")

                })

    gen_by_name.U1_i1.add_idems(pil_A.idem_by_name.i1, 0)
    gen_by_name.U1_j2.add_idems(pil_A.idem_by_name.j2, 0)
    gen_by_name.U1_i2.add_idems(pil_A.idem_by_name.i2, 0)
    gen_by_name.U1_j1.add_idems(pil_A.idem_by_name.j1, 0)
    

    left_d_arrows=Bunch_of_arrows([
        (              gen_by_name.U1_i1,
           pil_A.gen_by_name.ks1, gen_by_name.U1_i2),
        (              gen_by_name.U1_i2,
             pil_A.gen_by_name.r2, gen_by_name.U1_j2),
        (              gen_by_name.U1_j2,
             pil_A.gen_by_name.ks3, gen_by_name.U1_j1),
        (              gen_by_name.U1_i1,
             pil_A.gen_by_name.et2, gen_by_name.U1_j1),
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="N_U1")
N_U1=init_left_d_N_U1(pil_A)

#### modules over B_r
def init_Left_B_N_L0(B_r):
    gen_by_name=AttrDict({
                "x": Generator("x"),
                })

    gen_by_name.x.add_idems(B_r.idem_by_name.l0,0)
    

    left_d_arrows=Bunch_of_arrows([
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,B_r,name="B_N_L0")
B_N_L0=init_Left_B_N_L0(B_r)
def init_Left_B_N_L1(B_r):
    gen_by_name=AttrDict({
                "y": Generator("y"),
                })

    gen_by_name.y.add_idems(B_r.idem_by_name.l1,0)
    

    left_d_arrows=Bunch_of_arrows([
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,B_r,name="B_N_L1")
B_N_L1=init_Left_B_N_L1(B_r)
def init_Left_B_N_L2(B_r):
    gen_by_name=AttrDict({
                "z0": Generator("z0"),
                "z1": Generator("z1"),
                })

    gen_by_name.z0.add_idems(B_r.idem_by_name.l0,0)
    gen_by_name.z1.add_idems(B_r.idem_by_name.l1,0)
    
        
    left_d_arrows=Bunch_of_arrows([
        (              gen_by_name.z0,
           B_r.gen_by_name.p01, gen_by_name.z1),
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,B_r,name="B_N_L2")
B_N_L2=init_Left_B_N_L2(B_r)




################
################
################ playing around with the general decomposition T_1+T+2=K

with open('fuk.pkl', 'rb') as input:
    Fuk = pickle.load(input)
#### a_AA_b_r from Fuk(N_L0,N_L1,Di0,...,Dj2)
generators=[gen for gen in Fuk.genset if gen.name[:2]=='(a']
a_AA_b_r=base_change_AA_from_fuk(Fuk,generators,pil_A,B_r)
a_AA_b_r=aa_randomly_cancel_until_possible(a_AA_b_r)

####
# b_r_AA_a=dualization_of_AA(a_AA_b_r)
# DA=dd_aa_box_tensor_product(DD_bar_r_dual,a_AA_b_r)
# DA=da_cancel_until_possible(DA)

# two_b_B_r_b=aa_da_box_tensor_product(b_r_AA_a,DA)
# simpler_names_for_generators(two_b_B_r_b)
# two_b_B_r_b=aa_cancel_until_possible_clever(two_b_B_r_b)
# rename_gen_in_module(two_b_B_r_b,'x2','b_c0')
# rename_gen_in_module(two_b_B_r_b,'x0','b_l0')
# rename_gen_in_module(two_b_B_r_b,'x1','b_p01')
# rename_gen_in_module(two_b_B_r_b,'x7','b_c1')
# rename_gen_in_module(two_b_B_r_b,'x3','b_l1')
# rename_gen_in_module(two_b_B_r_b,'x4','b_q10')
# rename_gen_in_module(two_b_B_r_b,'x10','a_c0')
# rename_gen_in_module(two_b_B_r_b,'x12','a_p01')
# rename_gen_in_module(two_b_B_r_b,'x11','a_l0')
# rename_gen_in_module(two_b_B_r_b,'x16','a_c1')
# rename_gen_in_module(two_b_B_r_b,'x19','a_l1')
# rename_gen_in_module(two_b_B_r_b,'x15','a_q10')

# b_B_r_b=a_AA_a(B_r)
# real_two_b_B_r_b=aa_direct_sum(b_B_r_b,b_B_r_b)

# f=Bunch_of_arrows([])
# f[((),two_b_B_r_b.gen_by_name['a_l0'],(),real_two_b_B_r_b.gen_by_name['aa_l0'])]+=1
# f[((),two_b_B_r_b.gen_by_name['a_c0'],(),real_two_b_B_r_b.gen_by_name['aa_c0'])]+=1
# f[((),two_b_B_r_b.gen_by_name['a_l1'],(),real_two_b_B_r_b.gen_by_name['aa_l1'])]+=1
# f[((),two_b_B_r_b.gen_by_name['a_c1'],(),real_two_b_B_r_b.gen_by_name['aa_c1'])]+=1
# f[((),two_b_B_r_b.gen_by_name['a_p01'],(),real_two_b_B_r_b.gen_by_name['aa_p01'])]+=1
# f[((),two_b_B_r_b.gen_by_name['a_q10'],(),real_two_b_B_r_b.gen_by_name['aa_q10'])]+=1
# f[((),two_b_B_r_b.gen_by_name['b_l0'],(),real_two_b_B_r_b.gen_by_name['bb_l0'])]+=1
# f[((),two_b_B_r_b.gen_by_name['b_c0'],(),real_two_b_B_r_b.gen_by_name['bb_c0'])]+=1
# f[((),two_b_B_r_b.gen_by_name['b_l1'],(),real_two_b_B_r_b.gen_by_name['bb_l1'])]+=1
# f[((),two_b_B_r_b.gen_by_name['b_c1'],(),real_two_b_B_r_b.gen_by_name['bb_c1'])]+=1
# f[((),two_b_B_r_b.gen_by_name['b_p01'],(),real_two_b_B_r_b.gen_by_name['bb_p01'])]+=1
# f[((),two_b_B_r_b.gen_by_name['b_q10'],(),real_two_b_B_r_b.gen_by_name['bb_q10'])]+=1

# f[((B_r.gen_by_name['c0'],),two_b_B_r_b.gen_by_name['a_l0'],(),real_two_b_B_r_b.gen_by_name['bb_l0'])]+=1
# f[((B_r.gen_by_name['c0'],),two_b_B_r_b.gen_by_name['a_c0'],(),real_two_b_B_r_b.gen_by_name['bb_c0'])]+=1
# f[((B_r.gen_by_name['c0'],),two_b_B_r_b.gen_by_name['a_p01'],(),real_two_b_B_r_b.gen_by_name['bb_p01'])]+=1

# f[((B_r.gen_by_name['c0'],),two_b_B_r_b.gen_by_name['a_l0'],(),real_two_b_B_r_b.gen_by_name['bb_l0'])]+=1
# f[((B_r.gen_by_name['c0'],),two_b_B_r_b.gen_by_name['a_c0'],(),real_two_b_B_r_b.gen_by_name['bb_c0'])]+=1
# f[((B_r.gen_by_name['c1'],),two_b_B_r_b.gen_by_name['a_l1'],(),real_two_b_B_r_b.gen_by_name['bb_l1'])]+=1

# f[((),two_b_B_r_b.gen_by_name['a_l0'],(B_r.gen_by_name['c0'],),real_two_b_B_r_b.gen_by_name['bb_l0'])]+=1
# f[((),two_b_B_r_b.gen_by_name['a_l1'],(B_r.gen_by_name['c1'],),real_two_b_B_r_b.gen_by_name['bb_l1'])]+=1


# f[((B_r.gen_by_name['c0'],),two_b_B_r_b.gen_by_name['a_l0'],(),real_two_b_B_r_b.gen_by_name['bb_l0'])]+=1


# f[((B_r.gen_by_name['c0'],),two_b_B_r_b.gen_by_name['a_l0'],(),real_two_b_B_r_b.gen_by_name['bb_l0'])]+=1
# f[((B_r.gen_by_name['c1'],),two_b_B_r_b.gen_by_name['a_l1'],(),real_two_b_B_r_b.gen_by_name['bb_l1'])]+=1
# f[((B_r.gen_by_name['p01'],),two_b_B_r_b.gen_by_name['a_c1'],(),real_two_b_B_r_b.gen_by_name['bb_p01'])]+=1
# f[((B_r.gen_by_name['q10'],),two_b_B_r_b.gen_by_name['a_c0'],(),real_two_b_B_r_b.gen_by_name['bb_q10'])]+=1



# f[((B_r.gen_by_name['c1'],),two_b_B_r_b.gen_by_name['a_c1'],(),real_two_b_B_r_b.gen_by_name['bb_c1'])]+=1
# f[((B_r.gen_by_name['c1'],),two_b_B_r_b.gen_by_name['a_q10'],(),real_two_b_B_r_b.gen_by_name['bb_q10'])]+=1



# f[((B_r.gen_by_name['c1'],),two_b_B_r_b.gen_by_name['a_c1'],(),real_two_b_B_r_b.gen_by_name['bb_c1'])]+=1
# f[((B_r.gen_by_name['q10'],),two_b_B_r_b.gen_by_name['a_c0'],(),real_two_b_B_r_b.gen_by_name['bb_q10'])]+=1
# f[((B_r.gen_by_name['q10'],),two_b_B_r_b.gen_by_name['a_p01'],(),real_two_b_B_r_b.gen_by_name['bb_l1'])]+=1
# f[((B_r.gen_by_name['c0'],),two_b_B_r_b.gen_by_name['a_p01'],(),real_two_b_B_r_b.gen_by_name['bb_p01'])]+=1
# f[((B_r.gen_by_name['c0'],),two_b_B_r_b.gen_by_name['a_c0'],(),real_two_b_B_r_b.gen_by_name['bb_c0'])]+=1

# f[((),two_b_B_r_b.gen_by_name['a_l0'],(B_r.gen_by_name['c0'],),real_two_b_B_r_b.gen_by_name['bb_l0'])]+=1
# f[((),two_b_B_r_b.gen_by_name['a_c0'],(B_r.gen_by_name['p01'],),real_two_b_B_r_b.gen_by_name['bb_p01'])]+=1


# f[((B_r.gen_by_name['c0'],),two_b_B_r_b.gen_by_name['a_p01'],(),real_two_b_B_r_b.gen_by_name['bb_q10'])]+=1


# two_b_B_r_b.show()
# f.delete_arrows_with_even_coeff()
# f.show()
# df=aa_check_df_is_0(two_b_B_r_b,real_two_b_B_r_b,f)


# #########  b_r_AA_a from Fuk(N_L0,N_L1,Di0,...,Dj2)
# generators=[gen for gen in Fuk.genset if gen.name[:2]=='(L']
# b_r_AA_a=base_change_AA_from_fuk(Fuk,generators,B_r,pil_A)
# b_r_AA_a=aa_randomly_cancel_until_possible(b_r_AA_a)

# Amod=aa_d_box_tensor_product(a_AA_b_r,B_N_L2)
# N_L2=dd_a_box_tensor_product(DD_bar_r_dual,Amod)
# N_L2=left_d_randomly_cancel_until_possible(N_L2)

# ########## !!!!
# Aa=d_aa_box_tensor_product(dualization_left_to_right_D(B_N_L0),b_r_AA_a) 
# Aa.show() # получается А модуль для L_0, а мне нужен для W_0!!!
# Kh=a_d_box_tensor_product(Aa,N_L2)
# print homology_dim(Kh) # 2 incorrect!

# Ab=d_aa_box_tensor_product(dualization_left_to_right_D(B_N_L0),a_AA_a(B_r)) 
# Kh=a_d_box_tensor_product(Ab,B_N_L2)
# print homology_dim(Kh) # 1 correct

# DA=dd_aa_box_tensor_product(DD_bar_r_dual,a_AA_b_r)
# DA=da_randomly_cancel_until_possible(DA)
# new_AA=aa_da_box_tensor_product(b_r_AA_a,DA)
# new_AA=aa_randomly_cancel_until_possible(new_AA)
# new_AA.show()

################################
################################ trying to find bar_B_r
# def init_bar_B_r(B_r):
#     gen_by_name=AttrDict({
#                 "p01": Generator("p01"),
#                 "q10": Generator("q10"),
#                 "c0": Generator("c0"),
#                 "c1": Generator("c1"),
#                 "l1": Generator("l1"),
#                 "l0": Generator("l0"),
#                 "p01_c1": Generator("p01_c1"),
#                 "q10_c0": Generator("q10_c0"),
#                 # "c0_p01": Generator("c0_p01"),
#                 # "c1_q10": Generator("c1_q10"),
#                 # "c1_q10_c0": Generator("c1_q10_c0"),
#                 # "c0_p01_c1": Generator("c0_p01_c1"),
#                 # "p01_c1_q10": Generator("p01_c1_q10"),
#                 # "q10_c0_p01": Generator("q10_c0_p01"),

#                 # "c1_q10_c0_p01": Generator("c1_q10_c0_p01"),
#                 # "c0_p01_c1_q10": Generator("c0_p01_c1_q10"),
#                 # "p01_c1_q10_c0": Generator("p01_c1_q10_c0"),
#                 # "q10_c0_p01_c1": Generator("q10_c0_p01_c1"),
#                 })

#     gen_by_name.l0.add_idems(B_r.idem_by_name.l0, B_r.idem_by_name.l0)
#     gen_by_name.l1.add_idems(B_r.idem_by_name.l1, B_r.idem_by_name.l1)
#     gen_by_name.p01.add_idems(B_r.idem_by_name.l0, B_r.idem_by_name.l1)
#     gen_by_name.q10.add_idems(B_r.idem_by_name.l1, B_r.idem_by_name.l0)
#     gen_by_name.c0.add_idems(B_r.idem_by_name.l0, B_r.idem_by_name.l0)
#     gen_by_name.c1.add_idems(B_r.idem_by_name.l1, B_r.idem_by_name.l1)

#     gen_by_name.p01_c1.add_idems(B_r.idem_by_name.l0, B_r.idem_by_name.l1)
#     gen_by_name.q10_c0.add_idems(B_r.idem_by_name.l1, B_r.idem_by_name.l0)
#     # gen_by_name.c0_p01.add_idems(B_r.idem_by_name.l0, B_r.idem_by_name.l1)
#     # gen_by_name.c1_q10.add_idems(B_r.idem_by_name.l1, B_r.idem_by_name.l0)

#     # gen_by_name.c1_q10_c0.add_idems(B_r.idem_by_name.l1, B_r.idem_by_name.l0)
#     # gen_by_name.c0_p01_c1.add_idems(B_r.idem_by_name.l0, B_r.idem_by_name.l1)
#     # gen_by_name.p01_c1_q10.add_idems(B_r.idem_by_name.l0, B_r.idem_by_name.l0)
#     # gen_by_name.q10_c0_p01.add_idems(B_r.idem_by_name.l1, B_r.idem_by_name.l1)

#     # gen_by_name.c1_q10_c0_p01.add_idems(B_r.idem_by_name.l1, B_r.idem_by_name.l1)
#     # gen_by_name.c0_p01_c1_q10.add_idems(B_r.idem_by_name.l0, B_r.idem_by_name.l0)
#     # gen_by_name.p01_c1_q10_c0.add_idems(B_r.idem_by_name.l0, B_r.idem_by_name.l0)
#     # gen_by_name.q10_c0_p01_c1.add_idems(B_r.idem_by_name.l1, B_r.idem_by_name.l1)


#     dd_arrows=Bunch_of_arrows([
#         (      gen_by_name.c0,
#         B_r.gen_by_name.c0,gen_by_name.l0,1),
#         (      gen_by_name.c0,
#         1,gen_by_name.l0,B_r.gen_by_name.c0),
#         (      gen_by_name.c1,
#         B_r.gen_by_name.c1,gen_by_name.l1,1),
#         (      gen_by_name.c1,
#         1,gen_by_name.l1,B_r.gen_by_name.c1),

#         (      gen_by_name.p01,
#         B_r.gen_by_name.p01,gen_by_name.l1,1),
#         (      gen_by_name.p01,
#         1,gen_by_name.l0,B_r.gen_by_name.p01),
#         (      gen_by_name.q10,
#         B_r.gen_by_name.q10,gen_by_name.l0,1),
#         (      gen_by_name.q10,
#         1,gen_by_name.l1,B_r.gen_by_name.q10),

#         (      gen_by_name.p01_c1,
#         B_r.gen_by_name.p01,gen_by_name.c1,1),
#         (      gen_by_name.p01_c1,
#         1,gen_by_name.p01,B_r.gen_by_name.c1),
#         (      gen_by_name.q10_c0,
#         B_r.gen_by_name.q10,gen_by_name.c0,1),
#         (      gen_by_name.q10_c0,
#         1,gen_by_name.q10,B_r.gen_by_name.c0),

#         # (      gen_by_name.c0_p01,
#         # B_r.gen_by_name.c0,gen_by_name.p01,1),
#         # (      gen_by_name.c0_p01,
#         # 1,gen_by_name.c0,B_r.gen_by_name.p01),
#         # (      gen_by_name.c1_q10,
#         # B_r.gen_by_name.c1,gen_by_name.q10,1),
#         # (      gen_by_name.c1_q10,
#         # 1,gen_by_name.c1,B_r.gen_by_name.q10),
                                  


#         # (      gen_by_name.c1_q10_c0,
#         # B_r.gen_by_name.c1,gen_by_name.q10_c0,1),
#         # (      gen_by_name.c1_q10_c0,
#         # 1,gen_by_name.c1_q10,B_r.gen_by_name.c0),
#         # (      gen_by_name.c0_p01_c1,
#         # B_r.gen_by_name.c0,gen_by_name.p01_c1,1),
#         # (      gen_by_name.c0_p01_c1,
#         # 1,gen_by_name.c0_p01,B_r.gen_by_name.c1),
#         # (      gen_by_name.p01_c1_q10,
#         # B_r.gen_by_name.p01,gen_by_name.c1_q10,1),
#         # (      gen_by_name.p01_c1_q10,
#         # 1,gen_by_name.p01_c1,B_r.gen_by_name.q10),
#         # (      gen_by_name.q10_c0_p01,
#         # B_r.gen_by_name.q10,gen_by_name.c0_p01,1),
#         # (      gen_by_name.q10_c0_p01,
#         # 1,gen_by_name.q10_c0,B_r.gen_by_name.p01),

#         # (      gen_by_name.c1_q10_c0_p01,
#         # B_r.gen_by_name.c1,gen_by_name.q10_c0_p01,1),
#         # (      gen_by_name.c1_q10_c0_p01,
#         # 1,gen_by_name.c1_q10_c0,B_r.gen_by_name.p01),
#         # (      gen_by_name.c0_p01_c1_q10,
#         # B_r.gen_by_name.c0,gen_by_name.p01_c1_q10,1),
#         # (      gen_by_name.c0_p01_c1_q10,
#         # 1,gen_by_name.c0_p01_c1,B_r.gen_by_name.q10),

#         # (      gen_by_name.p01_c1_q10_c0,
#         # B_r.gen_by_name.p01,gen_by_name.c1_q10_c0,1),
#         # (      gen_by_name.p01_c1_q10_c0,
#         # 1,gen_by_name.p01_c1_q10,B_r.gen_by_name.c0),
#         # (      gen_by_name.q10_c0_p01_c1,
#         # B_r.gen_by_name.q10,gen_by_name.c0_p01_c1,1),
#         # (      gen_by_name.q10_c0_p01_c1,
#         # 1,gen_by_name.q10_c0_p01,B_r.gen_by_name.c1),
#                                     ])


#     return DD_bimodule(gen_by_name,dd_arrows,B_r,B_r,name="bar_B_r")
# bar_B_r=init_bar_B_r(B_r)
# bar_B_r.show()

# DA_id=dd_aa_box_tensor_product(bar_B_r,a_AA_a(B_r))
# DA_id=da_randomly_cancel_until_possible(DA_id)
# DA_id.show()

##################################################################################
##################################################################################
##################################################################################
###########  computing HFK algebra Fuk(U0,U1)
# Fuk=algebra_from_mor_spaces_of_left_D_structures(
#                                             N_U0,
#                                             N_U1,
#                                             )

# Fuk=rename_generators(Fuk,[
#                         ('(U0_j1, j1, U0_j1)','00(j1)' ), 
#                         ('(U0_i0, et123, U0_j0)','00(et123)' ),
#                         ('(U0_i1, et2, U0_j1)','00(et2)' ),
#                         ('(U0_i0, et12, U0_j1)','00(et12)' ),
#                         ('(U0_j1, et3, U0_j0)','00(et3)' ),
#                         ('(U0_i1, et23, U0_j0)','00(et23)' ),
#                         ('(U0_i0, r0, U0_j0)','00(r0)' ),
#                         ('(U0_i1, i1, U0_i1)','00(i1)' ),
#                         ('(U0_i0, i0, U0_i0)','00(i0)' ),
#                         ('(U0_j0, j0, U0_j0)','00(j0)' ),
#                         ('(U0_i1, ks123, U0_j1)','00(ks123)' ),
#                         ('(U0_i0, et1, U0_i1)','00(et1)' ),

#                         ('(U1_j2, j2, U1_j2)','11(j2)'), 
#                         ('(U1_i1, ks12, U1_j2)','11(ks12)'), 
#                         ('(U1_i2, ks23, U1_j1)','11(ks23)'), 
#                         ('(U1_i1, ks123, U1_j1)','11(ks123)'), 
#                         ('(U1_i1, ks1, U1_i2)','11(ks1)'), 
#                         ('(U1_i2, i2, U1_i2)','11(i2)'), 
#                         ('(U1_i2, ks2, U1_j2)','11(ks2)'), 
#                         ('(U1_i1, et2, U1_j1)','11(et2)'), 
#                         ('(U1_i1, i1, U1_i1)','11(i1)'),
#                         ('(U1_i2, r2, U1_j2)','11(r2)'), 
#                         ('(U1_j2, ks3, U1_j1)','11(ks3)'), 
#                         ('(U1_j1, j1, U1_j1)','11(j1)'), 

#                         ('(U0_i1, ks123, U1_j1)','01(ks123)'),
#                         ('(U0_i1, et2, U1_j1)','01(et2)'), 
#                         ('(U0_i1, i1, U1_i1)','01(i1)'), 
#                         ('(U0_j1, j1, U1_j1)','01(j1)'), 
#                         ('(U0_i1, ks1, U1_i2)','01(ks1)'), 
#                         ('(U0_i0, et12, U1_j1)','01(et12)'), 
#                         ('(U0_i1, ks12, U1_j2)','01(ks12)'), 
#                         ('(U0_i0, et1, U1_i1)','01(et1)'),

#                         ('(U1_i2, ks23, U0_j1)','10(ks23)'), 
#                         ('(U1_j1, et3, U0_j0)','10(et3)'), 
#                         ('(U1_j1, j1, U0_j1)','10(j1)'), 
#                         ('(U1_j2, ks3, U0_j1)','10(ks3)'), 
#                         ('(U1_i1, et23, U0_j0)','10(et23)'), 
#                         ('(U1_i1, et2, U0_j1)','10(et2)'), 
#                         ('(U1_i1, i1, U0_i1)','10(i1)'), 
#                         ('(U1_i1, ks123, U0_j1)','10(ks123)'),

#                         ])

# ####### let's reduce :)
# max_a_infty_action=10
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['00(j1)'],Fuk.gen_by_name['00(et3)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['00(j0)'],Fuk.gen_by_name['00(ks123)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['00(i1)'],Fuk.gen_by_name['00(r0)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['00(et12)'],Fuk.gen_by_name['00(et123)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['00(et2)'],Fuk.gen_by_name['00(et23)']),max_a_infty_action)


# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['11(i1)'],Fuk.gen_by_name['11(et2)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['11(i2)'],Fuk.gen_by_name['11(ks1)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['11(j2)'],Fuk.gen_by_name['11(ks3)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['11(ks2)'],Fuk.gen_by_name['11(ks23)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['11(ks12)'],Fuk.gen_by_name['11(ks123)']),max_a_infty_action)

# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['10(j1)'],Fuk.gen_by_name['10(et2)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['10(ks23)'],Fuk.gen_by_name['10(ks123)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['10(et3)'],Fuk.gen_by_name['10(et23)']),max_a_infty_action)

# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['01(i1)'],Fuk.gen_by_name['01(ks1)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['01(j1)'],Fuk.gen_by_name['01(ks123)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['01(et1)'],Fuk.gen_by_name['01(et12)']),max_a_infty_action)

# Fuk.show()
# Fuk.show(restrict=[
#             Fuk.gen_by_name['11(r2)'],
#             Fuk.gen_by_name['00(et1)'],
#             Fuk.gen_by_name['00(i0)'],
#             Fuk.gen_by_name['11(j1)'],
            
#             Fuk.gen_by_name['01(ks12)'],
#             Fuk.gen_by_name['10(ks3)'],

#             # Fuk.gen_by_name['01(et2)'],
#             # Fuk.gen_by_name['10(i1)'],
#             ])

##################################################################################
##################################################################################
##################################################################################
########### computing PL (perutz-lekili) algebra by homological perturbation lemma
# def init_left_d_N0(torus_2bp_A):
#     gen_by_name=AttrDict({
#                 "x0": Generator("x0"),
#                 "x1": Generator("x1"),
#                 })

#     gen_by_name.x0.add_idems(torus_2bp_A.idem_by_name.i0, 0)
#     gen_by_name.x1.add_idems(torus_2bp_A.idem_by_name.i1, 0)
    

#     left_d_arrows=Bunch_of_arrows([
#         (              gen_by_name.x0,
#            torus_2bp_A.gen_by_name.r1, gen_by_name.x1),
#         (              gen_by_name.x0,
#            torus_2bp_A.gen_by_name.ks1, gen_by_name.x1),
#                                     ])
#     return Left_D_module(gen_by_name,left_d_arrows,torus_2bp_A,name="N0")
# N0=init_left_d_N0(torus_2bp_A)
# def init_left_d_N1(torus_2bp_A):
#     gen_by_name=AttrDict({
#                 "y1": Generator("y1"),
#                 "y2": Generator("y2"),
#                 })

#     gen_by_name.y1.add_idems(torus_2bp_A.idem_by_name.i1, 0)
#     gen_by_name.y2.add_idems(torus_2bp_A.idem_by_name.i2, 0)
    

#     left_d_arrows=Bunch_of_arrows([
#         (              gen_by_name.y1,
#            torus_2bp_A.gen_by_name.r2, gen_by_name.y2),
#         (              gen_by_name.y1,
#            torus_2bp_A.gen_by_name.ks2, gen_by_name.y2),
#                                     ])
#     return Left_D_module(gen_by_name,left_d_arrows,torus_2bp_A,name="N1")
# N1=init_left_d_N1(torus_2bp_A)
# N1.show()

# PL=algebra_from_mor_spaces_of_left_D_structures(
#                                             N0,
#                                             N1,
#                                             )
# PL=rename_generators(PL,[
#                         ('(x1, i1, x1)','00(i1)' ),
#                         ('(x0, i0, x0)','00(i0)' ),
#                         ('(x0, r1, x1)','00(r1)' ),
#                         ('(x0, ks1, x1)','00(ks1)' ),
#                         ('(y2, i2, y2)','11(i2)' ),
#                         ('(x0, r1, y1)','01(r1)' ),
#                         ('(y1, i1, y1)','11(i1)' ),
#                         ('(x0, r12, y2)','01(r12)' ),
#                         ('(x0, ks1, y1)','01(ks1)' ),
#                         ('(y1, ks2, y2)','11(ks2)' ),
#                         ('(y1, i1, x1)','10(i1)' ),
#                         ('(x1, i1, y1)','01(i1)' ),
#                         ('(y1, r2, y2)','11(r2)' ),
#                         ('(x1, ks2, y2)','01(ks2)' ),
#                         ('(x1, r2, y2)','01(r2)' ), 
#                         ('(x0, ks12, y2)','01(ks12)' ),
#                         ])
# PL.show()

# PL=perturb_algebra(PL,(PL.gen_by_name['00(i0)'],PL.gen_by_name['00(ks1)']))
# PL=perturb_algebra(PL,(PL.gen_by_name['11(i2)'],PL.gen_by_name['11(ks2)']))
# PL=perturb_algebra(PL,(PL.gen_by_name['01(ks2)'],PL.gen_by_name['01(ks12)']))
# PL=perturb_algebra(PL,(PL.gen_by_name['01(i1)'],PL.gen_by_name['01(r2)']))
# PL=perturb_algebra(PL,(PL.gen_by_name['01(r1)'],PL.gen_by_name['01(r12)']))


# PL.show()


