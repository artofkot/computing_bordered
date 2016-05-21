# -*- coding: utf-8 -*- 
from utility import AttrDict 
from algebra import Generator, torus_algebra, check_idempotents_match_left_left, check_idempotents_match_left_right,check_idempotents_match_right_right
from collections import Counter
from itertools import permutations

# conventions: D side is left, A side is right
class DA_bimodule(object):
    def __init__(self,gen_by_name,arrows,algebra,name):
        self.name=name
        self.gen_by_name=gen_by_name
        self.genset=self.gen_by_name.values()
        #differentials are represented by bunch of arrows with coefficients 1
        self.arrows=arrows
        self.arrows.delete_arrows_with_even_coeff()
        self.algebra=algebra

        

        dd=self.compute_dd()
        dd.delete_arrows_with_even_coeff()

        if dd:
            if name=="g2_M_RHD": dd.show()
            raise NameError("DA_bimodule " + self.name + " doesn't satisfy dd=0 !!!")

    
    def show(self):
        print "=========="
        print self.name + ':\n'
        print 'Generators with their idempotents'
        for gen in self.genset:
            print str(gen.idem.left) + '___' + str(gen) + '___' + str(gen.idem.right)

        print '\nActions'
        for generator1 in self.genset:
            for generator2 in self.genset:
                arrows=[arrow for arrow in self.arrows if (in_mod_gen(arrow)==generator1 and out_mod_gen(arrow)==generator2)]
                if len(arrows)!=0:
                    print generator1
                    print "↓",
                    for ind, arrow in enumerate(arrows):
                        print str(out_alg_gen(arrow)) + '⊗' + str(in_alg_tuple(arrow)),
                        if ind+1!=len(arrows): print '+',
                    print '\n' + str(generator2) + '\n'
                
        # for arrow in self.arrows:
        #     print arrow_to_str(arrow)

    def check_matching_of_idempotents_in_action(self): 
        count_of_mismatches=0
        for arrow in self.arrows:

            # matching out algebra and out gen
            if not check_idempotents_match_left_right( out_alg_gen(arrow),out_mod_gen(arrow) ): 
                print arrow 
                count_of_mismatches+=1

            # matching out algebra and in gen
            if not check_idempotents_match_left_left( in_mod_gen(arrow),out_alg_gen(arrow) ): 
                print arrow_to_str(arrow) + '   idempotents are messed up in this arrow!1'
                count_of_mismatches+=1

            # matching in last element of algebra and out gen
            if len(in_alg_tuple(arrow))!=0:
                if not check_idempotents_match_right_right( in_alg_tuple(arrow)[-1],out_mod_gen(arrow) ): 
                    print arrow_to_str(arrow) + '   idempotents are messed up in this arrow!2'
                    count_of_mismatches+=1
            
            for i in range(len(in_alg_tuple(arrow))):
                if (i==0):
                    #matching in algebra and gen
                    if not check_idempotents_match_left_right(in_mod_gen(arrow),in_alg_tuple(arrow)[0]): 
                        print arrow_to_str(arrow) + '   idempotents are messed up in this arrow!3'
                        count_of_mismatches+=1
                else:
                    #matching in algebras
                    if not check_idempotents_match_left_right(in_alg_tuple(arrow)[i-1],in_alg_tuple(arrow)[i]): 
                        print arrow
                        count_of_mismatches+=1
        return count_of_mismatches==0

    def compute_dd(self):
        dd=Bunch_of_arrows()
        #contribution of double arrows
        for arrow1 in self.arrows:
            for arrow2 in self.arrows:
                if not out_mod_gen(arrow1)==in_mod_gen(arrow2): continue
                a1a2=self.algebra.multiply(out_alg_gen(arrow1),out_alg_gen(arrow2))
                if a1a2:
                    ar=(in_mod_gen(arrow1), in_alg_tuple(arrow1) + in_alg_tuple(arrow2),a1a2,out_mod_gen(arrow2))
                    dd[ar]+=1


        #contribution of factorizing algebra elements        
        for arrow in self.arrows:

            for index, a in enumerate(in_alg_tuple(arrow)):
                for factorization in getattr(a,'factorizations', []):
                    new_tuple=in_alg_tuple(arrow)[:index] + factorization + in_alg_tuple(arrow)[index+1:]
                    ar=(in_mod_gen(arrow), new_tuple,
                        out_alg_gen(arrow),out_mod_gen(arrow))
                    # if arrow_to_str(arrow)=="x1⊗(r45,)---->r45⊗x3" and self.name=="g2_M_RHD": 
                    #     print 'yo'
                    #     print factorization
                    #     print ar
                    dd[ar]+=1

        return dd

    def check_dd_is_0(self):
        dd=self.compute_dd()

        # print '\n{\nHere are all the arrows in dd'
        # dd.show()
        # print '}'



        for arrow in dd:
            if dd[arrow] % 2 != 0:
                return False
        return True

    def check(self):
        print "========\nHere we check that our " + self.name + " has all idempotents matching and dd=0:"
        t=self.check_matching_of_idempotents_in_action()

        if not t:
            print "\nSomething is wrong with idempotents!"
        else: print "\nEverything is ok, idempotents match!"
        
        if not self.check_dd_is_0():
            print "Something is wrong with dd=0!"
        else: print "Everything is ok, dd=0!"

    # def differential_of_generator_and_a_tuple(self, gen1, alg_tuple): #gives element in AtensorM
    #     s=Counter()
    #     for arrow in self.arrows: 
    #         if (in_mod_gen(arrow)==gen1 and in_alg_tuple(arrow)==alg_tuple):
    #             s[GeneratorA_tensor_M( out_alg_gen(arrow),out_mod_gen(arrow) )]+=1
    #     return s

class GeneratorA_tensor_M(object):
    def __init__(self, alg_gen,mod_gen):
        self.name=(alg_gen,mod_gen)
        self.alg_gen = alg_gen
        self.mod_gen = mod_gen

    def add_idems(self,idem1,idem2):
        self.idem=AttrDict({"left":idem1, "right":idem2})

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

class Bunch_of_arrows(Counter):
    def show(self):
        for arrow_as_a_tuple in self:
            print arrow_to_str(arrow_as_a_tuple) + '     *' + str(self[arrow_as_a_tuple])

    def delete_arrows_with_even_coeff(self): 
        arrows_to_delete=[]
        for arrow in self:
            if self[arrow] % 2 ==0:
                arrows_to_delete.append(arrow)
            else:
                self[arrow]=1

        for ar in arrows_to_delete:
            del self[ar]



def arrow_to_str(tuplee):
    if len(tuplee)==4:
        return str(tuplee[0]) +'⊗'+ str(tuplee[1]) + "---->" + str(tuplee[2]) +'⊗'+ str(tuplee[3])

    if len(tuplee)==2:
        return str(tuplee[0]) + "---->" + str(tuplee[1])    

def in_mod_gen(arrow):
    return arrow[0]

def in_alg_tuple(arrow):
    return arrow[1]

def out_alg_gen(arrow):
    return arrow[2]

def out_mod_gen(arrow):
    return arrow[3]

# def delete_arrows_with_even_coeff(arrows):
#     arrows_to_delete=[]
#     for arrow in arrows:
#         if arrows[arrow] % 2 ==0:
#             arrows_to_delete.append(arrow)
#         else:
#             arrows[arrow]=1

#     for ar in arrows_to_delete:
#         del arrows[ar]

def cancel_pure_differential(DAbimodule_old,pure_differential):
    #z1--->z2
    z1=in_mod_gen(pure_differential)
    z2=out_mod_gen(pure_differential)

    #form generators
    generators_of_new_DA=DAbimodule_old.gen_by_name
    del generators_of_new_DA[z1.name]
    del generators_of_new_DA[z2.name]

    #form old differentials
    old_arrows_that_survive=[arrow for arrow in DAbimodule_old.arrows if (out_mod_gen(arrow)!=z1 and out_mod_gen(arrow)!=z2  and in_mod_gen(arrow)!=z1 and in_mod_gen(arrow)!=z2 ) ]
    arrows_in_new_DA=Bunch_of_arrows(old_arrows_that_survive)

    #form new differentials
    arrows_in_z2=[arrow for arrow in DAbimodule_old.arrows if (out_mod_gen(arrow)==z2 and in_mod_gen(arrow)!=z1 and in_mod_gen(arrow)!=z2)]
    arrows_from_z1=[arrow for arrow in DAbimodule_old.arrows if (in_mod_gen(arrow)==z1 and out_mod_gen(arrow)!=z2 and out_mod_gen(arrow)!=z1)]

    for arrow_in_z2 in arrows_in_z2:
        for arrow_from_z1 in arrows_from_z1:
            new_out_alg_gen=DAbimodule_old.algebra.multiply(out_alg_gen(arrow_in_z2),out_alg_gen(arrow_from_z1))

            if new_out_alg_gen:
                new_arrow=(in_mod_gen(arrow_in_z2), in_alg_tuple(arrow_in_z2)+in_alg_tuple(arrow_from_z1),
                    new_out_alg_gen,out_mod_gen(arrow_from_z1) )
                arrows_in_new_DA[new_arrow]+=1


    arrows_in_new_DA.delete_arrows_with_even_coeff()

    return DA_bimodule(generators_of_new_DA,arrows_in_new_DA,DAbimodule_old.algebra,name= DAbimodule_old.name +'_red')

def randomly_cancel_until_possible(DA1):
    there_is_diff=0
    for arrow in DA1.arrows:
        if (in_alg_tuple(arrow)==() and out_alg_gen(arrow)==1 and in_mod_gen(arrow)!=out_mod_gen(arrow)):
            there_is_diff=1

            canceled_DA=cancel_pure_differential(DA1,arrow)

            return (randomly_cancel_until_possible(canceled_DA))

    if there_is_diff==0:
        return DA1

def cancel_this_number_of_times(DA1,n):
    if n==0: return DA1

    there_is_diff=0
    for arrow in DA1.arrows:
        if (in_alg_tuple(arrow)==() and out_alg_gen(arrow)==1):
            there_is_diff=1
            canceled_DA=cancel_pure_differential(DA1,arrow)
            return (cancel_this_number_of_times(canceled_DA,n-1))

    if there_is_diff==0:
        return DA1


def are_equal(DA1,DA2):
    from morphism import check_df_is_0
    if len(DA1.genset)!=len(DA2.genset): return False

    perms=permutations(DA1.genset,len(DA1.genset))
    for perm in perms:
        f=Bunch_of_arrows()
        for ind,gen in enumerate(perm):
            f[(gen,(),
                1,DA2.genset[ind])]+=1
        if check_df_is_0: return True
    return False



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
            arrows_to_continue=[arrow for arrow in arrows if (out_alg_gen(arrow)==needed_alg_tuple_to_finish_sequence[0] and current_gen==in_mod_gen(arrow))]
            for arrow in arrows_to_continue:
                # print 'presequence of arrows: '
                # for ar in presequence_of_arrows_from_right:
                #     print arrow_to_str(ar) + ', ',
                # print '\n'
                # print needed_alg_tuple_to_finish_sequence[1:]

                find_sequence_for_box_tensor_product(final_list_of_sequences_of_arrows,
                                                    needed_alg_tuple_to_finish_sequence[1:],
                                                    out_mod_gen(arrow),
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
            arrows_inDA2_without_out_alg_gen=[arrow for arrow in DAbimodule2.arrows if (in_mod_gen(arrow)==generator_from_DA2 and out_alg_gen(arrow)==1)]
            for ar in arrows_inDA2_without_out_alg_gen:
                #add differential
                arrows_in_tensor_product[(in_generator_of_tensor_product,in_alg_tuple(ar),
                    1,generators_of_tensor_product_by_name[generator_from_DA1.name+'_'+out_mod_gen(ar).name]) ]+=1

            #differentials with one action on the left DAbimodule1 and multiple on the right DAbimodule2
            for arrow_on_DA1_side in [arrow for arrow in DAbimodule1.arrows if (in_mod_gen(arrow)==generator_from_DA1)]:
                # print 'matching this arrow on the DA1 side: ' + arrow_to_str(arrow_on_DA1_side)
                final_list_of_sequences_of_arrows=[]
                find_sequence_for_box_tensor_product(final_list_of_sequences_of_arrows,
                                                    in_alg_tuple(arrow_on_DA1_side),
                                                    generator_from_DA2,
                                                    DAbimodule2.arrows,
                                                    presequence_of_arrows_from_right=[])

                for sequence in final_list_of_sequences_of_arrows:
                    final_right_action=()
                    final_gen_on_DA2_side=generator_from_DA2
                    for ind,arrow in enumerate(sequence): 
                        final_right_action=final_right_action+in_alg_tuple(arrow)
                        if ind+1==len(sequence): final_gen_on_DA2_side=out_mod_gen(arrow)
                    #add differential
                    arrows_in_tensor_product[(in_generator_of_tensor_product,final_right_action,
                    out_alg_gen(arrow_on_DA1_side),generators_of_tensor_product_by_name[out_mod_gen(arrow_on_DA1_side).name+'_'+final_gen_on_DA2_side.name]) ]+=1

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
    return tensor_prod
