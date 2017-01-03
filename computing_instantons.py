# -*- coding: utf-8 -*- 
from algebraic_structures.algebra import AttrDict, Generator, torus_A, g2_A, pil_A
from algebraic_structures.da_bimodule import  Bunch_of_arrows, DA_bimodule,cancel_pure_differential
from algebraic_structures.da_bimodule import  randomly_cancel_until_possible, are_equal_smart, cancel_this_number_of_times
from algebraic_structures.tensoring import box_tensor_efficient, box_tensor, box_tensor_product

from algebraic_structures.morphism import check_df_is_0, composition
from algebraic_structures.hochschild_homology import is_bounded, CH, homology_dim, ChainComplex, dimHH
from algebraic_structures.visual import draw_DA_bimodule, draw_chain_complex

from input_instanton_modules import paths, DD_dual_bar

from itertools import permutations
import os

###

pil_A.show()
DD_dual_bar.show()