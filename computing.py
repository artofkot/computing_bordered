# -*- coding: utf-8 -*- 
from algebraic_structures.algebra import AttrDict, Generator, A
from algebraic_structures.da_bimodule import  Bunch_of_arrows, DA_bimodule,cancel_pure_differential, box_tensor,arrow_to_str
from algebraic_structures.da_bimodule import  randomly_cancel_until_possible, are_equal, cancel_this_number_of_times
from algebraic_structures.morphism import check_df_is_0, composition
from algebraic_structures.hochschild_homology import is_bounded, CH, homology_dim, ChainComplex
from visual import draw_DA_bimodule, draw_chain_complex

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
def init_ID3(A):
    gen_by_name=AttrDict({
                "x": Generator("x"),
                "y": Generator("y"),
                "z1": Generator("z1"),
                "z2": Generator("z2"),
                "w1": Generator("w1"),
                "w2": Generator("w2")
                })
    gen_by_name.x.add_idems(A.idem.i0,A.idem.i0)
    gen_by_name.y.add_idems(A.idem.i1,A.idem.i1)
    gen_by_name.z1.add_idems(A.idem.i0,A.idem.i1)
    gen_by_name.z2.add_idems(A.idem.i0,A.idem.i1)
    gen_by_name.w1.add_idems(A.idem.i1,A.idem.i0)
    gen_by_name.w2.add_idems(A.idem.i1,A.idem.i0)

    arrows=Bunch_of_arrows([
        (       gen_by_name.x,(),
                A.gen_by_name.r1,gen_by_name.w2
        ),
        (     gen_by_name.x,(A.gen_by_name.r3,),
                1,gen_by_name.z2
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
        ),



        (        gen_by_name.w1,(),
                1,gen_by_name.w2
        ),
        (        gen_by_name.w1,(A.gen_by_name.r12,),
                A.gen_by_name.r2,gen_by_name.x
        ),
        (        gen_by_name.w1,(A.gen_by_name.r1,),
                1,gen_by_name.y
        ),
        (        gen_by_name.w1,(A.gen_by_name.r123,),
                A.gen_by_name.r2,gen_by_name.z2
        )

        ])

    return DA_bimodule(gen_by_name,arrows,A,name="ID3")
def init_M_RHD(A):
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

    return DA_bimodule(gen_by_name,arrows,A,name="M_RHD")
def init_M_LHD(A):
    gen_by_name=AttrDict({
                "p": Generator("p"),
                "q": Generator("q"),
                "r": Generator("r")
                })
    gen_by_name.p.add_idems(A.idem.i0,A.idem.i0)
    gen_by_name.q.add_idems(A.idem.i1,A.idem.i1)
    gen_by_name.r.add_idems(A.idem.i1,A.idem.i0)

    arrows=Bunch_of_arrows([
        # from p
        (                         gen_by_name.p,(A.gen_by_name.r1,),
                A.gen_by_name.r1,gen_by_name.q),
        (                           gen_by_name.p,(A.gen_by_name.r123,),
                A.gen_by_name.r123,gen_by_name.q),
        (              gen_by_name.p,(A.gen_by_name.r123,A.gen_by_name.r2),
                A.gen_by_name.r12,gen_by_name.p),
        (              gen_by_name.p,(A.gen_by_name.r12,),
                A.gen_by_name.r1,gen_by_name.r),
        (              gen_by_name.p,(),
                A.gen_by_name.r3,gen_by_name.r),

        #from r
        (              gen_by_name.r,(A.gen_by_name.r3,A.gen_by_name.r2),
                A.gen_by_name.r2,gen_by_name.p),
        (              gen_by_name.r,(A.gen_by_name.r3,),
                A.gen_by_name.r23,gen_by_name.q),

        #from q
        (              gen_by_name.q,(A.gen_by_name.r2,),
                1,gen_by_name.r),
        (              gen_by_name.q,(A.gen_by_name.r23,),
                A.gen_by_name.r23,gen_by_name.q),
        (              gen_by_name.q,(A.gen_by_name.r23,A.gen_by_name.r2),
                A.gen_by_name.r2,gen_by_name.p),
    ])

    return DA_bimodule(gen_by_name,arrows,A,name="M_LHD")
def init_L_RHD(A):
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

    return DA_bimodule(gen_by_name,arrows,A,name="L_RHD")


# BIMODULES
ID1=init_ID1(A) 
ID2=init_ID2(A)
ID3=init_ID3(A)
M_RHD=init_M_RHD(A)
M_LHD=init_M_LHD(A)
L_RHD=init_L_RHD(A)

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
                1,M_RHD.gen_by_name.p),
        (                           ID1.gen_by_name.x,(),
                A.gen_by_name.r3,M_RHD.gen_by_name.r),
        (              ID1.gen_by_name.x,(A.gen_by_name.r12,),
                A.gen_by_name.r1,M_RHD.gen_by_name.r),
        (              ID1.gen_by_name.x,(A.gen_by_name.r123,),
                A.gen_by_name.r1,M_RHD.gen_by_name.q),
        # from y
        (              ID1.gen_by_name.y,(),
                1,M_RHD.gen_by_name.q),
        (              ID1.gen_by_name.y,(A.gen_by_name.r2,),
                1,M_RHD.gen_by_name.r),
        (              ID1.gen_by_name.y,(A.gen_by_name.r23,),
                1,M_RHD.gen_by_name.q)
    ])

# COMPUTATIONS

# F2_THETA=composition(F2,THETA,A)
# F2_THETA.show()
# check_df_is_0(ID2,M_RHD,F2_THETA)

# computation of CH gives different results for this!
X=box_tensor(ID2,L_RHD,M_RHD,ID3,ID3)
# draw_DA_bimodule(X)
# X.show()
C=CH(X)
# draw_chain_complex(C)
# C.show()
print "\ndim(HH)=" + str(homology_dim(C))

# C=ChainComplex([1,2,3,4],Bunch_of_arrows([(1,2),(2,3),(1,4),(4,3)]),'TEST')
# C.show()
# print "\ndim(H)=" + str(homology_dim(C))

