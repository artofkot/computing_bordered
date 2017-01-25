# -*- coding: utf-8 -*- 
import sys
sys.path.append('../../')
sys.path.append('../')

from algebraic_structures.algebra import torus_A

from input_DA_bimodules import (
    ID1,g2_M_RHD,g2_ID) 

from algebraic_structures.basics import (
    AttrDict, Generator, Bunch_of_arrows)

from algebraic_structures.dd_bimodule import (
    DD_bimodule,are_equal_smart_dd)

from algebraic_structures.da_bimodule import (
    da_randomly_cancel_until_possible,
    are_equal_smart_da)

from algebraic_structures.aa_bimodule import (
    AA_bimodule, a_A_a,
    aa_randomly_cancel_until_possible)

from algebraic_structures.dualization import (
    dualization_of_DD, dualization_of_AA)

from algebraic_structures.tensoring import (
 dd_aa_box_tensor_product,
 aa_da_box_tensor_product,
 da_dd_box_tensor_product )

###### genus=2. First, for split pointed matched circle, which we denote by pmc1
from algebras_from_Bohua_program import A_pmc1_str1,A_pmc1_str3
def init_DD_pmc1(A_pmc1_str1,A_pmc1_str3):
    gen_by_name=AttrDict({
            "x0": Generator("x0"),
            "x1": Generator("x1"),
            "x2": Generator("x2"),
            "x3": Generator("x3"),
            })

    gen_by_name.x0.add_idems(A_pmc1_str1.idem_by_name.i0,A_pmc1_str3.idem_by_name['|(1, 3),(4, 6),(5, 7)|'] )
    gen_by_name.x1.add_idems(A_pmc1_str1.idem_by_name.i1,A_pmc1_str3.idem_by_name['|(0, 2),(4, 6),(5, 7)|'])
    gen_by_name.x2.add_idems(A_pmc1_str1.idem_by_name.i2,A_pmc1_str3.idem_by_name['|(0, 2),(1, 3),(5, 7)|'] )
    gen_by_name.x3.add_idems(A_pmc1_str1.idem_by_name.i3,A_pmc1_str3.idem_by_name['|(0, 2),(1, 3),(4, 6)|'])
    


    dd_arrows=Bunch_of_arrows([
                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r1'], 
        gen_by_name.x1, 
        A_pmc1_str3.gen_by_name['|(4, 6),(5, 7),(0->1)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r3'], 
        gen_by_name.x1, 
        A_pmc1_str3.gen_by_name['|(4, 6),(5, 7),(2->3)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r123'], 
        gen_by_name.x1, 
        A_pmc1_str3.gen_by_name['|(4, 6),(5, 7),(0->3)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r2'], 
        gen_by_name.x0, 
        A_pmc1_str3.gen_by_name['|(4, 6),(5, 7),(1->2)|']),

                    (gen_by_name.x2,
        A_pmc1_str1.gen_by_name['r5'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(0, 2),(1, 3),(4->5)|']),

                    (gen_by_name.x2,
        A_pmc1_str1.gen_by_name['r7'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(0, 2),(1, 3),(6->7)|']),

                    (gen_by_name.x2,
        A_pmc1_str1.gen_by_name['r567'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(0, 2),(1, 3),(4->7)|']),

                    (gen_by_name.x3,
        A_pmc1_str1.gen_by_name['r6'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(0, 2),(1, 3),(5->6)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r1234'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(1, 3),(5, 7),(0->4)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r34'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(1, 3),(5, 7),(2->4)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r3456'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(1, 3),(5, 7),(2->6)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r123456'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(1, 3),(5, 7),(0->6)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r4'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(0, 2),(5, 7),(3->4)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r456'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(0, 2),(5, 7),(3->6)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r234'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(0, 2),(5, 7),(1->4)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r23456'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(0, 2),(5, 7),(1->6)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r45'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(0, 2),(4, 6),(3->5)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r4567'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(0, 2),(4, 6),(3->7)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r2345'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(0, 2),(4, 6),(1->5)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r234567'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(0, 2),(4, 6),(1->7)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r345'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(1, 3),(4, 6),(2->5)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r34567'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(1, 3),(4, 6),(2->7)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r12345'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(1, 3),(4, 6),(0->5)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r1234567'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(1, 3),(4, 6),(0->7)|']),

        ])
    
    return DD_bimodule(gen_by_name,dd_arrows,A_pmc1_str1,A_pmc1_str3,name="K_pmc1")
def init_DD_pmc1_M_RHD(A_pmc1_str1,A_pmc1_str3):
    gen_by_name=AttrDict({
            "x0": Generator("x0"),
            "x1": Generator("x1"),
            "x2": Generator("x2"),
            "x3": Generator("x3"),
            "r": Generator("r"),
            })

    gen_by_name.x0.add_idems(A_pmc1_str1.idem_by_name.i0,A_pmc1_str3.idem_by_name['|(1, 3),(4, 6),(5, 7)|'] )
    gen_by_name.x1.add_idems(A_pmc1_str1.idem_by_name.i1,A_pmc1_str3.idem_by_name['|(0, 2),(4, 6),(5, 7)|'])
    gen_by_name.x2.add_idems(A_pmc1_str1.idem_by_name.i2,A_pmc1_str3.idem_by_name['|(0, 2),(1, 3),(5, 7)|'] )
    gen_by_name.x3.add_idems(A_pmc1_str1.idem_by_name.i3,A_pmc1_str3.idem_by_name['|(0, 2),(1, 3),(4, 6)|'])
    gen_by_name.r.add_idems(A_pmc1_str1.idem_by_name.i1,A_pmc1_str3.idem_by_name['|(1, 3),(4, 6),(5, 7)|'])
        

    dd_arrows=Bunch_of_arrows([
                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r1'], 
        gen_by_name.x1, 
        A_pmc1_str3.gen_by_name['|(4, 6),(5, 7),(0->1)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r123'], 
        gen_by_name.x1, 
        A_pmc1_str3.gen_by_name['|(4, 6),(5, 7),(0->3)|']),

                    (gen_by_name.x2,
        A_pmc1_str1.gen_by_name['r5'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(0, 2),(1, 3),(4->5)|']),

                    (gen_by_name.x2,
        A_pmc1_str1.gen_by_name['r7'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(0, 2),(1, 3),(6->7)|']),

                    (gen_by_name.x2,
        A_pmc1_str1.gen_by_name['r567'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(0, 2),(1, 3),(4->7)|']),

                    (gen_by_name.x3,
        A_pmc1_str1.gen_by_name['r6'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(0, 2),(1, 3),(5->6)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r1234'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(1, 3),(5, 7),(0->4)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r34'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(5, 7),(1->4),(2->3)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r3456'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(5, 7),(1->6),(2->3)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r123456'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(1, 3),(5, 7),(0->6)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r4'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(0, 2),(5, 7),(3->4)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r456'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(0, 2),(5, 7),(3->6)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r234'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(0, 2),(5, 7),(1->4)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r23456'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(0, 2),(5, 7),(1->6)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r45'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(0, 2),(4, 6),(3->5)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r4567'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(0, 2),(4, 6),(3->7)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r2345'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(0, 2),(4, 6),(1->5)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r234567'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(0, 2),(4, 6),(1->7)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r345'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(4, 6),(1->5),(2->3)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r34567'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(4, 6),(1->7),(2->3)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r12345'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(1, 3),(4, 6),(0->5)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r1234567'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(1, 3),(4, 6),(0->7)|']),

                    (gen_by_name.r,
        A_pmc1_str1.gen_by_name['r2'], 
        gen_by_name.x0, 
        1),
                    (gen_by_name.r,
        1, 
        gen_by_name.x1, 
        A_pmc1_str3.gen_by_name['|(4, 6),(5, 7),(2->3)|']),

                    (gen_by_name.x1,
        A_pmc1_str1.gen_by_name['r23'], 
        gen_by_name.r, 
        A_pmc1_str3.gen_by_name['|(4, 6),(5, 7),(1->2)|']),

                    (gen_by_name.x0,
        A_pmc1_str1.gen_by_name['r3'], 
        gen_by_name.r, 
        A_pmc1_str3.gen_by_name['|(4, 6),(5, 7),(1->3)|']),

                    (gen_by_name.r,
        A_pmc1_str1.gen_by_name['r45'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(1, 3),(4, 6),(2->5)|']),

                    (gen_by_name.r,
        A_pmc1_str1.gen_by_name['r4567'], 
        gen_by_name.x3, 
        A_pmc1_str3.gen_by_name['|(1, 3),(4, 6),(2->7)|']),

                    (gen_by_name.r,
        A_pmc1_str1.gen_by_name['r4'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(1, 3),(5, 7),(2->4)|']),

                    (gen_by_name.r,
        A_pmc1_str1.gen_by_name['r456'], 
        gen_by_name.x2, 
        A_pmc1_str3.gen_by_name['|(1, 3),(5, 7),(2->6)|']),

        ])
    
    return DD_bimodule(gen_by_name,dd_arrows,A_pmc1_str1,A_pmc1_str3,name="DD_pmc1_M_RHD")
K_pmc1=init_DD_pmc1(A_pmc1_str1,A_pmc1_str3)
DA_pmc1=g2_ID

####### experimenting with M_RHD
g2_M_RHD=g2_M_RHD
DD_pmc1_M_RHD=init_DD_pmc1_M_RHD(A_pmc1_str1,A_pmc1_str3)
mb_dd=da_dd_box_tensor_product(g2_M_RHD,K_pmc1)
print are_equal_smart_dd(mb_dd,DD_pmc1_M_RHD)
# YES, THEY ARE EQUAL!




######## genus=1
def init_g1_DD_id(torus_A,torus_A2):
    gen_by_name=AttrDict({ 
            "(i0⊗i1)": Generator("(i0⊗i1)"),
            "(i1⊗i0)": Generator("(i1⊗i0)"),
            })

    gen_by_name['(i0⊗i1)'].add_idems(torus_A.idem_by_name.i0,torus_A2.idem_by_name.i1 )
    gen_by_name['(i1⊗i0)'].add_idems(torus_A.idem_by_name.i1,torus_A2.idem_by_name.i0)

    dd_arrows=Bunch_of_arrows([
                    (gen_by_name['(i0⊗i1)'],
        torus_A.gen_by_name['r1'], 
        gen_by_name['(i1⊗i0)'], 
        torus_A2.gen_by_name['r1']),

                    (gen_by_name['(i0⊗i1)'],
        torus_A.gen_by_name['r3'], 
        gen_by_name['(i1⊗i0)'], 
        torus_A2.gen_by_name['r3']),

                    (gen_by_name['(i0⊗i1)'],
        torus_A.gen_by_name['r123'], 
        gen_by_name['(i1⊗i0)'], 
        torus_A2.gen_by_name['r123']),

                    (gen_by_name['(i1⊗i0)'],
        torus_A.gen_by_name['r2'], 
        gen_by_name['(i0⊗i1)'], 
        torus_A2.gen_by_name['r2']),

        ])
    
    return DD_bimodule(gen_by_name,dd_arrows,torus_A,torus_A2,name="g1_DD_id")
def init_g1_AA_id(torus_A,torus_A2):
    gen_by_name=AttrDict({
            "y": Generator("y"),
            "x": Generator("x"),
            "w1": Generator("w1"),
            "w2": Generator("w2"),
            "z1": Generator("z1"),
            "z2": Generator("z2"),
            })

    gen_by_name.y.add_idems(torus_A.idem_by_name.i0,torus_A2.idem_by_name.i1 )
    gen_by_name.x.add_idems(torus_A.idem_by_name.i1,torus_A2.idem_by_name.i0)
    gen_by_name.z1.add_idems(torus_A.idem_by_name.i1,torus_A2.idem_by_name.i1 )
    gen_by_name.z2.add_idems(torus_A.idem_by_name.i1,torus_A2.idem_by_name.i1)
    gen_by_name.w1.add_idems(torus_A.idem_by_name.i0,torus_A2.idem_by_name.i0 )
    gen_by_name.w2.add_idems(torus_A.idem_by_name.i0,torus_A2.idem_by_name.i0)

    dd_arrows=Bunch_of_arrows([
            ((torus_A.gen_by_name['r2'],),
            gen_by_name.y,
            (torus_A2.gen_by_name['r2'],),
            gen_by_name.x),

            ((torus_A.gen_by_name['r2'],),
            gen_by_name.y,
            (torus_A2.gen_by_name['r23'],),
            gen_by_name.z2),

            ((torus_A.gen_by_name['r12'],),
            gen_by_name.y,
            (torus_A2.gen_by_name['r2'],),
            gen_by_name.w2),

            ((),
            gen_by_name.w1,
            (torus_A2.gen_by_name['r1'],),
            gen_by_name.y),

            ((torus_A.gen_by_name['r3'],),
            gen_by_name.z1,
            (),
            gen_by_name.y),

            ((torus_A2.gen_by_name['r2'],),
            gen_by_name.w1,
            (torus_A2.gen_by_name['r12'],),
            gen_by_name.x),

            ((torus_A.gen_by_name['r23'],),
            gen_by_name.z1,
            (torus_A.gen_by_name['r2'],),
            gen_by_name.x),

            ((),
            gen_by_name.x,
            (torus_A2.gen_by_name['r3'],),
            gen_by_name.z2),

            ((torus_A.gen_by_name['r1'],),
            gen_by_name.x,
            (),
            gen_by_name.w2),

            ((),
            gen_by_name.w1,
            (),
            gen_by_name.w2),

            ((torus_A2.gen_by_name['r12'],),
            gen_by_name.w1,
            (torus_A2.gen_by_name['r12'],),
            gen_by_name.w2),

            ((),
            gen_by_name.z1,
            (),
            gen_by_name.z2),

            ((torus_A2.gen_by_name['r23'],),
            gen_by_name.z1,
            (torus_A2.gen_by_name['r23'],),
            gen_by_name.z2),

            ((torus_A2.gen_by_name['r123'],),
            gen_by_name.z1,
            (torus_A2.gen_by_name['r2'],),
            gen_by_name.w2),

            ((torus_A2.gen_by_name['r2'],),
            gen_by_name.w1,
            (torus_A2.gen_by_name['r123'],),
            gen_by_name.z2),

            ((torus_A2.gen_by_name['r2'],),
            gen_by_name.w1,
            (torus_A2.gen_by_name['r3'],torus_A2.gen_by_name['r2'],torus_A2.gen_by_name['r1']),
            gen_by_name.z2),


        ])
    
    return AA_bimodule(gen_by_name,dd_arrows,torus_A,torus_A2,name="g1_AA_id")
# g1_AA_id=init_g1_AA_id(torus_A,torus_A)
# g1_DD_id=init_g1_DD_id(torus_A,torus_A)
# g1_DA_id=ID1
# dual_g1_DD_id=dualization_of_DD(g1_DD_id)
# a_A_a=a_A_a(torus_A)
# dual_a_A_a=dualization_of_AA(a_A_a)

# da=dd_aa_box_tensor_product(dual_g1_DD_id,a_A_a)
# aa=aa_da_box_tensor_product(dual_a_A_a,da)
# aa.show()
# aa=aa_randomly_cancel_until_possible(aa)

# mb_da_id=dd_aa_box_tensor_product(g1_DD_id,aa)
# mb_da_id=da_randomly_cancel_until_possible(mb_da_id)
# mb_da_id.show()
##### it is DA(id), but it has too many generators


