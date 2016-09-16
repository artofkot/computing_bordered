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

def init_genus2_algebra():
    gen_by_name=AttrDict({
                "r1": Generator("r1"),
                "r2": Generator("r2"),
                "r3": Generator("r3"),
                "r12": Generator("r12"),
                "r23": Generator("r23"),
                "r123": Generator("r123"),

                "i0": Generator("i0"),
                "i1": Generator("i1"),

                "r5": Generator("r5"),
                "r6": Generator("r6"),
                "r7": Generator("r7"),
                "r56": Generator("r56"),
                "r67": Generator("r67"),
                "r567": Generator("r567"),

                "i2": Generator("i2"),
                "i3": Generator("i3"),

                "r1234": Generator("r1234"),
                "r12345": Generator("r12345"),
                "r123456": Generator("r123456"),
                "r1234567": Generator("r1234567"),
                "r234": Generator("r234"),
                "r2345": Generator("r2345"),
                "r23456": Generator("r23456"),
                "r234567": Generator("r234567"),
                "r34": Generator("r34"),
                "r345": Generator("r345"),
                "r3456": Generator("r3456"),
                "r34567": Generator("r34567"),
                "r4": Generator("r4"),
                "r45": Generator("r45"),
                "r456": Generator("r456"),
                "r4567": Generator("r4567")
                })
    gen_by_name.r12.add_factorizations((gen_by_name.r1,gen_by_name.r2))
    gen_by_name.r23.add_factorizations((gen_by_name.r2,gen_by_name.r3))
    gen_by_name.r34.add_factorizations((gen_by_name.r3,gen_by_name.r4))

    gen_by_name.r45.add_factorizations((gen_by_name.r4,gen_by_name.r5))
    gen_by_name.r56.add_factorizations((gen_by_name.r5,gen_by_name.r6))
    gen_by_name.r67.add_factorizations((gen_by_name.r6,gen_by_name.r7))

    gen_by_name.r123.add_factorizations((gen_by_name.r1,gen_by_name.r23),(gen_by_name.r12,gen_by_name.r3))
    gen_by_name.r234.add_factorizations((gen_by_name.r2,gen_by_name.r34),(gen_by_name.r23,gen_by_name.r4))
    gen_by_name.r345.add_factorizations((gen_by_name.r3,gen_by_name.r45),(gen_by_name.r34,gen_by_name.r5))
    gen_by_name.r456.add_factorizations((gen_by_name.r4,gen_by_name.r56),(gen_by_name.r45,gen_by_name.r6))
    gen_by_name.r567.add_factorizations((gen_by_name.r5,gen_by_name.r67),(gen_by_name.r56,gen_by_name.r7))

    gen_by_name.r1234.add_factorizations((gen_by_name.r1,gen_by_name.r234),(gen_by_name.r12,gen_by_name.r34),
                                        (gen_by_name.r123,gen_by_name.r4))
    gen_by_name.r2345.add_factorizations((gen_by_name.r2,gen_by_name.r345),(gen_by_name.r23,gen_by_name.r45),
                                        (gen_by_name.r234,gen_by_name.r5))
    gen_by_name.r3456.add_factorizations((gen_by_name.r3,gen_by_name.r456),(gen_by_name.r34,gen_by_name.r56),
                                        (gen_by_name.r345,gen_by_name.r6))
    gen_by_name.r4567.add_factorizations((gen_by_name.r4,gen_by_name.r567),(gen_by_name.r45,gen_by_name.r67),
                                        (gen_by_name.r456,gen_by_name.r7))

    gen_by_name.r12345.add_factorizations((gen_by_name.r1,gen_by_name.r2345),(gen_by_name.r12,gen_by_name.r345),
                                        (gen_by_name.r123,gen_by_name.r45),(gen_by_name.r1234,gen_by_name.r5))
    gen_by_name.r23456.add_factorizations((gen_by_name.r2,gen_by_name.r3456),(gen_by_name.r23,gen_by_name.r456),
                                        (gen_by_name.r234,gen_by_name.r56),(gen_by_name.r2345,gen_by_name.r6))
    gen_by_name.r34567.add_factorizations((gen_by_name.r3,gen_by_name.r4567),(gen_by_name.r34,gen_by_name.r567),
                                        (gen_by_name.r345,gen_by_name.r67),(gen_by_name.r3456,gen_by_name.r7))   


    gen_by_name.r123456.add_factorizations((gen_by_name.r1,gen_by_name.r23456),(gen_by_name.r12,gen_by_name.r3456),
                                        (gen_by_name.r123,gen_by_name.r456),(gen_by_name.r1234,gen_by_name.r56),
                                        (gen_by_name.r12345,gen_by_name.r6))
    gen_by_name.r234567.add_factorizations((gen_by_name.r2,gen_by_name.r34567),(gen_by_name.r23,gen_by_name.r4567),
                                        (gen_by_name.r234,gen_by_name.r567),(gen_by_name.r2345,gen_by_name.r67),
                                        (gen_by_name.r23456,gen_by_name.r7)) 

    gen_by_name.r1234567.add_factorizations((gen_by_name.r1,gen_by_name.r234567),(gen_by_name.r12,gen_by_name.r34567),
                                        (gen_by_name.r123,gen_by_name.r4567),(gen_by_name.r1234,gen_by_name.r567),
                                        (gen_by_name.r12345,gen_by_name.r67),(gen_by_name.r123456,gen_by_name.r7)) 


    idem=AttrDict({
                    "i0": gen_by_name.i0,
                    "i1": gen_by_name.i1,
                    "i2": gen_by_name.i2,
                    "i3": gen_by_name.i3,
                    })
    multiplication_table={(gen_by_name.r1,gen_by_name.r2):gen_by_name.r12, #first torus algebra part
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

                        (gen_by_name.r5,gen_by_name.r6):gen_by_name.r56, #second torus algebra part
                        (gen_by_name.r6,gen_by_name.r7):gen_by_name.r67,
                        (gen_by_name.r5,gen_by_name.r67):gen_by_name.r567,
                        (gen_by_name.r56,gen_by_name.r7):gen_by_name.r567,
                        (gen_by_name.i2,gen_by_name.r5):gen_by_name.r5,
                        (gen_by_name.i2,gen_by_name.r7):gen_by_name.r7,
                        (gen_by_name.i2,gen_by_name.r56):gen_by_name.r56,
                        (gen_by_name.i2,gen_by_name.r567):gen_by_name.r567,
                        (gen_by_name.i2,gen_by_name.i2):gen_by_name.i2,
                        (gen_by_name.i3,gen_by_name.i3):gen_by_name.i3,
                        (gen_by_name.i3,gen_by_name.r67):gen_by_name.r67,
                        (gen_by_name.i3,gen_by_name.r6):gen_by_name.r6,
                        (gen_by_name.r5,gen_by_name.i3):gen_by_name.r5,
                        (gen_by_name.r6,gen_by_name.i2):gen_by_name.r6,
                        (gen_by_name.r7,gen_by_name.i3):gen_by_name.r7,
                        (gen_by_name.r56,gen_by_name.i2):gen_by_name.r56,
                        (gen_by_name.r67,gen_by_name.i3):gen_by_name.r67,
                        (gen_by_name.r567,gen_by_name.i3):gen_by_name.r567,

                        (gen_by_name.i0,gen_by_name.r1234):gen_by_name.r1234, #rest of idempotent multiplications
                        (gen_by_name.i0,gen_by_name.r12345):gen_by_name.r12345,
                        (gen_by_name.i0,gen_by_name.r123456):gen_by_name.r123456,
                        (gen_by_name.i0,gen_by_name.r1234567):gen_by_name.r1234567,
                        (gen_by_name.i0,gen_by_name.r34):gen_by_name.r34,
                        (gen_by_name.i0,gen_by_name.r345):gen_by_name.r345,
                        (gen_by_name.i0,gen_by_name.r3456):gen_by_name.r3456,
                        (gen_by_name.i0,gen_by_name.r34567):gen_by_name.r34567,

                        (gen_by_name.i1,gen_by_name.r234):gen_by_name.r234,
                        (gen_by_name.i1,gen_by_name.r2345):gen_by_name.r2345,
                        (gen_by_name.i1,gen_by_name.r23456):gen_by_name.r23456,
                        (gen_by_name.i1,gen_by_name.r234567):gen_by_name.r234567,
                        (gen_by_name.i1,gen_by_name.r4):gen_by_name.r4,
                        (gen_by_name.i1,gen_by_name.r45):gen_by_name.r45,
                        (gen_by_name.i1,gen_by_name.r456):gen_by_name.r456,
                        (gen_by_name.i1,gen_by_name.r4567):gen_by_name.r4567,    

                        (gen_by_name.r1234,gen_by_name.i2):gen_by_name.r1234,
                        (gen_by_name.r12345,gen_by_name.i3):gen_by_name.r12345,
                        (gen_by_name.r123456,gen_by_name.i2):gen_by_name.r123456,
                        (gen_by_name.r1234567,gen_by_name.i3):gen_by_name.r1234567,
                        (gen_by_name.r34,gen_by_name.i2):gen_by_name.r34,
                        (gen_by_name.r345,gen_by_name.i3):gen_by_name.r345,
                        (gen_by_name.r3456,gen_by_name.i2):gen_by_name.r3456,
                        (gen_by_name.r34567,gen_by_name.i3):gen_by_name.r34567,

                        (gen_by_name.r234,gen_by_name.i2):gen_by_name.r234,
                        (gen_by_name.r2345,gen_by_name.i3):gen_by_name.r2345,
                        (gen_by_name.r23456,gen_by_name.i2):gen_by_name.r23456,
                        (gen_by_name.r234567,gen_by_name.i3):gen_by_name.r234567,
                        (gen_by_name.r4,gen_by_name.i2):gen_by_name.r4,
                        (gen_by_name.r45,gen_by_name.i3):gen_by_name.r45,
                        (gen_by_name.r456,gen_by_name.i2):gen_by_name.r456,
                        (gen_by_name.r4567,gen_by_name.i3):gen_by_name.r4567,  

                        (gen_by_name.r4,gen_by_name.r5):gen_by_name.r45, #actual elements (havinig r4 inside) factorizations
                        (gen_by_name.r3,gen_by_name.r4):gen_by_name.r34, 
                        (gen_by_name.r1,gen_by_name.r23):gen_by_name.r123,
                        (gen_by_name.r12,gen_by_name.r3):gen_by_name.r123,
                        (gen_by_name.r2,gen_by_name.r34):gen_by_name.r234,
                        (gen_by_name.r23,gen_by_name.r4):gen_by_name.r234,
                        (gen_by_name.r3,gen_by_name.r45):gen_by_name.r345,
                        (gen_by_name.r34,gen_by_name.r5):gen_by_name.r345,
                        (gen_by_name.r4,gen_by_name.r56):gen_by_name.r456,
                        (gen_by_name.r45,gen_by_name.r6):gen_by_name.r456,
                        (gen_by_name.r5,gen_by_name.r67):gen_by_name.r567,
                        (gen_by_name.r56,gen_by_name.r7):gen_by_name.r567,

  
                        (gen_by_name.r1,gen_by_name.r234):gen_by_name.r1234,
                        (gen_by_name.r12,gen_by_name.r34):gen_by_name.r1234,
                        (gen_by_name.r123,gen_by_name.r4):gen_by_name.r1234,

                        (gen_by_name.r2,gen_by_name.r345):gen_by_name.r2345,
                        (gen_by_name.r23,gen_by_name.r45):gen_by_name.r2345,
                        (gen_by_name.r234,gen_by_name.r5):gen_by_name.r2345,

                        (gen_by_name.r3,gen_by_name.r456):gen_by_name.r3456,
                        (gen_by_name.r34,gen_by_name.r56):gen_by_name.r3456,
                        (gen_by_name.r345,gen_by_name.r6):gen_by_name.r3456,

                        (gen_by_name.r4,gen_by_name.r567):gen_by_name.r4567,
                        (gen_by_name.r45,gen_by_name.r67):gen_by_name.r4567,
                        (gen_by_name.r456,gen_by_name.r7):gen_by_name.r4567,

                        (gen_by_name.r1,gen_by_name.r2345):gen_by_name.r12345,
                        (gen_by_name.r12,gen_by_name.r345):gen_by_name.r12345,
                        (gen_by_name.r123,gen_by_name.r45):gen_by_name.r12345,
                        (gen_by_name.r1234,gen_by_name.r5):gen_by_name.r12345,

                        (gen_by_name.r2,gen_by_name.r3456):gen_by_name.r23456,
                        (gen_by_name.r23,gen_by_name.r456):gen_by_name.r23456,
                        (gen_by_name.r234,gen_by_name.r56):gen_by_name.r23456,
                        (gen_by_name.r2345,gen_by_name.r6):gen_by_name.r23456,

                        (gen_by_name.r3,gen_by_name.r4567):gen_by_name.r34567,
                        (gen_by_name.r34,gen_by_name.r567):gen_by_name.r34567,
                        (gen_by_name.r345,gen_by_name.r67):gen_by_name.r34567,
                        (gen_by_name.r3456,gen_by_name.r7):gen_by_name.r34567,   

                        (gen_by_name.r1,gen_by_name.r23456):gen_by_name.r123456,
                        (gen_by_name.r12,gen_by_name.r3456):gen_by_name.r123456,
                        (gen_by_name.r123,gen_by_name.r456):gen_by_name.r123456,
                        (gen_by_name.r1234,gen_by_name.r56):gen_by_name.r123456,
                        (gen_by_name.r12345,gen_by_name.r6):gen_by_name.r123456,

                        (gen_by_name.r2,gen_by_name.r34567):gen_by_name.r234567,
                        (gen_by_name.r23,gen_by_name.r4567):gen_by_name.r234567,
                        (gen_by_name.r234,gen_by_name.r567):gen_by_name.r234567,
                        (gen_by_name.r2345,gen_by_name.r67):gen_by_name.r234567,
                        (gen_by_name.r23456,gen_by_name.r7):gen_by_name.r234567, 

                        (gen_by_name.r1,gen_by_name.r234567):gen_by_name.r1234567,
                        (gen_by_name.r12,gen_by_name.r34567):gen_by_name.r1234567,
                        (gen_by_name.r123,gen_by_name.r4567):gen_by_name.r1234567,
                        (gen_by_name.r1234,gen_by_name.r567):gen_by_name.r1234567,
                        (gen_by_name.r12345,gen_by_name.r67):gen_by_name.r1234567,
                        (gen_by_name.r123456,gen_by_name.r7):gen_by_name.r1234567
                
                                    }

    return DGAlgebra(gen_by_name=gen_by_name,idem=idem,multiplication_table=multiplication_table)



torus_algebra=init_torus_algebra()
A=torus_algebra
g2_A=init_genus2_algebra()
# g2_A.show()
# A.show()
# Identity_DA_bimodule.show()
# Identity_DA_bimodule.check()