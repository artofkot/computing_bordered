# -*- coding: utf-8 -*- 
import sys
sys.path.append('../')

from algebraic_structures.dualization import dualization_right_to_left_A
from algebraic_structures.algebra import pil_A
from input_instanton_modules import DD_bar_dual, Right_A_L0, Right_A_test
from input_instanton_modules import (
    Left_D_test,Left_A_test,DD_test, 
    Right_A_L6, Right_A_L7, Right_A_L1,
    Right_A_L2, Right_A_L3, Right_A_L0)
from algebraic_structures.tensoring import a_d_box_tensor_product,dd_a_box_tensor_product
from algebraic_structures.chain_complex import homology_dim

##### algebra, and all modules
# pil_A.show()
# DD_bar_dual.show()
# Right_A_L0.show()
# Left_A_L0_dual.show()
# Left_D_test.show()
# Left_A_test.show()

##### testing A⊠D=Chain_complex
# Right_A_test.show()
# Left_D_test.show()
# C=a_d_box_tensor_product(Right_A_test,Left_D_test)
# C.show()
# homology_dim(C)

##### testing DD⊠Left_A=Left_D
# DD_test.show()
# Left_A_test.show()
# D=dd_a_box_tensor_product(DD_test,Left_A_test)
# D.show()

##### experimenting
RA=Right_A_L7
LA=dualization_right_to_left_A(Right_A_L7)
D=dd_a_box_tensor_product(DD_bar_dual,LA)
C=a_d_box_tensor_product(RA,D)
C.show()
homology_dim(C)

##### computations from the paper
# leftD_to_pair_with=dd_a_box_tensor_product(DD_bar_dual,dualization_right_to_left_A(Right_A_L0))
# C=a_d_box_tensor_product(Right_A_L1,leftD_to_pair_with)
# homology_dim(C)
