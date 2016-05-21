# -*- coding: utf-8 -*- 
from algebraic_structures.algebra import AttrDict, Generator, A, g2_A
from algebraic_structures.da_bimodule import  Bunch_of_arrows, DA_bimodule,cancel_pure_differential, box_tensor,arrow_to_str
from algebraic_structures.da_bimodule import  randomly_cancel_until_possible, are_equal, cancel_this_number_of_times
from algebraic_structures.morphism import check_df_is_0, composition
from algebraic_structures.hochschild_homology import is_bounded, CH, homology_dim, ChainComplex


 

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

def init_L_LHD(A):
    gen_by_name=AttrDict({
                "p": Generator("p"),
                "q": Generator("q"),
                "s": Generator("s")
                })
    gen_by_name.p.add_idems(A.idem.i0,A.idem.i0)
    gen_by_name.q.add_idems(A.idem.i1,A.idem.i1)
    gen_by_name.s.add_idems(A.idem.i0,A.idem.i1)

    arrows=Bunch_of_arrows([
        # from q
        (                         gen_by_name.q,(),
                A.gen_by_name.r2,gen_by_name.s),
        #from s
        (              gen_by_name.s,(A.gen_by_name.r2,),
                A.gen_by_name.r12,gen_by_name.p),
        (              gen_by_name.s,(A.gen_by_name.r23,),
                A.gen_by_name.r123,gen_by_name.q),
        (              gen_by_name.s,(A.gen_by_name.r2,A.gen_by_name.r1),
                A.gen_by_name.r1,gen_by_name.q),

        #from p
        (              gen_by_name.p,(A.gen_by_name.r1,),
                1,gen_by_name.s),
        (              gen_by_name.p,(A.gen_by_name.r123,),
                A.gen_by_name.r123,gen_by_name.q),
        (              gen_by_name.p,(A.gen_by_name.r3,),
                A.gen_by_name.r3,gen_by_name.q),
        (              gen_by_name.p,(A.gen_by_name.r12,A.gen_by_name.r1),
                A.gen_by_name.r1,gen_by_name.q),
        (              gen_by_name.p,(A.gen_by_name.r12,),
                A.gen_by_name.r12,gen_by_name.p)
    ])

    return DA_bimodule(gen_by_name,arrows,A,name="L_LHD")












# genus 2 bimodules:

def init_g2_ID(g2_A):
    gen_by_name=AttrDict({
                "x0": Generator("x0"),
                "x1": Generator("x1"),
                "x2": Generator("x2"),
                "x3": Generator("x3")
                })
    gen_by_name.x0.add_idems(g2_A.idem.i0,g2_A.idem.i0)
    gen_by_name.x1.add_idems(g2_A.idem.i1,g2_A.idem.i1)
    gen_by_name.x2.add_idems(g2_A.idem.i2,g2_A.idem.i2)
    gen_by_name.x3.add_idems(g2_A.idem.i3,g2_A.idem.i3)

    #this is for convenience
    idem_to_gens={g2_A.idem.i0:gen_by_name.x0,
                    g2_A.idem.i1:gen_by_name.x1,
                    g2_A.idem.i2:gen_by_name.x2,
                    g2_A.idem.i3:gen_by_name.x3}

    #initializing all actions
    arrows=Bunch_of_arrows()
    for algebra_element in (set(g2_A.genset) - set(g2_A.idemset)):
        gen_in=idem_to_gens[algebra_element.idem.left]
        gen_out=idem_to_gens[algebra_element.idem.right]
        
        arrows[(gen_in,(algebra_element,),
                algebra_element,gen_out)]+=1

    return DA_bimodule(gen_by_name,arrows,g2_A,name="g2_ID")

def init_g2_M_RHD(g2_A):
    gen_by_name=AttrDict({
                "x0": Generator("x0"),
                "x1": Generator("x1"),
                "x2": Generator("x2"),
                "x3": Generator("x3"),
                "r":Generator("r")
                })
    gen_by_name.x0.add_idems(g2_A.idem.i0,g2_A.idem.i0)
    gen_by_name.x1.add_idems(g2_A.idem.i1,g2_A.idem.i1)
    gen_by_name.x2.add_idems(g2_A.idem.i2,g2_A.idem.i2)
    gen_by_name.x3.add_idems(g2_A.idem.i3,g2_A.idem.i3)
    gen_by_name.r.add_idems(g2_A.idem.i1,g2_A.idem.i0)

    arrows=Bunch_of_arrows([
        (              gen_by_name.x2,(g2_A.gen_by_name.r56,),
                g2_A.gen_by_name.r56,gen_by_name.x2),

        (              gen_by_name.x3,(g2_A.gen_by_name.r67,),
                g2_A.gen_by_name.r67,gen_by_name.x3),

        (              gen_by_name.x2,(g2_A.gen_by_name.r5,),
                g2_A.gen_by_name.r5,gen_by_name.x3),

        (              gen_by_name.x3,(g2_A.gen_by_name.r6,),
                g2_A.gen_by_name.r6,gen_by_name.x2),

        (              gen_by_name.x2,(g2_A.gen_by_name.r567,),
                g2_A.gen_by_name.r567,gen_by_name.x3),

        (              gen_by_name.x2,(g2_A.gen_by_name.r7,),
                g2_A.gen_by_name.r7,gen_by_name.x3),

        # from x0
        (                         gen_by_name.x0,(g2_A.gen_by_name.r1,),
                g2_A.gen_by_name.r1,gen_by_name.x1),
        (                           gen_by_name.x0,(g2_A.gen_by_name.r123,),
                g2_A.gen_by_name.r123,gen_by_name.x1),
        (              gen_by_name.x0,(g2_A.gen_by_name.r3,g2_A.gen_by_name.r23),
                g2_A.gen_by_name.r3,gen_by_name.x1),
        (              gen_by_name.x0,(g2_A.gen_by_name.r12,),
                g2_A.gen_by_name.r123,gen_by_name.r),
        (              gen_by_name.x0,(g2_A.gen_by_name.r3,g2_A.gen_by_name.r2),
                g2_A.gen_by_name.r3,gen_by_name.r),

        (              gen_by_name.x0,(g2_A.gen_by_name.r3,g2_A.gen_by_name.r2345),
                g2_A.gen_by_name.r345,gen_by_name.x3),
        (              gen_by_name.x0,(g2_A.gen_by_name.r12345,),
                g2_A.gen_by_name.r12345,gen_by_name.x3),
        (              gen_by_name.x0,(g2_A.gen_by_name.r1234567,),
                g2_A.gen_by_name.r1234567,gen_by_name.x3),
        (              gen_by_name.x0,(g2_A.gen_by_name.r3,g2_A.gen_by_name.r234567),
                g2_A.gen_by_name.r34567,gen_by_name.x3),

        (              gen_by_name.x0,(g2_A.gen_by_name.r3,g2_A.gen_by_name.r234),
                g2_A.gen_by_name.r34,gen_by_name.x2),
        (              gen_by_name.x0,(g2_A.gen_by_name.r1234,),
                g2_A.gen_by_name.r1234,gen_by_name.x2),
        (              gen_by_name.x0,(g2_A.gen_by_name.r123456,),
                g2_A.gen_by_name.r123456,gen_by_name.x2),
        (              gen_by_name.x0,(g2_A.gen_by_name.r3,g2_A.gen_by_name.r23456),
                g2_A.gen_by_name.r3456,gen_by_name.x2),



        #from r
        (              gen_by_name.r,(),
                g2_A.gen_by_name.r2,gen_by_name.x0),
        (              gen_by_name.r,(g2_A.gen_by_name.r3,),
                1,gen_by_name.x1),
        (              gen_by_name.r,(g2_A.gen_by_name.r34,),
                g2_A.gen_by_name.r4,gen_by_name.x2),
        (              gen_by_name.r,(g2_A.gen_by_name.r3456,),
                g2_A.gen_by_name.r456,gen_by_name.x2),
        (              gen_by_name.r,(g2_A.gen_by_name.r345,),
                g2_A.gen_by_name.r45,gen_by_name.x3),
        (              gen_by_name.r,(g2_A.gen_by_name.r34567,),
                g2_A.gen_by_name.r4567,gen_by_name.x3),

        #from x1
        (              gen_by_name.x1,(g2_A.gen_by_name.r2,),
                g2_A.gen_by_name.r23,gen_by_name.r),
        (              gen_by_name.x1,(g2_A.gen_by_name.r23,),
                g2_A.gen_by_name.r23,gen_by_name.x1),
        (              gen_by_name.x1,(g2_A.gen_by_name.r45,),
                g2_A.gen_by_name.r45,gen_by_name.x3),
        (              gen_by_name.x1,(g2_A.gen_by_name.r4567,),
                g2_A.gen_by_name.r4567,gen_by_name.x3),
        (              gen_by_name.x1,(g2_A.gen_by_name.r2345,),
                g2_A.gen_by_name.r2345,gen_by_name.x3),
        (              gen_by_name.x1,(g2_A.gen_by_name.r234567,),
                g2_A.gen_by_name.r234567,gen_by_name.x3),
        (              gen_by_name.x1,(g2_A.gen_by_name.r4,),
                g2_A.gen_by_name.r4,gen_by_name.x2),
        (              gen_by_name.x1,(g2_A.gen_by_name.r456,),
                g2_A.gen_by_name.r456,gen_by_name.x2),

        (              gen_by_name.x1,(g2_A.gen_by_name.r23456,),
                g2_A.gen_by_name.r23456,gen_by_name.x2),

        (              gen_by_name.x1,(g2_A.gen_by_name.r234,),
                g2_A.gen_by_name.r234,gen_by_name.x2)



        ])

    return DA_bimodule(gen_by_name,arrows,g2_A,name="g2_M_RHD")

def init_g2_M_LHD(g2_A):
    gen_by_name=AttrDict({
                "x0": Generator("x0"),
                "x1": Generator("x1"),
                "x2": Generator("x2"),
                "x3": Generator("x3"),
                "r":Generator("r")
                })
    gen_by_name.x0.add_idems(g2_A.idem.i0,g2_A.idem.i0)
    gen_by_name.x1.add_idems(g2_A.idem.i1,g2_A.idem.i1)
    gen_by_name.x2.add_idems(g2_A.idem.i2,g2_A.idem.i2)
    gen_by_name.x3.add_idems(g2_A.idem.i3,g2_A.idem.i3)
    gen_by_name.r.add_idems(g2_A.idem.i1,g2_A.idem.i0)

    arrows=Bunch_of_arrows([
        (              gen_by_name.x2,(g2_A.gen_by_name.r56,),
                g2_A.gen_by_name.r56,gen_by_name.x2),

        (              gen_by_name.x3,(g2_A.gen_by_name.r67,),
                g2_A.gen_by_name.r67,gen_by_name.x3),

        (              gen_by_name.x2,(g2_A.gen_by_name.r5,),
                g2_A.gen_by_name.r5,gen_by_name.x3),

        (              gen_by_name.x3,(g2_A.gen_by_name.r6,),
                g2_A.gen_by_name.r6,gen_by_name.x2),

        (              gen_by_name.x2,(g2_A.gen_by_name.r567,),
                g2_A.gen_by_name.r567,gen_by_name.x3),

        (              gen_by_name.x2,(g2_A.gen_by_name.r7,),
                g2_A.gen_by_name.r7,gen_by_name.x3),

        # from x0
        (                         gen_by_name.x0,(g2_A.gen_by_name.r1,),
                g2_A.gen_by_name.r1,gen_by_name.x1),
        (                           gen_by_name.x0,(g2_A.gen_by_name.r123,),
                g2_A.gen_by_name.r123,gen_by_name.x1),
        (              gen_by_name.x0,(),
                g2_A.gen_by_name.r3,gen_by_name.r),
        (              gen_by_name.x0,(g2_A.gen_by_name.r12,),
                g2_A.gen_by_name.r1,gen_by_name.r),
        (              gen_by_name.x0,(g2_A.gen_by_name.r123,g2_A.gen_by_name.r2),
                g2_A.gen_by_name.r12,gen_by_name.x0),

        (              gen_by_name.x0,(g2_A.gen_by_name.r12345,),
                g2_A.gen_by_name.r12345,gen_by_name.x3),
        (              gen_by_name.x0,(g2_A.gen_by_name.r1234567,),
                g2_A.gen_by_name.r1234567,gen_by_name.x3),

        (              gen_by_name.x0,(g2_A.gen_by_name.r1234,),
                g2_A.gen_by_name.r1234,gen_by_name.x2),
        (              gen_by_name.x0,(g2_A.gen_by_name.r123456,),
                g2_A.gen_by_name.r123456,gen_by_name.x2),


        #from x1
        (              gen_by_name.x1,(g2_A.gen_by_name.r2,),
                1,gen_by_name.r),
        (              gen_by_name.x1,(g2_A.gen_by_name.r23,),
                g2_A.gen_by_name.r23,gen_by_name.x1),
        (              gen_by_name.x1,(g2_A.gen_by_name.r23,g2_A.gen_by_name.r2),
                g2_A.gen_by_name.r2,gen_by_name.x0),

        (              gen_by_name.x1,(g2_A.gen_by_name.r45,),
                g2_A.gen_by_name.r45,gen_by_name.x3),
        (              gen_by_name.x1,(g2_A.gen_by_name.r4567,),
                g2_A.gen_by_name.r4567,gen_by_name.x3),
        (              gen_by_name.x1,(g2_A.gen_by_name.r2345,),
                g2_A.gen_by_name.r2345,gen_by_name.x3),
        (              gen_by_name.x1,(g2_A.gen_by_name.r234567,),
                g2_A.gen_by_name.r234567,gen_by_name.x3),

        (              gen_by_name.x1,(g2_A.gen_by_name.r4,),
                g2_A.gen_by_name.r4,gen_by_name.x2),
        (              gen_by_name.x1,(g2_A.gen_by_name.r456,),
                g2_A.gen_by_name.r456,gen_by_name.x2),

        (              gen_by_name.x1,(g2_A.gen_by_name.r23456,),
                g2_A.gen_by_name.r23456,gen_by_name.x2),

        (              gen_by_name.x1,(g2_A.gen_by_name.r234,),
                g2_A.gen_by_name.r234,gen_by_name.x2),

        #from r
        (              gen_by_name.r,(g2_A.gen_by_name.r3,g2_A.gen_by_name.r2),
                g2_A.gen_by_name.r2,gen_by_name.x0),
        (              gen_by_name.r,(g2_A.gen_by_name.r3,),
                g2_A.gen_by_name.r23,gen_by_name.x1),

        (              gen_by_name.r,(g2_A.gen_by_name.r34,),
                g2_A.gen_by_name.r234,gen_by_name.x2),
        (              gen_by_name.r,(g2_A.gen_by_name.r3456,),
                g2_A.gen_by_name.r23456,gen_by_name.x2),

        (              gen_by_name.r,(g2_A.gen_by_name.r345,),
                g2_A.gen_by_name.r2345,gen_by_name.x3),
        (              gen_by_name.r,(g2_A.gen_by_name.r34567,),
                g2_A.gen_by_name.r234567,gen_by_name.x3)



        ])

    return DA_bimodule(gen_by_name,arrows,g2_A,name="g2_M_RHD")


g2_M_LHD

# BIMODULES
ID1=init_ID1(A) 
ID2=init_ID2(A)
ID3=init_ID3(A)
M_RHD=init_M_RHD(A)
M_LHD=init_M_LHD(A)
L_RHD=init_L_RHD(A)
L_LHD=init_L_LHD(A)

g2_ID=init_g2_ID(g2_A)
g2_M_RHD=init_g2_M_RHD(g2_A)
g2_M_LHD=init_g2_M_LHD(g2_A)

