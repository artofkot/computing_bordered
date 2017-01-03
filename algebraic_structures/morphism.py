# -*- coding: utf-8 -*- 

from da_bimodule import  da_out_mod_gen,da_in_mod_gen,da_in_alg_tuple,da_out_alg_gen
from algebraic_structures.da_bimodule import  Bunch_of_arrows


# morphism is represented by bunch of arrows, where all coefficients are 1!
# and also I assume tha there are no differentials in algebra!
def compute_df(DA1,DA2,f):
    df=Bunch_of_arrows()

    #contribution of double arrows, with morphism on the second place
    for arrow1 in DA1.arrows:
        for arrow2 in [arrow2 for arrow2 in f if da_out_mod_gen(arrow1)==da_in_mod_gen(arrow2)]:
        # for arrow2 in f:
        #     if not da_out_mod_gen(arrow1)==da_in_mod_gen(arrow2): continue
            a1a2=DA1.algebra.multiply(da_out_alg_gen(arrow1),da_out_alg_gen(arrow2))
            if a1a2:
                new_arrow_in_df=(da_in_mod_gen(arrow1), da_in_alg_tuple(arrow1) + da_in_alg_tuple(arrow2),a1a2,da_out_mod_gen(arrow2))
                df[new_arrow_in_df]+=1

    #contribution of double arrows, with morphism on the first place
    for arrow1 in f:
        for arrow2 in [arrow2 for arrow2 in DA2.arrows if da_out_mod_gen(arrow1)==da_in_mod_gen(arrow2)]:
        # for arrow2 in DA2.arrows:
        #     if not da_out_mod_gen(arrow1)==da_in_mod_gen(arrow2): continue
            a1a2=DA1.algebra.multiply(da_out_alg_gen(arrow1),da_out_alg_gen(arrow2))
            if a1a2:
                new_arrow_in_df=(da_in_mod_gen(arrow1), da_in_alg_tuple(arrow1) + da_in_alg_tuple(arrow2),
                            a1a2,da_out_mod_gen(arrow2))
                df[new_arrow_in_df]+=1


    #contribution of factorizing algebra elements        
    for arrow in f:
        for index, a in enumerate(da_in_alg_tuple(arrow)):
            for factorization in getattr(a,'factorizations', []):
                new_tuple=da_in_alg_tuple(arrow)[:index] + factorization + da_in_alg_tuple(arrow)[index+1:]
                new_arrow_in_df=(da_in_mod_gen(arrow), new_tuple,
                    da_out_alg_gen(arrow),da_out_mod_gen(arrow))
                # add arrow to df
                df[new_arrow_in_df]+=1

    return df

def check_df_is_0(DA1,DA2,f):
    df=compute_df(DA1,DA2,f)
    df.delete_arrows_with_even_coeff()
    # print '\n{\nHere are all the arrows in df'
    # df.show()
    # print '}'
    for arrow in df:
        if df[arrow] % 2 != 0:
            # print "Something is wrong with df=0 for this one, " + str(len(df)) + "arrows in df"
            return False
    print 'Everything is ok, we found isomorphism f such that df=0!'
    return True

def composition(f,g,A):
    f_g=Bunch_of_arrows()

    #contribution of double arrows
    for arrow1 in f:
        for arrow2 in g:
            if not da_out_mod_gen(arrow1)==da_in_mod_gen(arrow2): continue
            a1a2=A.multiply(da_out_alg_gen(arrow1),da_out_alg_gen(arrow2))
            if a1a2:
                new_arrow_in_df=(da_in_mod_gen(arrow1), da_in_alg_tuple(arrow1) + da_in_alg_tuple(arrow2),
                            a1a2,da_out_mod_gen(arrow2))
                f_g[new_arrow_in_df]+=1

    f_g.delete_arrows_with_even_coeff()
    return f_g

