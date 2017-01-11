# -*- coding: utf-8 -*- 
from algebra import check_idempotents_match_left_left, check_idempotents_match_right_left,check_idempotents_match_right_right
from da_bimodule import Bunch_of_arrows

# def dd_arrow_to_str(tuplee): #works only for DD arrows
    # if len(tuplee)==4:
    #     return str(tuplee[0]) +'⊗'+ str(tuplee[1]) + "---->" + str(tuplee[2]) +'⊗'+ str(tuplee[3])  

def dd_in_mod_gen(dd_arrow):
    return dd_arrow[0]

def dd_out_alg_left_gen(dd_arrow):
    return dd_arrow[1]

def dd_out_mod_gen(dd_arrow):
    return dd_arrow[2]

def dd_out_alg_right_gen(dd_arrow):
    return dd_arrow[3]


class DD_bimodule(object):
    def __init__(self,gen_by_name,dd_arrows,algebra,name):
        self.name=name
        self.gen_by_name=gen_by_name
        self.genset=self.gen_by_name.values()
        #differentials are represented by bunch of dd_arrows with coefficients 1
        self.dd_arrows=dd_arrows
        self.dd_arrows.delete_arrows_with_even_coeff()
        self.algebra=algebra

        self.check()

    def check(self):
        ##Here we check that our " + self.name + " has all idempotents matching and d_squared=0:
        if not self.check_matching_of_idempotents_in_action():
            print "\nSomething is wrong with idempotents!"
            raise NameError("DD_bimodule " + self.name + " has problems with idempotents")
        
        d_squared=self.compute_d_squared()
        d_squared.delete_arrows_with_even_coeff()
        if d_squared:
            print "d_squared is not 0! the terms that are not canceled:"
            d_squared.show()
            raise NameError("DD_bimodule " + self.name + " doesn't satisfy d_squared=0.")

    def show(self):
        print "=========="
        print self.name + ':\n'
        print 'Generators with their idempotents (' + str(len(self.genset))+ ' generators)'
        for gen in self.genset:
            print str(gen.idem.left) + '___' + str(gen) + '___' + str(gen.idem.right)

        print '\nActions:'
        for dd_arrow in self.dd_arrows:
            print str(dd_arrow)


    def check_matching_of_idempotents_in_action(self): 
        count_of_mismatches=0
        for dd_arrow in self.dd_arrows:

            # matching out left algebra and out gen
            if not check_idempotents_match_right_left( dd_out_alg_left_gen(dd_arrow),dd_out_mod_gen(dd_arrow) ): 
                print str(dd_arrow) + '   idempotents are messed up in this dd_arrow!1'
                count_of_mismatches+=1

            # matching out left algebra and in gen
            if not check_idempotents_match_left_left( dd_in_mod_gen(dd_arrow),dd_out_alg_left_gen(dd_arrow) ): 
                print str(dd_arrow) + '   idempotents are messed up in this dd_arrow!1'
                count_of_mismatches+=1

            # matching out right algebra and out gen
            if not check_idempotents_match_right_left(dd_out_mod_gen(dd_arrow),dd_out_alg_right_gen(dd_arrow)): 
                print str(dd_arrow) + '   idempotents are messed up in this dd_arrow!1'
                count_of_mismatches+=1

            # matching out right algebra and in gen
            if not check_idempotents_match_right_right(dd_in_mod_gen(dd_arrow),dd_out_alg_right_gen(dd_arrow)): 
                print str(dd_arrow) + '   idempotents are messed up in this dd_arrow!1'
                count_of_mismatches+=1
        return count_of_mismatches==0

    def compute_d_squared(self):
        d_squared=Bunch_of_arrows()
        #contribution of double dd_arrows
        for dd_arrow1 in self.dd_arrows:
            for dd_arrow2 in self.dd_arrows:
                if not dd_out_mod_gen(dd_arrow1)==dd_in_mod_gen(dd_arrow2): continue
                a1a2_left=self.algebra.multiply(dd_out_alg_left_gen(dd_arrow1),dd_out_alg_left_gen(dd_arrow2))
                a1a2_right=self.algebra.multiply(dd_out_alg_right_gen(dd_arrow2),dd_out_alg_right_gen(dd_arrow1))
                if a1a2_left and a1a2_right:
                    ar=(dd_in_mod_gen(dd_arrow1),a1a2_left,dd_out_mod_gen(dd_arrow2),a1a2_right)
                    d_squared[ar]+=1
        return d_squared





