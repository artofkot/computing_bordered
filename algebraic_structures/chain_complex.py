# -*- coding: utf-8 -*- 
from basics import Bunch_of_arrows

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
    
    arrows_in_z2=[arrow for arrow in C.arrows if (arrow[1]==z2 and arrow[0]!=z1 and arrow[0]!=z2)]
    arrows_from_z1=[arrow for arrow in C.arrows if (arrow[0]==z1 and arrow[1]!=z1 and arrow[1]!=z2)]

    for arrow_in_z2 in arrows_in_z2:
        for arrow_from_z1 in arrows_from_z1:
            new_arrows[(arrow_in_z2[0],arrow_from_z1[1])]+=1

    new_arrows.delete_arrows_with_even_coeff()

    C2=ChainComplex(new_generators,new_arrows, C.name + '_red')
    return C2

def homology_dim(C):
    C.arrows.delete_arrows_with_even_coeff()
    there_is_diff=0
    for arrow in C.arrows:
        if arrow[0]==arrow[1]: continue
        there_is_diff=1
        canceled_C=cancel_differential(C,arrow)
        return (homology_dim(canceled_C))

    if there_is_diff==0:
        print "\n generators of HH are:"
        print C.genset
        return len(C.genset)

