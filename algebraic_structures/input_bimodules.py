# -*- coding: utf-8 -*- 
from algebra import AttrDict, Generator, A
from da_bimodule import  Bunch_of_arrows, DA_bimodule,cancel_pure_differential, box_tensor,arrow_to_str
from da_bimodule import  randomly_cancel_until_possible, are_equal, cancel_this_number_of_times
from morphism import check_df_is_0, composition
from hochschild_homology import is_bounded, CH, homology_dim, ChainComplex

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
