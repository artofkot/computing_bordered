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


##### experimenting
RA=Right_A_L8
RA.show()
# LA=dualization_right_to_left_A(Right_A_L7)
# D=dd_a_box_tensor_product(DD_bar_dual,LA)
# C=a_d_box_tensor_product(RA,D)
# C.show()
# homology_dim(C)
