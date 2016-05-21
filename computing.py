# -*- coding: utf-8 -*- 
from algebraic_structures.algebra import AttrDict, Generator, A, g2_A
from algebraic_structures.da_bimodule import  Bunch_of_arrows, DA_bimodule,cancel_pure_differential, box_tensor,arrow_to_str
from algebraic_structures.da_bimodule import  randomly_cancel_until_possible, are_equal, cancel_this_number_of_times,box_tensor_efficient
from algebraic_structures.morphism import check_df_is_0, composition
from algebraic_structures.hochschild_homology import is_bounded, CH, homology_dim, ChainComplex, dimHH
from algebraic_structures.visual import draw_DA_bimodule, draw_chain_complex

from input_bimodules import ID1,ID2,ID3,M_RHD,M_LHD,L_RHD,L_LHD, g2_ID , g2_M_RHD, g2_M_LHD

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

########## COMPUTATIONS ##########

# F2_THETA=composition(F2,THETA,A)
# F2_THETA.show()
# check_df_is_0(ID2,M_RHD,F2_THETA)

########### Pseudo_Anosov mapping class
# X=box_tensor_efficient(L_RHD,M_LHD)
# X=box_tensor(ID3,X,ID3)
# print "\ndim(HH)=" + str(dimHH(X))


########### Boundary Dehn twist
# AB=box_tensor(M_RHD,L_RHD)
# BD=randomly_cancel_until_possible(box_tensor(AB,AB,AB))
# BD=randomly_cancel_until_possible(box_tensor(BD,BD))
# BD_bounded=box_tensor(ID3,BD,ID3)
# # draw_DA_bimodule(BD)
# print "\ndim(HH)=" + str(dimHH(BD_bounded))

########### Any
# X=box_tensor_efficient(L_RHD,M_LHD)
# X=box_tensor_efficient(X,X,X)
# X=box_tensor(ID3,X,ID3)
# HC=CH(X)
# HC.show()
# print is_bounded(X)
# print "\n2 BASEPOINT CASE(+1 added here)! dim(HH)=" + str(dimHH(X)+1)
# print "\ndim(HH)=" + str(dimHH(X))


##### New algebra computations
# g2_ID.show()
# g2_M_RHD.show()
g2_M_LHD.show()
