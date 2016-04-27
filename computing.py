# -*- coding: utf-8 -*- 
from algebraic_structures.algebra import AttrDict, Generator, A
from algebraic_structures.da_bimodule import  Bunch_of_arrows, DA_bimodule,cancel_pure_differential, box_tensor,arrow_to_str
from algebraic_structures.da_bimodule import  randomly_cancel_until_possible, are_equal, cancel_this_number_of_times
from algebraic_structures.morphism import check_df_is_0, composition
from algebraic_structures.hochschild_homology import is_bounded, CH, homology_dim, ChainComplex
from visual import draw_DA_bimodule, draw_chain_complex

from agebraic_structures.input_bimodules import ID1,ID2,ID3,M_RHD,M_LHD,L_RHD

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

X=box_tensor(ID2,L_RHD,M_RHD,ID3,ID3)
# draw_DA_bimodule(X)
C=CH(X)
# draw_chain_complex(C)
# C.show()
print "\ndim(HH)=" + str(homology_dim(C))

# C=ChainComplex([1,2,3,4],Bunch_of_arrows([(1,2),(2,3),(1,4),(4,3)]),'TEST')
# C.show()
# print "\ndim(H)=" + str(homology_dim(C))

