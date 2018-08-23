# -*- coding: utf-8 -*- 
import sys
sys.path.append('../')
import cPickle as pickle

from algebraic_structures.visual import  *
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

#### modules over B_r
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
def init_DA_sigm1(B_r):
    gen_by_name=AttrDict({
                "x": Generator("x"),
                "y": Generator("y"),
                "t": Generator("t"),
                })
    gen_by_name.x.add_idems(B_r.idem_by_name.l1,B_r.idem_by_name.l1)
    gen_by_name.y.add_idems(B_r.idem_by_name.l0,B_r.idem_by_name.l1)
    gen_by_name.t.add_idems(B_r.idem_by_name.l0,B_r.idem_by_name.l0)

    arrows=Bunch_of_arrows([
        (              gen_by_name.x,(B_r.gen_by_name.c1,),
                B_r.gen_by_name.c1,gen_by_name.x),
        (              gen_by_name.x,(),
                B_r.gen_by_name.q10,gen_by_name.y),
        (              gen_by_name.y,(B_r.gen_by_name.q10,),
                B_r.gen_by_name.c0,gen_by_name.t),
        (              gen_by_name.y,(B_r.gen_by_name.q10,B_r.gen_by_name.p01),
                B_r.gen_by_name.p01,gen_by_name.x),
        (              gen_by_name.t,(B_r.gen_by_name.p01,),
                1,gen_by_name.y),
        (              gen_by_name.t,(B_r.gen_by_name.c0,),
                B_r.gen_by_name.c0,gen_by_name.t),
        (              gen_by_name.t,(B_r.gen_by_name.c0,B_r.gen_by_name.p01),
                B_r.gen_by_name.p01,gen_by_name.x),

        ])

    return DA_bimodule(gen_by_name,arrows,B_r,B_r,name="DA_sigm1")     #return DA_bimodule(gen_by_name,arrows,B_r,B_r,name="DA_sigm1") # from the bordered Khovanov DA construction Andy showed to you
DA_sigm1=init_DA_sigm1(B_r)
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

def init_Pretzel_2_3_short(B_r):
    gen_by_name=AttrDict({
                "x": Generator("x"),
                "y": Generator("y"),
                "z": Generator("z"),
                })

    gen_by_name.x.add_idems(B_r.idem_by_name.l0,0)
    gen_by_name.y.add_idems(B_r.idem_by_name.l1,0)
    gen_by_name.z.add_idems(B_r.idem_by_name.l1,0)
    

    left_d_arrows=Bunch_of_arrows([
                (              gen_by_name.x,
           B_r.gen_by_name.p01, gen_by_name.y),
                (              gen_by_name.y,
           B_r.gen_by_name.c1, gen_by_name.z),
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,B_r,name="Pretzel_2_3_short")
Pretzel_2_3_short=init_Pretzel_2_3_short(B_r)
def init_Pretzel_2_3_long(B_r):
    gen_by_name=AttrDict({
                "x1": Generator("x1"),
                "x2": Generator("x2"),
                "x3": Generator("x3"),
                "x4": Generator("x4"),
                "x5": Generator("x5"),
                "x6": Generator("x6"),
                "x7": Generator("x7"),
                "x8": Generator("x8"),
                })

    gen_by_name.x1.add_idems(B_r.idem_by_name.l0,0)
    gen_by_name.x2.add_idems(B_r.idem_by_name.l0,0)
    gen_by_name.x3.add_idems(B_r.idem_by_name.l1,0)
    gen_by_name.x4.add_idems(B_r.idem_by_name.l1,0)
    gen_by_name.x5.add_idems(B_r.idem_by_name.l0,0)
    gen_by_name.x6.add_idems(B_r.idem_by_name.l0,0)
    gen_by_name.x7.add_idems(B_r.idem_by_name.l1,0)
    gen_by_name.x8.add_idems(B_r.idem_by_name.l1,0)
    
    left_d_arrows=Bunch_of_arrows([
                    ( gen_by_name.x1,
           B_r.gen_by_name.c0, gen_by_name.x2),
                    ( gen_by_name.x2,
           B_r.gen_by_name.p01, gen_by_name.x3),
                    ( gen_by_name.x3,
           B_r.gen_by_name.c1, gen_by_name.x4),
                    ( gen_by_name.x5,
           B_r.gen_by_name.p01, gen_by_name.x4),
                    ( gen_by_name.x5,
           B_r.gen_by_name.c0, gen_by_name.x6),
                    ( gen_by_name.x6,
           B_r.gen_by_name.p01, gen_by_name.x7),
                    ( gen_by_name.x7,
           B_r.gen_by_name.c1, gen_by_name.x8),
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,B_r,name="Pretzel_2_3_long")
Pretzel_2_3_long=init_Pretzel_2_3_long(B_r)


##### loading Fuk(N_L0,N_L1,Di0,...,Dj2) from the pickle
with open('fuk.pkl', 'rb') as input:
    Fuk = pickle.load(input)
##### a_AA_b_r from Fuk(N_L0,N_L1,Di0,...,Dj2)
generators=[gen for gen in Fuk.genset if gen.name[:2]=='(a']
a_AA_b_r=base_change_AA_from_fuk(Fuk,generators,pil_A,B_r)
a_AA_b_r=aa_randomly_cancel_until_possible(a_AA_b_r)
simpler_names_for_generators(a_AA_b_r)
# a_AA_b_r.show()

main_DA=dd_aa_box_tensor_product(DD_bar_r_dual,a_AA_b_r)
main_DA=da_cancel_until_possible(main_DA)
simpler_names_for_generators(main_DA)
# main_DA.show()

##### RHT d structure
# DA=da_da_box_tensor_many_efficient_cancelations(DA_sigm2,DA_sigm2)
# D=da_d_box_tensor_product(DA,B_N_L0)
# simpler_names_for_generators(D)
# D.show()
# A=aa_d_box_tensor_product(a_AA_b_r,D)
# A=left_a_randomly_cancel_until_possible(A)
# a_D=dd_a_box_tensor_product(DD_bar_r_dual,A)
# a_D=left_d_randomly_cancel_until_possible(a_D)
# simpler_names_for_generators(a_D)
# a_D.show()


###### sigm2^(-1)

##### MAIN PROOF OF THE PAPER
MW_0=d_aa_box_tensor_product(dualization_left_to_right_D(Di1),a_AA_a(pil_A))
MW_0.show()
# # ##### because I have dd_a, but not a_dd, I dualize everything here...
DDD=dd_a_box_tensor_product(dualization_of_DD(DD_bar_r_dual),dualization_right_to_left_A(MW_0))
DDD=left_d_randomly_cancel_until_possible(DDD)
dual_Amod_Q=aa_d_box_tensor_product(dualization_of_AA(a_AA_b_r),DDD)
dual_Amod_Q=left_a_randomly_cancel_until_possible(dual_Amod_Q)
simpler_names_for_generators(dual_Amod_Q)
dual_Amod_Q.show()
##### WORKS!!!!!! 


######################## counterexample to general pairing of twisted complexes
# def init_Left_ContrE(B_r):
#     gen_by_name=AttrDict({
#                 "x1": Generator("x1"),
#                 "x2": Generator("x2"),
#                 "x3": Generator("x3"),
#                 "x4": Generator("x4"),
#                 "x5": Generator("x5")
#                 })

#     gen_by_name.x1.add_idems(B_r.idem_by_name.l1,0)
#     gen_by_name.x2.add_idems(B_r.idem_by_name.l0,0)
#     gen_by_name.x3.add_idems(B_r.idem_by_name.l0,0)
#     gen_by_name.x4.add_idems(B_r.idem_by_name.l0,0)
#     gen_by_name.x5.add_idems(B_r.idem_by_name.l1,0)
    
#     left_d_arrows=Bunch_of_arrows([
#         (              gen_by_name.x1,
#            B_r.gen_by_name.q10, gen_by_name.x2),
#         (              gen_by_name.x2,
#            B_r.gen_by_name.c0, gen_by_name.x3),
#         (              gen_by_name.x3,
#            B_r.gen_by_name.c0, gen_by_name.x4),
#         (              gen_by_name.x4,
#            B_r.gen_by_name.p01, gen_by_name.x5),
#                                     ])

#     return Left_D_module(gen_by_name,left_d_arrows,B_r,name="B_N_L0")
# ContrE=init_Left_ContrE(B_r)
# ## khovanov pairing (6*2=12 dim)
# uu=d_aa_box_tensor_product(dualization_left_to_right_D(ContrE),a_AA_a(B_r))
# kh=a_d_box_tensor_product(uu,ContrE)
# # print homology_dim(kh)

# ## lagrangian algebraic pairing (8 dim)
# vvvv=aa_da_box_tensor_product(dualization_of_AA(a_AA_b_r),main_DA)
# uu=d_aa_box_tensor_product(dualization_left_to_right_D(ContrE),vvvv)
# kh=a_d_box_tensor_product(uu,ContrE)
# # print homology_dim(kh)

# ## computing a curve
# d_contr=da_d_box_tensor_product(main_DA,ContrE)
# d_contr=left_d_randomly_cancel_until_possible(d_contr)
# d_contr.show()
# simpler_names_for_generators(d_contr)
# draw_D_bimodule(d_contr)

######################## curve for any tangle
# DA=da_da_box_tensor_many_efficient_cancelations(DA_new,DA_sigm2,DA_sigm2,DA_sigm2)
# F=da_d_box_tensor_product(DA, B_N_L0)
# F=left_d_randomly_cancel_until_possible(F)
# simpler_names_for_generators(F)

# A=aa_d_box_tensor_product(a_AA_b_r,Pretzel_2_3_long)
# A=left_a_randomly_cancel_until_possible(A)
# a_D=dd_a_box_tensor_product(DD_bar_r_dual,A)
# a_D=left_d_randomly_cancel_until_possible(a_D)
# simpler_names_for_generators(a_D)
# a_D.show()
# draw_D_bimodule(a_D)

####$$$$ khovanov homology for a knot
# A_b=d_aa_box_tensor_product(dualization_left_to_right_D(B_N_L1),a_AA_a(B_r)) 
# C=a_d_box_tensor_product(A_b,Pretzel_2_3_long)
# print homology_dim(C)
# Pretzel_2_3_long


######## new strategy for braid moves
# first thing
# AA1=aa_da_box_tensor_product(a_AA_b_r, DA_sigm2)
# AA1=aa_randomly_cancel_until_possible(AA1)
# DA1=dd_aa_box_tensor_product(DD_bar_r_dual,AA1)
# DA1=da_cancel_until_possible(DA1)
# DA1.show()

# second thing

#######
##################################################################################
##################################################################################
##################################################################################
########### finding bimodule associated to a braid move
# Dl0=B_N_L0
# Dl1=B_N_L1
# Dl2=B_N_L2
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
# #                 C.gen_by_name['01(p01⊗t)'],
# #                 C.gen_by_name['02(c0⊗x)'],
# #                 C.gen_by_name['12(l1⊗y)'],
# #                 C.gen_by_name['11(c1⊗t)'],
# #                 C.gen_by_name['11(l1⊗t)'],



# # ############################# comparing AA⊗DA with AA coming from C:
# # #### AA⊗DA
# A_B_r_A=a_AA_a(B_r)
# AA_sigm2=aa_da_box_tensor_product(A_B_r_A,DA_sigm2)
# AA_sigm2=aa_randomly_cancel_until_possible(AA_sigm2)
# AA_sigm2.show()

# # #### now compare AA_phi with the computed algebra C, and find the fact that they match.
# ##### below there relevant actions in the FUK
# # 01(p01⊗t) ⊗ 12(l1⊗y) ⊗ 22(c0) ⟶   02(c0⊗x)
# # 12(l1⊗y) ⊗ 20(l0) ⊗ 01(p01⊗t) ⟶   11(l1⊗t)
# # 22(c0) ⊗ 20(l0) ⊗ 01(p01⊗t) ⟶   21(c1)
# # 20(l0) ⊗ 00(c0) ⊗ 01(p01⊗t) ⟶   21(c1)
# # 12(l1⊗y) ⊗ 22(c0) ⊗ 20(l0) ⟶   10(q10)
# # 10(q10) ⊗ 01(p01⊗t) ⟶   11(c1⊗t)
# # 21(c1) ⊗ 12(l1⊗y) ⟶   22(c0)
# # 20(l0) ⊗ 02(c0⊗x) ⟶   22(c0)
# # 21(c1) ⊗ 11(l1⊗t) ⟶   21(c1)
# # 12(l1⊗y) ⊗ 21(c1) ⟶   11(c1⊗t)
# # 02(c0⊗x) ⊗ 20(l0) ⟶   00(c0)
# # 11(l1⊗t) ⊗ 10(q10) ⟶   10(q10)
# # 01(p01⊗t) ⊗ 10(q10) ⟶   00(c0)
