# -*- coding: utf-8 -*- 
import sys
sys.path.append('../')
import matplotlib.pyplot as plt
from algebraic_structures.algebra import B_r, pil_A, AttrDict, Generator, dg_algebra
from algebraic_structures.left_d_module import left_d_in_mod_gen, left_d_out_alg_gen, left_d_out_mod_gen
from B_by_homol_pert_lemma import N_L0, D

# https://nickcharlton.net/posts/drawing-animating-shapes-matplotlib.html
def draw_D(N, pil_A): #N is a left D structure over A_pil
    plt.axes()
    circle1 = plt.Circle((0, 0), radius=0.1, fc='g')
    circle2 = plt.Circle((0, 5), radius=0.1, fc='g')
    circle3 = plt.Circle((5, 5), radius=0.1, fc='g')
    circle4 = plt.Circle((5, 0), radius=0.1, fc='g')

    plt.gca().add_patch(circle1)
    plt.gca().add_patch(circle2)
    plt.gca().add_patch(circle3)
    plt.gca().add_patch(circle4)

    line = plt.Line2D((0, 0), (0, 5), lw=0.5)
    plt.gca().add_line(line)

    plt.axis('scaled')
    plt.show()

def loops(N):
    gens_in_arrows=[]
    for ar in N.left_d_arrows:
        gens_in_arrows.append(left_d_in_mod_gen(ar))
        gens_in_arrows.append(left_d_out_mod_gen(ar))

    for gen in N.genset:
        if gens_in_arrows.count(gen)!=2: 
            print "not loop-type!"
            print gen
            print gens_in_arrows.count(gen)

loops(D)
# draw_D(N_L0,pil_A)
