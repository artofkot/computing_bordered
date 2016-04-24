# -*- coding: utf-8 -*- 
from algebraic_structures.algebra import AttrDict, Generator, A
from algebraic_structures.da_bimodule import  Bunch_of_arrows, DA_bimodule,cancel_pure_differential, box_tensor_product,arrow_to_str
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




ID1=init_ID1(A) 
ID2=init_ID2(A)
M1=init_M1(A)


X=box_tensor_product(M1,ID2)
Y=box_tensor_product(X,ID2)

Y=randomly_cancel_until_possible(Y)
print are_equal(M1,Y)

# Y=cancel_pure_differential(X,(X.gen_by_name.r_z1,
#                                                     (),1,
#                                                     X.gen_by_name.r_z2))
# Y.show()
# Y.check()
