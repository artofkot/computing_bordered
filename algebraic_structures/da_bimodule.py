# -*- coding: utf-8 -*- 
import time
from basics import AttrDict 
from algebra import Generator, torus_A, check_idempotents_match_left_left, check_idempotents_match_right_left,check_idempotents_match_right_right
from collections import Counter
from itertools import permutations
from random import shuffle
from basics import Bunch_of_arrows


def da_arrow_to_str(tuplee): #works only for DA arrows
    if len(tuplee)==4:
        return str(tuplee[0]) +'⊗'+ str(tuplee[1]) + "---->" + str(tuplee[2]) +'⊗'+ str(tuplee[3])  

def da_in_mod_gen(da_arrow):
    return da_arrow[0]

def da_in_alg_tuple(da_arrow):
    return da_arrow[1]

def da_out_alg_gen(da_arrow):
    return da_arrow[2]

def da_out_mod_gen(da_arrow):
    return da_arrow[3]

# conventions: D side is left, A side is right
class DA_bimodule(object):
    def __init__(self,gen_by_name,da_arrows,algebra,name):
        self.name=name
        self.gen_by_name=gen_by_name
        self.genset=self.gen_by_name.values()
        #differentials are represented by bunch of arrows with coefficients 1
        self.arrows=da_arrows
        self.arrows.delete_arrows_with_even_coeff()
        self.algebra=algebra

        self.check()

    def check(self):
        ##Here we check that our " + self.name + " has all idempotents matching and d_squared=0:
        
        if not self.check_matching_of_idempotents_in_action():
            print "\nSomething is wrong with idempotents!"
            raise NameError("DA_bimodule " + self.name + " has problems with idempotents")
        
        d_squared=self.compute_d_squared()
        d_squared.delete_arrows_with_even_coeff()
        if d_squared:
            print "d_squared is not 0! the terms that are not canceled:"
            d_squared.show()
            raise NameError("DA_bimodule " + self.name + " doesn't satisfy d_squared=0.")


    def show(self):
        print "=========="
        print self.name + ':\n'
        print 'Generators with their idempotents (' + str(len(self.genset))+ ' generators)'
        for gen in self.genset:
            print str(gen.idem.left) + '___' + str(gen) + '___' + str(gen.idem.right)

        print '\nActions'
        for generator1 in self.genset:
            for generator2 in self.genset:
                arrows=[arrow for arrow in self.arrows if (da_in_mod_gen(arrow)==generator1 and da_out_mod_gen(arrow)==generator2)]
                if len(arrows)!=0:
                    print generator1
                    print "↓",
                    for ind, arrow in enumerate(arrows):
                        print str(da_out_alg_gen(arrow)) + '⊗' + str(da_in_alg_tuple(arrow)),
                        if ind+1!=len(arrows): print '+',
                    print '\n' + str(generator2) + '\n'
                
        # for arrow in self.arrows:
        #     print da_arrow_to_str(arrow)



    def show_for_tex(self):
        print '============='
        print self.name + ':\n'
        print str(len(self.genset)) + ' generators with their idempotents: \n'
        for gen in self.genset:
            # _{i_2}{(t_{12})}_{i_2}
            print '$_{' + str(gen.idem.left) + '}{(' + str(gen) + ')}_{' + str(gen.idem.right) +'}$,'

        print '\nActions:\n'
        for generator1 in self.genset:
            for generator2 in self.genset:
                arrows=[arrow for arrow in self.arrows if (da_in_mod_gen(arrow)==generator1 and da_out_mod_gen(arrow)==generator2)]
                if len(arrows)!=0:
                    for arrow in arrows:
                        print '$'+str(da_in_mod_gen(arrow)) +'\\otimes ' + str(da_in_alg_tuple(arrow)) + '\\rightarrow ' + str(da_out_alg_gen(arrow)) +'\\otimes '+ str(da_out_mod_gen(arrow)) + '$, '
                
                
        # for arrow in self.arrows:
        #     print da_arrow_to_str(arrow)

    def show_short(self):
        print "=========="
        print self.name
        print str(len(self.genset))+ ' generators with their idempotents (' + str(len(self.genset))+ ' generators)'
        for gen in self.genset:
            print str(gen.idem.left) + '___' + str(gen) + '___' + str(gen.idem.right)


    def check_matching_of_idempotents_in_action(self): 
        count_of_mismatches=0
        for da_arrow in self.arrows:

            # matching out algebra and out gen
            if not check_idempotents_match_right_left( da_out_alg_gen(da_arrow),da_out_mod_gen(da_arrow) ): 
                print da_arrow 
                count_of_mismatches+=1

            # matching out algebra and in gen
            if not check_idempotents_match_left_left( da_in_mod_gen(da_arrow),da_out_alg_gen(da_arrow) ): 
                print da_arrow_to_str(da_arrow) + '   idempotents are messed up in this da_arrow!1'
                count_of_mismatches+=1

            # matching in last element of algebra and out gen
            if len(da_in_alg_tuple(da_arrow))!=0:
                if not check_idempotents_match_right_right( da_in_alg_tuple(da_arrow)[-1],da_out_mod_gen(da_arrow) ): 
                    print da_arrow_to_str(da_arrow) + '   idempotents are messed up in this da_arrow!2'
                    count_of_mismatches+=1
            
            for i in range(len(da_in_alg_tuple(da_arrow))):
                if (i==0):
                    #matching in algebra and gen
                    if not check_idempotents_match_right_left(da_in_mod_gen(da_arrow),da_in_alg_tuple(da_arrow)[0]): 
                        print da_arrow_to_str(da_arrow) + '   idempotents are messed up in this da_arrow!3'
                        count_of_mismatches+=1
                else:
                    #matching in algebras
                    if not check_idempotents_match_right_left(da_in_alg_tuple(da_arrow)[i-1],da_in_alg_tuple(da_arrow)[i]): 
                        print da_arrow
                        count_of_mismatches+=1
        return count_of_mismatches==0

    def compute_d_squared(self):
        d_squared=Bunch_of_arrows()
        #contribution of double arrows
        for arrow1 in self.arrows:
            for arrow2 in self.arrows:
                if not da_out_mod_gen(arrow1)==da_in_mod_gen(arrow2): continue
                a1a2=self.algebra.multiply(da_out_alg_gen(arrow1),da_out_alg_gen(arrow2))
                if a1a2:
                    ar=(da_in_mod_gen(arrow1), da_in_alg_tuple(arrow1) + da_in_alg_tuple(arrow2),a1a2,da_out_mod_gen(arrow2))
                    d_squared[ar]+=1


        #contribution of factorizing algebra elements        
        for arrow in self.arrows:
            for index, a in enumerate(da_in_alg_tuple(arrow)):
                for factorization in getattr(a,'factorizations', []):
                    new_tuple=da_in_alg_tuple(arrow)[:index] + factorization + da_in_alg_tuple(arrow)[index+1:]
                    ar=(da_in_mod_gen(arrow), new_tuple,
                        da_out_alg_gen(arrow),da_out_mod_gen(arrow))
                    d_squared[ar]+=1

        return d_squared

def cancel_pure_differential(DAbimodule_old,pure_differential):
    #z1--->z2
    z1=da_in_mod_gen(pure_differential)
    z2=da_out_mod_gen(pure_differential)

    #form generators
    generators_of_new_DA=DAbimodule_old.gen_by_name
    del generators_of_new_DA[z1.name]
    del generators_of_new_DA[z2.name]

    #form old differentials
    old_arrows_that_survive=[arrow for arrow in DAbimodule_old.arrows if (da_out_mod_gen(arrow)!=z1 and da_out_mod_gen(arrow)!=z2  and da_in_mod_gen(arrow)!=z1 and da_in_mod_gen(arrow)!=z2 ) ]
    arrows_in_new_DA=Bunch_of_arrows(old_arrows_that_survive)

    #form new differentials
    arrows_in_z2=[arrow for arrow in DAbimodule_old.arrows if (da_out_mod_gen(arrow)==z2 and da_in_mod_gen(arrow)!=z1 and da_in_mod_gen(arrow)!=z2)]
    arrows_from_z1=[arrow for arrow in DAbimodule_old.arrows if (da_in_mod_gen(arrow)==z1 and da_out_mod_gen(arrow)!=z2 and da_out_mod_gen(arrow)!=z1)]

    for arrow_in_z2 in arrows_in_z2:
        for arrow_from_z1 in arrows_from_z1:
            new_out_alg_gen=DAbimodule_old.algebra.multiply(da_out_alg_gen(arrow_in_z2),da_out_alg_gen(arrow_from_z1))

            if new_out_alg_gen:
                new_arrow=(da_in_mod_gen(arrow_in_z2), da_in_alg_tuple(arrow_in_z2)+da_in_alg_tuple(arrow_from_z1),
                    new_out_alg_gen,da_out_mod_gen(arrow_from_z1) )
                arrows_in_new_DA[new_arrow]+=1


    arrows_in_new_DA.delete_arrows_with_even_coeff()

    return DA_bimodule(generators_of_new_DA,arrows_in_new_DA,DAbimodule_old.algebra,name= DAbimodule_old.name +'_red')

def randomly_cancel_until_possible(DA1):
    there_is_diff=0
    # arrs=DA1.arrows
    arrs=list(DA1.arrows)
    shuffle(arrs)
    for arrow in arrs:
        if (da_in_alg_tuple(arrow)==() and da_out_alg_gen(arrow)==1 and da_in_mod_gen(arrow)!=da_out_mod_gen(arrow)):
            there_is_diff=1

            canceled_DA=cancel_pure_differential(DA1,arrow)

            return (randomly_cancel_until_possible(canceled_DA))

    if there_is_diff==0:
        return DA1

def cancel_this_number_of_times(DA1,n):
    if n==0: return DA1

    there_is_diff=0
    for arrow in DA1.arrows:
        if (da_in_alg_tuple(arrow)==() and da_out_alg_gen(arrow)==1):
            there_is_diff=1
            canceled_DA=cancel_pure_differential(DA1,arrow)
            return (cancel_this_number_of_times(canceled_DA,n-1))

    if there_is_diff==0:
        return DA1

# bijection = list of pairs (tuples)
# set of bijections= list of lists of pairs
def find_bijections(genset1,possible_images_of_generators,genset2):
    # print genset1

    if len(genset1)!=len(genset2): raise NameError("tried to find bijections between different size sets")
    if len(genset1)==1:
        gen1=genset1[0]
        gen2=genset2[0]
        if gen2 in possible_images_of_generators[gen1]: 
            all_bijections=[[(gen1,gen2)]]
        else: all_bijections=[]
    else:
        all_bijections=[]
        gen1=genset1[0]
        # if len(genset1)==10:
        #     print gen1
        for gen2 in possible_images_of_generators[gen1]:
            if not gen2 in genset2:continue
            # print possible_images_of_generators[gen1]
            # print str(gen1) +' '+ str(gen2)
            a1=list(genset1)
            a2=list(genset2)
            a1.remove(gen1)
            a2.remove(gen2)
            bijections_in_the_rest=find_bijections(a1,possible_images_of_generators,a2)
            bijections_with_fixed_first_pair=[bij+[(gen1,gen2)] for bij in bijections_in_the_rest]
            all_bijections=all_bijections+bijections_with_fixed_first_pair
    return all_bijections
    
def are_equal_smart(DA1,DA2):
    from morphism import check_df_is_0
    if len(DA1.genset)!=len(DA2.genset): return False
    print 'number of generators in bimodules we compare is ' + str(len(DA1.genset))
    
    # next we compute all the possible module homos w.r.t. idempotent ring
    possible_images_of_generators={}
    for gen1 in DA1.genset:
        possible_images_of_generators[gen1]=[]
        for gen2 in DA2.genset:
            if gen1.idem.left==gen2.idem.left and gen1.idem.right==gen2.idem.right: 
                possible_images_of_generators[gen1].append(gen2)
    # now, let us check any of module homos satisfy df=0
    
    # print find_bijections(['x','z'],{'x':['y','t'],'z':['y','t']},['y','t'])
    module_homos=find_bijections(DA1.genset,possible_images_of_generators,DA2.genset)
    
    for bijection in module_homos:
        f=Bunch_of_arrows()
        for pair in bijection:
            f[(pair[0],(),
                1,pair[1])]+=1
        if check_df_is_0(DA1,DA2,f): return True
    print 'there is no bijective isomorphism'
    return False




