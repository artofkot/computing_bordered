# -*- coding: utf-8 -*- 
import sys
sys.path.append('../')

from algebraic_structures.basics import  Bunch_of_arrows
from algebraic_structures.dualization import (
        dualization_right_to_left_A,
        dualization_left_to_right_D)
from algebraic_structures.algebra import pil_A,AttrDict, Generator
from algebraic_structures.tensoring import (
    a_d_box_tensor_product,
    dd_a_box_tensor_product, 
    aa_d_box_tensor_product,
    d_aa_box_tensor_product)
from algebraic_structures.chain_complex import homology_dim
from algebraic_structures.dd_bimodule import DD_bimodule, dd_randomly_cancel_until_possible
from algebraic_structures.aa_bimodule import AA_bimodule, a_A_a
from algebraic_structures.right_a_module import Right_A_module
from algebraic_structures.left_a_module import Left_A_module
from algebraic_structures.algebra_simpler import (
    algebra_from_mor_spaces_of_left_D_structures,
    opposite_algebra,
    perturb_algebra,
    simpler_A_inf_Algebra,
    change_of_basis,
    u_i_rename_generators,
    rename_generators
    )
from algebraic_structures.left_d_module import (
    Left_D_module, 
    left_d_randomly_cancel_until_possible,
    morphism_space_for_left_D_structures,
    )
from algebraic_structures.right_d_module import Right_D_module

from input_instanton_modules import DD_bar_dual, Right_A_L0, Right_A_test
from input_instanton_modules import (
    Left_D_test,Left_A_test,DD_test, 
    Right_A_L6, Right_A_L7, Right_A_R4,
    Right_A_L37, Right_A_L3, Right_A_L0,
    Right_A_L8, Right_A_L9, Right_A_R0,
    Right_A_R00, Right_A_LU,Right_A_R1,Right_A_R2,Right_A_R3,
     Right_A_LT23 )


# breaking the d^2=0 test
# def init_Right_D_test(pil_A):
#     gen_by_name=AttrDict({
#                 "y1": Generator("y1"),
#                 "y2": Generator("y2"),
#                 "y3": Generator("y3"),
#                 "y4": Generator("y4")

#                 })

#     gen_by_name.y1.add_idems(0, pil_A.idem_by_name.i1)
#     gen_by_name.y2.add_idems(0, pil_A.idem_by_name.j2)
#     gen_by_name.y3.add_idems(0, pil_A.idem_by_name.i2)
#     gen_by_name.y4.add_idems(0, pil_A.idem_by_name.j1)
    

#     right_d_arrows=Bunch_of_arrows([
#         (              gen_by_name.y2,
#             gen_by_name.y3, pil_A.gen_by_name.ks2),

#         (              gen_by_name.y3,
#             gen_by_name.y1, pil_A.gen_by_name.ks1)
#                                     ])

#     return Right_D_module(gen_by_name,right_d_arrows,pil_A,name="Right_D_test")
# test=init_Right_D_test(pil_A)


def init_left_d_N_L0(pil_A):
    gen_by_name=AttrDict({
                "x1": Generator("x1"),
                "x2": Generator("x2"),
                "x3": Generator("x3"),
                "x4": Generator("x4"),
                })

    gen_by_name.x1.add_idems(pil_A.idem_by_name.i0, 0)
    gen_by_name.x2.add_idems(pil_A.idem_by_name.i1, 0)
    gen_by_name.x3.add_idems(pil_A.idem_by_name.j0, 0)
    gen_by_name.x4.add_idems(pil_A.idem_by_name.j1, 0)
    

    left_d_arrows=Bunch_of_arrows([
        (              gen_by_name.x1,
           pil_A.gen_by_name.r0, gen_by_name.x3),
        (              gen_by_name.x1,
           pil_A.gen_by_name.et12, gen_by_name.x4),
        (              gen_by_name.x2,
           pil_A.gen_by_name.ks123, gen_by_name.x4),
        (              gen_by_name.x2,
           pil_A.gen_by_name.et23, gen_by_name.x3),
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="N_L0")
N_L0=init_left_d_N_L0(pil_A)
def init_left_d_N_L1(pil_A):
    gen_by_name=AttrDict({
                "y1": Generator("y1"),
                "y2": Generator("y2"),
                "y3": Generator("y3"),
                "y4": Generator("y4")

                })

    gen_by_name.y1.add_idems(pil_A.idem_by_name.i1, 0)
    gen_by_name.y2.add_idems(pil_A.idem_by_name.j2, 0)
    gen_by_name.y3.add_idems(pil_A.idem_by_name.i2, 0)
    gen_by_name.y4.add_idems(pil_A.idem_by_name.j1, 0)
    

    left_d_arrows=Bunch_of_arrows([
        (              gen_by_name.y1,
           pil_A.gen_by_name.ks12, gen_by_name.y2),

        (              gen_by_name.y3,
             pil_A.gen_by_name.r2, gen_by_name.y2),
        (              gen_by_name.y3,
             pil_A.gen_by_name.ks23, gen_by_name.y4),
        (              gen_by_name.y1,
             pil_A.gen_by_name.et2, gen_by_name.y4),
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="N_L1")
N_L1=init_left_d_N_L1(pil_A)
def init_left_d_N_L2(pil_A):
    gen_by_name=AttrDict({
                "t1": Generator("t1"),
                })

    gen_by_name.t1.add_idems(pil_A.idem_by_name.i1, 0)

    left_d_arrows=Bunch_of_arrows([])

    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="N_L2")
N_L2=init_left_d_N_L2(pil_A)
a_A_a=a_A_a(pil_A)
DD_bar_r_dual=dd_randomly_cancel_until_possible(DD_bar_dual)

def init_Right_A_j1(pil_A):
    gen_by_name=AttrDict({
                "p": Generator("p"),
                "q": Generator("q")

                })

    gen_by_name.q.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.p.add_idems(0,pil_A.idem_by_name.j0)

    right_a_arrows=Bunch_of_arrows([
        (              gen_by_name.q,(pil_A.gen_by_name.et3,)
                        ,gen_by_name.p),
                                    ])
    return Right_A_module(gen_by_name,right_a_arrows,pil_A,name="Right_A_j1")
Right_A_j1=init_Right_A_j1(pil_A)
def init_Right_A_j2(pil_A):
    gen_by_name=AttrDict({
                "p": Generator("p"),
                "q": Generator("q")

                })

    gen_by_name.q.add_idems(0,pil_A.idem_by_name.j2)
    gen_by_name.p.add_idems(0,pil_A.idem_by_name.j1)

    right_a_arrows=Bunch_of_arrows([
        (              gen_by_name.q,(pil_A.gen_by_name.ks3,)
                        ,gen_by_name.p),
                                    ])
    return Right_A_module(gen_by_name,right_a_arrows,pil_A,name="Right_A_j2")
Right_A_j2=init_Right_A_j2(pil_A)
def init_Left_D_j1(pil_A):
    gen_by_name=AttrDict({
                "t1": Generator("t1"),
                })

    gen_by_name.t1.add_idems(pil_A.idem_by_name.j1, 0)
    

    left_d_arrows=Bunch_of_arrows([])

    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="Left_D_j1")
Left_D_j1=init_Left_D_j1(pil_A)
def init_Left_D_j2(pil_A):
    gen_by_name=AttrDict({
                "t2": Generator("t2"),
                })

    gen_by_name.t2.add_idems(pil_A.idem_by_name.j2, 0)
    

    left_d_arrows=Bunch_of_arrows([])

    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="Left_D_j2")
Left_D_j2=init_Left_D_j2(pil_A)


##### B_algebra
# gen_by_name=AttrDict({
#     "a_0": Generator("a_0"),
#     "b_0": Generator("b_0"),
#     "c_0": Generator("c_0"),
#     "d_0": Generator("d_0"),
#     "a_1": Generator("a_1"),
#     "b_1": Generator("b_1"),
#     "c_1": Generator("c_1"),
#     "d_1": Generator("d_1"),
#     "p_01": Generator("p_01"),
#     "p_10": Generator("p_10"),
#     "q_01": Generator("q_01"),
#     "q_10": Generator("q_10"),
#     })
# actions=Bunch_of_arrows([
#     (gen_by_name.a_0,gen_by_name.a_0,
#         gen_by_name.a_0),
#     (gen_by_name.a_0,gen_by_name.b_0,
#         gen_by_name.b_0),
#     (gen_by_name.a_0,gen_by_name.c_0,
#         gen_by_name.c_0),
#     (gen_by_name.a_0,gen_by_name.d_0,
#         gen_by_name.d_0),
#     (gen_by_name.a_0,gen_by_name.p_01,
#         gen_by_name.p_01),
#     (gen_by_name.a_0,gen_by_name.q_01,
#         gen_by_name.q_01),
#     (gen_by_name.b_0,gen_by_name.a_0,
#         gen_by_name.b_0),
#     (gen_by_name.c_0,gen_by_name.a_0,
#         gen_by_name.c_0),
#     (gen_by_name.d_0,gen_by_name.a_0,
#         gen_by_name.d_0),
#     (gen_by_name.p_10,gen_by_name.a_0,
#         gen_by_name.p_10),
#     (gen_by_name.q_10,gen_by_name.a_0,
#         gen_by_name.q_10),
#     (gen_by_name.b_0,gen_by_name.c_0,
#         gen_by_name.d_0),
#     (gen_by_name.c_0,gen_by_name.b_0,
#         gen_by_name.d_0),

#     (gen_by_name.a_1,gen_by_name.a_1,
#         gen_by_name.a_1),
#     (gen_by_name.a_1,gen_by_name.b_1,
#         gen_by_name.b_1),
#     (gen_by_name.a_1,gen_by_name.c_1,
#         gen_by_name.c_1),
#     (gen_by_name.a_1,gen_by_name.d_1,
#         gen_by_name.d_1),
#     (gen_by_name.a_1,gen_by_name.p_10,
#         gen_by_name.p_10),
#     (gen_by_name.a_1,gen_by_name.q_10,
#         gen_by_name.q_10),
#     (gen_by_name.b_1,gen_by_name.a_1,
#         gen_by_name.b_1),
#     (gen_by_name.c_1,gen_by_name.a_1,
#         gen_by_name.c_1),
#     (gen_by_name.d_1,gen_by_name.a_1,
#         gen_by_name.d_1),
#     (gen_by_name.p_01,gen_by_name.a_1,
#         gen_by_name.p_01),
#     (gen_by_name.q_01,gen_by_name.a_1,
#         gen_by_name.q_01),
#     (gen_by_name.b_1,gen_by_name.c_1,
#         gen_by_name.d_1),
#     (gen_by_name.c_1,gen_by_name.b_1,
#         gen_by_name.d_1),
    

#     (gen_by_name.p_01,gen_by_name.p_10,
#         gen_by_name.d_0),
#     (gen_by_name.q_01,gen_by_name.q_10,
#         gen_by_name.d_0),
#     (gen_by_name.p_10,gen_by_name.p_01,
#         gen_by_name.d_1),
#     (gen_by_name.q_10,gen_by_name.q_01,
#         gen_by_name.d_1),

#     (gen_by_name.p_01,gen_by_name.q_10,
#         gen_by_name.c_0),
#     (gen_by_name.q_10,gen_by_name.p_01,
#         gen_by_name.c_1),

#     (gen_by_name.b_0,gen_by_name.p_01,
#         gen_by_name.q_01),
#     (gen_by_name.p_01,gen_by_name.b_1,
#         gen_by_name.q_01),

#     (gen_by_name.b_1,gen_by_name.q_10,
#         gen_by_name.p_10),
#     (gen_by_name.q_10,gen_by_name.b_0,
#         gen_by_name.p_10),

#     # 0,0,0,0
#     (gen_by_name.c_0,gen_by_name.b_0,gen_by_name.c_0,
#         gen_by_name.c_0),
#     (gen_by_name.c_0,gen_by_name.b_0,gen_by_name.d_0,
#         gen_by_name.d_0),
#     (gen_by_name.d_0,gen_by_name.b_0,gen_by_name.c_0,
#         gen_by_name.d_0),

#     # 0,0,1,0
#     (gen_by_name.d_0,gen_by_name.q_01,gen_by_name.q_10,
#         gen_by_name.d_0),
#     (gen_by_name.c_0,gen_by_name.q_01,gen_by_name.q_10,
#         gen_by_name.c_0),
#     (gen_by_name.d_0,gen_by_name.p_01,gen_by_name.p_10,
#         gen_by_name.d_0),
#     (gen_by_name.c_0,gen_by_name.p_01,gen_by_name.p_10,
#         gen_by_name.c_0),

#     # 0,1,0,0
#     (gen_by_name.p_01,gen_by_name.p_10,gen_by_name.b_0,
#         gen_by_name.b_0),
#     (gen_by_name.q_01,gen_by_name.q_10,gen_by_name.b_0,
#         gen_by_name.b_0),
#     (gen_by_name.p_01,gen_by_name.q_10,gen_by_name.b_0,
#         gen_by_name.a_0),

#     # 0,1,0,1
#     (gen_by_name.p_01,gen_by_name.p_10,gen_by_name.q_01,
#         gen_by_name.q_01),

#     # 1,0,0,1
#     (gen_by_name.q_10,gen_by_name.b_0,gen_by_name.p_01,
#         gen_by_name.a_1),

#     # 1,0,1,0
#     (gen_by_name.q_10,gen_by_name.p_01,gen_by_name.p_10,
#         gen_by_name.q_10),
#     (gen_by_name.q_10,gen_by_name.q_01,gen_by_name.q_10,
#         gen_by_name.q_10),
#     (gen_by_name.p_10,gen_by_name.p_01,gen_by_name.p_10,
#         gen_by_name.p_10),

#     # 1,0,1,1
#     (gen_by_name.q_10,gen_by_name.q_01,gen_by_name.d_1,
#         gen_by_name.d_1),
#     (gen_by_name.q_10,gen_by_name.q_01,gen_by_name.c_1,
#         gen_by_name.c_1),
#     (gen_by_name.p_10,gen_by_name.p_01,gen_by_name.b_1,
#         gen_by_name.b_1),

#     # 1,1,0,1
#     (gen_by_name.b_1,gen_by_name.q_10,gen_by_name.q_01,
#         gen_by_name.b_1),
#     (gen_by_name.c_1,gen_by_name.p_10,gen_by_name.p_01,
#         gen_by_name.c_1),
#     (gen_by_name.d_1,gen_by_name.p_10,gen_by_name.p_01,
#         gen_by_name.d_1),

#     # 1,1,1,1
#     (gen_by_name.c_1,gen_by_name.b_1,gen_by_name.c_1,
#         gen_by_name.c_1),
#     (gen_by_name.c_1,gen_by_name.b_1,gen_by_name.d_1,
#         gen_by_name.d_1),
#     (gen_by_name.d_1,gen_by_name.b_1,gen_by_name.c_1,
#         gen_by_name.d_1),

#     ])
# B=simpler_A_inf_Algebra(gen_by_name,'B',actions)
# B.show()

##### Bsym_algebra
gen_by_name=AttrDict({
    "a_0": Generator("a_0"),
    "b_0": Generator("b_0"),
    "c_0": Generator("c_0"),
    "d_0": Generator("d_0"),
    "a_1": Generator("a_1"),
    "b_1": Generator("b_1"),
    "c_1": Generator("c_1"),
    "d_1": Generator("d_1"),
    "p_01": Generator("p_01"),
    "p_10": Generator("p_10"),
    "q_01": Generator("q_01"),
    "q_10": Generator("q_10"),
    })
actions=Bunch_of_arrows([
    (gen_by_name.a_0,gen_by_name.a_0,
        gen_by_name.a_0),
    (gen_by_name.a_0,gen_by_name.b_0,
        gen_by_name.b_0),
    (gen_by_name.a_0,gen_by_name.c_0,
        gen_by_name.c_0),
    (gen_by_name.a_0,gen_by_name.d_0,
        gen_by_name.d_0),
    (gen_by_name.a_0,gen_by_name.p_01,
        gen_by_name.p_01),
    (gen_by_name.a_0,gen_by_name.q_01,
        gen_by_name.q_01),
    (gen_by_name.b_0,gen_by_name.a_0,
        gen_by_name.b_0),
    (gen_by_name.c_0,gen_by_name.a_0,
        gen_by_name.c_0),
    (gen_by_name.d_0,gen_by_name.a_0,
        gen_by_name.d_0),
    (gen_by_name.p_10,gen_by_name.a_0,
        gen_by_name.p_10),
    (gen_by_name.q_10,gen_by_name.a_0,
        gen_by_name.q_10),
    (gen_by_name.b_0,gen_by_name.c_0,
        gen_by_name.d_0),
    (gen_by_name.c_0,gen_by_name.b_0,
        gen_by_name.d_0),

    (gen_by_name.a_1,gen_by_name.a_1,
        gen_by_name.a_1),
    (gen_by_name.a_1,gen_by_name.b_1,
        gen_by_name.b_1),
    (gen_by_name.a_1,gen_by_name.c_1,
        gen_by_name.c_1),
    (gen_by_name.a_1,gen_by_name.d_1,
        gen_by_name.d_1),
    (gen_by_name.a_1,gen_by_name.p_10,
        gen_by_name.p_10),
    (gen_by_name.a_1,gen_by_name.q_10,
        gen_by_name.q_10),
    (gen_by_name.b_1,gen_by_name.a_1,
        gen_by_name.b_1),
    (gen_by_name.c_1,gen_by_name.a_1,
        gen_by_name.c_1),
    (gen_by_name.d_1,gen_by_name.a_1,
        gen_by_name.d_1),
    (gen_by_name.p_01,gen_by_name.a_1,
        gen_by_name.p_01),
    (gen_by_name.q_01,gen_by_name.a_1,
        gen_by_name.q_01),
    (gen_by_name.b_1,gen_by_name.c_1,
        gen_by_name.d_1),
    (gen_by_name.c_1,gen_by_name.b_1,
        gen_by_name.d_1),
    

    (gen_by_name.p_01,gen_by_name.p_10,
        gen_by_name.d_0),
    (gen_by_name.q_01,gen_by_name.q_10,
        gen_by_name.d_0),
    (gen_by_name.p_10,gen_by_name.p_01,
        gen_by_name.d_1),
    (gen_by_name.q_10,gen_by_name.q_01,
        gen_by_name.d_1),

    (gen_by_name.p_01,gen_by_name.q_10,
        gen_by_name.c_0),
    (gen_by_name.q_10,gen_by_name.p_01,
        gen_by_name.c_1),

    (gen_by_name.b_0,gen_by_name.p_01,
        gen_by_name.q_01),
    (gen_by_name.p_01,gen_by_name.b_1,
        gen_by_name.q_01),

    (gen_by_name.b_1,gen_by_name.q_10,
        gen_by_name.p_10),
    (gen_by_name.q_10,gen_by_name.b_0,
        gen_by_name.p_10),

    # 0,0,0,0
    (gen_by_name.c_0,gen_by_name.b_0,gen_by_name.c_0,
        gen_by_name.c_0),
    (gen_by_name.c_0,gen_by_name.b_0,gen_by_name.d_0,
        gen_by_name.d_0),
    (gen_by_name.d_0,gen_by_name.b_0,gen_by_name.c_0,
        gen_by_name.d_0),

    # 0,0,1,0
    (gen_by_name.d_0,gen_by_name.q_01,gen_by_name.q_10,
        gen_by_name.d_0),
    (gen_by_name.c_0,gen_by_name.q_01,gen_by_name.q_10,
        gen_by_name.c_0),
    (gen_by_name.b_0,gen_by_name.p_01,gen_by_name.p_10,
        gen_by_name.b_0),

    # 0,1,0,0
    (gen_by_name.p_01,gen_by_name.p_10,gen_by_name.d_0,
        gen_by_name.d_0),
    (gen_by_name.p_01,gen_by_name.p_10,gen_by_name.c_0,
        gen_by_name.c_0),
    (gen_by_name.q_01,gen_by_name.q_10,gen_by_name.b_0,
        gen_by_name.b_0),

    # 0,1,1,0
    (gen_by_name.p_01,gen_by_name.b_1,gen_by_name.q_10,
        gen_by_name.a_0),

    # 0,1,0,1
    (gen_by_name.p_01,gen_by_name.p_10,gen_by_name.p_01,
        gen_by_name.p_01),

    # 1,0,0,1
    (gen_by_name.q_10,gen_by_name.b_0,gen_by_name.p_01,
        gen_by_name.a_1),

    # 1,0,1,0
    (gen_by_name.q_10,gen_by_name.q_01,gen_by_name.q_10,
        gen_by_name.q_10),

    # 1,0,1,1
    (gen_by_name.q_10,gen_by_name.q_01,gen_by_name.d_1,
        gen_by_name.d_1),
    (gen_by_name.q_10,gen_by_name.q_01,gen_by_name.c_1,
        gen_by_name.c_1),
    (gen_by_name.p_10,gen_by_name.p_01,gen_by_name.b_1,
        gen_by_name.b_1),

    # 1,1,0,1
    (gen_by_name.b_1,gen_by_name.q_10,gen_by_name.q_01,
        gen_by_name.b_1),
    (gen_by_name.c_1,gen_by_name.p_10,gen_by_name.p_01,
        gen_by_name.c_1),
    (gen_by_name.d_1,gen_by_name.p_10,gen_by_name.p_01,
        gen_by_name.d_1),

    # 1,1,1,1
    (gen_by_name.c_1,gen_by_name.b_1,gen_by_name.c_1,
        gen_by_name.c_1),
    (gen_by_name.c_1,gen_by_name.b_1,gen_by_name.d_1,
        gen_by_name.d_1),
    (gen_by_name.d_1,gen_by_name.b_1,gen_by_name.c_1,
        gen_by_name.d_1),

    ])
Bsym=simpler_A_inf_Algebra(gen_by_name,'Bsym',actions)
Bsym.show()

##### H_algebra without ◎,ʚ,ᗧ,8
# list_of_tuples_rename_B_to_H2=[
#     ('a_0','1⊗1__00'),
#     ('b_0','x_1'),
#     ('c_0','x_1+x_2'),
#     ('d_0','x_1*x_2'),
#     ('p_01','1__01'),
#     ('q_01','y__01'),
#     ('p_10','y__10'),
#     ('q_10','1__10'),
#     ('a_1','1⊗1__11'),
#     ('b_1','z_1'),
#     ('c_1','z_1+z_2'),
#     ('d_1','z_1*z_2'),
#     ]
# H=rename_generators(B,list_of_tuples_rename_B_to_H2)
# H=change_of_basis(H,H.gen_by_name['x_1+x_2'],H.gen_by_name['x_1'])
# H=change_of_basis(H,H.gen_by_name['z_1+z_2'],H.gen_by_name['z_1'])
# H=rename_generators(H,[('x_1+x_2','x_2'),('z_1+z_2','z_2')])
# H.show()

##### H_algebra with ◎,ʚ,ᗧ,8
list_of_tuples_rename_B_to_H2=[
    ('a_0','1⊗1_8'),
    ('b_0','x_1_8'),
    ('c_0','x_1+x_2'),
    ('d_0','x_1*x_2_8'),
    ('p_01','1_ʚ'),
    ('q_01','y_ʚ'),
    ('p_10','y_ᗧ'),
    ('q_10','1_ᗧ'),
    ('a_1','1⊗1_◎'),
    ('b_1','z_1_◎'),
    ('c_1','z_1+z_2'),
    ('d_1','z_1*z_2_◎'),
    ]
H=rename_generators(Bsym,list_of_tuples_rename_B_to_H2)
H=change_of_basis(H,H.gen_by_name['x_1+x_2'],H.gen_by_name['x_1_8'])
H=change_of_basis(H,H.gen_by_name['z_1+z_2'],H.gen_by_name['z_1_◎'])
H=rename_generators(H,[('x_1+x_2','x_2_8'),('z_1+z_2','z_2_◎')])
H.show()

##### CF(lagr_0,lagr_1) via morphism space of D-modules
# D_lagr_0=Left_D_j1
# D_lagr_1=Left_D_j2
# Mor=morphism_space_for_left_D_structures(D_lagr_1,D_lagr_0)
# Mor.show()
# homology_dim(Mor)

##### CF(lagr_0,lagr_1) via tensor product of D-modules
# D_lagr_0=N_L0
# D_lagr_1=N_L1
# right_A=d_aa_box_tensor_product(dualization_left_to_right_D(D_lagr_1),a_A_a)
# C=a_d_box_tensor_product(right_A,D_lagr_0) 
# C.show()
# homology_dim(C)

##### CF(lagr_0,lagr_1) via A-modules
# A_lagr_0=Right_A_L0
# A_lagr_1=Right_A_L9
# D=dd_a_box_tensor_product(DD_bar_r_dual,dualization_right_to_left_A(A_lagr_0))
# C=a_d_box_tensor_product(A_lagr_1,D) 
# C.show()
# homology_dim(C)

#### arxiv
# NN_L0=dd_a_box_tensor_product=dd_a_box_tensor_product(DD_bar_r_dual,dualization_right_to_left_A(Right_A_L0))
# NN_L0=left_d_randomly_cancel_until_possible(NN_L0)
# NN_L0.show()
# N_L0.show()

##### computing B algebra
# B=algebra_from_mor_spaces_of_left_D_structures(N_L0)
# B=u_i_rename_generators(B)
# pure_diff=True
# while pure_diff==True:
#     differentials=[act for act in list(B.a_inf_actions.elements()) if len(act)==2]
#     if differentials:
#         B=perturb_algebra(B,differentials[0])
#     else: pure_diff=False
# B.show()