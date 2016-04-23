# -*- coding: utf-8 -*- 
from algebra import AttrDict, Generator, A
from da_bimodule import  Bunch_of_arrows, DA_bimodule,cancel_pure_differential, box_tensor_product,arrow_to_str
from da_bimodule import  out_mod_gen,in_mod_gen,in_alg_tuple,out_alg_gen

# morphism is represented by bunch of arrows, where all coefficients are 1!
# and also I assume tha there are no differentials in algebra!
def compute_df(DA1,DA2,f):
    df=Bunch_of_arrows()

    #contribution of double arrows, with morphism on the second place
    for arrow1 in DA1.arrows:
        for arrow2 in f:
            if not out_mod_gen(arrow1)==in_mod_gen(arrow2): continue
            a1a2=DA1.algebra.multiply(out_alg_gen(arrow1),out_alg_gen(arrow2))
            if a1a2:
                new_arrow_in_df=(in_mod_gen(arrow1), in_alg_tuple(arrow1) + in_alg_tuple(arrow2),a1a2,out_mod_gen(arrow2))
                df[new_arrow_in_df]+=1

    #contribution of double arrows, with morphism on the first place
    for arrow1 in f:
        for arrow2 in DA2.arrows:
            if not out_mod_gen(arrow1)==in_mod_gen(arrow2): continue
            a1a2=DA1.algebra.multiply(out_alg_gen(arrow1),out_alg_gen(arrow2))
            if a1a2:
                new_arrow_in_df=(in_mod_gen(arrow1), in_alg_tuple(arrow1) + in_alg_tuple(arrow2),
                            a1a2,out_mod_gen(arrow2))
                df[new_arrow_in_df]+=1


    #contribution of factorizing algebra elements        
    for arrow in f:
        for index, a in enumerate(in_alg_tuple(arrow)):
            for factorization in getattr(a,'factorizations', []):
                new_tuple=in_alg_tuple(arrow)[:index] + factorization + in_alg_tuple(arrow)[index+1:]
                new_arrow_in_df=(in_mod_gen(arrow), new_tuple,
                    out_alg_gen(arrow),out_mod_gen(arrow))
                # add arrow to df
                df[new_arrow_in_df]+=1

    return df

def check_df_is_0(DA1,DA2,f):
    df=compute_df(DA1,DA2,f)

    # print '\n{\nHere are all the arrows in df'
    # df.show()
    # print '}'

    for arrow in df:
        if df[arrow] % 2 != 0:
            print "Something is wrong with df=0!"
            return False
    print 'Everything is ok, df=0!'
    return True

def composition(f,g,A):
    f_g=Bunch_of_arrows()

    #contribution of double arrows
    for arrow1 in f:
        for arrow2 in g:
            if not out_mod_gen(arrow1)==in_mod_gen(arrow2): continue
            a1a2=A.multiply(out_alg_gen(arrow1),out_alg_gen(arrow2))
            if a1a2:
                new_arrow_in_df=(in_mod_gen(arrow1), in_alg_tuple(arrow1) + in_alg_tuple(arrow2),
                            a1a2,out_mod_gen(arrow2))
                f_g[new_arrow_in_df]+=1

    f_g.delete_arrows_with_even_coeff()
    return f_g

