# -*- coding: utf-8 -*- 
import sys
sys.path.append('../')

from algebraic_structures.algebra import AttrDict, Generator, pil_A
from algebraic_structures.basics import  Bunch_of_arrows
from algebraic_structures.dd_bimodule import DD_bimodule
from algebraic_structures.right_a_module import Right_A_module
from algebraic_structures.left_a_module import Left_A_module
from algebraic_structures.left_d_module import Left_D_module

##### graph of pillow algebra
vertices=pil_A.idemset
edges=pil_A.genset
#the following works only for graphs without cycles
def paths(idem1,idem2):
    paths_to_add=set()
    if idem1==idem2: 
        paths_to_add.add((idem1,))
        return paths_to_add
    
    outgoing_edges=[edge for edge in (set(edges)-set(vertices)) if edge.idem.left==idem1]
    for edge in outgoing_edges:
        if edge.idem.right==idem2:
            paths_to_add.add((edge,))
        else:
            auxilary_paths=paths(edge.idem.right,idem2)
            for a_path in auxilary_paths:  
                paths_to_add.add((edge,)+a_path)
    return paths_to_add

##### dual(A^bar^A) DD-bimodule from Mor paper, for algebra with no differential
def init_DD_bar_dual(pil_A):
    all_paths_in_pillow_graph=set()
    for idem1 in pil_A.idemset:
        for idem2 in pil_A.idemset:
            all_paths_in_pillow_graph=all_paths_in_pillow_graph.union(paths(idem1,idem2))

    gen_by_name=AttrDict({})
    for path in all_paths_in_pillow_graph:
        gen_by_name['a' + str(path)]=Generator('a' + str(path))

        idemleft=path[-1].idem.right
        idemright=path[0].idem.left
        gen_by_name['a' + str(path)].add_idems(idemleft,idemright) #because A^bar^A reverses idempotents, and dual reverses one more time

    dd_arrows=Bunch_of_arrows([])
    for path in all_paths_in_pillow_graph:
        in_path_gen=gen_by_name['a'+str(path)]
        for chord in (set(pil_A.genset)-set(pil_A.idemset)):
            rightaction_out=(chord.idem.right==path[0].idem.left)
            if rightaction_out:
                if path[0] in (pil_A.idemset):
                    out_path=(chord,)
                else:
                    out_path=(chord,)+path
                out_path_gen=gen_by_name['a'+str(out_path)]
                dd_arrows[(in_path_gen,1,out_path_gen,chord)]+=1

            leftaction_out=(chord.idem.left==path[-1].idem.right)
            if leftaction_out:
                if path[0] in (pil_A.idemset):
                    out_path=(chord,)
                else:
                    out_path=path+(chord,)
                out_path_gen=gen_by_name['a'+str(out_path)]
                dd_arrows[(in_path_gen,chord,out_path_gen,1)]+=1

        for ind, chord_in_path in enumerate(path):
            for factorization in getattr(chord_in_path,'factorizations', []):
                out_path=path[:ind]+factorization+path[ind+1:]
                out_path_gen=gen_by_name['a'+str(out_path)]
                dd_arrows[(in_path_gen,1,out_path_gen,1)]+=1
    
    return DD_bimodule(gen_by_name,dd_arrows,pil_A,pil_A,name="DD_bar_dual")

def init_Right_A_L0(pil_A):
    gen_by_name=AttrDict({
                "z": Generator("z"),
                "w": Generator("w"),
                "s": Generator("s"),
                "t": Generator("t"),
                "y": Generator("y"),
                "x": Generator("x")

                })

    gen_by_name.z.add_idems(0,pil_A.idem_by_name.i0)
    gen_by_name.w.add_idems(0,pil_A.idem_by_name.i2)
    gen_by_name.s.add_idems(0,pil_A.idem_by_name.j2)
    gen_by_name.t.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.y.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.x.add_idems(0,pil_A.idem_by_name.j0)

    right_a_arrows=Bunch_of_arrows([
        (              gen_by_name.z,(pil_A.gen_by_name.et1,pil_A.gen_by_name.ks1)
                        ,gen_by_name.w),
        (              gen_by_name.w,(pil_A.gen_by_name.ks2,)
                        ,gen_by_name.s),
        (              gen_by_name.z,(pil_A.gen_by_name.et1,pil_A.gen_by_name.ks12)
                        ,gen_by_name.s),
        (              gen_by_name.t,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.y),
        (              gen_by_name.y,(pil_A.gen_by_name.et3,)
                        ,gen_by_name.x),
        (              gen_by_name.t,(pil_A.gen_by_name.et23,)
                        ,gen_by_name.x),
        (              gen_by_name.t,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2)
                        ,gen_by_name.s),
        (              gen_by_name.z,(pil_A.gen_by_name.r0,)
                        ,gen_by_name.x),
                                    ])
    return Right_A_module(gen_by_name,right_a_arrows,pil_A,name="Right_A_L0")
def init_Right_A_L6(pil_A):
    gen_by_name=AttrDict({
                "u": Generator("u"),
                "v": Generator("v"),

                })

    gen_by_name.u.add_idems(0,pil_A.idem_by_name.i0)
    gen_by_name.v.add_idems(0,pil_A.idem_by_name.j0)

    right_a_arrows=Bunch_of_arrows([
        (              gen_by_name.u,(pil_A.gen_by_name.et1, pil_A.gen_by_name.ks1, pil_A.gen_by_name.r2, pil_A.gen_by_name.ks3,  pil_A.gen_by_name.et3)
                        ,gen_by_name.v),
        (              gen_by_name.u,(pil_A.gen_by_name.r0,)
                        ,gen_by_name.v),
                                    ])
    return Right_A_module(gen_by_name,right_a_arrows,pil_A,name="Right_A_L6")
def init_Right_A_L7(pil_A):
    gen_by_name=AttrDict({
                "u": Generator("u"),
                "v": Generator("v"),

                })

    gen_by_name.u.add_idems(0,pil_A.idem_by_name.i2)
    gen_by_name.v.add_idems(0,pil_A.idem_by_name.j2)

    right_a_arrows=Bunch_of_arrows([
        (              gen_by_name.u,(pil_A.gen_by_name.ks2,)
                        ,gen_by_name.v),
        (              gen_by_name.u,(pil_A.gen_by_name.r2,)
                        ,gen_by_name.v),
                                    ])
    return Right_A_module(gen_by_name,right_a_arrows,pil_A,name="Right_A_L7")
def init_Right_A_L1(pil_A):
    gen_by_name=AttrDict({
                "a": Generator("a"),
                "b": Generator("b"),
                "c": Generator("c"),
                "d": Generator("d"),
                "g": Generator("g"),
                "h": Generator("h"),
                "p": Generator("p"),
                "q": Generator("q"),
                "s": Generator("s"),
                "t": Generator("t"),
                "x": Generator("x"),
                "y": Generator("y"),
                "l": Generator("l"),
                "m": Generator("m"),
                "z": Generator("z"),
                "w": Generator("w"),
                "e": Generator("e"),
                "r": Generator("r"),
                "u": Generator("u"),
                "v": Generator("v"),
                })

    gen_by_name.a.add_idems(0,pil_A.idem_by_name.i0)
    gen_by_name.b.add_idems(0,pil_A.idem_by_name.i0)
    gen_by_name.z.add_idems(0,pil_A.idem_by_name.j0)
    gen_by_name.w.add_idems(0,pil_A.idem_by_name.j0)
    gen_by_name.t.add_idems(0,pil_A.idem_by_name.i2)
    gen_by_name.s.add_idems(0,pil_A.idem_by_name.i2)
    gen_by_name.c.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.g.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.d.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.h.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.r.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.e.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.p.add_idems(0,pil_A.idem_by_name.j2)
    gen_by_name.q.add_idems(0,pil_A.idem_by_name.j2)
    gen_by_name.x.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.y.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.u.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.v.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.l.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.m.add_idems(0,pil_A.idem_by_name.j1)

    right_a_arrows=Bunch_of_arrows([
        (              gen_by_name.b,(pil_A.gen_by_name.r0,)
                        ,gen_by_name.z),
        (              gen_by_name.y,(pil_A.gen_by_name.et3,)
                        ,gen_by_name.z),
        (              gen_by_name.d,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.y),
        (              gen_by_name.d,(pil_A.gen_by_name.et23,)
                        ,gen_by_name.z),
        (              gen_by_name.d,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.l),
        (              gen_by_name.r,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.l),
        (              gen_by_name.r,(pil_A.gen_by_name.ks1,)
                        ,gen_by_name.s),
        (              gen_by_name.r,(pil_A.gen_by_name.ks12,)
                        ,gen_by_name.p),
        (              gen_by_name.r,(pil_A.gen_by_name.ks123,)
                        ,gen_by_name.u),
        (              gen_by_name.s,(pil_A.gen_by_name.ks2,)
                        ,gen_by_name.p),
        (              gen_by_name.s,(pil_A.gen_by_name.ks23,)
                        ,gen_by_name.u),
        (              gen_by_name.p,(pil_A.gen_by_name.ks3,)
                        ,gen_by_name.u),
        (              gen_by_name.g,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.u),
        (              gen_by_name.a,(pil_A.gen_by_name.et12,)
                        ,gen_by_name.u),
        (              gen_by_name.a,(pil_A.gen_by_name.et1,)
                        ,gen_by_name.g),
        (              gen_by_name.a,(pil_A.gen_by_name.r0,)
                        ,gen_by_name.w),
        (              gen_by_name.x,(pil_A.gen_by_name.et3,)
                        ,gen_by_name.w),
        (              gen_by_name.c,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.x),
        (              gen_by_name.c,(pil_A.gen_by_name.et23,)
                        ,gen_by_name.w),
        (              gen_by_name.c,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.m),
        (              gen_by_name.e,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.m),
        (              gen_by_name.e,(pil_A.gen_by_name.ks1,)
                        ,gen_by_name.t),
        (              gen_by_name.e,(pil_A.gen_by_name.ks12,)
                        ,gen_by_name.q),
        (              gen_by_name.e,(pil_A.gen_by_name.ks123,)
                        ,gen_by_name.v),
        (              gen_by_name.t,(pil_A.gen_by_name.ks2,)
                        ,gen_by_name.q),
        (              gen_by_name.t,(pil_A.gen_by_name.ks23,)
                        ,gen_by_name.v),
        (              gen_by_name.q,(pil_A.gen_by_name.ks3,)
                        ,gen_by_name.v),
        (              gen_by_name.h,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.v),
        (              gen_by_name.b,(pil_A.gen_by_name.et12,)
                        ,gen_by_name.v),
        (              gen_by_name.b,(pil_A.gen_by_name.et1,)
                        ,gen_by_name.h),
                                    ])
    return Right_A_module(gen_by_name,right_a_arrows,pil_A,name="Right_A_L1")
def init_Right_A_L2(pil_A):
    gen_by_name=AttrDict({
                "a": Generator("a"),
                "b": Generator("b"),
                "c": Generator("c"),
                "d": Generator("d"),
                "y1": Generator("y1"),
                "x1": Generator("x1"),
                "z1": Generator("z1"),
                "t1": Generator("t1"),
                "y2": Generator("y2"),
                "x2": Generator("x2"),
                "z2": Generator("z2"),
                "t2": Generator("t2"),

                })

    gen_by_name.a.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.b.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.c.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.d.add_idems(0,pil_A.idem_by_name.j0)
    gen_by_name.x1.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.y1.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.z1.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.t1.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.x2.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.y2.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.z2.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.t2.add_idems(0,pil_A.idem_by_name.i1)

    right_a_arrows=Bunch_of_arrows([
        (              gen_by_name.b,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.c),
        (              gen_by_name.b,(pil_A.gen_by_name.et23,)
                        ,gen_by_name.d),
        (              gen_by_name.b,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.a),
        (              gen_by_name.a,(pil_A.gen_by_name.et3,)
                        ,gen_by_name.d),
        (              gen_by_name.z1,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.y1),
        (              gen_by_name.t1,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.x1),
        (              gen_by_name.t1,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.y1),
        (              gen_by_name.z1,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.x1),
        (              gen_by_name.z2,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.y2),
        (              gen_by_name.t2,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.x2),
        (              gen_by_name.t2,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.y2),
        (              gen_by_name.z2,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.x2),
                                    ])
    return Right_A_module(gen_by_name,right_a_arrows,pil_A,name="Right_A_L2")
def init_Right_A_L3(pil_A):
    gen_by_name=AttrDict({
                "a": Generator("a"),
                "b": Generator("b"),
                "c": Generator("c"),
                "d": Generator("d"),
                "x1": Generator("x1"),
                "x2": Generator("x2"),
                "x3": Generator("x3"),
                "x4": Generator("x4"),
                "x5": Generator("x5"),
                "x6": Generator("x6"),
                "x7": Generator("x7"),
                "x8": Generator("x8"),
                "x9": Generator("x9"),
                "x10": Generator("x10"),
                "x11": Generator("x11"),
                "x12": Generator("x12"),
                "x13": Generator("x13"),
                "x14": Generator("x14"),
                "x15": Generator("x15"),
                "x16": Generator("x16"),

                })

    gen_by_name.a.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.b.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.c.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.d.add_idems(0,pil_A.idem_by_name.j0)
    gen_by_name.x1.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.x2.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.x3.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.x4.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.x5.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.x6.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.x7.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.x8.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.x9.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.x10.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.x11.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.x12.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.x13.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.x14.add_idems(0,pil_A.idem_by_name.j1)
    gen_by_name.x15.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.x16.add_idems(0,pil_A.idem_by_name.j1)

    right_a_arrows=Bunch_of_arrows([
        (              gen_by_name.b,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.c),
        (              gen_by_name.b,(pil_A.gen_by_name.et23,)
                        ,gen_by_name.d),
        (              gen_by_name.b,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.a),
        (              gen_by_name.a,(pil_A.gen_by_name.et3,)
                        ,gen_by_name.d),
        (              gen_by_name.x1,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.x2),
        (              gen_by_name.x3,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.x2),
        (              gen_by_name.x3,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.x4),
        (              gen_by_name.x5,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.x4),
        (              gen_by_name.x5,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.x6),
        (              gen_by_name.x7,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.x6),
        (              gen_by_name.x7,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.x8),
        (              gen_by_name.x9,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.x8),
        (              gen_by_name.x9,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.x10),
        (              gen_by_name.x11,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.x10),
        (              gen_by_name.x11,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.x12),
        (              gen_by_name.x13,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.x12),
        (              gen_by_name.x13,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.x14),
        (              gen_by_name.x15,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.x14),
        (              gen_by_name.x15,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.x16),
        (              gen_by_name.x1,(pil_A.gen_by_name.ks1,pil_A.gen_by_name.r2,pil_A.gen_by_name.ks3)
                        ,gen_by_name.x16),
                                    ])
    return Right_A_module(gen_by_name,right_a_arrows,pil_A,name="Right_A_L3")

def init_Left_D_test(pil_A):
    gen_by_name=AttrDict({
                "w": Generator("w"),
                "y": Generator("y"),
                "x": Generator("x"),
                "t": Generator("t")

                })

    gen_by_name.x.add_idems(pil_A.idem_by_name.i0,0)
    gen_by_name.t.add_idems(pil_A.idem_by_name.i0,0)
    gen_by_name.y.add_idems(pil_A.idem_by_name.i1,0)
    gen_by_name.w.add_idems(pil_A.idem_by_name.i2,0)
    

    left_d_arrows=Bunch_of_arrows([
        (              gen_by_name.x,
            pil_A.gen_by_name.et1,gen_by_name.y),
        (              gen_by_name.y,
            pil_A.gen_by_name.ks1,gen_by_name.w),
        (              gen_by_name.x,
            1,gen_by_name.t),
                                    ])

    return Left_D_module(gen_by_name,left_d_arrows,pil_A,name="Left_D_test")
def init_Right_A_test(pil_A):
    gen_by_name=AttrDict({
                "w": Generator("w"),
                "u": Generator("u"),
                "z": Generator("z"),
                })

    gen_by_name.w.add_idems(0,pil_A.idem_by_name.i2)
    gen_by_name.u.add_idems(0,pil_A.idem_by_name.i0)
    gen_by_name.z.add_idems(0,pil_A.idem_by_name.i0)
    
    right_a_arrows=Bunch_of_arrows([
        (      gen_by_name.z,(),
            gen_by_name.u),
        (     gen_by_name.z,(pil_A.gen_by_name.et1,pil_A.gen_by_name.ks1),
            gen_by_name.w),
                                    ])

    return Right_A_module(gen_by_name,right_a_arrows,pil_A,name="Right_A_test")
def init_Left_A_test(pil_A):
    gen_by_name=AttrDict({
                "w": Generator("w"),
                "t": Generator("t"),
                "z": Generator("z"),
                })

    gen_by_name.w.add_idems(pil_A.idem_by_name.i2,0)
    gen_by_name.t.add_idems(pil_A.idem_by_name.i0,0)
    gen_by_name.z.add_idems(pil_A.idem_by_name.i2,0)
    
    left_a_arrows=Bunch_of_arrows([
        (     (pil_A.gen_by_name.et1,pil_A.gen_by_name.ks1), gen_by_name.w,
            gen_by_name.t),
        (     (), gen_by_name.w,
            gen_by_name.z),
                                    ])

    return Left_A_module(gen_by_name,left_a_arrows,pil_A,name="Left_A_test")
def init_DD_test(pil_A):
    gen_by_name=AttrDict({
                "x": Generator("x"),
                "y": Generator("y"),
                "l": Generator("l"),
                "w": Generator("w"),
                })

    gen_by_name.x.add_idems(pil_A.idem_by_name.i1,pil_A.idem_by_name.i2)
    gen_by_name.w.add_idems(pil_A.idem_by_name.i1,pil_A.idem_by_name.i2)
    gen_by_name.y.add_idems(pil_A.idem_by_name.i2,pil_A.idem_by_name.i1)
    gen_by_name.l.add_idems(pil_A.idem_by_name.j2,pil_A.idem_by_name.i0)
    

    dd_arrows=Bunch_of_arrows([
        (      gen_by_name.x,
        pil_A.gen_by_name.ks1,gen_by_name.y,pil_A.gen_by_name.ks1),
        (      gen_by_name.y,
        pil_A.gen_by_name.ks2,gen_by_name.l,pil_A.gen_by_name.et1),
        (      gen_by_name.x,
                1,gen_by_name.w,1),
                                    ])

    return DD_bimodule(gen_by_name,dd_arrows,pil_A,pil_A,name="DD_test")
def init_Right_A_L8(pil_A):
    gen_by_name=AttrDict({
                "j1": Generator("j1"),
                "i1": Generator("i1"),
                "i2": Generator("i2"),
                "j2": Generator("j2"),

                })

    gen_by_name.i1.add_idems(0,pil_A.idem_by_name.i1)
    gen_by_name.i2.add_idems(0,pil_A.idem_by_name.i2)
    gen_by_name.j2.add_idems(0,pil_A.idem_by_name.j2)
    gen_by_name.j1.add_idems(0,pil_A.idem_by_name.j1)


    right_a_arrows=Bunch_of_arrows([
        (              gen_by_name.i1,(pil_A.gen_by_name.ks1,)
                        ,gen_by_name.i2),
        (              gen_by_name.i2,(pil_A.gen_by_name.ks2,)
                        ,gen_by_name.j2),
        (              gen_by_name.j2,(pil_A.gen_by_name.ks3,)
                        ,gen_by_name.j1),
        (              gen_by_name.i1,(pil_A.gen_by_name.et2,)
                        ,gen_by_name.j1),
                                    ])
    return Right_A_module(gen_by_name,right_a_arrows,pil_A,name="Right_A_L8")



DD_test=init_DD_test(pil_A)
Left_A_test=init_Left_A_test(pil_A)
Left_D_test=init_Left_D_test(pil_A)
Right_A_test=init_Right_A_test(pil_A)

DD_bar_dual=init_DD_bar_dual(pil_A)
Right_A_L0=init_Right_A_L0(pil_A) #eight curve
Right_A_L6=init_Right_A_L6(pil_A) #curve around north-west puncture
Right_A_L7=init_Right_A_L7(pil_A) #curve around north-east puncture
Right_A_L1=init_Right_A_L1(pil_A) #curve for (5,11) torus knot
Right_A_L2=init_Right_A_L2(pil_A) #curve for (3,7) torus knot
Right_A_L3=init_Right_A_L3(pil_A) #curve for (5,7) torus knot
Right_A_L8=init_Right_A_L8(pil_A)


