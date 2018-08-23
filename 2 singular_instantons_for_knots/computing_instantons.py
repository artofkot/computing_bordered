# -*- coding: utf-8 -*- 
import sys
sys.path.append('../')

from algebraic_structures.dualization import dualization_right_to_left_A
from algebraic_structures.algebra import pil_A
from algebraic_structures.specific_algebras_modules_bimodules import *
from input_instanton_modules import DD_bar_dual, Right_A_L0, Right_A_test
from input_instanton_modules import (
    Left_D_test,Left_A_test,DD_test, 
    Right_A_L6, Right_A_L7, Right_A_R4,
    Right_A_L37, Right_A_L3, Right_A_L0,
    Right_A_L8, Right_A_L9, Right_A_R0,
    Right_A_R00, Right_A_LU,Right_A_R1,Right_A_R2,Right_A_R3,
     Right_A_LT23 )
from algebraic_structures.tensoring import a_d_box_tensor_product,dd_a_box_tensor_product
from algebraic_structures.chain_complex import homology_dim
from algebraic_structures.dd_bimodule import dd_randomly_cancel_until_possible


DD=DD_bar_r_dual

##### experimenting HF(L0,R4)
RA=Right_A_L9
RA.show()
LA=dualization_right_to_left_A(Right_A_L0)
LA.show()
D=dd_a_box_tensor_product(DD,LA)
C=a_d_box_tensor_product(RA,D)
C.show()
homology_dim(C)

# DD.show_for_tex()

##### two arcs HF(R0,R00)=HF(R0, perturbed(R00))
# RA=Right_A_R00
# RA.show()
# LA=dualization_right_to_left_A(Right_A_R0)
# D=dd_a_box_tensor_product(DD,LA)
# C=a_d_box_tensor_product(RA,D)
# C.show()
# homology_dim(C)