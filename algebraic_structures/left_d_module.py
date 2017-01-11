# -*- coding: utf-8 -*- 
from algebra import check_idempotents_match_left_left, check_idempotents_match_right_left,check_idempotents_match_right_right
from basics import Bunch_of_arrows

def left_d_in_mod_gen(left_d_arrow):
    return left_d_arrow[0]

def left_d_out_alg_gen(left_d_arrow):
    return left_d_arrow[1]

def left_d_out_mod_gen(left_d_arrow):
    return left_d_arrow[2]


class Left_D_module(object):
    def __init__(self,gen_by_name,left_d_arrows,algebra,name):
        self.name=name
        self.gen_by_name=gen_by_name
        self.genset=self.gen_by_name.values()
        #differentials are represented by bunch of left_d_arrows with coefficients 1
        self.left_d_arrows=left_d_arrows
        self.left_d_arrows.delete_arrows_with_even_coeff()
        self.algebra=algebra

        self.check()

    def check(self):
        ##Here we check that our " + self.name + " has all idempotents matching and d_squared=0:
        if not self.check_matching_of_idempotents_in_action():
            print "\nSomething is wrong with idempotents!"
            raise NameError("Left_D_module " + self.name + " has problems with idempotents")
        
        d_squared=self.compute_d_squared()
        d_squared.delete_arrows_with_even_coeff()
        if d_squared:
            print "d_squared is not 0! the terms that are not canceled:"
            d_squared.show()
            raise NameError("Left_D_module " + self.name + " doesn't satisfy d_squared=0.")

    def show(self):
        print "=========="
        print self.name + ':\n'
        print 'Generators with their idempotents (' + str(len(self.genset))+ ' generators)'
        for gen in self.genset:
            print str(gen.idem.left) + '___'  + str(gen)

        print '\nActions:'
        for left_d_arrow in self.left_d_arrows:
            print str(left_d_arrow)


    def check_matching_of_idempotents_in_action(self): 
        count_of_mismatches=0
        for left_d_arrow in self.left_d_arrows:
            # matching out alg gen and out mod gen
            if not check_idempotents_match_right_left(left_d_out_alg_gen(left_d_arrow),left_d_out_mod_gen(left_d_arrow)): 
                print str(left_d_arrow) + '   idempotents are messed up in this left_d_arrow!1'
                count_of_mismatches+=1
            
            # matching out alg gen and in mod gen
            if not check_idempotents_match_left_left(left_d_out_alg_gen(left_d_arrow),left_d_in_mod_gen(left_d_arrow)): 
                print str(left_d_arrow) + '   idempotents are messed up in this left_d_arrow!1'
                count_of_mismatches+=1
            
        return count_of_mismatches==0

    def compute_d_squared(self):
        d_squared=Bunch_of_arrows()

        #contribution of double left_d_arrows
        for arrow1 in self.left_d_arrows:
            for arrow2 in self.left_d_arrows:
                if not left_d_out_mod_gen(arrow1)==left_d_in_mod_gen(arrow2): continue
                new_alg_gen=self.algebra.multiply(left_d_out_alg_gen(arrow1),left_d_out_alg_gen(arrow2))
                if not new_alg_gen: continue
                ar=(left_d_in_mod_gen(arrow1),
                    new_alg_gen,left_d_out_mod_gen(arrow2))
                d_squared[ar]+=1

        return d_squared



