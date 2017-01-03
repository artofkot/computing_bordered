# -*- coding: utf-8 -*- 
from basics import AttrDict 
from algebra import Generator, torus_A, check_idempotents_match_left_left, check_idempotents_match_right_left,check_idempotents_match_right_right
from collections import Counter
from itertools import permutations
from random import shuffle

from da_bimodule import randomly_cancel_until_possible, Bunch_of_arrows, DA_bimodule, da_in_mod_gen, da_in_alg_tuple, da_out_alg_gen, da_out_mod_gen

#I assume that all 4 algebras here are the same
def box_tensor_product(DAbimodule1,DAbimodule2):
    def find_sequence_for_box_tensor_product(final_list_of_sequences_of_arrows,
                                            needed_alg_tuple_to_finish_sequence,
                                            current_gen,
                                            arrows,
                                            presequence_of_arrows_from_right):
        # print 'loop starts, and this is needed sequence'
        # print needed_alg_tuple_to_finish_sequence
        # print len(needed_alg_tuple_to_finish_sequence)>0

        if len(needed_alg_tuple_to_finish_sequence)>0:
            arrows_to_continue=[arrow for arrow in arrows if (da_out_alg_gen(arrow)==needed_alg_tuple_to_finish_sequence[0] and current_gen==da_in_mod_gen(arrow))]
            for arrow in arrows_to_continue:
                # print 'presequence of arrows: '
                # for ar in presequence_of_arrows_from_right:
                #     print arrow_to_str(ar) + ', ',
                # print '\n'
                # print needed_alg_tuple_to_finish_sequence[1:]

                find_sequence_for_box_tensor_product(final_list_of_sequences_of_arrows,
                                                    needed_alg_tuple_to_finish_sequence[1:],
                                                    da_out_mod_gen(arrow),
                                                    arrows,
                                                    presequence_of_arrows_from_right+[arrow])

        if len(needed_alg_tuple_to_finish_sequence)==0:
            final_list_of_sequences_of_arrows.append(presequence_of_arrows_from_right)


    #let's compute generators
    generators_of_tensor_product_by_name=AttrDict({})
    for generator_from_DA1 in DAbimodule1.genset:
        for generator_from_DA2 in DAbimodule2.genset:
            if generator_from_DA1.idem.right!=generator_from_DA2.idem.left:
                continue
            else:
                generators_of_tensor_product_by_name[generator_from_DA1.name+'_'+generator_from_DA2.name]=Generator(generator_from_DA1.name+'_'+generator_from_DA2.name)
                generators_of_tensor_product_by_name[generator_from_DA1.name+'_'+generator_from_DA2.name].add_idems(generator_from_DA1.idem.left,generator_from_DA2.idem.right)

    #we want to compute differential now
    arrows_in_tensor_product=Bunch_of_arrows()

    for generator_from_DA1 in DAbimodule1.genset:
        for generator_from_DA2 in DAbimodule2.genset:
            in_generator_of_tensor_product=generators_of_tensor_product_by_name.get(generator_from_DA1.name+'_'+generator_from_DA2.name, None)
            if not in_generator_of_tensor_product: continue
            # print 'FROM this generator:' + str((generator_from_DA1,generator_from_DA2))
             
            #here we compute differentials with one action on right DAbimodule2
            arrows_inDA2_without_out_alg_gen=[arrow for arrow in DAbimodule2.arrows if (da_in_mod_gen(arrow)==generator_from_DA2 and da_out_alg_gen(arrow)==1)]
            for ar in arrows_inDA2_without_out_alg_gen:
                #add differential
                arrows_in_tensor_product[(in_generator_of_tensor_product,da_in_alg_tuple(ar),
                    1,generators_of_tensor_product_by_name[generator_from_DA1.name+'_'+da_out_mod_gen(ar).name]) ]+=1

            #differentials with one action on the left DAbimodule1 and multiple on the right DAbimodule2
            for arrow_on_DA1_side in [arrow for arrow in DAbimodule1.arrows if (da_in_mod_gen(arrow)==generator_from_DA1)]:
                # print 'matching this arrow on the DA1 side: ' + arrow_to_str(arrow_on_DA1_side)
                final_list_of_sequences_of_arrows=[]
                find_sequence_for_box_tensor_product(final_list_of_sequences_of_arrows,
                                                    da_in_alg_tuple(arrow_on_DA1_side),
                                                    generator_from_DA2,
                                                    DAbimodule2.arrows,
                                                    presequence_of_arrows_from_right=[])

                for sequence in final_list_of_sequences_of_arrows:
                    final_right_action=()
                    final_gen_on_DA2_side=generator_from_DA2
                    for ind,arrow in enumerate(sequence): 
                        final_right_action=final_right_action+da_in_alg_tuple(arrow)
                        if ind+1==len(sequence): final_gen_on_DA2_side=da_out_mod_gen(arrow)
                    #add differential
                    arrows_in_tensor_product[(in_generator_of_tensor_product,final_right_action,
                    da_out_alg_gen(arrow_on_DA1_side),generators_of_tensor_product_by_name[da_out_mod_gen(arrow_on_DA1_side).name+'_'+final_gen_on_DA2_side.name]) ]+=1

    arrows_in_tensor_product.delete_arrows_with_even_coeff()

    return DA_bimodule(generators_of_tensor_product_by_name,arrows_in_tensor_product,DAbimodule1.algebra,name= DAbimodule1.name +'⊠'+DAbimodule2.name)

def box_tensor(*args):
    tensor_prod=args[0]
    for bimodule_n in args[1:]:
        tensor_prod=box_tensor_product(tensor_prod,bimodule_n)
    return tensor_prod

def box_tensor_efficient(*args):
    tensor_prod=args[0]
    for bimodule_n in args[1:]:
        tensor_prod=randomly_cancel_until_possible(box_tensor_product(tensor_prod,bimodule_n))
    return randomly_cancel_until_possible(tensor_prod)