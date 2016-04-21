# -*- coding: utf-8 -*- 
from sets import Set
from collections import Counter

def arrow_to_str(tuplee):
    return str(tuplee[0]) +'⊗'+ str(tuplee[1]) + "---->" + str(tuplee[2]) +'⊗'+ str(tuplee[3])

def in_mod_gen(arrow):
    return arrow[0]

def in_alg_tuple(arrow):
    return arrow[1]

def out_alg_gen(arrow):
    return arrow[2]

def out_mod_gen(arrow):
    return arrow[3]

def check_idempotents_match(l,m):
    if l==1: return True
    if m==1: return True
    return (l.idem.right==m.idem.left)

class Bunch_of_arrows(Counter):
    def show(self):
        for arrow_as_a_tuple in self:
            print arrow_to_str(arrow_as_a_tuple) + '     *' + str(self[arrow_as_a_tuple])  
        print '}'

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

class Generator(object):
    def __init__(self, name):
        self.name = name

    def add_idems(self,idem1,idem2):
        self.idem=AttrDict({"left":idem1, "right":idem2})

    def add_factorizations(self,*factorizations): #for algebra generators only!
        self.factorizations=getattr(self,'factorizations', [])
        for factorization in factorizations:
            self.factorizations.append(factorization)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

# I will assume that algebra is vector space over F2, and does not have differentials, 
# which happens in the first symmetric product
class DGAlgebra(object):
    def __init__(self,gen_by_name,idem,multiplication_table):
        self.gen_by_name=gen_by_name #dictionary of generators, where keys are their names
        self.genset=self.gen_by_name.values() #list of generators
        self.idem=idem #dictionary with idempotents, where keys are their names
        self.idemset=idem.values() #list of idempotents
        self.multiplication_table=multiplication_table

        for gen in self.genset:
            for idem1 in self.idemset:
                for idem2 in self.idemset:
                    if (self.multiplication_table.get((gen,idem2))==gen) and (self.multiplication_table.get((idem1,gen))==gen):
                        gen.add_idems(idem1,idem2)


    def mult2(self, gen1, gen2):
        if gen1==1: return gen2
        if gen2==1: return gen1
        if (gen1,gen2) in self.multiplication_table:
            return self.multiplication_table[(gen1,gen2)]
        else: return 0

    def multiply(self, *args):
        x=args[0]
        for i in range(len(args)-1):
            x=self.mult2(x,args[i+1])
        return x

    def show(self):
        print('========\nGenerators of algebra with their idempotents:')
        for gen in self.genset:
            print str(gen.idem.left) + ' ' + str(gen) + ' ' + str(gen.idem.right)
        print('Multiplications in algebra:')
        for k in self.multiplication_table:
            print str(k[0]) + '*' + str(k[1]) + '=' + str(self.multiplication_table[k])

# conventions: D side is left, A side is right
class DA_bimodule(object):
    def __init__(self,gen_by_name,arrows,algebra,name):
        self.name=name
        self.gen_by_name=gen_by_name
        self.genset=self.gen_by_name.values()
        self.arrows=arrows
        self.algebra=algebra
    
    def show(self):
        print '========\nGenerators of ' + self.name + ' with their idempotents:'
        for gen in self.genset:
            print str(gen.idem.left) + ' ' + str(gen) + ' ' + str(gen.idem.right)

        print '\nActions of' + self.name + ':'
        for arrow in self.arrows:
            print arrow_to_str(arrow)

    def check_matching_of_idempotents_in_action(self): 
        count_of_mismatches=0
        for arrow in self.arrows:
            # matching out algebra and out gen
            if not check_idempotents_match( out_alg_gen(arrow),out_mod_gen(arrow) ): 
                count_of_mismatches+=1
            
            for i in range(len(in_alg_tuple(arrow))):
                if (i==0):
                    #matching in algebra and gen
                    if not check_idempotents_match(in_mod_gen(arrow),in_alg_tuple(arrow)[0]): 
                        count_of_mismatches+=1
                else:
                    #matching in algebras
                    if not check_idempotents_match(in_alg_tuple(arrow)[i-1],in_alg_tuple(arrow)[i]): 
                        count_of_mismatches+=1
        return count_of_mismatches==0

    def compute_dd(self):
        dd=Bunch_of_arrows()
        #contribution of double arrows
        for arrow1 in self.arrows:
            for arrow2 in self.arrows:
                a1a2=self.algebra.multiply(out_alg_gen(arrow1),out_alg_gen(arrow2))
                if a1a2 and out_mod_gen(arrow1)==in_mod_gen(arrow2):
                    ar=(in_mod_gen(arrow1), in_alg_tuple(arrow1) + in_alg_tuple(arrow2),a1a2,out_mod_gen(arrow2))
                    dd[ar]+=1




        #contribution of factorizing algebra elements        
        for arrow in self.arrows:
            for index, a in enumerate(in_alg_tuple(arrow)):
                for factorization in getattr(a,'factorizations', []):
                    new_tuple=in_alg_tuple(arrow)[:index] + factorization + in_alg_tuple(arrow)[index+1:]
                    ar=(in_mod_gen(arrow), new_tuple,
                        out_alg_gen(arrow),out_mod_gen(arrow))
                    # print_arrow_from_tuple(ar)
                    dd[ar]+=1

        return dd

    def check_dd_is_0(self):
        dd=self.compute_dd()

        print '\n{\nHere are all the arrows in dd'
        dd.show()
        for arrow in dd:
            if dd[arrow] % 2 != 0:
                return False
        return True

    def check(self):
        print "========\nHere we check that our " + self.name + " has all idempotents matching and dd=0:"
        if not self.check_matching_of_idempotents_in_action():
            print "\nSomething is wrong with idempotents!"
        else: print "\nIdempotents match!"
        if not self.check_dd_is_0():
            print "Something is wrong with dd=0!"
        else: print "dd=0!"


    def differential_of_generator_and_a_tuple(self, gen1, alg_tuple): #gives element in AtensorM
        s=Counter()
        for arrow in self.arrows: 
            if (in_mod_gen(arrow)==gen1 and in_alg_tuple(arrow)==alg_tuple):
                s[GeneratorA_tensor_M( out_alg_gen(arrow),out_mod_gen(arrow) )]+=1
        return s


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



#########################################################################################################
#########################################################################################################

def init_torus_algebra():
    gen_by_name=AttrDict({
                "r1": Generator("r1"),
                "r2": Generator("r2"),
                "r3": Generator("r3"),
                "r12": Generator("r12"),
                "r23": Generator("r23"),
                "r123": Generator("r123"),
                "i0": Generator("i0"),
                "i1": Generator("i1"),
                })
    gen_by_name.r12.add_factorizations((gen_by_name.r1,gen_by_name.r2))
    gen_by_name.r23.add_factorizations((gen_by_name.r2,gen_by_name.r3))
    gen_by_name.r123.add_factorizations((gen_by_name.r1,gen_by_name.r23),(gen_by_name.r12,gen_by_name.r3))

    idem=AttrDict({
                    "i0": gen_by_name.i0,
                    "i1": gen_by_name.i1,
                    })
    multiplication_table={(gen_by_name.r1,gen_by_name.r2):gen_by_name.r12,
                        (gen_by_name.r2,gen_by_name.r3):gen_by_name.r23,
                        (gen_by_name.r1,gen_by_name.r23):gen_by_name.r123,
                        (gen_by_name.r12,gen_by_name.r3):gen_by_name.r123,
                        (gen_by_name.i0,gen_by_name.r1):gen_by_name.r1,
                        (gen_by_name.i0,gen_by_name.r3):gen_by_name.r3,
                        (gen_by_name.i0,gen_by_name.r12):gen_by_name.r12,
                        (gen_by_name.i0,gen_by_name.r123):gen_by_name.r123,
                        (gen_by_name.i0,gen_by_name.i0):gen_by_name.i0,
                        (gen_by_name.i1,gen_by_name.i1):gen_by_name.i1,
                        (gen_by_name.i1,gen_by_name.r23):gen_by_name.r23,
                        (gen_by_name.i1,gen_by_name.r2):gen_by_name.r2,
                        (gen_by_name.r1,gen_by_name.i1):gen_by_name.r1,
                        (gen_by_name.r2,gen_by_name.i0):gen_by_name.r2,
                        (gen_by_name.r3,gen_by_name.i1):gen_by_name.r3,
                        (gen_by_name.r12,gen_by_name.i0):gen_by_name.r12,
                        (gen_by_name.r23,gen_by_name.i1):gen_by_name.r23,
                        (gen_by_name.r123,gen_by_name.i1):gen_by_name.r123,
                                    }

    return DGAlgebra(gen_by_name=gen_by_name,idem=idem,multiplication_table=multiplication_table)

def init_identity_DA_bimodule(torus_algebra):
    gen_by_name=AttrDict({
                "x": Generator("x"),
                "y": Generator("y")
                })
    gen_by_name.x.add_idems(torus_algebra.idem.i0,torus_algebra.idem.i0)
    gen_by_name.y.add_idems(torus_algebra.idem.i1,torus_algebra.idem.i1)

    arrows=Bunch_of_arrows([
        (              gen_by_name.x,(torus_algebra.gen_by_name.r12,),
                torus_algebra.gen_by_name.r12,gen_by_name.x),

        (              gen_by_name.y,(torus_algebra.gen_by_name.r23,),
                torus_algebra.gen_by_name.r23,gen_by_name.y),

        (              gen_by_name.x,(torus_algebra.gen_by_name.r1,),
                torus_algebra.gen_by_name.r1,gen_by_name.y),

        (              gen_by_name.y,(torus_algebra.gen_by_name.r2,),
                torus_algebra.gen_by_name.r2,gen_by_name.x),

        (              gen_by_name.x,(torus_algebra.gen_by_name.r123,),
                torus_algebra.gen_by_name.r123,gen_by_name.y),

        (              gen_by_name.x,(torus_algebra.gen_by_name.r3,),
                torus_algebra.gen_by_name.r3,gen_by_name.y)])

    return DA_bimodule(gen_by_name,arrows,torus_algebra,name="Identity_DA_bimodule")

torus_algebra=init_torus_algebra()
Identity_DA_bimodule=init_identity_DA_bimodule(A)

# A.show()
# Identity_DA_bimodule.show()
# Identity_DA_bimodule.check()