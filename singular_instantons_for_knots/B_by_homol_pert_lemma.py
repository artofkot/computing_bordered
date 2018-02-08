# -*- coding: utf-8 -*- 
import sys
sys.path.append('../')

from algebraic_structures.basics import  Bunch_of_arrows
from algebraic_structures.dualization import (
        dualization_right_to_left_A,
        dualization_left_to_right_D)
from algebraic_structures.algebra import pil_A,AttrDict, Generator, dg_algebra
from algebraic_structures.tensoring import (
    a_d_box_tensor_product,
    dd_a_box_tensor_product, 
    aa_d_box_tensor_product,
    d_aa_box_tensor_product,
    aa_da_box_tensor_product)
from algebraic_structures.chain_complex import homology_dim
from algebraic_structures.dd_bimodule import DD_bimodule, dd_randomly_cancel_until_possible
from algebraic_structures.aa_bimodule import AA_bimodule, a_A_a,aa_randomly_cancel_until_possible
from algebraic_structures.da_bimodule import DA_bimodule
from algebraic_structures.right_a_module import Right_A_module
from algebraic_structures.left_a_module import Left_A_module
from algebraic_structures.algebra_simpler import (
    algebra_from_mor_spaces_of_left_D_structures,
    opposite_algebra,
    perturb_algebra,
    simpler_A_inf_Algebra,
    change_of_basis,
    u_i_rename_generators,
    rename_generators,
    act_by_G2
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

A_pil_A_A=a_A_a(pil_A)
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


##### CF(lagr_0,lagr_1) via morphism space of D-modules
# D_lagr_0=N_L0
# D_lagr_1=N_L0
# Mor=morphism_space_for_left_D_structures(D_lagr_0,D_lagr_1)
# Mor.show()
# homology_dim(Mor)

##################################################################################
##################################################################################
##################################################################################
########### computing BL_0 algebra by homological perturbation lemma

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
def init_Left_D_j1(pil_A):
    gen_by_name=AttrDict({
                "w": Generator("w"),
                })

    gen_by_name.w.add_idems(pil_A.idem_by_name.j1, 0)
    

    left_d_arrows=Bunch_of_arrows([])

    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="Left_D_j1")
Dj1=init_Left_D_j1(pil_A)
def init_Left_D_i1(pil_A):
    gen_by_name=AttrDict({
                "w": Generator("w"),
                })

    gen_by_name.w.add_idems(pil_A.idem_by_name.i1, 0)

    left_d_arrows=Bunch_of_arrows([])
    
    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="Left_D_i1")
Di1=init_Left_D_i1(pil_A)

BL_0=algebra_from_mor_spaces_of_left_D_structures(
                                            N_L0,
                                            N_L1,
                                            Di1,
                                            )
BL_0=rename_generators(BL_0,[
                        ('(x4, j1, x4)','00(j1)' ), 
                        ('(x1, et123, x3)','00(et123)' ),
                        ('(x2, et2, x4)','00(et2)' ),
                        ('(x1, et12, x4)','00(et12)' ),
                        ('(x4, et3, x3)','00(et3)' ),
                        ('(x2, et23, x3)','00(et23)' ),
                        ('(x1, r0, x3)','00(r0)' ),
                        ('(x2, i1, x2)','00(i1)' ),
                        ('(x1, i0, x1)','00(i0)' ),
                        ('(x3, j0, x3)','00(j0)' ),
                        ('(x2, ks123, x4)','00(ks123)' ),
                        ('(x1, et1, x2)','00(et1)' ),

                        ('(y2, j2, y2)','11(j2)'), 
                        ('(y1, ks12, y2)','11(ks12)'), 
                        ('(y3, ks23, y4)','11(ks23)'), 
                        ('(y1, ks123, y4)','11(ks123)'), 
                        ('(y1, ks1, y3)','11(ks1)'), 
                        ('(y3, i2, y3)','11(i2)'), 
                        ('(y3, ks2, y2)','11(ks2)'), 
                        ('(y1, et2, y4)','11(et2)'), 
                        ('(y1, i1, y1)','11(i1)'),
                        ('(y3, r2, y2)','11(r2)'), 
                        ('(y2, ks3, y4)','11(ks3)'), 
                        ('(y4, j1, y4)','11(j1)'), 

                        ('(x2, ks123, y4)','01(ks123)'),
                        ('(x2, et2, y4)','01(et2)'), 
                        ('(x2, i1, y1)','01(i1)'), 
                        ('(x4, j1, y4)','01(j1)'), 
                        ('(x2, ks1, y3)','01(ks1)'), 
                        ('(x1, et12, y4)','01(et12)'), 
                        ('(x2, ks12, y2)','01(ks12)'), 
                        ('(x1, et1, y1)','01(et1)'),

                        ('(y3, ks23, x4)','10(ks23)'), 
                        ('(y4, et3, x3)','10(et3)'), 
                        ('(y4, j1, x4)','10(j1)'), 
                        ('(y2, ks3, x4)','10(ks3)'), 
                        ('(y1, et23, x3)','10(et23)'), 
                        ('(y1, et2, x4)','10(et2)'), 
                        ('(y1, i1, x2)','10(i1)'), 
                        ('(y1, ks123, x4)','10(ks123)')
                        ])

#### gives bounded algebra B

BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['00(i1)'],BL_0.gen_by_name['00(et23)']))
BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['00(i0)'],BL_0.gen_by_name['00(et12)']))
BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['00(j1)'],BL_0.gen_by_name['00(r0)']))
BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['00(et3)'],BL_0.gen_by_name['00(et123)']))

BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['11(i2)'],BL_0.gen_by_name['11(r2)']))
BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['11(j2)'],BL_0.gen_by_name['11(ks23)']))
BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['11(ks1)'],BL_0.gen_by_name['11(ks123)']))
BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['11(i1)'],BL_0.gen_by_name['11(ks12)']))

BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['10(ks3)'],BL_0.gen_by_name['10(ks123)']))
BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['10(j1)'],BL_0.gen_by_name['10(ks23)']))
BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['10(i1)'],BL_0.gen_by_name['10(et23)']))

BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['01(ks1)'],BL_0.gen_by_name['01(ks123)']))
BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['01(i1)'],BL_0.gen_by_name['01(ks12)']))
BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['01(j1)'],BL_0.gen_by_name['01(et12)']))

BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['(w, ks1, y3)'],BL_0.gen_by_name['(w, ks123, y4)']))
BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['(w, i1, y1)'],BL_0.gen_by_name['(w, ks12, y2)']))
BL_0=perturb_algebra(BL_0,(BL_0.gen_by_name['(w, i1, x2)'],BL_0.gen_by_name['(w, ks123, x4)']))


# BL_0=change_of_basis(BL_0,BL_0.gen_by_name['11(ks2)'],BL_0.gen_by_name['11(et2)'])
# BL_0=act_by_G2(BL_0, G2=Bunch_of_arrows([
#             (BL_0.gen_by_name['00(ks123)'],BL_0.gen_by_name['00(ks123)'],
#             BL_0.gen_by_name['00(ks123)'])       ])
#         )

BL_0.show()
BL_0.show(restrict=[
                BL_0.gen_by_name['00(j0)'],
                BL_0.gen_by_name['00(et1)'],
                BL_0.gen_by_name['11(j1)'],
                BL_0.gen_by_name['11(ks3)'],
                BL_0.gen_by_name['01(et1)'],
                BL_0.gen_by_name['10(et3)'],

                BL_0.gen_by_name['(w, et2, x4)'],
                BL_0.gen_by_name['(w, et23, x3)'],
                BL_0.gen_by_name['(w, et2, y4)'],
                ])


##################################################################################
##################################################################################
##################################################################################
########### finding bimodule associated to a braid move

def init_B_r():
    gen_by_name=AttrDict({
                "l0": Generator("l0","l_0"),
                "l1": Generator("l1","l_1"),
                "p01": Generator("p01","p_\{01\}"),
                "q10": Generator("q10","p_\{10\}"),
                "c0": Generator("c0","c_0"),
                "c1": Generator("c1","c_1"),
                })


    idem_by_name=AttrDict({
                    "l0": gen_by_name.l0,
                    "l1": gen_by_name.l1,
                    })

    multiplication_table={(gen_by_name.l0,gen_by_name.l0):gen_by_name.l0,
                        (gen_by_name.l0,gen_by_name.p01):gen_by_name.p01,
                        (gen_by_name.l0,gen_by_name.c0):gen_by_name.c0,
                        (gen_by_name.c0,gen_by_name.l0):gen_by_name.c0,
                        (gen_by_name.l1,gen_by_name.l1):gen_by_name.l1,
                        (gen_by_name.l1,gen_by_name.q10):gen_by_name.q10,
                        (gen_by_name.l1,gen_by_name.c1):gen_by_name.c1,
                        (gen_by_name.c1,gen_by_name.l1):gen_by_name.c1,
                        (gen_by_name.p01,gen_by_name.q10):gen_by_name.c0,
                        (gen_by_name.p01,gen_by_name.l1):gen_by_name.p01,
                        (gen_by_name.q10,gen_by_name.p01):gen_by_name.c1,
                        (gen_by_name.q10,gen_by_name.l0):gen_by_name.q10,
                                    }

    return dg_algebra(gen_by_name=gen_by_name,idem_by_name=idem_by_name,multiplication_table=multiplication_table,name='B_r')
B_r=init_B_r()
def init_Left_Dl0(B_r):
    gen_by_name=AttrDict({
                "x": Generator("x"),
                })

    gen_by_name.x.add_idems(B_r.idem_by_name.l0,0)
    

    left_d_arrows=Bunch_of_arrows([
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,B_r,name="Dl0")
Dl0=init_Left_Dl0(B_r)
def init_Left_Dl1(B_r):
    gen_by_name=AttrDict({
                "y": Generator("y"),
                })

    gen_by_name.y.add_idems(B_r.idem_by_name.l1,0)
    

    left_d_arrows=Bunch_of_arrows([
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,B_r,name="Dl1")
Dl1=init_Left_Dl1(B_r)
def init_Left_Dl2(B_r):
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

    return Left_D_module(gen_by_name,left_d_arrows,B_r,name="Dl2")
Dl2=init_Left_Dl2(B_r)

C=algebra_from_mor_spaces_of_left_D_structures(
                                            Dl0,
                                            Dl1,
                                            Dl2,
                                            )
C=rename_generators(C,[
                        ('(x, l0, x)','00(l0)'),
                        ('(x, c0, x)','00(c0)'), 
                        ('(x, p01, y)','01(p01⊗t)'), #01(p01) 
                        ('(y, q10, x)','10(q10)'), 
                        ('(y, c1, y)','11(c1⊗t)'),  #11(c1)
                        ('(y, l1, y)','11(l1⊗t)'),  #11(l1)

                        ('(x, l0, z0)','02(l0)'),
                        ('(x, c0, z0)','02(c0⊗x)'),  # 02(c0)
                        ('(y, q10, z0)','12(q10)'), 
                        ('(x, p01, z1)','02(p01)'), 
                        ('(y, c1, z1)','12(c1)'),  # 
                        ('(y, l1, z1)','12(l1⊗y)'), #12(l1)

                        ('(z0, l0, x)','20(l0)'),
                        ('(z0, c0, x)','20(c0)'), 
                        ('(z0, p01, y)','21(p01)'), 
                        ('(z1, q10, x)','20(q10)'), 
                        ('(z1, c1, y)','21(c1)'), 
                        ('(z1, l1, y)','21(l1)'),

                        ('(z0, l0, z0)','22(l0)'),
                        ('(z0, c0, z0)','22(c0)'), 
                        ('(z0, p01, z1)','22(p01)'), 
                        ('(z1, q10, z0)','22(q10)'), 
                        ('(z1, c1, z1)','22(c1)'), 
                        ('(z1, l1, z1)','22(l1)'),
                        ])

C=perturb_algebra(C,(C.gen_by_name['22(l0)'],C.gen_by_name['22(p01)']))
C=perturb_algebra(C,(C.gen_by_name['22(q10)'],C.gen_by_name['22(c1)']))
C=perturb_algebra(C,(C.gen_by_name['02(l0)'],C.gen_by_name['02(p01)']))
C=perturb_algebra(C,(C.gen_by_name['21(l1)'],C.gen_by_name['21(p01)']))
C=perturb_algebra(C,(C.gen_by_name['20(q10)'],C.gen_by_name['20(c0)']))
C=perturb_algebra(C,(C.gen_by_name['12(q10)'],C.gen_by_name['12(c1)']))

C.show()

# C.show(restrict=[
#                 C.gen_by_name['22(c0)'],
#                 C.gen_by_name['22(l1)'],
#                 C.gen_by_name['11(l1)'],
#                 C.gen_by_name['11(c1)'],
#                 C.gen_by_name['21(c1)'],
#                 C.gen_by_name['12(l1)'],
#                 ])

############################# comparing AA⊗DA with AA coming from C:
#### AA⊗DA
A_B_r_A=a_A_a(B_r)
def init_DA_phi(B_r):
    gen_by_name=AttrDict({
                "x": Generator("x"),
                "y": Generator("y"),
                "t": Generator("t"),
                })
    gen_by_name.x.add_idems(B_r.idem_by_name.l0,B_r.idem_by_name.l0)
    gen_by_name.y.add_idems(B_r.idem_by_name.l1,B_r.idem_by_name.l0)
    gen_by_name.t.add_idems(B_r.idem_by_name.l1,B_r.idem_by_name.l1)

    arrows=Bunch_of_arrows([
        (              gen_by_name.x,(B_r.gen_by_name.c0,),
                B_r.gen_by_name.c0,gen_by_name.x),
        (              gen_by_name.x,(),
                B_r.gen_by_name.p01,gen_by_name.y),
        (              gen_by_name.y,(B_r.gen_by_name.p01,),
                B_r.gen_by_name.c1,gen_by_name.t),
        (              gen_by_name.y,(B_r.gen_by_name.p01,B_r.gen_by_name.q10),
                B_r.gen_by_name.q10,gen_by_name.x),
        (              gen_by_name.t,(B_r.gen_by_name.q10,),
                1,gen_by_name.y),
        (              gen_by_name.t,(B_r.gen_by_name.c1,),
                B_r.gen_by_name.c1,gen_by_name.t),
        (              gen_by_name.t,(B_r.gen_by_name.c1,B_r.gen_by_name.q10),
                B_r.gen_by_name.q10,gen_by_name.x),

        ])

    return DA_bimodule(gen_by_name,arrows,B_r,B_r,name="DA_phi")
DA_phi=init_DA_phi(B_r)

AA_phi=aa_da_box_tensor_product(A_B_r_A,DA_phi)
AA_phi=aa_randomly_cancel_until_possible(AA_phi)
AA_phi.show()

# now compare AA_phi with the computed algebra C

# pure_diff=True
# while pure_diff==True:
#     differentials=[act for act in list(BL_0.a_inf_actions.elements()) if len(act)==2]
#     if differentials:
#         BL_0=perturb_algebra(BL_0,differentials[0])
#     else: pure_diff=False
# BL_0.show()

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
#     (gen_by_name.b_0,gen_by_name.p_01,gen_by_name.p_10,
#         gen_by_name.b_0),

#     # 0,1,0,0
#     (gen_by_name.p_01,gen_by_name.p_10,gen_by_name.d_0,
#         gen_by_name.d_0),
#     (gen_by_name.p_01,gen_by_name.p_10,gen_by_name.c_0,
#         gen_by_name.c_0),
#     (gen_by_name.q_01,gen_by_name.q_10,gen_by_name.b_0,
#         gen_by_name.b_0),

#     # 0,1,1,0
#     (gen_by_name.p_01,gen_by_name.b_1,gen_by_name.q_10,
#         gen_by_name.a_0),

#     # 0,1,0,1
#     (gen_by_name.p_01,gen_by_name.p_10,gen_by_name.p_01,
#         gen_by_name.p_01),

#     # 1,0,0,1
#     (gen_by_name.q_10,gen_by_name.b_0,gen_by_name.p_01,
#         gen_by_name.a_1),

#     # 1,0,1,0
#     (gen_by_name.q_10,gen_by_name.q_01,gen_by_name.q_10,
#         gen_by_name.q_10),

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
# Bsym=simpler_A_inf_Algebra(gen_by_name,'Bsym',actions)
# Bsym.show()

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
# list_of_tuples_rename_B_to_H2=[
#     ('a_0','1⊗1_8'),
#     ('b_0','x_1_8'),
#     ('c_0','x_1+x_2'),
#     ('d_0','x_1*x_2_8'),
#     ('p_01','1_ʚ'),
#     ('q_01','y_ʚ'),
#     ('p_10','y_ᗧ'),
#     ('q_10','1_ᗧ'),
#     ('a_1','1⊗1_◎'),
#     ('b_1','z_1_◎'),
#     ('c_1','z_1+z_2'),
#     ('d_1','z_1*z_2_◎'),
#     ]
# H=rename_generators(Bsym,list_of_tuples_rename_B_to_H2)
# H=change_of_basis(H,H.gen_by_name['x_1+x_2'],H.gen_by_name['x_1_8'])
# H=change_of_basis(H,H.gen_by_name['z_1+z_2'],H.gen_by_name['z_1_◎'])
# H=rename_generators(H,[('x_1+x_2','x_2_8'),('z_1+z_2','z_2_◎')])
# H.show()