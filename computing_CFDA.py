# -*- coding: utf-8 -*- 
from algebraic_structures.algebra import AttrDict, Generator, torus_A, g2_A
from algebraic_structures.da_bimodule import  Bunch_of_arrows, DA_bimodule,cancel_pure_differential, da_arrow_to_str
from algebraic_structures.da_bimodule import  randomly_cancel_until_possible, are_equal_smart, cancel_this_number_of_times
from algebraic_structures.tensoring import box_tensor_efficient, box_tensor, box_tensor_product
from algebraic_structures.morphism import check_df_is_0, composition
from algebraic_structures.hochschild_homology import is_bounded, CH, homology_dim, ChainComplex, dimHH
from algebraic_structures.visual import draw_DA_bimodule, draw_chain_complex

from input_DA_bimodules import ID1,ID2,ID3,M_RHD,M_LHD,L_RHD,L_LHD  
from input_DA_bimodules import g2_ID, g2_ID_bounded, g2_M_RHD, g2_M_LHD, g2_L_RHD,g2_L_LHD, g2_K_LHD, g2_K_RHD, g2_N_LHD, g2_N_RHD
from input_DA_bimodules import g2_T_RHD, g2_T_LHD

from itertools import permutations
import os

# MORPHISMS
F2=Bunch_of_arrows([
        # from x
        (                         ID2.gen_by_name.x,(),
                1,ID1.gen_by_name.x),
        (                           ID2.gen_by_name.y,(),
                1,ID1.gen_by_name.y),
        (              ID2.gen_by_name.z2,(),
                torus_A.gen_by_name.r3,ID1.gen_by_name.y)
    ])
#morphism from Tova's paper
THETA=Bunch_of_arrows([
        # from x
        (                         ID1.gen_by_name.x,(),
                1,M_RHD.gen_by_name.p),
        (                           ID1.gen_by_name.x,(),
                torus_A.gen_by_name.r3,M_RHD.gen_by_name.r),
        (              ID1.gen_by_name.x,(torus_A.gen_by_name.r12,),
                torus_A.gen_by_name.r1,M_RHD.gen_by_name.r),
        (              ID1.gen_by_name.x,(torus_A.gen_by_name.r123,),
                torus_A.gen_by_name.r1,M_RHD.gen_by_name.q),
        # from y
        (              ID1.gen_by_name.y,(),
                1,M_RHD.gen_by_name.q),
        (              ID1.gen_by_name.y,(torus_A.gen_by_name.r2,),
                1,M_RHD.gen_by_name.r),
        (              ID1.gen_by_name.y,(torus_A.gen_by_name.r23,),
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


##### genus two algebra computations 
# Bimodules: 
# g2_ID, g2_ID_bounded
# g2_K_RHD,g2_K_LHD
# g2_N_RHD,g2_N_LHD
# g2_T_RHD,g2_T_LHD
# g2_M_RHD,g2_M_LHD
# g2_L_RHD,g2_L_LHD

A_=g2_K_RHD
B_=g2_N_RHD
C_=g2_T_RHD
D_=g2_L_RHD
E_=g2_M_RHD
A_inv=g2_K_LHD
B_inv=g2_N_LHD
C_inv=g2_T_LHD
D_inv=g2_L_LHD
E_inv=g2_M_LHD

##### checking relations
# X=box_tensor_efficient(B_,C_,B_)
# Y=box_tensor_efficient(C_,B_,C_)
# X.show()
# Y.show_short()
# print are_equal_smart(X,Y)

##### computing HH
X=box_tensor_efficient(A_inv,A_inv,A_inv,A_inv,A_inv,B_inv,C_inv,D_inv,E_inv,E_inv,E_inv,E_inv,E_inv)
X=box_tensor_efficient(X)
X=box_tensor(g2_ID_bounded,X,g2_ID_bounded)
# X.show_short()
print "\ndim(HH)=" + str(dimHH(X))
# HC=CH(X)
# HC.show()

##### experiment, that shows that order of elements in the product matters for HH
##### (cyclic order doesnt matter due to conjugation invariance)
# a=[A_,B_,C_,A_,B_,C_]
# perms=permutations(a,len(a))
# for perm in perms:
#     X=g2_ID
#     for bim in perm:
#         X=box_tensor_efficient(X,bim)
#     X=box_tensor(g2_ID_bounded,X,g2_ID_bounded)
#     print "\ndim(HH)=" + str(dimHH(X))

##### experiment, that doesn't show dependence on substituting RHD by LHD
# a=[(A_,A_inv),(B_,B_inv),(C_,C_inv),(A_,A_inv),(B_,B_inv)]
# perms=permutations(a,len(a))
# for perm in perms:
#     X1=g2_ID
#     X2=g2_ID
#     for bim in perm:
#         X1=box_tensor_efficient(X1,bim[0])
#         X2=box_tensor_efficient(X2,bim[1])
#     X1=box_tensor(g2_ID_bounded,X1,g2_ID_bounded)
#     X2=box_tensor(g2_ID_bounded,X2,g2_ID_bounded)
#     print "\ndim(HH)=" + str(dimHH(X1)),
#     print " dim(HH)=" + str(dimHH(X2))

##### experiment, where one computes possible ranks
# a=[A_,A_inv,B_,B_inv,C_,C_inv,A_,A_inv,B_,B_inv]
# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             for l in range(10):
#                 X=box_tensor_efficient(a[i],a[j],a[k],a[l])
#                 X=box_tensor(g2_ID_bounded,X,g2_ID_bounded)
#                 BINGO=dimHH(X)
#                 if BINGO==0: 
#                     print 'YEAHEAYEAYEAYHEAHAEYEAYAEEHA'
#                     os._exit(1)
#                 print "\ndim(HH)=" + str(BINGO)




