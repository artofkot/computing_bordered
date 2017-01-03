# -*- coding: utf-8 -*- 
from algebraic_structures.algebra import AttrDict, Generator, torus_A, g2_A, pil_A
from algebraic_structures.da_bimodule import  Bunch_of_arrows, DA_bimodule,cancel_pure_differential,da_arrow_to_str
from algebraic_structures.da_bimodule import  randomly_cancel_until_possible, cancel_this_number_of_times
from algebraic_structures.dd_bimodule import DD_bimodule
from algebraic_structures.morphism import check_df_is_0, composition
from algebraic_structures.hochschild_homology import is_bounded, CH, homology_dim, ChainComplex

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
def init_DD_dual_bar(pil_A):
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
    
    return DD_bimodule(gen_by_name,dd_arrows,pil_A,name="DD_dual_bar_"+pil_A.name)

DD_dual_bar=init_DD_dual_bar(pil_A) 