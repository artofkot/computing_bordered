# -*- coding: utf-8 -*- 
from basics import debug, check_idempotents_match_left_left, check_idempotents_match_right_left,check_idempotents_match_right_right
from basics import Bunch_of_arrows, AttrDict, Generator
from random import shuffle

# def aa_arrow_to_str(tuplee): #works only for aa arrows
    # if len(tuplee)==4:
    #     return str(tuplee[0]) +'⊗'+ str(tuplee[1]) + "---->" + str(tuplee[2]) +'⊗'+ str(tuplee[3])  

def aa_in_left_alg_tuple(aa_arrow):
    return aa_arrow[0]

def aa_in_mod_gen(aa_arrow):
    return aa_arrow[1]

def aa_in_right_alg_tuple(aa_arrow):
    return aa_arrow[2]

def aa_out_mod_gen(aa_arrow):
    return aa_arrow[3]


class AA_bimodule(object):
    def __init__(self,gen_by_name,aa_arrows,left_algebra,right_algebra,name,to_check=True):
        self.name=name
        self.gen_by_name=gen_by_name
        self.genset=self.gen_by_name.values()
        #differentials are represented by bunch of aa_arrows with coefficients 1
        self.aa_arrows=aa_arrows
        self.aa_arrows.delete_arrows_with_even_coeff()
        self.left_algebra=left_algebra
        self.right_algebra=right_algebra

        if to_check==True and len(self.genset)<33:
            self.check()

    def check(self):
        ##Here we check that our " + self.name + " has all idempotents matching and d_squared=0:
        if not self.check_matching_of_idempotents_in_action():
            print "\nSomething is wrong with idempotents!"
            raise NameError("aa_bimodule " + self.name + " has problems with idempotents")
        
        d_squared=self.compute_d_squared()
        d_squared.delete_arrows_with_even_coeff()
        if d_squared:
            print "d_squared is not 0! the terms that are not canceled:"
            d_squared.show()
            raise NameError("aa_bimodule " + self.name + " doesn't satisfy d_squared=0.")

    def show(self):
        print "=========="
        print self.name + ':\n'
        print 'Generators with their idempotents (' + str(len(self.genset))+ ' generators)'
        for gen in self.genset:
            print str(gen.idem.left) + '___' + str(gen) + '___' + str(gen.idem.right)

        print '\nActions:'
        for aa_arrow in self.aa_arrows:
            print str(aa_arrow)


    def check_matching_of_idempotents_in_action(self): 
        count_of_mismatches=0
        for aa_arrow in self.aa_arrows:

            # matching out left algebra tuple and out gen
            if len(aa_in_left_alg_tuple(aa_arrow))!=0:
                if not check_idempotents_match_left_left( aa_in_left_alg_tuple(aa_arrow)[0],aa_out_mod_gen(aa_arrow) ): 
                    print str(aa_arrow) + '   idempotents are messed up in this aa_arrow!1'
                    count_of_mismatches+=1

            # matching out left algebra tuple and in gen
            if len(aa_in_left_alg_tuple(aa_arrow))!=0:
                if not check_idempotents_match_right_left( aa_in_left_alg_tuple(aa_arrow)[-1],aa_in_mod_gen(aa_arrow) ): 
                    print str(aa_arrow) + '   idempotents are messed up in this aa_arrow!1'
                    count_of_mismatches+=1

            # matching out right algebra tuple and out gen
            if len(aa_in_right_alg_tuple(aa_arrow))!=0:
                if not check_idempotents_match_right_right(aa_out_mod_gen(aa_arrow),aa_in_right_alg_tuple(aa_arrow)[-1]): 
                    print str(aa_arrow) + '   idempotents are messed up in this aa_arrow!1'
                    count_of_mismatches+=1

            # matching out right algebra and in gen
            if len(aa_in_right_alg_tuple(aa_arrow))!=0:
                if not check_idempotents_match_right_left(aa_in_mod_gen(aa_arrow),aa_in_right_alg_tuple(aa_arrow)[0]): 
                    print str(aa_arrow) + '   idempotents are messed up in this aa_arrow!1'
                    count_of_mismatches+=1

            # we don't check the following:
            # matchings between algebra elements in tuple, 
            # matchings between generators if tuple is empty

        return count_of_mismatches==0

    def compute_d_squared(self):
        d_squared=Bunch_of_arrows()
        # contribution of double aa_arrows
        for aa_arrow1 in self.aa_arrows:
            for aa_arrow2 in self.aa_arrows:
                if not aa_out_mod_gen(aa_arrow1)==aa_in_mod_gen(aa_arrow2): continue
                a1a2_left_tuple=aa_in_left_alg_tuple(aa_arrow2) + aa_in_left_alg_tuple(aa_arrow1)
                a1a2_right_tuple=aa_in_right_alg_tuple(aa_arrow1) + aa_in_right_alg_tuple(aa_arrow2)
                ar=(a1a2_left_tuple,aa_in_mod_gen(aa_arrow1),a1a2_right_tuple,aa_out_mod_gen(aa_arrow2))
                d_squared[ar]+=1
        
        # contribution of aa_arrow and differential in algebra, or factorization in algebra
        for aa_arrow in self.aa_arrows:
            for index, a in enumerate(aa_in_left_alg_tuple(aa_arrow)):
                # factorizations on the left 
                for factorization in getattr(a,'factorizations', []):
                    new_tuple=aa_in_left_alg_tuple(aa_arrow)[:index] + factorization + aa_in_left_alg_tuple(aa_arrow)[index+1:]
                    d_squared[(new_tuple,aa_in_mod_gen(aa_arrow),aa_in_right_alg_tuple(aa_arrow),aa_out_mod_gen(aa_arrow))]+=1
                # predifferentials on the left
                for b in [algebra_diff_arrow[0] for algebra_diff_arrow in self.left_algebra.algebra_diff_arrows if algebra_diff_arrow[1]==a]:
                    new_tuple=aa_in_left_alg_tuple(aa_arrow)[:index] + (b,) + aa_in_left_alg_tuple(aa_arrow)[index+1:]
                    d_squared[(new_tuple,aa_in_mod_gen(aa_arrow),aa_in_right_alg_tuple(aa_arrow),aa_out_mod_gen(aa_arrow))]+=1
        
            for index, a in enumerate(aa_in_right_alg_tuple(aa_arrow)):
                # factorizations on the right
                for factorization in getattr(a,'factorizations', []):
                    new_tuple=aa_in_right_alg_tuple(aa_arrow)[:index] + factorization + aa_in_right_alg_tuple(aa_arrow)[index+1:]
                    d_squared[(aa_in_left_alg_tuple(aa_arrow),aa_in_mod_gen(aa_arrow),new_tuple,aa_out_mod_gen(aa_arrow))]+=1
                # predifferentials on the right
                for b in [algebra_diff_arrow[0] for algebra_diff_arrow in self.right_algebra.algebra_diff_arrows if algebra_diff_arrow[1]==a]:
                    new_tuple=aa_in_right_alg_tuple(aa_arrow)[:index] + (b,) + aa_in_right_alg_tuple(aa_arrow)[index+1:]
                    d_squared[(aa_in_left_alg_tuple(aa_arrow),aa_in_mod_gen(aa_arrow),new_tuple,aa_out_mod_gen(aa_arrow))]+=1
        

        return d_squared

def aa_cancel_pure_differential(AAbimodule_old,pure_differential):
    #z1--->z2
    z1=aa_in_mod_gen(pure_differential)
    z2=aa_out_mod_gen(pure_differential)

    #form generators
    generators_of_new_AA=AAbimodule_old.gen_by_name
    del generators_of_new_AA[z1.name]
    del generators_of_new_AA[z2.name]

    #form old differentials
    old_arrows_that_survive=[arrow for arrow in AAbimodule_old.aa_arrows if (aa_out_mod_gen(arrow)!=z1 and aa_out_mod_gen(arrow)!=z2  and aa_in_mod_gen(arrow)!=z1 and aa_in_mod_gen(arrow)!=z2 ) ]
    arrows_in_new_AA=Bunch_of_arrows(old_arrows_that_survive)

    #form new differentials
    arrows_in_z2=[arrow for arrow in AAbimodule_old.aa_arrows if (aa_out_mod_gen(arrow)==z2 and aa_in_mod_gen(arrow)!=z1 and aa_in_mod_gen(arrow)!=z2)]
    arrows_from_z1=[arrow for arrow in AAbimodule_old.aa_arrows if (aa_in_mod_gen(arrow)==z1 and aa_out_mod_gen(arrow)!=z2 and aa_out_mod_gen(arrow)!=z1)]

    for arrow_in_z2 in arrows_in_z2:
        for arrow_from_z1 in arrows_from_z1:
            
            new_arrow=(aa_in_left_alg_tuple(arrow_from_z1)+aa_in_left_alg_tuple(arrow_in_z2),aa_in_mod_gen(arrow_in_z2), aa_in_right_alg_tuple(arrow_in_z2)+aa_in_right_alg_tuple(arrow_from_z1),
                        aa_out_mod_gen(arrow_from_z1) )
            arrows_in_new_AA[new_arrow]+=1


    arrows_in_new_AA.delete_arrows_with_even_coeff()

    return AA_bimodule(generators_of_new_AA,arrows_in_new_AA,AAbimodule_old.left_algebra,AAbimodule_old.right_algebra,name= AAbimodule_old.name +'_red')

def aa_randomly_cancel_until_possible(AA):
    there_is_diff=0
    # arrs=AA.aa_arrows
    arrs=list(AA.aa_arrows)
    shuffle(arrs)
    for arrow in arrs:
        if (aa_in_left_alg_tuple(arrow)==() and aa_in_right_alg_tuple(arrow)==() and aa_in_mod_gen(arrow)!=aa_out_mod_gen(arrow)):
            
            # now we need to check that there are no other arrows between these two generators
            other_arrows=[ar for ar in arrs if (aa_in_mod_gen(ar)==aa_in_mod_gen(arrow) and aa_out_mod_gen(ar)==aa_out_mod_gen(arrow) and ar!=arrow)]
            if other_arrows: continue
            else:
                there_is_diff=1
                canceled_AA=aa_cancel_pure_differential(AA,arrow)
                return (aa_randomly_cancel_until_possible(canceled_AA))

    if there_is_diff==0:
        return AA


# making AA bimodule out of dg algebra
def a_A_a(algebra,to_check=True):
    gen_by_name=AttrDict({})
    for x in algebra.genset:
        gen_by_name[''+x.name+'']=Generator(''+x.name+'')
        gen_by_name[''+x.name+''].add_idems(x.idem.left, x.idem.right)        

    arrows=Bunch_of_arrows([])

    for diff_arrow in algebra.algebra_diff_arrows:
        arrows[((),gen_by_name[''+diff_arrow[0].name+''],(),gen_by_name[''+diff_arrow[1].name+''])]+=1

    for mult in algebra.multiplication_table:
        # we don't care about idempotents here, the action of idempotents is encapsulated 8 rows before
        if (mult[0] in algebra.idemset): continue
        if (mult[1] in algebra.idemset): continue
        if (algebra.multiplication_table[mult] in algebra.idemset): continue
        
        arrows[((),gen_by_name[''+mult[0].name+''],(mult[1],),gen_by_name[''+algebra.multiplication_table[mult].name+''])]+=1
        arrows[((mult[0],),gen_by_name[''+mult[1].name+''],(),gen_by_name[''+algebra.multiplication_table[mult].name+''])]+=1

    return AA_bimodule(gen_by_name,arrows,algebra,algebra,name="AA("+algebra.name+')',to_check=to_check)




