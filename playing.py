from sets import Set
import collections

def check_idempotents_match(l,m):
    return (l.idem.right==m.idem.left)

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

class Arrow(object):
    def __init__(self, in_mod_gen, in_alg_tuple, out_alg_gen, out_mod_gen):
        self.in_mod_gen=in_mod_gen
        self.out_mod_gen=out_mod_gen
        self.in_alg_tuple=in_alg_tuple
        self.out_alg_gen=out_alg_gen

class Generator(object): # over F2
    def __init__(self, name):
        self.name = name

    def add_idems(self,idem1,idem2):
        self.idem=AttrDict({"left":idem1, "right":idem2})

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
                    print 
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
        print('Generators of algebra with their idempotents:')
        for gen in self.genset:
            print str(gen.idem.left) + ' ' + str(gen) + ' ' + str(gen.idem.right)
        print('Multiplications:')
        for k in self.multiplication_table:
            print str(k[0]) + '*' + str(k[1]) + '=' + str(self.multiplication_table[k])

# conventions: D side is left, A side is right
class DA_Bimodule(object):
    def __init__(self,gen_by_name,arrows,algebra):
        self.gen_by_name=gen_by_name
        self.genset=self.gen_by_name.values()
        self.arrows=arrows
        self.algebra=algebra
    
    def show(self):
        print('Generators of Da bimodule with their idempotents:')
        for gen in self.genset:
            print str(gen.idem.left) + ' ' + str(gen) + ' ' + str(gen.idem.right)

        print('Actions of DA bimodule:')
        for arrow in self.arrows:
            print "incoming:         " + str(arrow.in_mod_gen) +' '+ str(arrow.in_alg_tuple)
            print "outgoing: " + str(arrow.out_alg_gen) +' '+ str(arrow.out_mod_gen) + '\n'

    def check_matching_of_idempotents_in_action(self): 
        count_of_mismatches=0
        for arrow in self.arrows:
            if not check_idempotents_match(arrow.in_mod_gen,arrow.in_alg_tuple[0]):
                count_of_mismatches+=1
            if not check_idempotents_match(arrow.out_alg_gen,arrow.out_mod_gen):
                count_of_mismatches+=1
            for i in range(len(arrow.in_alg_tuple)-1):
                if not check_idempotents_match(arrow.in_alg_tuple[i],arrow.in_alg_tuple[i+1]):
                    count_of_mismatches+=1
        return count_of_mismatches==0


    def check_dd_is_0(self): 
        dd=collections.Counter()

        #contribution of double arrows
        # for arrow1 in self.arrows
        #     for arrow2 in self.arrows
        #         if arrow1.in


        #contribution of factorizing algebra elements
        
        for arrow in dd:
            if dd[arrow] % 2 != 0:  
                return False
        return True

    def check(self):
        if not self.check_matching_of_idempotents_in_action():
            print "Something is wrong with idempotents!"
        else: print "Idempotents match!"
        if not self.check_dd_is_0():
            print "Something is wrong with dd=0!"
        else: print "dd=0!"


    def differential_of_generator_and_a_tuple(self, gen1, alg_tuple): #gives element in AtensorM
        s=collections.Counter()
        for arrow in self.arrows: 
            if (arrow.in_mod_gen==gen1 and arrow.in_alg_tuple==alg_tuple):
                s[GeneratorA_tensor_M(arrow.out_alg_gen,arrow.out_mod_gen)]+=1
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

    return DGAlgebra(gen=gen,idem=idem,multiplication_table=multiplication_table)

def init_identity_DA_bimodule(torus_algebra):
    gen_by_name=AttrDict({
                "x": Generator("x"),
                "y": Generator("y")
                })
    gen_by_name.x.add_idems(torus_algebra.idem.i0,torus_algebra.idem.i0)
    gen_by_name.y.add_idems(torus_algebra.idem.i1,torus_algebra.idem.i1)

    arrows=Set([
        Arrow(              gen_by_name.x,(torus_algebra.gen_by_name.r12,),
                torus_algebra.gen_by_name.r12,gen_by_name.x),

        Arrow(              gen_by_name.y,(torus_algebra.gen_by_name.r23,),
                torus_algebra.gen_by_name.r23,gen_by_name.y),

        Arrow(              gen_by_name.x,(torus_algebra.gen_by_name.r1,),
                torus_algebra.gen_by_name.r1,gen_by_name.y),

        Arrow(              gen_by_name.y,(torus_algebra.gen_by_name.r2,),
                torus_algebra.gen_by_name.r2,gen_by_name.x),

        Arrow(              gen_by_name.x,(torus_algebra.gen_by_name.r123,),
                torus_algebra.gen_by_name.r123,gen_by_name.y),

        Arrow(              gen_by_name.x,(torus_algebra.gen_by_name.r3,),
                torus_algebra.gen_by_name.r3,gen_by_name.y)
    ])

    return DA_Bimodule(gen_by_name,arrows,torus_algebra)


#########################################################################################################
#########################################################################################################

A=init_torus_algebra()
Id_DA=init_identity_DA_bimodule(A)

A.show()
Id_DA.show()
Id_DA.check()
