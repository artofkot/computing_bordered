# -*- coding: utf-8 -*- 
from utility import AttrDict
from sets import Set

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
 

def check_idempotents_match_left_right(l,m):
    if l==1: return True
    if m==1: return True
    if not (l.idem.right==m.idem.left): 
        print "These elements idempotents don't match! " + str((l,m))
    return (l.idem.right==m.idem.left)

def check_idempotents_match_right_right(l,m):
    if l==1: return True
    if m==1: return True
    if not (l.idem.right==m.idem.right): 
        print "These elements idempotents don't match! " + str((l,m))
    return (l.idem.right==m.idem.right)


def check_idempotents_match_left_left(l,m):
    if l==1: return True
    if m==1: return True
    if not (l.idem.left==m.idem.left): 
        print "These elements idempotents don't match! " + str((l,m))
    return (l.idem.left==m.idem.left)


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

torus_algebra=init_torus_algebra()
A=torus_algebra
# A.show()
# Identity_DA_bimodule.show()
# Identity_DA_bimodule.check()