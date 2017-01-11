# -*- coding: utf-8 -*- 
from algebra import check_idempotents_match_left_left, check_idempotents_match_right_left,check_idempotents_match_right_right
from da_bimodule import Bunch_of_arrows

def left_a_in_mod_gen(left_a_arrow):
    return left_a_arrow[1]

def left_a_in_alg_tuple(left_a_arrow):
    return left_a_arrow[0]

def left_a_out_mod_gen(left_a_arrow):
    return left_a_arrow[2]


class Left_A_module(object):
    def __init__(self,gen_by_name,left_a_arrows,algebra,name):
        self.name=name
        self.gen_by_name=gen_by_name
        self.genset=self.gen_by_name.values()
        #differentials are represented by bunch of left_a_arrows with coefficients 1
        self.left_a_arrows=left_a_arrows
        self.left_a_arrows.delete_arrows_with_even_coeff()
        self.algebra=algebra

        self.check()

    def check(self):
        ##Here we check that our " + self.name + " has all idempotents matching and d_squared=0:
        if not self.check_matching_of_idempotents_in_action():
            print "\nSomething is wrong with idempotents!"
            raise NameError("Left_A_module " + self.name + " has problems with idempotents")
        
        d_squared=self.compute_d_squared()
        d_squared.delete_arrows_with_even_coeff()
        if d_squared:
            print "d_squared is not 0! the terms that are not canceled:"
            d_squared.show()
            raise NameError("Left_A_module " + self.name + " doesn't satisfy d_squared=0.")

    def show(self):
        print "=========="
        print self.name + ':\n'
        print 'Generators with their idempotents (' + str(len(self.genset))+ ' generators)'
        for gen in self.genset:
            print str(gen.idem.left) + '___'  + str(gen)

        print '\nActions:'
        for left_a_arrow in self.left_a_arrows:
            print str(left_a_arrow)


    def check_matching_of_idempotents_in_action(self): 
        count_of_mismatches=0
        for left_a_arrow in self.left_a_arrows:

            # matching in last element of algebra and in gen
            if len(left_a_in_alg_tuple(left_a_arrow))!=0:
                if not check_idempotents_match_right_left(left_a_in_alg_tuple(left_a_arrow)[-1],left_a_in_mod_gen(left_a_arrow)): 
                    print str(left_a_arrow) + '   idempotents are messed up in this left_a_arrow!1'
                    count_of_mismatches+=1
            
            # matching algebra elements between themselves, and with in generator
            for i in range(len(left_a_in_alg_tuple(left_a_arrow))):
                if (i==0):
                    #matching in algebra and gen
                    if not check_idempotents_match_left_left(left_a_out_mod_gen(left_a_arrow),left_a_in_alg_tuple(left_a_arrow)[0]): 
                        print str(left_a_arrow) + '   idempotents are messed up in this left_a_arrow!1'
                        count_of_mismatches+=1  
                else:
                    #matching in algebras
                    if not check_idempotents_match_right_left(left_a_in_alg_tuple(left_a_arrow)[i-1],left_a_in_alg_tuple(left_a_arrow)[i]): 
                        print left_a_arrow
                        count_of_mismatches+=1
            
        return count_of_mismatches==0

    def compute_d_squared(self):
        d_squared=Bunch_of_arrows()

        #contribution of double left_a_arrows
        for arrow1 in self.left_a_arrows:
            for arrow2 in self.left_a_arrows:
                if not left_a_out_mod_gen(arrow1)==left_a_in_mod_gen(arrow2): continue
                ar=(left_a_in_alg_tuple(arrow2) + left_a_in_alg_tuple(arrow1), left_a_in_mod_gen(arrow1)
                                ,left_a_out_mod_gen(arrow2))
                d_squared[ar]+=1


        #contribution of factorizing algebra elements        
        for arrow in self.left_a_arrows:
            for index, a in enumerate(left_a_in_alg_tuple(arrow)):
                for factorization in getattr(a,'factorizations', []):
                    new_tuple=left_a_in_alg_tuple(arrow)[:index] + factorization + left_a_in_alg_tuple(arrow)[index+1:]
                    ar=( new_tuple,left_a_in_mod_gen(arrow),
                        left_a_out_mod_gen(arrow))
                    d_squared[ar]+=1

        return d_squared


