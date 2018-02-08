# -*- coding: utf-8 -*- 
from basics import AttrDict, Bunch_of_arrows, Generator, debug
from sets import Set

# I will assume that algebra is vector space over F2, and does not have differentials, 
# which happens in the first symmetric product
class dg_algebra(object):
    def __init__(self,gen_by_name,
                idem_by_name,
                multiplication_table,
                name,
                algebra_diff_arrows=Bunch_of_arrows([]),
                a_inf_actions=Bunch_of_arrows([]),
                to_check=True):
        self.algebra_diff_arrows=algebra_diff_arrows
        self.name=name
        self.gen_by_name=gen_by_name #dictionary of generators, where keys are their names
        self.genset=self.gen_by_name.values() #list of generators
        self.idem_by_name=idem_by_name #dictionary with idempotents, where keys are their names
        self.idemset=idem_by_name.values() #list of idempotents
        self.multiplication_table=multiplication_table
        self.a_inf_actions=a_inf_actions

        # adding factorizations of elements which are not idempotents into non-idempotent product
        for gen1 in set(self.genset) - set(self.idemset):
            for gen2 in set(self.genset) - set(self.idemset):
                gen3=self.multiplication_table.get((gen1,gen2),None)
                if gen3:
                    gen3.add_factorizations((gen1,gen2))
                    
        for gen in self.genset:
            
            for idem1 in self.idemset:
                for idem2 in self.idemset:
                    if (self.multiplication_table.get((gen,idem2))==gen) and (self.multiplication_table.get((idem1,gen))==gen):
                        gen.add_idems(idem1,idem2)
        if to_check==True:
            self.check()

    def check(self):
        # Here we check that our satisfies associativity, and Leibnitz rule (i.e. A_infty relations hold):
        
        #### Associativity we don't check, it takes too much time cause its hard to violate it:
        #### all my algebras are associative, and Bohua's algebras also
        # for gen1 in self.genset:
        #     for gen2 in self.genset:
        #         for gen3 in self.genset:
        #             if self.multiply(self.multiply(gen1,gen2), gen3)!=self.multiply(gen1, self.multiply(gen2,gen3)):
        #                 print "Associativity in" + self.name + " is broken"
        #                 raise NameError("Associativity in" + self.name + " is broken")

        # Leibnitz rule
        d_squared=Bunch_of_arrows([])
        for gen1 in self.genset:
            for gen2 in self.genset:
                gen3=self.multiply(gen1,gen2)
                if gen3: 
                    for a in self.algebra_diff_arrows:
                        if a[0]==gen3: d_squared[(gen1,gen2,a[1])]+=1

        for a in self.algebra_diff_arrows:
            for gen in self.genset:
                if self.multiply(gen,a[1]):  d_squared[(gen,a[0],self.multiply(gen,a[1]))]+=1
                if self.multiply(a[1],gen):  d_squared[(a[0],gen,self.multiply(a[1],gen))]+=1

        d_squared.delete_arrows_with_even_coeff()
        if d_squared:
            print "d_squared is not 0 in" + self.name + ". The terms that are not canceled:"
            d_squared.show()
            raise NameError("algebra " + self.name + " doesn't satisfy d_squared=0.")


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
        print ('========\n'+ self.name)
        print('({} generators in this algebra)'.format(len(self.genset)) ) 
        # for gen in self.genset:
        #     print str(gen.idem.left) + ' ' + str(gen) + ' ' + str(gen.idem.right)
        # print('Multiplications in algebra:')
        # for k in self.multiplication_table:
        #     print str(k[0]) + '*' + str(k[1]) + '=' + str(self.multiplication_table[k])


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

    # now this stuff is done when algebra is initiated
    # gen_by_name.r12.add_factorizations((gen_by_name.r1,gen_by_name.r2))
    # gen_by_name.r23.add_factorizations((gen_by_name.r2,gen_by_name.r3))
    # gen_by_name.r123.add_factorizations((gen_by_name.r1,gen_by_name.r23),(gen_by_name.r12,gen_by_name.r3))

    idem_by_name=AttrDict({
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

    return dg_algebra(gen_by_name=gen_by_name,idem_by_name=idem_by_name,multiplication_table=multiplication_table,name='torus_A')

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

    # now this stuff is done when algebra is initiated
    # gen_by_name.r12.add_factorizations((gen_by_name.r1,gen_by_name.r2))
    # gen_by_name.r23.add_factorizations((gen_by_name.r2,gen_by_name.r3))
    # gen_by_name.r34.add_factorizations((gen_by_name.r3,gen_by_name.r4))

    # gen_by_name.r45.add_factorizations((gen_by_name.r4,gen_by_name.r5))
    # gen_by_name.r56.add_factorizations((gen_by_name.r5,gen_by_name.r6))
    # gen_by_name.r67.add_factorizations((gen_by_name.r6,gen_by_name.r7))

    # gen_by_name.r123.add_factorizations((gen_by_name.r1,gen_by_name.r23),(gen_by_name.r12,gen_by_name.r3))
    # gen_by_name.r234.add_factorizations((gen_by_name.r2,gen_by_name.r34),(gen_by_name.r23,gen_by_name.r4))
    # gen_by_name.r345.add_factorizations((gen_by_name.r3,gen_by_name.r45),(gen_by_name.r34,gen_by_name.r5))
    # gen_by_name.r456.add_factorizations((gen_by_name.r4,gen_by_name.r56),(gen_by_name.r45,gen_by_name.r6))
    # gen_by_name.r567.add_factorizations((gen_by_name.r5,gen_by_name.r67),(gen_by_name.r56,gen_by_name.r7))

    # gen_by_name.r1234.add_factorizations((gen_by_name.r1,gen_by_name.r234),(gen_by_name.r12,gen_by_name.r34),
    #                                     (gen_by_name.r123,gen_by_name.r4))
    # gen_by_name.r2345.add_factorizations((gen_by_name.r2,gen_by_name.r345),(gen_by_name.r23,gen_by_name.r45),
    #                                     (gen_by_name.r234,gen_by_name.r5))
    # gen_by_name.r3456.add_factorizations((gen_by_name.r3,gen_by_name.r456),(gen_by_name.r34,gen_by_name.r56),
    #                                     (gen_by_name.r345,gen_by_name.r6))
    # gen_by_name.r4567.add_factorizations((gen_by_name.r4,gen_by_name.r567),(gen_by_name.r45,gen_by_name.r67),
    #                                     (gen_by_name.r456,gen_by_name.r7))

    # gen_by_name.r12345.add_factorizations((gen_by_name.r1,gen_by_name.r2345),(gen_by_name.r12,gen_by_name.r345),
    #                                     (gen_by_name.r123,gen_by_name.r45),(gen_by_name.r1234,gen_by_name.r5))
    # gen_by_name.r23456.add_factorizations((gen_by_name.r2,gen_by_name.r3456),(gen_by_name.r23,gen_by_name.r456),
    #                                     (gen_by_name.r234,gen_by_name.r56),(gen_by_name.r2345,gen_by_name.r6))
    # gen_by_name.r34567.add_factorizations((gen_by_name.r3,gen_by_name.r4567),(gen_by_name.r34,gen_by_name.r567),
    #                                     (gen_by_name.r345,gen_by_name.r67),(gen_by_name.r3456,gen_by_name.r7))   


    # gen_by_name.r123456.add_factorizations((gen_by_name.r1,gen_by_name.r23456),(gen_by_name.r12,gen_by_name.r3456),
    #                                     (gen_by_name.r123,gen_by_name.r456),(gen_by_name.r1234,gen_by_name.r56),
    #                                     (gen_by_name.r12345,gen_by_name.r6))
    # gen_by_name.r234567.add_factorizations((gen_by_name.r2,gen_by_name.r34567),(gen_by_name.r23,gen_by_name.r4567),
    #                                     (gen_by_name.r234,gen_by_name.r567),(gen_by_name.r2345,gen_by_name.r67),
    #                                     (gen_by_name.r23456,gen_by_name.r7)) 

    # gen_by_name.r1234567.add_factorizations((gen_by_name.r1,gen_by_name.r234567),(gen_by_name.r12,gen_by_name.r34567),
    #                                     (gen_by_name.r123,gen_by_name.r4567),(gen_by_name.r1234,gen_by_name.r567),
    #                                     (gen_by_name.r12345,gen_by_name.r67),(gen_by_name.r123456,gen_by_name.r7)) 


    idem_by_name=AttrDict({
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

    return dg_algebra(gen_by_name=gen_by_name,idem_by_name=idem_by_name,multiplication_table=multiplication_table,name='g2_A')

def init_pillowcase_algebra():
    gen_by_name=AttrDict({
                "i0": Generator("i0","i_0"),
                "i1": Generator("i1","i_1"),
                "i2": Generator("i2","i_2"),
                "j0": Generator("j0","j_0"),
                "j1": Generator("j1","j_1"),
                "j2": Generator("j2","j_2"),

                "r0": Generator("r0","r_0","r'_0"),
                "r2": Generator("r2","r_2","r'_2"),

                "et1": Generator("et1","\\eta_1","\\eta'_1"),
                "et2": Generator("et2","\\eta_2","\\eta'_2"),
                "et3": Generator("et3","\\eta_3","\\eta'_3"),
                "et12": Generator("et12","\\eta_{12}","\\eta'_{21}"),
                "et23": Generator("et23","\\eta_{23}","\\eta'_{32}"),
                "et123": Generator("et123","\\eta_{123}","\\eta'_{321}"),

                "ks1": Generator("ks1","\\xi_1","\\xi'_1"),
                "ks2": Generator("ks2","\\xi_2","\\xi'_2"),
                "ks3": Generator("ks3","\\xi_3","\\xi'_3"),
                "ks12": Generator("ks12","\\xi_{12}","\\xi'_{21}"),
                "ks23": Generator("ks23","\\xi_{23}","\\xi'_{32}"),
                "ks123": Generator("ks123","\\xi_{123}","\\xi'_{321}"),
                })


    # now this stuff is done when algebra is initiated
    # gen_by_name.et12.add_factorizations((gen_by_name.et1,gen_by_name.et2))
    # gen_by_name.et23.add_factorizations((gen_by_name.et2,gen_by_name.et3))
    # gen_by_name.et123.add_factorizations((gen_by_name.et1,gen_by_name.et23),(gen_by_name.et12,gen_by_name.et3))
    # gen_by_name.ks12.add_factorizations((gen_by_name.ks1,gen_by_name.ks2))
    # gen_by_name.ks23.add_factorizations((gen_by_name.ks2,gen_by_name.ks3))
    # gen_by_name.ks123.add_factorizations((gen_by_name.ks1,gen_by_name.ks23),(gen_by_name.ks12,gen_by_name.ks3))

    idem_by_name=AttrDict({
                    "i0": gen_by_name.i0,
                    "i1": gen_by_name.i1,
                    "i2": gen_by_name.i2,
                    "j0": gen_by_name.j0,
                    "j1": gen_by_name.j1,
                    "j2": gen_by_name.j2
                    })

    multiplication_table={(gen_by_name.et1,gen_by_name.et2):gen_by_name.et12,
                        (gen_by_name.et2,gen_by_name.et3):gen_by_name.et23,
                        (gen_by_name.et1,gen_by_name.et23):gen_by_name.et123,
                        (gen_by_name.et12,gen_by_name.et3):gen_by_name.et123,

                        (gen_by_name.ks1,gen_by_name.ks2):gen_by_name.ks12,
                        (gen_by_name.ks2,gen_by_name.ks3):gen_by_name.ks23,
                        (gen_by_name.ks1,gen_by_name.ks23):gen_by_name.ks123,
                        (gen_by_name.ks12,gen_by_name.ks3):gen_by_name.ks123,

                        (gen_by_name.i0,gen_by_name.r0):gen_by_name.r0,
                        (gen_by_name.i0,gen_by_name.i0):gen_by_name.i0,
                        (gen_by_name.i0,gen_by_name.et1):gen_by_name.et1,
                        (gen_by_name.i0,gen_by_name.et12):gen_by_name.et12,
                        (gen_by_name.i0,gen_by_name.et123):gen_by_name.et123,

                        (gen_by_name.r0,gen_by_name.j0):gen_by_name.r0,
                        (gen_by_name.j0,gen_by_name.j0):gen_by_name.j0,
                        (gen_by_name.et3,gen_by_name.j0):gen_by_name.et3,
                        (gen_by_name.et23,gen_by_name.j0):gen_by_name.et23,
                        (gen_by_name.et123,gen_by_name.j0):gen_by_name.et123,

                        (gen_by_name.r2,gen_by_name.j2):gen_by_name.r2,
                        (gen_by_name.j2,gen_by_name.j2):gen_by_name.j2,
                        (gen_by_name.j2,gen_by_name.ks3):gen_by_name.ks3,
                        (gen_by_name.ks2,gen_by_name.j2):gen_by_name.ks2,
                        (gen_by_name.ks12,gen_by_name.j2):gen_by_name.ks12,

                        (gen_by_name.i2,gen_by_name.r2):gen_by_name.r2,
                        (gen_by_name.i2,gen_by_name.i2):gen_by_name.i2,
                        (gen_by_name.i2,gen_by_name.ks2):gen_by_name.ks2,
                        (gen_by_name.i2,gen_by_name.ks23):gen_by_name.ks23,
                        (gen_by_name.ks1,gen_by_name.i2):gen_by_name.ks1,

                        (gen_by_name.i1,gen_by_name.i1):gen_by_name.i1,
                        (gen_by_name.i1,gen_by_name.ks1):gen_by_name.ks1,
                        (gen_by_name.i1,gen_by_name.ks12):gen_by_name.ks12,
                        (gen_by_name.i1,gen_by_name.ks123):gen_by_name.ks123,
                        (gen_by_name.i1,gen_by_name.et2):gen_by_name.et2,
                        (gen_by_name.i1,gen_by_name.et23):gen_by_name.et23,
                        (gen_by_name.et1,gen_by_name.i1):gen_by_name.et1,

                        (gen_by_name.j1,gen_by_name.j1):gen_by_name.j1,
                        (gen_by_name.j1,gen_by_name.et3):gen_by_name.et3,
                        (gen_by_name.et12,gen_by_name.j1):gen_by_name.et12,
                        (gen_by_name.et2,gen_by_name.j1):gen_by_name.et2,
                        (gen_by_name.ks3,gen_by_name.j1):gen_by_name.ks3,
                        (gen_by_name.ks23,gen_by_name.j1):gen_by_name.ks23,
                        (gen_by_name.ks123,gen_by_name.j1):gen_by_name.ks123,
                                    }

    return dg_algebra(gen_by_name=gen_by_name,idem_by_name=idem_by_name,multiplication_table=multiplication_table,name='pil_A')

torus_A=init_torus_algebra()
g2_A=init_genus2_algebra()
pil_A=init_pillowcase_algebra()
# g2_A.show()
# A.show()
# Identity_DA_bimodule.show()
# Identity_DA_bimodule.check()