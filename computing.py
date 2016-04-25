# -*- coding: utf-8 -*- 
from algebraic_structures.algebra import AttrDict, Generator, A
from algebraic_structures.da_bimodule import  Bunch_of_arrows, DA_bimodule,cancel_pure_differential, box_tensor,arrow_to_str
from algebraic_structures.da_bimodule import  randomly_cancel_until_possible, are_equal
from algebraic_structures.morphism import check_df_is_0, composition

def init_ID1(A):
    gen_by_name=AttrDict({
                "x": Generator("x"),
                "y": Generator("y")
                })
    gen_by_name.x.add_idems(A.idem.i0,A.idem.i0)
    gen_by_name.y.add_idems(A.idem.i1,A.idem.i1)

    arrows=Bunch_of_arrows([
        (              gen_by_name.x,(A.gen_by_name.r12,),
                A.gen_by_name.r12,gen_by_name.x),

        (              gen_by_name.y,(A.gen_by_name.r23,),
                A.gen_by_name.r23,gen_by_name.y),

        (              gen_by_name.x,(A.gen_by_name.r1,),
                A.gen_by_name.r1,gen_by_name.y),

        (              gen_by_name.y,(A.gen_by_name.r2,),
                A.gen_by_name.r2,gen_by_name.x),

        (              gen_by_name.x,(A.gen_by_name.r123,),
                A.gen_by_name.r123,gen_by_name.y),

        (              gen_by_name.x,(A.gen_by_name.r3,),
                A.gen_by_name.r3,gen_by_name.y)])

    return DA_bimodule(gen_by_name,arrows,A,name="ID1")
def init_ID2(A):
    gen_by_name=AttrDict({
                "x": Generator("x"),
                "y": Generator("y"),
                "z1": Generator("z1"),
                "z2": Generator("z2")
                })
    gen_by_name.x.add_idems(A.idem.i0,A.idem.i0)
    gen_by_name.y.add_idems(A.idem.i1,A.idem.i1)
    gen_by_name.z1.add_idems(A.idem.i0,A.idem.i1)
    gen_by_name.z2.add_idems(A.idem.i0,A.idem.i1)

    arrows=Bunch_of_arrows([
        (       gen_by_name.x,(A.gen_by_name.r12,),
                A.gen_by_name.r12,gen_by_name.x
        ),

        (     gen_by_name.x,(A.gen_by_name.r3,),
                1,gen_by_name.z2
        ),

        (       gen_by_name.x,(A.gen_by_name.r123,),
                A.gen_by_name.r12,gen_by_name.z2
        ),

        (                                       
            gen_by_name.x,(A.gen_by_name.r1,),
            A.gen_by_name.r1,gen_by_name.y
        ),

        (        gen_by_name.y,(A.gen_by_name.r2,),
                A.gen_by_name.r2,gen_by_name.x
        ),
        

        (        gen_by_name.y,(A.gen_by_name.r23,),
                A.gen_by_name.r2,gen_by_name.z2
        ),

        (        gen_by_name.z1,(),
                1,gen_by_name.z2
        ),

        (        gen_by_name.z1,(),
                A.gen_by_name.r3,gen_by_name.y
        )

        ])

    return DA_bimodule(gen_by_name,arrows,A,name="ID2")
def init_M1(A):
    gen_by_name=AttrDict({
                "p": Generator("p"),
                "q": Generator("q"),
                "r": Generator("r")
                })
    gen_by_name.p.add_idems(A.idem.i0,A.idem.i0)
    gen_by_name.q.add_idems(A.idem.i1,A.idem.i1)
    gen_by_name.r.add_idems(A.idem.i1,A.idem.i0)

    arrows=Bunch_of_arrows([
        # from p to q
        (                         gen_by_name.p,(A.gen_by_name.r1,),
                A.gen_by_name.r1,gen_by_name.q),
        (                           gen_by_name.p,(A.gen_by_name.r123,),
                A.gen_by_name.r123,gen_by_name.q),
        (              gen_by_name.p,(A.gen_by_name.r3,A.gen_by_name.r23),
                A.gen_by_name.r3,gen_by_name.q),

        # from p to r 
        (              gen_by_name.p,(A.gen_by_name.r12,),
                A.gen_by_name.r123,gen_by_name.r),
        (              gen_by_name.p,(A.gen_by_name.r3,A.gen_by_name.r2),
                A.gen_by_name.r3,gen_by_name.r),

        #from r to p
        (              gen_by_name.r,(),
                A.gen_by_name.r2,gen_by_name.p),

        #from r to q
        (              gen_by_name.r,(A.gen_by_name.r3,),
                1,gen_by_name.q),

        #from q to r
        (              gen_by_name.q,(A.gen_by_name.r2,),
                A.gen_by_name.r23,gen_by_name.r),

        #from q to q
        (              gen_by_name.q,(A.gen_by_name.r23,),
                A.gen_by_name.r23,gen_by_name.q)
    ])

    return DA_bimodule(gen_by_name,arrows,A,name="M1")
def init_L1(A):
    gen_by_name=AttrDict({
                "p": Generator("p"),
                "q": Generator("q"),
                "s": Generator("s")
                })
    gen_by_name.p.add_idems(A.idem.i0,A.idem.i0)
    gen_by_name.q.add_idems(A.idem.i1,A.idem.i1)
    gen_by_name.s.add_idems(A.idem.i0,A.idem.i1)

    arrows=Bunch_of_arrows([
        # from p to q
        (                         gen_by_name.q,(A.gen_by_name.r2,A.gen_by_name.r123),
                A.gen_by_name.r23,gen_by_name.q),
        (                           gen_by_name.q,(A.gen_by_name.r2,A.gen_by_name.r12),
                A.gen_by_name.r2,gen_by_name.p),
        (              gen_by_name.q,(A.gen_by_name.r2,A.gen_by_name.r1),
                A.gen_by_name.r2,gen_by_name.s),

        # from p to r 
        (              gen_by_name.s,(A.gen_by_name.r2,),
                1,gen_by_name.p),
        (              gen_by_name.s,(A.gen_by_name.r23,),
                A.gen_by_name.r3,gen_by_name.q),
        (              gen_by_name.s,(),
                A.gen_by_name.r1,gen_by_name.q),

        #from r to p
        (              gen_by_name.p,(A.gen_by_name.r123,),
                A.gen_by_name.r123,gen_by_name.q),

        #from r to q
        (              gen_by_name.p,(A.gen_by_name.r3,),
                A.gen_by_name.r3,gen_by_name.q),

        #from q to r
        (              gen_by_name.p,(A.gen_by_name.r1,),
                A.gen_by_name.r12,gen_by_name.s),

        #from q to q
        (              gen_by_name.p,(A.gen_by_name.r12,),
                A.gen_by_name.r12,gen_by_name.p)
    ])

    return DA_bimodule(gen_by_name,arrows,A,name="L1")



# BIMODULES
ID1=init_ID1(A) 
ID2=init_ID2(A)
M1=init_M1(A)
L1=init_L1(A)

# MORPHISMS
F2=Bunch_of_arrows([
        # from x
        (                         ID2.gen_by_name.x,(),
                1,ID1.gen_by_name.x),
        (                           ID2.gen_by_name.y,(),
                1,ID1.gen_by_name.y),
        (              ID2.gen_by_name.z2,(),
                A.gen_by_name.r3,ID1.gen_by_name.y)
    ])
#morphism from Tova's paper
THETA=Bunch_of_arrows([
        # from x
        (                         ID1.gen_by_name.x,(),
                1,M1.gen_by_name.p),
        (                           ID1.gen_by_name.x,(),
                A.gen_by_name.r3,M1.gen_by_name.r),
        (              ID1.gen_by_name.x,(A.gen_by_name.r12,),
                A.gen_by_name.r1,M1.gen_by_name.r),
        (              ID1.gen_by_name.x,(A.gen_by_name.r123,),
                A.gen_by_name.r1,M1.gen_by_name.q),
        # from y
        (              ID1.gen_by_name.y,(),
                1,M1.gen_by_name.q),
        (              ID1.gen_by_name.y,(A.gen_by_name.r2,),
                1,M1.gen_by_name.r),
        (              ID1.gen_by_name.y,(A.gen_by_name.r23,),
                1,M1.gen_by_name.q)
    ])

# COMPUTATIONS

# F2_THETA=composition(F2,THETA,A)
# F2_THETA.show()
# check_df_is_0(ID2,M1,F2_THETA)

N=box_tensor(M1,L1)
N=randomly_cancel_until_possible(N)
N.show()
N.check()