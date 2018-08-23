# -*- coding: utf-8 -*- 
import sys
sys.path.append('../')
import cPickle as pickle
from algebraic_structures.basics import  *
from algebraic_structures.dualization import *
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
def init_left_d_N_L2(pil_A):
    gen_by_name=AttrDict({
                "L2_j0": Generator("L2_j0"),
                "L2_j2": Generator("L2_j2"),
                "L2_i1_0": Generator("L2_i1_0"),
                "L2_i0": Generator("L2_i0"),
                "L2_i2": Generator("L2_i2"),
                "L2_i1_5": Generator("L2_i1_5")

                })

    gen_by_name.L2_i1_0.add_idems(pil_A.idem_by_name.i1, 0)
    gen_by_name.L2_i1_5.add_idems(pil_A.idem_by_name.i1, 0)
    gen_by_name.L2_j0.add_idems(pil_A.idem_by_name.j0, 0)
    gen_by_name.L2_j2.add_idems(pil_A.idem_by_name.j2, 0)
    gen_by_name.L2_i0.add_idems(pil_A.idem_by_name.i0, 0)
    gen_by_name.L2_i2.add_idems(pil_A.idem_by_name.i2, 0)
    

    left_d_arrows=Bunch_of_arrows([
        (              gen_by_name.L2_i1_0,
           pil_A.gen_by_name.ks12, gen_by_name.L2_j2),
        (              gen_by_name.L2_i0,
           pil_A.gen_by_name.et1, gen_by_name.L2_i1_0),
        (              gen_by_name.L2_i0,
           pil_A.gen_by_name.r0, gen_by_name.L2_j0),
        (              gen_by_name.L2_i1_5,
           pil_A.gen_by_name.et23, gen_by_name.L2_j0),
        (              gen_by_name.L2_i2,
           pil_A.gen_by_name.r2, gen_by_name.L2_j2),
        (              gen_by_name.L2_i1_5,
           pil_A.gen_by_name.ks1, gen_by_name.L2_i2),
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="N_L2")
N_L2=init_left_d_N_L2(pil_A)
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


def init_Right_B_M_W0(B_r):
    gen_by_name=AttrDict({
                "x": Generator("x"),
                "y": Generator("y"),
                "z": Generator("z"),
                })

    gen_by_name.x.add_idems(0,B_r.idem_by_name.l0)
    gen_by_name.y.add_idems(0,B_r.idem_by_name.l0)
    gen_by_name.z.add_idems(0,B_r.idem_by_name.l1)
    

    right_a_arrows=Bunch_of_arrows([
                                (gen_by_name.x, (B_r.gen_by_name.c0,)
                                , gen_by_name.y),
                                (gen_by_name.x, (B_r.gen_by_name.p01,)
                                , gen_by_name.z),
                                (gen_by_name.z, (B_r.gen_by_name.q10,)
                                , gen_by_name.y),
                                    ])
    return Right_A_module(gen_by_name,right_a_arrows,B_r,name="B_M_W0")
B_M_W0=init_Right_B_M_W0(B_r)
def init_Left_B_N_L0(B_r):
    gen_by_name=AttrDict({
                "x": Generator("x"),
                })

    gen_by_name.x.add_idems(B_r.idem_by_name.l0,0)
    

    left_d_arrows=Bunch_of_arrows([
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,B_r,name="B_N_L0")
B_N_L0=init_Left_B_N_L0(B_r)
def init_Left_B_N_L0_deform(B_r):
    gen_by_name=AttrDict({
                "x": Generator("x"),
                })

    gen_by_name.x.add_idems(B_r.idem_by_name.l0,0)
    

    left_d_arrows=Bunch_of_arrows([
        (              gen_by_name.x,
           B_r.gen_by_name.c0, gen_by_name.x),
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,B_r,name="B_N_L0_deform")
B_N_L0_deform=init_Left_B_N_L0_deform(B_r)
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
def init_DA_sigm2(B_r):
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

    return DA_bimodule(gen_by_name,arrows,B_r,B_r,name="DA_sigm2")     #return DA_bimodule(gen_by_name,arrows,B_r,B_r,name="DA_sigm2") # from the bordered Khovanov DA construction Andy showed to you
DA_sigm2=init_DA_sigm2(B_r)
def init_DA_new(B_r):
    gen_by_name=AttrDict({
                "x001": Generator("x001"),
                "x002": Generator("x002"),
                "x003": Generator("x003"),
                "x011": Generator("x011"),
                "x012": Generator("x012"),
                "x101": Generator("x101"),
                "x102": Generator("x102"),
                "x111": Generator("x111"),
                "x112": Generator("x112"),
                "x113": Generator("x113"),
                "x114": Generator("x114"),
                })
    gen_by_name.x001.add_idems(B_r.idem_by_name.l0,B_r.idem_by_name.l0)
    gen_by_name.x002.add_idems(B_r.idem_by_name.l0,B_r.idem_by_name.l0)
    gen_by_name.x003.add_idems(B_r.idem_by_name.l0,B_r.idem_by_name.l1)
    gen_by_name.x011.add_idems(B_r.idem_by_name.l0,B_r.idem_by_name.l0)
    gen_by_name.x012.add_idems(B_r.idem_by_name.l1,B_r.idem_by_name.l1)
    gen_by_name.x101.add_idems(B_r.idem_by_name.l0,B_r.idem_by_name.l0)
    gen_by_name.x102.add_idems(B_r.idem_by_name.l1,B_r.idem_by_name.l1)
    gen_by_name.x111.add_idems(B_r.idem_by_name.l0,B_r.idem_by_name.l0)
    gen_by_name.x112.add_idems(B_r.idem_by_name.l0,B_r.idem_by_name.l0)
    gen_by_name.x113.add_idems(B_r.idem_by_name.l1,B_r.idem_by_name.l1)
    gen_by_name.x114.add_idems(B_r.idem_by_name.l1,B_r.idem_by_name.l1)

    arrows=Bunch_of_arrows([
        (              gen_by_name.x002,(B_r.gen_by_name.c0,),
                1,gen_by_name.x001),
        (              gen_by_name.x002,(B_r.gen_by_name.p01,),
                1,gen_by_name.x003),
        (              gen_by_name.x003,(B_r.gen_by_name.q10,),
                1,gen_by_name.x001),

        (              gen_by_name.x011,(B_r.gen_by_name.c0,),
                B_r.gen_by_name.c0,gen_by_name.x011),
        (              gen_by_name.x011,(B_r.gen_by_name.p01,),
                B_r.gen_by_name.p01,gen_by_name.x012),
        (              gen_by_name.x012,(B_r.gen_by_name.q10,),
                B_r.gen_by_name.q10,gen_by_name.x011),
        (              gen_by_name.x012,(B_r.gen_by_name.c1,),
                B_r.gen_by_name.c1,gen_by_name.x012),

        (              gen_by_name.x101,(B_r.gen_by_name.c0,),
                B_r.gen_by_name.c0,gen_by_name.x101),
        (              gen_by_name.x101,(B_r.gen_by_name.p01,),
                B_r.gen_by_name.p01,gen_by_name.x102),
        (              gen_by_name.x102,(B_r.gen_by_name.q10,),
                B_r.gen_by_name.q10,gen_by_name.x101),
        (              gen_by_name.x102,(B_r.gen_by_name.c1,),
                B_r.gen_by_name.c1,gen_by_name.x102),

        (              gen_by_name.x111,(B_r.gen_by_name.c0,),
                B_r.gen_by_name.c0,gen_by_name.x111),
        (              gen_by_name.x111,(B_r.gen_by_name.p01,),
                B_r.gen_by_name.p01,gen_by_name.x113),
        (              gen_by_name.x113,(B_r.gen_by_name.q10,),
                B_r.gen_by_name.q10,gen_by_name.x111),
        (              gen_by_name.x113,(B_r.gen_by_name.c1,),
                B_r.gen_by_name.c1,gen_by_name.x113),

        (              gen_by_name.x112,(B_r.gen_by_name.c0,),
                B_r.gen_by_name.c0,gen_by_name.x112),
        (              gen_by_name.x112,(B_r.gen_by_name.p01,),
                B_r.gen_by_name.p01,gen_by_name.x114),
        (              gen_by_name.x114,(B_r.gen_by_name.q10,),
                B_r.gen_by_name.q10,gen_by_name.x112),
        (              gen_by_name.x114,(B_r.gen_by_name.c1,),
                B_r.gen_by_name.c1,gen_by_name.x114),

        (              gen_by_name.x002,(),
                1,gen_by_name.x011),
        (              gen_by_name.x002,(),
                1,gen_by_name.x101),
        (              gen_by_name.x012,(),
                1,gen_by_name.x114),
        (              gen_by_name.x102,(),
                1,gen_by_name.x114),
        (              gen_by_name.x011,(),
                1,gen_by_name.x112),
        (              gen_by_name.x101,(),
                1,gen_by_name.x112),
        (              gen_by_name.x001,(),
                B_r.gen_by_name.c0,gen_by_name.x011),
        (              gen_by_name.x001,(),
                B_r.gen_by_name.c0,gen_by_name.x101),
        (              gen_by_name.x003,(),
                B_r.gen_by_name.p01,gen_by_name.x012),
        (              gen_by_name.x003,(),
                B_r.gen_by_name.p01,gen_by_name.x102),
        (              gen_by_name.x012,(),
                B_r.gen_by_name.c1,gen_by_name.x113),
        (              gen_by_name.x101,(),
                B_r.gen_by_name.c0,gen_by_name.x111),
        (              gen_by_name.x011,(),
                B_r.gen_by_name.c0,gen_by_name.x111),

        ])

    return DA_bimodule(gen_by_name,arrows,B_r,B_r,name="DA_new")     #return DA_bimodule(gen_by_name,arrows,B_r,B_r,name="DA_new") # from the bordered Khovanov DA construction Andy showed to you
DA_new=init_DA_new(B_r)

########## computing Fuk
# Fuk=algebra_from_mor_spaces_of_left_D_structures(
#                                             N_L0,
#                                             N_L1,
#                                             Di1,
#                                             Dj1,
#                                             Di2,
#                                             Dj2,
#                                             Di0,
#                                             Dj0,
#                                             )
# Fuk=rename_generators(Fuk,[
#                         ('(L0_j1, j1, L0_j1)','00(j1)' ), 
#                         ('(L0_i0, et123, L0_j0)','00(et123)' ),
#                         ('(L0_i1, et2, L0_j1)','00(et2)' ),
#                         ('(L0_i0, et12, L0_j1)','00(et12)' ),
#                         ('(L0_j1, et3, L0_j0)','00(et3)' ),
#                         ('(L0_i1, et23, L0_j0)','00(et23)' ),
#                         ('(L0_i0, r0, L0_j0)','00(r0)' ),
#                         ('(L0_i1, i1, L0_i1)','00(i1)' ),
#                         ('(L0_i0, i0, L0_i0)','00(i0)' ),
#                         ('(L0_j0, j0, L0_j0)','b_r(l0)' ),
#                         ('(L0_i1, ks123, L0_j1)','00(ks123)' ),
#                         ('(L0_i0, et1, L0_i1)','b_r(c0)' ),

#                         ('(L1_j2, j2, L1_j2)','11(j2)'), 
#                         ('(L1_i1, ks12, L1_j2)','11(ks12)'), 
#                         ('(L1_i2, ks23, L1_j1)','11(ks23)'), 
#                         ('(L1_i1, ks123, L1_j1)','11(ks123)'), 
#                         ('(L1_i1, ks1, L1_i2)','11(ks1)'), 
#                         ('(L1_i2, i2, L1_i2)','11(i2)'), 
#                         ('(L1_i2, ks2, L1_j2)','11(ks2)'), 
#                         ('(L1_i1, et2, L1_j1)','11(et2)'), 
#                         ('(L1_i1, i1, L1_i1)','11(i1)'),
#                         ('(L1_i2, r2, L1_j2)','11(r2)'), 
#                         ('(L1_j2, ks3, L1_j1)','b_r(c1)'), 
#                         ('(L1_j1, j1, L1_j1)','b_r(l1)'), 

#                         ('(L0_i1, ks123, L1_j1)','01(ks123)'),
#                         ('(L0_i1, et2, L1_j1)','01(et2)'), 
#                         ('(L0_i1, i1, L1_i1)','01(i1)'), 
#                         ('(L0_j1, j1, L1_j1)','01(j1)'), 
#                         ('(L0_i1, ks1, L1_i2)','01(ks1)'), 
#                         ('(L0_i0, et12, L1_j1)','01(et12)'), 
#                         ('(L0_i1, ks12, L1_j2)','01(ks12)'), 
#                         ('(L0_i0, et1, L1_i1)','b_r(p01)'),

#                         ('(L1_i2, ks23, L0_j1)','10(ks23)'), 
#                         ('(L1_j1, et3, L0_j0)','b_r(q10)'), 
#                         ('(L1_j1, j1, L0_j1)','10(j1)'), 
#                         ('(L1_j2, ks3, L0_j1)','10(ks3)'), 
#                         ('(L1_i1, et23, L0_j0)','10(et23)'), 
#                         ('(L1_i1, et2, L0_j1)','10(et2)'), 
#                         ('(L1_i1, i1, L0_i1)','10(i1)'), 
#                         ('(L1_i1, ks123, L0_j1)','10(ks123)'),

#                         ('(arc_i1, ks1, arc_i2)','a(ks1)'),
#                         ('(arc_i2, ks2, arc_j2)','a(ks2)'),
#                         ('(arc_j2, ks3, arc_j1)','a(ks3)'),
#                         ('(arc_i1, ks12, arc_j2)','a(ks12)'),
#                         ('(arc_i2, ks23, arc_j1)','a(ks23)'),
#                         ('(arc_i1, ks123, arc_j1)','a(ks123)'),
#                         ('(arc_i0, et1, arc_i1)','a(et1)'),
#                         ('(arc_i1, et2, arc_j1)','a(et2)'),
#                         ('(arc_j1, et3, arc_j0)','a(et3)'),
#                         ('(arc_i0, et12, arc_j1)','a(et12)'),
#                         ('(arc_i1, et23, arc_j0)','a(et23)'),
#                         ('(arc_i0, et123, arc_j0)','a(et123)'),
#                         ('(arc_i0, i0, arc_i0)','a(i0)'),
#                         ('(arc_i1, i1, arc_i1)','a(i1)'),
#                         ('(arc_i2, i2, arc_i2)','a(i2)'),
#                         ('(arc_j0, j0, arc_j0)','a(j0)'),
#                         ('(arc_j1, j1, arc_j1)','a(j1)'),
#                         ('(arc_j2, j2, arc_j2)','a(j2)'),
#                         ('(arc_i0, r0, arc_j0)','a(r0)'),
#                         ('(arc_i2, r2, arc_j2)','a(r2)'),

#                         ])
# ### gives bounded algebra B

# max_a_infty_action=10
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['00(i1)'],Fuk.gen_by_name['00(et23)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['00(i0)'],Fuk.gen_by_name['00(et12)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['00(j1)'],Fuk.gen_by_name['00(r0)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['00(et3)'],Fuk.gen_by_name['00(et123)']),max_a_infty_action)

# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['11(i2)'],Fuk.gen_by_name['11(r2)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['11(j2)'],Fuk.gen_by_name['11(ks23)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['11(ks1)'],Fuk.gen_by_name['11(ks123)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['11(i1)'],Fuk.gen_by_name['11(ks12)']),max_a_infty_action)

# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['10(ks3)'],Fuk.gen_by_name['10(ks123)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['10(j1)'],Fuk.gen_by_name['10(ks23)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['10(i1)'],Fuk.gen_by_name['10(et23)']),max_a_infty_action)

# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['01(ks1)'],Fuk.gen_by_name['01(ks123)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['01(i1)'],Fuk.gen_by_name['01(ks12)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['01(j1)'],Fuk.gen_by_name['01(et12)']),max_a_infty_action)

# #### works for Fuk(N_L0,N_L1,Di1)
# #### Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['(arc_i1, ks1, L1_i2)'],Fuk.gen_by_name['(arc_i1, ks123, L1_j1)']),max_a_infty_action)
# #### Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['(arc_i1, i1, L1_i1)'],Fuk.gen_by_name['(arc_i1, ks12, L1_j2)']),max_a_infty_action)
# #### Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['(arc_i1, i1, L0_i1)'],Fuk.gen_by_name['(arc_i1, ks123, L0_j1)']),max_a_infty_action)


# #### for Fuk(N_L0,N_L1,Di0,...,Dj2)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['(arc_i1, ks1, L1_i2)'],Fuk.gen_by_name['(arc_i1, ks123, L1_j1)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['(arc_i1, i1, L1_i1)'],Fuk.gen_by_name['(arc_i1, ks12, L1_j2)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['(L1_j1, j1, arc_j1)'],Fuk.gen_by_name['(L1_i2, ks23, arc_j1)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['(L1_j2, ks3, arc_j1)'],Fuk.gen_by_name['(L1_i1, ks123, arc_j1)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['(arc_i1, i1, L0_i1)'],Fuk.gen_by_name['(arc_i1, et23, L0_j0)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['(L0_j1, j1, arc_j1)'],Fuk.gen_by_name['(L0_i0, et12, arc_j1)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['(arc_i2, i2, L1_i2)'],Fuk.gen_by_name['(arc_i2, r2, L1_j2)']),max_a_infty_action)

# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['(L1_j2, j2, arc_j2)'],Fuk.gen_by_name['(L1_i2, r2, arc_j2)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['(arc_i0, i0, L0_i0)'],Fuk.gen_by_name['(arc_i0, r0, L0_j0)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['(arc_i0, et1, L0_i1)'],Fuk.gen_by_name['(arc_i0, et123, L0_j0)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['(L0_j0, j0, arc_j0)'],Fuk.gen_by_name['(L0_i0, r0, arc_j0)']),max_a_infty_action)
# #### actually I realized it is not necessary for computing the AA bimodule. The cancellation can be done to AA bimodule itself :) 

# # Fuk=change_of_basis(Fuk,Fuk.gen_by_name['11(ks2)'],Fuk.gen_by_name['11(et2)'])
# # Fuk=act_by_G2(Fuk, G2=Bunch_of_arrows([
# #             (Fuk.gen_by_name['00(ks123)'],Fuk.gen_by_name['00(ks123)'],
# #             Fuk.gen_by_name['00(ks123)'])       ])
# #         )

# Fuk=rename_generators(Fuk,[
#                         ('b_r(l0)' , 'l0'),
#                         ('b_r(c0)' , 'c0'),
#                         ('b_r(c1)', 'c1'), 
#                         ('b_r(l1)', 'l1'), 
#                         ('b_r(p01)', 'p01'),
#                         ('b_r(q10)', 'q10'), 

#                         ('a(ks1)','ks1'),
#                         ('a(ks2)','ks2'),
#                         ('a(ks3)','ks3'),
#                         ('a(ks12)','ks12'),
#                         ('a(ks23)','ks23'),
#                         ('a(ks123)','ks123'),
#                         ('a(et1)','et1'),
#                         ('a(et2)','et2'),
#                         ('a(et3)','et3'),
#                         ('a(et12)','et12'),
#                         ('a(et23)','et23'),
#                         ('a(et123)','et123'),
#                         ('a(i0)','i0'),
#                         ('a(i1)','i1'),
#                         ('a(i2)','i2'),
#                         ('a(j0)','j0'),
#                         ('a(j1)','j1'),
#                         ('a(j2)','j2'),
#                         ('a(r0)','r0'),
#                         ('a(r2)','r2'),
#                         ])
# with open('fuk.pkl', 'wb') as output:
#     pickle.dump(Fuk, output, pickle.HIGHEST_PROTOCOL)


##### loading Fuk(N_L0,N_L1,Di0,...,Dj2) from the pickle
with open('fuk.pkl', 'rb') as input:
    Fuk = pickle.load(input)
##### a_AA_b_r from Fuk(N_L0,N_L1,Di0,...,Dj2)
generators=[gen for gen in Fuk.genset if gen.name[:2]=='(a']
a_AA_b_r=base_change_AA_from_fuk(Fuk,generators,pil_A,B_r)
a_AA_b_r=aa_randomly_cancel_until_possible(a_AA_b_r)

# Amod=aa_d_box_tensor_product(a_AA_b_r,B_N_L0)
# N_L0_candidate=dd_a_box_tensor_product(DD_bar_r_dual,Amod)
# N_L0_candidate=left_d_randomly_cancel_until_possible(N_L0_candidate)
# N_L0_candidate.show()
# N_L0.show()

### getting dual(a_AA_b_r) by hom pert lemma
# generators=[gen for gen in Fuk.genset if gen.name[:2]=='(L']
# b_r_AA_a=base_change_AA_from_fuk(Fuk,generators,B_r,pil_A)
# b_r_AA_a=aa_randomly_cancel_until_possible(b_r_AA_a)


##### MAIN PROOF OF THE PAPER
# MW_0=d_aa_box_tensor_product(dualization_left_to_right_D(Di1),a_AA_a(pil_A))
# ##### because I have dd_a, but not a_dd, I dualize everything here...
# DDD=dd_a_box_tensor_product(dualization_of_DD(DD_bar_r_dual),dualization_right_to_left_A(MW_0))
# DDD=left_d_randomly_cancel_until_possible(DDD)
# dual_Amod_Q=aa_d_box_tensor_product(dualization_of_AA(a_AA_b_r),DDD)
# dual_Amod_Q=left_a_randomly_cancel_until_possible(dual_Amod_Q)
# dual_Amod_Q.show()
##### WORKS!!!!!! 

##################################################################################
##################################################################################
##################################################################################
########### finding bimodule associated to a braid move
# C=algebra_from_mor_spaces_of_left_D_structures(
#                                             Dl0,
#                                             Dl1,
#                                             Dl2,
#                                             )
# C=rename_generators(C,[
#                         ('(x, l0, x)','00(l0)'),
#                         ('(x, c0, x)','00(c0)'), 
#                         ('(x, p01, y)','01(p01⊗t)'), #01(p01) 
#                         ('(y, q10, x)','10(q10)'), 
#                         ('(y, c1, y)','11(c1⊗t)'),  #11(c1)
#                         ('(y, l1, y)','11(l1⊗t)'),  #11(l1)

#                         ('(x, l0, z0)','02(l0)'),
#                         ('(x, c0, z0)','02(c0⊗x)'),  # 02(c0)
#                         ('(y, q10, z0)','12(q10)'), 
#                         ('(x, p01, z1)','02(p01)'), 
#                         ('(y, c1, z1)','12(c1)'),  # 
#                         ('(y, l1, z1)','12(l1⊗y)'), #12(l1)

#                         ('(z0, l0, x)','20(l0)'),
#                         ('(z0, c0, x)','20(c0)'), 
#                         ('(z0, p01, y)','21(p01)'), 
#                         ('(z1, q10, x)','20(q10)'), 
#                         ('(z1, c1, y)','21(c1)'), 
#                         ('(z1, l1, y)','21(l1)'),

#                         ('(z0, l0, z0)','22(l0)'),
#                         ('(z0, c0, z0)','22(c0)'), 
#                         ('(z0, p01, z1)','22(p01)'), 
#                         ('(z1, q10, z0)','22(q10)'), 
#                         ('(z1, c1, z1)','22(c1)'), 
#                         ('(z1, l1, z1)','22(l1)'),
#                         ])

# max_a_infty_action=25
# C=perturb_algebra(C,(C.gen_by_name['22(l0)'],C.gen_by_name['22(p01)']),max_a_infty_action)
# C=perturb_algebra(C,(C.gen_by_name['22(q10)'],C.gen_by_name['22(c1)']),max_a_infty_action)
# C=perturb_algebra(C,(C.gen_by_name['02(l0)'],C.gen_by_name['02(p01)']),max_a_infty_action)
# C=perturb_algebra(C,(C.gen_by_name['21(l1)'],C.gen_by_name['21(p01)']),max_a_infty_action)
# C=perturb_algebra(C,(C.gen_by_name['20(q10)'],C.gen_by_name['20(c0)']),max_a_infty_action)
# C=perturb_algebra(C,(C.gen_by_name['12(q10)'],C.gen_by_name['12(c1)']),max_a_infty_action)

# C.show()

# #### C.show(restrict=[
# ####                 C.gen_by_name['22(c0)'],
# ####                 C.gen_by_name['22(l1)'],
# ####                 C.gen_by_name['11(l1)'],
# ####                 C.gen_by_name['11(c1)'],
# ####                 C.gen_by_name['21(c1)'],
# ####                 C.gen_by_name['12(l1)'],
# ###                 ])

# ############################# comparing AA⊗DA with AA coming from C:
# #### AA⊗DA
# A_B_r_A=a_AA_a(B_r)
# AA_sigm2=aa_da_box_tensor_product(A_B_r_A,DA_sigm2)
# AA_sigm2=aa_randomly_cancel_until_possible(AA_sigm2)
# AA_sigm2.show()

# #### now compare AA_phi with the computed algebra C

######################## curve for (3,-2) pretzel tangle

# DA=da_da_box_tensor_many_efficient_cancelations(DA_new,DA_sigm2)
# AA=aa_randomly_cancel_until_possible(aa_da_box_tensor_product(a_AA_b_r,DA))
# A=aa_d_box_tensor_product(AA,B_N_L0)
# # A=aa_d_box_tensor_product(AA,B_N_L0_deform)
# D=left_d_randomly_cancel_until_possible(dd_a_box_tensor_product(DD_bar_r_dual,A))
# simpler_names_for_generators(D)
# D.show()

########################## new Fuk
Fuk=algebra_from_mor_spaces_of_left_D_structures(
                                            N_L2,
                                            N_L1,
                                            # Di1,
                                            # Dj1,
                                            # Di2,
                                            # Dj2,
                                            # Di0,
                                            # Dj0,
                                            )

Fuk=rename_generators(Fuk,[
                        ('(L2_i0, et1, L2_i1_0)','22(et1)_'),
                        ('(L2_i0, et1, L2_i1_5)','22(et1)'),
                        ('(L2_i0, et123, L2_j0)','22(et123)'),
                        ('(L2_i0, i0, L2_i0)','22(i0)'),
                        ('(L2_i0, r0, L2_j0)','22(r0)'),
                        ('(L2_i1_0, et23, L2_j0)','22(et23)_'),
                        ('(L2_i1_0, i1, L2_i1_0)','22(i1)_'),
                        ('(L2_i1_0, i1, L2_i1_5)','22(i1)'),
                        ('(L2_i1_0, ks1, L2_i2)','22(ks1)_'),
                        ('(L2_i1_0, ks12, L2_j2)','22(ks12)_'),
                        ('(L2_i1_5, et23, L2_j0)','22(et23)'),
                        ('(L2_i1_5, i1, L2_i1_0)','_22(i1)'),
                        ('(L2_i1_5, i1, L2_i1_5)','_22(i1)_'),
                        ('(L2_i1_5, ks1, L2_i2)','22(ks1)'),
                        ('(L2_i1_5, ks12, L2_j2)','22(ks12)'),
                        ('(L2_i2, i2, L2_i2)','22(i2)'),
                        ('(L2_i2, ks2, L2_j2)','22(ks2)'),
                        ('(L2_i2, r2, L2_j2)','22(r2)'),
                        ('(L2_j0, j0, L2_j0)','22(j0)'),
                        ('(L2_j2, j2, L2_j2)','22(j2)'),

                        ('(L2_i2, i2, L1_i2)','21(i2)'),
                        ('(L2_i0, et1, L1_i1)','21(et1)'),
                        ('(L2_i0, et12, L1_j1)','21(et12)'),
                        ('(L2_i1_0, et2, L1_j1)','21(et2)_'),
                        ('(L2_i1_0, i1, L1_i1)','21(i1)_'),
                        ('(L2_i1_0, ks1, L1_i2)','21(ks1)_'),
                        ('(L2_i1_0, ks12, L1_j2)','21(ks12)_'),
                        ('(L2_i1_0, ks123, L1_j1)','21(ks123)_'),
                        ('(L2_i1_5, et2, L1_j1)','21(et2)'),
                        ('(L2_j2, j2, L1_j2)','21(j2)'),
                        ('(L2_i2, r2, L1_j2)','21(r2)'),
                        ('(L2_j2, ks3, L1_j1)','21(ks3)'),
                        ('(L2_i1_5, i1, L1_i1)','21(i1)'),
                        ('(L2_i1_5, ks1, L1_i2)','21(ks1)'),
                        ('(L2_i1_5, ks12, L1_j2)','21(ks12)'),
                        ('(L2_i1_5, ks123, L1_j1)','21(ks123)'),
                        ('(L2_i2, ks2, L1_j2)','21(ks2)'),
                        ('(L2_i2, ks23, L1_j1)','21(ks23)'),

                        ('(L1_j2, j2, L1_j2)','11(j2)'), 
                        ('(L1_i1, ks12, L1_j2)','11(ks12)'), 
                        ('(L1_i2, ks23, L1_j1)','11(ks23)'), 
                        ('(L1_i1, ks123, L1_j1)','11(ks123)'), 
                        ('(L1_i1, ks1, L1_i2)','11(ks1)'), 
                        ('(L1_i2, i2, L1_i2)','11(i2)'), 
                        ('(L1_i2, ks2, L1_j2)','11(ks2)'), 
                        ('(L1_i1, et2, L1_j1)','11(et2)'), 
                        ('(L1_i1, i1, L1_i1)','11(i1)'),
                        ('(L1_i2, r2, L1_j2)','11(r2)'), 
                        ('(L1_j2, ks3, L1_j1)','11(ks3)'), 
                        ('(L1_j1, j1, L1_j1)','11(j1)'), 

                        ('(L1_i1, et23, L2_j0)','12(et23)'),
                        ('(L1_i1, i1, L2_i1_0)','12(i1)_'),
                        ('(L1_i1, i1, L2_i1_5)','12(i1)'),
                        ('(L1_i1, ks1, L2_i2)','12(ks1)'),
                        ('(L1_i1, ks12, L2_j2)','12(ks12)'),
                        ('(L1_i2, i2, L2_i2)','12(i2)'),
                        ('(L1_i2, ks2, L2_j2)','12(ks2)'),
                        ('(L1_i2, r2, L2_j2)','12(r2)'),
                        ('(L1_j1, et3, L2_j0)','12(et3)'),
                        ('(L1_j2, j2, L2_j2)','12(j2)'),

                        # ('(arc_i1, ks1, arc_i2)','a(ks1)'),
                        # ('(arc_i2, ks2, arc_j2)','a(ks2)'),
                        # ('(arc_j2, ks3, arc_j1)','a(ks3)'),
                        # ('(arc_i1, ks12, arc_j2)','a(ks12)'),
                        # ('(arc_i2, ks23, arc_j1)','a(ks23)'),
                        # ('(arc_i1, ks123, arc_j1)','a(ks123)'),
                        # ('(arc_i0, et1, arc_i1)','a(et1)'),
                        # ('(arc_i1, et2, arc_j1)','a(et2)'),
                        # ('(arc_j1, et3, arc_j0)','a(et3)'),
                        # ('(arc_i0, et12, arc_j1)','a(et12)'),
                        # ('(arc_i1, et23, arc_j0)','a(et23)'),
                        # ('(arc_i0, et123, arc_j0)','a(et123)'),
                        # ('(arc_i0, i0, arc_i0)','a(i0)'),
                        # ('(arc_i1, i1, arc_i1)','a(i1)'),
                        # ('(arc_i2, i2, arc_i2)','a(i2)'),
                        # ('(arc_j0, j0, arc_j0)','a(j0)'),
                        # ('(arc_j1, j1, arc_j1)','a(j1)'),
                        # ('(arc_j2, j2, arc_j2)','a(j2)'),
                        # ('(arc_i0, r0, arc_j0)','a(r0)'),
                        # ('(arc_i2, r2, arc_j2)','a(r2)'),
                        ])

max_a_infty_action=10
Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['22(i1)_'],Fuk.gen_by_name['22(et1)_']),max_a_infty_action)
Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['22(i1)'],Fuk.gen_by_name['22(et1)']),max_a_infty_action)
Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['22(et23)_'],Fuk.gen_by_name['22(et123)']),max_a_infty_action)
Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['22(i0)'],Fuk.gen_by_name['22(r0)']),max_a_infty_action)
Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['22(j2)'],Fuk.gen_by_name['22(ks12)_']),max_a_infty_action)
Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['22(j0)'],Fuk.gen_by_name['22(r2)']),max_a_infty_action)
Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['22(i2)'],Fuk.gen_by_name['22(et23)']),max_a_infty_action)
Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['_22(i1)'],Fuk.gen_by_name['22(ks12)']),max_a_infty_action)

Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['11(i2)'],Fuk.gen_by_name['11(r2)']),max_a_infty_action)
Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['11(j2)'],Fuk.gen_by_name['11(ks23)']),max_a_infty_action)
Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['11(ks1)'],Fuk.gen_by_name['11(ks123)']),max_a_infty_action)
Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['11(i1)'],Fuk.gen_by_name['11(ks12)']),max_a_infty_action)


# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['21(j2)'],Fuk.gen_by_name['21(ks12)_']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['21(i2)'],Fuk.gen_by_name['21(ks23)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['21(i1)'],Fuk.gen_by_name['21(et2)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['21(i1)'],Fuk.gen_by_name['21(et2)']),max_a_infty_action)

# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['21(i1)'],Fuk.gen_by_name['21(ks12)']),max_a_infty_action)

# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['21(ks1)_'],Fuk.gen_by_name['21(ks123)_']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['21(et2)_'],Fuk.gen_by_name['21(et12)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['21(ks1)'],Fuk.gen_by_name['21(ks123)']),max_a_infty_action)





# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['12(j2)'],Fuk.gen_by_name['12(r2)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['12(i1)_'],Fuk.gen_by_name['12(ks12)']),max_a_infty_action)
# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['12(i1)'],Fuk.gen_by_name['12(et23)']),max_a_infty_action)

# Fuk=perturb_algebra(Fuk,(Fuk.gen_by_name['12(et3)'],Fuk.gen_by_name['12(ks1)']),max_a_infty_action)



# 12(et3) ⟶   12(et23)
# 12(i1) ⟶   12(et23)
# 12(i1) ⟶   12(ks1)
# 12(i1)_ ⟶   12(ks12)
# 12(i2) ⟶   12(r2)
# 12(j2) ⟶   12(ks12)
# 12(j2) ⟶   12(r2)


Fuk.show()






