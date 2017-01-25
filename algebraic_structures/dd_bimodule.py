# -*- coding: utf-8 -*- 
from basics import (
    in_red,check_idempotents_match_left_left, 
    check_idempotents_match_right_left,
    check_idempotents_match_right_right)
from da_bimodule import Bunch_of_arrows

# def dd_arrow_to_str(tuplee): #works only for DD arrows
    # if len(tuplee)==4:
    #     return str(tuplee[0]) +'⊗'+ str(tuplee[1]) + "---->" + str(tuplee[2]) +'⊗'+ str(tuplee[3])  

def dd_in_mod_gen(dd_arrow):
    return dd_arrow[0]

def dd_out_left_alg_gen(dd_arrow):
    return dd_arrow[1]

def dd_out_mod_gen(dd_arrow):
    return dd_arrow[2]

def dd_out_right_alg_gen(dd_arrow):
    return dd_arrow[3]


class DD_bimodule(object):
    def __init__(self,gen_by_name,dd_arrows,left_algebra,right_algebra,name,to_check=True):
        self.name=name
        self.gen_by_name=gen_by_name
        self.genset=self.gen_by_name.values()
        #differentials are represented by bunch of dd_arrows with coefficients 1
        self.dd_arrows=dd_arrows
        self.dd_arrows.delete_arrows_with_even_coeff()
        self.left_algebra=left_algebra
        self.right_algebra=right_algebra

        if to_check==True:
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
            if not check_idempotents_match_right_left( dd_out_left_alg_gen(dd_arrow),dd_out_mod_gen(dd_arrow) ): 
                print str(dd_arrow) + '   idempotents are messed up in this dd_arrow!1'
                count_of_mismatches+=1

            # matching out left algebra and in gen
            if not check_idempotents_match_left_left( dd_in_mod_gen(dd_arrow),dd_out_left_alg_gen(dd_arrow) ): 
                print str(dd_arrow) + '   idempotents are messed up in this dd_arrow!1'
                count_of_mismatches+=1

            # matching out right algebra and out gen
            if not check_idempotents_match_right_left(dd_out_mod_gen(dd_arrow),dd_out_right_alg_gen(dd_arrow)): 
                print str(dd_arrow) + '   idempotents are messed up in this dd_arrow!1'
                count_of_mismatches+=1

            # matching out right algebra and in gen
            if not check_idempotents_match_right_right(dd_in_mod_gen(dd_arrow),dd_out_right_alg_gen(dd_arrow)): 
                print str(dd_arrow) + '   idempotents are messed up in this dd_arrow!1'
                count_of_mismatches+=1


            # we don't check the following:
            # matchings between generators if differential is pure
        return count_of_mismatches==0

    def compute_d_squared(self):
        d_squared=Bunch_of_arrows()
        
        #contribution of differential on both of outgoing algebra elements
        for arrow in self.dd_arrows:
            # left
            a = dd_out_left_alg_gen(arrow)
            if a:
                for b in [algebra_diff_arrow[1] for algebra_diff_arrow in self.left_algebra.algebra_diff_arrows if algebra_diff_arrow[0]==a]:
                    ar=(dd_in_mod_gen(arrow),b,dd_out_mod_gen(arrow),dd_out_right_alg_gen(arrow))
                    d_squared[ar]+=1

            # right
            a = dd_out_right_alg_gen(arrow)
            if a:
                for b in [algebra_diff_arrow[1] for algebra_diff_arrow in self.right_algebra.algebra_diff_arrows if algebra_diff_arrow[0]==a]:
                    ar=(dd_in_mod_gen(arrow),dd_out_left_alg_gen(arrow),dd_out_mod_gen(arrow),b)
                    d_squared[ar]+=1

        #contribution of double dd_arrows
        for dd_arrow1 in self.dd_arrows:
            for dd_arrow2 in self.dd_arrows:
                if not dd_out_mod_gen(dd_arrow1)==dd_in_mod_gen(dd_arrow2): continue
                a1a2_left=self.left_algebra.multiply(dd_out_left_alg_gen(dd_arrow1),dd_out_left_alg_gen(dd_arrow2))
                a1a2_right=self.right_algebra.multiply(dd_out_right_alg_gen(dd_arrow2),dd_out_right_alg_gen(dd_arrow1))
                if a1a2_left and a1a2_right:
                    ar=(dd_in_mod_gen(dd_arrow1),a1a2_left,dd_out_mod_gen(dd_arrow2),a1a2_right)
                    d_squared[ar]+=1
        return d_squared


# bijection = list of pairs (tuples)
# set of bijections= list of lists of pairs
# possible_images_of_generators = dictionary with keys from genset1, and values lists of gens in genset2

from da_bimodule import find_bijections

def are_equal_smart_dd(DD1,DD2):
    print 'number of generators in bimodules we compare are {} and {}'.format(str(len(DD1.genset)),str(len(DD2.genset)))
    print 'number of actions in bimodules we compare are {} and {}'.format(str(len(DD1.dd_arrows)),str(len(DD2.dd_arrows)))
    
    if len(DD1.genset)!=len(DD2.genset): 
        print 'incompatible sizes'
        return False
    
    # next we compute all the possible module homos w.r.t. idempotent ring
    possible_images_of_generators={}
    for gen1 in DD1.genset:
        possible_images_of_generators[gen1]=[]
        for gen2 in DD2.genset:
            if gen1.idem.left==gen2.idem.left and gen1.idem.right==gen2.idem.right: 
                possible_images_of_generators[gen1].append(gen2)
    
    # now, let us check if any of module homos satisfy df=0
    module_homos=find_bijections(DD1.genset,possible_images_of_generators,DD2.genset)
    for bijection in module_homos:
        f=Bunch_of_arrows()
        for pair in bijection:
            f[(pair[0],
                1,pair[1],1)]+=1
        if check_df_is_0(DD1,DD2,f): return True
    print 'there is no bijective isomorphism'
    return False


# morphism is represented by bunch of arrows, where all coefficients are 1!
# and also I assume tha there are no differentials in algebra!
def compute_df(DD1,DD2,f):
    df=Bunch_of_arrows()

    #contribution of double arrows, with morphism on the second place
    for arrow1 in DD1.dd_arrows:
        for arrow2 in [arrow2 for arrow2 in f if dd_out_mod_gen(arrow1)==dd_in_mod_gen(arrow2)]:
            left_a=DD1.left_algebra.multiply(dd_out_left_alg_gen(arrow1),dd_out_left_alg_gen(arrow2))
            right_a=DD1.right_algebra.multiply(dd_out_right_alg_gen(arrow2),dd_out_right_alg_gen(arrow1))
            if left_a and right_a:
                
                new_arrow_in_df=(dd_in_mod_gen(arrow1),
                    left_a,dd_out_mod_gen(arrow2),right_a)
                
                df[new_arrow_in_df]+=1

    #contribution of double arrows, with morphism on the first place
    for arrow1 in f:
        for arrow2 in [arrow2 for arrow2 in DD2.dd_arrows if dd_out_mod_gen(arrow1)==dd_in_mod_gen(arrow2)]:
            # if str(arrow1)='(x1, 1, x1⊗x1, 1)' and str(arrow2)=
            left_a=DD2.left_algebra.multiply(dd_out_left_alg_gen(arrow1),dd_out_left_alg_gen(arrow2))
            right_a=DD2.right_algebra.multiply(dd_out_right_alg_gen(arrow2),dd_out_right_alg_gen(arrow1))
            
            if left_a and right_a:
                new_arrow_in_df=(dd_in_mod_gen(arrow1),
                    left_a,dd_out_mod_gen(arrow2),right_a)


                df[new_arrow_in_df]+=1


    #contribution of differentials      
    for arrow in f:
        # contribution of differential on left algebra out element
        a = dd_out_left_alg_gen(arrow)
        if a:
            for b in [algebra_diff_arrow[1] for algebra_diff_arrow in DD1.left_algebra.algebra_diff_arrows if algebra_diff_arrow[0]==a]:
                new_arrow_in_df=(dd_in_mod_gen(arrow),
                            b,dd_out_mod_gen(arrow),dd_out_right_alg_gen(arrow) )
                df[new_arrow_in_df]+=1

        # contribution of differential on right algebra out element
        a = dd_out_right_alg_gen(arrow)
        if a:
            for b in [algebra_diff_arrow[1] for algebra_diff_arrow in DD2.right_algebra.algebra_diff_arrows if algebra_diff_arrow[0]==a]:
                new_arrow_in_df=(dd_in_mod_gen(arrow),
                    dd_out_left_alg_gen(arrow),dd_out_mod_gen(arrow),b)
                df[new_arrow_in_df]+=1

    return df

def check_df_is_0(DD1,DD2,f):
    df=compute_df(DD1,DD2,f)
    df.delete_arrows_with_even_coeff()
    # print '\n{\nHere are all the arrows in df'
    # df.show()
    # print '}'
    for arrow in df:
        if df[arrow] % 2 != 0:
            return False
    print 'Everything is ok, we found isomorphism f such that df=0!'
    return True




