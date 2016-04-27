# -*- coding: utf-8 -*- 
from algebraic_structures.algebra import AttrDict, Generator, A
from algebraic_structures.da_bimodule import  Bunch_of_arrows, DA_bimodule,cancel_pure_differential, box_tensor,arrow_to_str
from algebraic_structures.da_bimodule import  randomly_cancel_until_possible, are_equal, cancel_this_number_of_times
from algebraic_structures.da_bimodule  import in_mod_gen, out_mod_gen, in_alg_tuple, out_alg_gen
from algebraic_structures.morphism import check_df_is_0, composition
import time, sys, random

class ChainComplex(object):
    def __init__(self,genset,arrows,name):
        self.name=name
        self.genset=genset
        #differentials are represented by bunch of arrows with coefficients 1
        self.arrows=arrows
        self.arrows.delete_arrows_with_even_coeff()

        dd=self.compute_dd()
        dd.delete_arrows_with_even_coeff()
        if dd:
            # self.show()
            # print '\ndd is wrong:'
            # dd.show()
            raise NameError("Chain complex " + self.name + " doesn't satisfy dd=0 !!!")

    def compute_dd(self):
        dd=Bunch_of_arrows()
        #contribution of double arrows
        for arrow1 in self.arrows:
            for arrow2 in self.arrows:
                if not arrow1[1]==arrow2[0]: continue
                else:  
                    dd[(arrow1[0],arrow2[1])]+=1
        return dd

    def show(self):
        print "=========="
        print self.name + ':\n'
        print "Generators"
        print self.genset
        print "\nDifferentials"
        self.arrows.show()

def cancel_differential(C,d):
    z1=d[0]
    z2=d[1]
    
    new_generators=C.genset
    new_generators.remove(z1)
    new_generators.remove(z2)
    
    old_arrows_that_survive=[arrow for arrow in C.arrows if (arrow[0]!=z1 and arrow[1]!=z2  and arrow[1]!=z1 and arrow[0]!=z2 ) ]
    new_arrows=Bunch_of_arrows(old_arrows_that_survive)
    
    arrows_in_z2=[arrow for arrow in C.arrows if (arrow[1]==z2 and d!=arrow)]
    arrows_from_z1=[arrow for arrow in C.arrows if (arrow[0]==z1 and d!=arrow)]

    for arrow_in_z2 in arrows_in_z2:
        for arrow_from_z1 in arrows_from_z1:
            new_arrows[(arrow_in_z2[0],arrow_from_z1[1])]+=1

    new_arrows.delete_arrows_with_even_coeff()

    C2=ChainComplex(new_generators,new_arrows, C.name + '_reduced')
    return C2



def homology_dim(C):
    C.arrows.delete_arrows_with_even_coeff()
    there_is_diff=0
    for arrow in C.arrows:
        there_is_diff=1
        canceled_C=cancel_differential(C,arrow)
        return (homology_dim(canceled_C))

    if there_is_diff==0:
        return len(C.genset)


def is_cyclic(g):
    """Return True if the directed graph g has a cycle.
    g must be represented as a dictionary mapping vertices to
    iterables of neighbouring vertices. For example:

    >>> cyclic({1: (2,), 2: (3,), 3: (1,)})
    True
    >>> cyclic({1: (2,), 2: (3,), 3: (4,)})
    False
    """
    path = set()

    def visit(vertex):
        path.add(vertex)
        for neighbour in g.get(vertex, ()):
            if neighbour in path or visit(neighbour):
                return True
        path.remove(vertex)

        return False

    return any(visit(v) for v in g)

def is_bounded(DA1):
    graph={}
    for gen in DA1.genset:
        graph[gen]=()
        for arrow in DA1.arrows:
            if in_mod_gen(arrow)==gen:
                graph[gen]=graph[gen]+(out_mod_gen(arrow),)
    return not is_cyclic(graph)


def CH(DA1):

    def looping(container_of_final_diffs, current_gen, current_alg_tuple, first_gen, DA1,depth):
        # print 'depth=' + str(depth)
        # print 'first_gen=' + str(first_gen)
        # print 'current_gen=' + str(current_gen)
        # print 'current_alg_tuple' + str(current_alg_tuple)
        try:
            ending_arrows=[ar for ar in DA1.arrows if (in_mod_gen(ar)==current_gen and in_alg_tuple(ar)==current_alg_tuple and out_alg_gen(ar)==1  )  ]
            for ar in ending_arrows:
                container_of_final_diffs[(first_gen,out_mod_gen(ar))]+=1
        except: pass

        for ind in range(len(current_alg_tuple)+1):
            possible_next_arrows=[ar for ar in DA1.arrows if (in_mod_gen(ar)==current_gen and in_alg_tuple(ar)==current_alg_tuple[:ind] and out_alg_gen(ar)!=1 )]

            for arrow in possible_next_arrows:
                looping(container_of_final_diffs,
                        current_gen=out_mod_gen(arrow),
                        current_alg_tuple=current_alg_tuple[ind:]+(out_alg_gen(arrow),),
                        first_gen=first_gen,
                        DA1=DA1,depth=depth+1)

    if not is_bounded(DA1):
        raise NameError("Bimodule " + DA1.name + " is not bounded, so can't take HH of it!")
    
    generators=[gen for gen in DA1.genset if gen.idem.left==gen.idem.right]
    differentials=Bunch_of_arrows()

    for first_gen in generators:
        first_arrows=[ar for ar in DA1.arrows if (in_mod_gen(ar)==first_gen and in_alg_tuple(ar)==() )]
        for first_arrow in first_arrows:
            if out_alg_gen(first_arrow)==1:
                # finding pure differentials
                differentials[(first_gen,out_mod_gen(first_arrow))]+=1
            else: 
                # finding all other differentials
                looping(container_of_final_diffs=differentials,
                    current_gen=out_mod_gen(first_arrow),
                    current_alg_tuple=(out_alg_gen(first_arrow),),
                    first_gen=first_gen,
                    DA1=DA1,depth=1)

    return ChainComplex(generators, differentials, "CH("+DA1.name+")")








