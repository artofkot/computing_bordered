# -*- coding: utf-8 -*- 
from basics import AttrDict, debug
from algebra import Generator
from da_bimodule import randomly_cancel_until_possible, Bunch_of_arrows, DA_bimodule, da_in_mod_gen, da_in_alg_tuple, da_out_alg_gen, da_out_mod_gen
from dd_bimodule import DD_bimodule, dd_in_mod_gen, dd_out_alg_left_gen, dd_out_alg_right_gen, dd_out_mod_gen
from left_a_module import Left_A_module, left_a_in_mod_gen, left_a_in_alg_tuple, left_a_out_mod_gen
from left_d_module import Left_D_module, left_d_in_mod_gen, left_d_out_alg_gen, left_d_out_mod_gen
from right_a_module import Right_A_module, right_a_in_mod_gen, right_a_in_alg_tuple, right_a_out_mod_gen
from chain_complex import ChainComplex

############### here we code DA⊠DA=DA ####################
#I assume that all 4 algebras here are the same
def da_da_box_tensor_product(DAbimodule1,DAbimodule2):
    def find_sequence_for_da_da_box_tensor_product(final_list_of_sequences_of_arrows,
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

                find_sequence_for_da_da_box_tensor_product(final_list_of_sequences_of_arrows,
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
            arrows_inDA2_without_out_alg_gen=[arrow for arrow in DAbimodule2.da_arrows if (da_in_mod_gen(arrow)==generator_from_DA2 and da_out_alg_gen(arrow)==1)]
            for ar in arrows_inDA2_without_out_alg_gen:
                #add differential
                arrows_in_tensor_product[(in_generator_of_tensor_product,da_in_alg_tuple(ar),
                    1,generators_of_tensor_product_by_name[generator_from_DA1.name+'_'+da_out_mod_gen(ar).name]) ]+=1

            #differentials with one action on the left DAbimodule1 and multiple on the right DAbimodule2
            for arrow_on_DA1_side in [arrow for arrow in DAbimodule1.da_arrows if (da_in_mod_gen(arrow)==generator_from_DA1)]:
                # print 'matching this arrow on the DA1 side: ' + arrow_to_str(arrow_on_DA1_side)
                final_list_of_sequences_of_arrows=[]
                find_sequence_for_da_da_box_tensor_product(final_list_of_sequences_of_arrows,
                                                    da_in_alg_tuple(arrow_on_DA1_side),
                                                    generator_from_DA2,
                                                    DAbimodule2.da_arrows,
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

def da_da_box_tensor_many_no_cancelations(*args):
    tensor_prod=args[0]
    for bimodule_n in args[1:]:
        tensor_prod=da_da_box_tensor_product(tensor_prod,bimodule_n)
    return tensor_prod

def da_da_box_tensor_many_efficient_cancelations(*args):
    tensor_prod=args[0]
    for bimodule_n in args[1:]:
        tensor_prod=randomly_cancel_until_possible(da_da_box_tensor_product(tensor_prod,bimodule_n))
    return randomly_cancel_until_possible(tensor_prod)

################ here we code A⊠D=Chain_complex #################
def a_d_box_tensor_product(Right_A_module,Left_D_module):
    
    def find_sequence_for_a_d_box_tensor_product(final_list_of_sequences_of_arrows,
                                            needed_alg_tuple_to_finish_sequence,
                                            current_gen,
                                            arrows,
                                            presequence_of_arrows_from_right):
        # loop starts, and this is needed sequence: needed_alg_tuple_to_finish_sequence

        if len(needed_alg_tuple_to_finish_sequence)>0:
            arrows_to_continue=[arrow for arrow in arrows if (left_d_out_alg_gen(arrow)==needed_alg_tuple_to_finish_sequence[0] and current_gen==left_d_in_mod_gen(arrow))]
            for arrow in arrows_to_continue:
                # print 'presequence of arrows: '
                # for ar in presequence_of_arrows_from_right:
                #     print arrow_to_str(ar) + ', ',
                # print '\n'
                # print needed_alg_tuple_to_finish_sequence[1:]

                find_sequence_for_a_d_box_tensor_product(final_list_of_sequences_of_arrows,
                                                    needed_alg_tuple_to_finish_sequence[1:],
                                                    left_d_out_mod_gen(arrow),
                                                    arrows,
                                                    presequence_of_arrows_from_right+[arrow])

        if len(needed_alg_tuple_to_finish_sequence)==0:
            final_list_of_sequences_of_arrows.append(presequence_of_arrows_from_right)


    #let's compute generators
    generators_of_tensor_product_by_name=AttrDict({})
    for generator_from_A in Right_A_module.genset:
        for generator_from_D in Left_D_module.genset:
            if generator_from_A.idem.right!=generator_from_D.idem.left:
                continue
            else:
                generators_of_tensor_product_by_name[generator_from_A.name+'_'+generator_from_D.name]=Generator(generator_from_A.name+'_'+generator_from_D.name)

    #we want to compute differential now
    arrows_in_tensor_product=Bunch_of_arrows()

    for generator_from_A in Right_A_module.genset:
        for generator_from_D in Left_D_module.genset:
            in_generator_of_tensor_product=generators_of_tensor_product_by_name.get(generator_from_A.name+'_'+generator_from_D.name, None)
            if not in_generator_of_tensor_product: continue
             
            #here we compute differentials with one action on Left_D_module (coming from the right)
            arrows_in_D_without_out_alg_gen=[arrow for arrow in Left_D_module.left_d_arrows if (left_d_in_mod_gen(arrow)==generator_from_D and left_d_out_alg_gen(arrow)==1)]
            for ar in arrows_in_D_without_out_alg_gen:
                #add differential
                arrows_in_tensor_product[(in_generator_of_tensor_product,generators_of_tensor_product_by_name[generator_from_A.name+'_'+left_d_out_mod_gen(ar).name]) ]+=1

            #differentials with one action on the Right_A_module and multiple on the Left_D_module (coming from the right)
            for arrow_on_A_side in [arrow for arrow in Right_A_module.right_a_arrows if (right_a_in_mod_gen(arrow)==generator_from_A)]:
                final_list_of_sequences_of_arrows=[]
                find_sequence_for_a_d_box_tensor_product(final_list_of_sequences_of_arrows,
                                                    right_a_in_alg_tuple(arrow_on_A_side),
                                                    generator_from_D,
                                                    Left_D_module.left_d_arrows,
                                                    presequence_of_arrows_from_right=[])

                for sequence in final_list_of_sequences_of_arrows:
                    final_gen_on_D_side=generator_from_D
                    if sequence:
                        final_gen_on_D_side=left_d_out_mod_gen(sequence[-1])
                    #add differential
                    arrows_in_tensor_product[(in_generator_of_tensor_product,generators_of_tensor_product_by_name[right_a_out_mod_gen(arrow_on_A_side).name+'_'+final_gen_on_D_side.name]) ]+=1

    arrows_in_tensor_product.delete_arrows_with_even_coeff()

    return ChainComplex(generators_of_tensor_product_by_name,arrows_in_tensor_product,name= Right_A_module.name +'⊠'+Left_D_module.name)

################ here we code DD⊠Left_A=Left_D #################
def dd_a_box_tensor_product(DD,Left_A):
    
    def find_sequence_for_dd_a_box_tensor_product(final_list_of_sequences_of_arrows,
                                            needed_alg_tuple_to_finish_sequence,
                                            current_gen,
                                            arrows,
                                            presequence_of_arrows_from_right):
        # loop starts, and this is needed sequence: needed_alg_tuple_to_finish_sequence

        if len(needed_alg_tuple_to_finish_sequence)>0:
            arrows_to_continue=[arrow for arrow in arrows if (dd_out_alg_right_gen(arrow)==needed_alg_tuple_to_finish_sequence[0] and current_gen==dd_in_mod_gen(arrow))]
            for arrow in arrows_to_continue:
                # print 'presequence of arrows: '
                # for ar in presequence_of_arrows_from_right:
                #     print arrow_to_str(ar) + ', ',
                # print '\n'
                # print needed_alg_tuple_to_finish_sequence[1:]

                find_sequence_for_dd_a_box_tensor_product(final_list_of_sequences_of_arrows,
                                                    needed_alg_tuple_to_finish_sequence[1:],
                                                    dd_out_mod_gen(arrow),
                                                    arrows,
                                                    presequence_of_arrows_from_right+[arrow])

        if len(needed_alg_tuple_to_finish_sequence)==0:
            final_list_of_sequences_of_arrows.append(presequence_of_arrows_from_right)


    #let's compute generators
    generators_of_tensor_product_by_name=AttrDict({})
    for generator_from_DD in DD.genset:
        for generator_from_A in Left_A.genset:
            if generator_from_DD.idem.right!=generator_from_A.idem.left:
                continue
            else:
                generators_of_tensor_product_by_name[generator_from_DD.name+'_'+generator_from_A.name]=Generator(generator_from_DD.name+'_'+generator_from_A.name)
                generators_of_tensor_product_by_name[generator_from_DD.name+'_'+generator_from_A.name].add_idems(generator_from_DD.idem.left,0)

    #we want to compute differential now
    arrows_in_tensor_product=Bunch_of_arrows()

    for generator_from_DD in DD.genset:
        for generator_from_A in Left_A.genset:
            in_generator_of_tensor_product=generators_of_tensor_product_by_name.get(generator_from_DD.name+'_'+generator_from_A.name, None)
            if not in_generator_of_tensor_product: continue
             
            #here we compute differentials with one action on DD (coming from the left)
            arrows_in_DD_without_out_alg_gen=[arrow for arrow in DD.dd_arrows if (dd_in_mod_gen(arrow)==generator_from_DD and dd_out_alg_right_gen(arrow)==1)]
            for ar in arrows_in_DD_without_out_alg_gen:
                #add differential
                arrows_in_tensor_product[(in_generator_of_tensor_product,
                        dd_out_alg_left_gen(ar),generators_of_tensor_product_by_name[dd_out_mod_gen(ar).name+'_'+generator_from_A.name]) ]+=1

            #differentials with one action on the DD and multiple on the Left_A (coming from the right)
            for arrow_on_A_side in [arrow for arrow in Left_A.left_a_arrows if (left_a_in_mod_gen(arrow)==generator_from_A)]:
                final_list_of_sequences_of_arrows=[]
                
                find_sequence_for_dd_a_box_tensor_product(final_list_of_sequences_of_arrows,
                                                    left_a_in_alg_tuple(arrow_on_A_side)[::-1], #tuple is reversed!
                                                    generator_from_DD,
                                                    DD.dd_arrows,
                                                    presequence_of_arrows_from_right=[])


                for sequence in final_list_of_sequences_of_arrows:
                    final_gen_on_DD_side=generator_from_DD
                    final_left_out=1
                    no_action_cause_no_product=False
                    for ind,arrow in enumerate(sequence):
                        if ind==0: 
                            final_left_out=dd_out_alg_left_gen(arrow)
                        else:  
                            final_left_out=DD.algebra.multiply(final_left_out,dd_out_alg_left_gen(arrow))
                            if not final_left_out: no_action_cause_no_product=True
                        if ind+1==len(sequence): final_gen_on_DD_side=dd_out_mod_gen(arrow)
                    #add differential
                    if no_action_cause_no_product==False:
                        arrows_in_tensor_product[(in_generator_of_tensor_product,
                            final_left_out,generators_of_tensor_product_by_name[final_gen_on_DD_side.name + '_' + left_a_out_mod_gen(arrow_on_A_side).name]) ]+=1

    arrows_in_tensor_product.delete_arrows_with_even_coeff()

    return Left_D_module(generators_of_tensor_product_by_name,arrows_in_tensor_product,DD.algebra,name= DD.name +'⊠'+Left_A.name)
