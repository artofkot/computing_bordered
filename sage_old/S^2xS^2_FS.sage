comm = lambda x, y: x*y*x^-1*y^-1
Fr.<a1,a2,b1,b2,c1,c2,d1,d2> = FreeGroup()
F=Fr/[comm(a1,c1),comm(a1,c2),comm(a1,d2),comm(b1,c1),comm(a2,c1),comm(a2,c2),comm(a2,d1),comm(b2,c2),
        comm(a1,b1)*comm(a2,b2), comm(c1,d1)*comm(c2,d2),
        (a1^-1)*comm(b1^-1,d1^-1),((b1)^-1)*comm(a1^-1,d1),(a2^-1)*comm(b2^-1,d2^-1),(b2^-1)*comm(a2^-1,d2),
        (c1^-1)*comm(d1^-1,b2^-1),(d1^-1)*comm(c1^-1,b2),(c2^-1)*comm(d2^-1,b1^-1),(d2^-1)*comm(c2^-1,b1)]

# a1 c1, b1 d1*c1*d1^-1, a2 c2, b2 d2*c2*d2^-1
# a2 c1, d1 b2*a2*b2^-1, c2 a1, d2 b1*a1*b1^-1

print F.gap().IsomorphismSimplifiedFpGroup()
print "\n"
print F.simplified()
print "\n"
print F.simplified().gap()

############## print F.gap().StructureDescription()


# for x in [a1,c1]:
#     for y in [b1, d1*c1*d1^-1]:
#         for t in [a2, c2]:
#             for z in [b2, d2*c2*d2^-1]:
#                 for k in [a2, c1]:
#                     for l in [d1,b2*a2*b2^-1]:
#                         for m in [c2, a1]:
#                             for n in [d2, b1*a1*b1^-1]:
#                                 F=Fr/[comm(a1,c1),comm(a1,c2),comm(a1,d2),comm(b1,c1),comm(a2,c1),comm(a2,c2),comm(a2,d1),comm(b2,c2),
#                                     comm(a1,b1)*comm(a2,b2), comm(c1,d1)*comm(c2,d2),
#                                     (x^-1)*comm(b1^-1,d1^-1),(y^-1)*comm(a1^-1,d1),(t^-1)*comm(b2^-1,d2^-1),(z^-1)*comm(a2^-1,d2),
#                                     (k^-1)*comm(d1^-1,b2^-1),(l^-1)*comm(c1^-1,b2),(m^-1)*comm(d2^-1,b1^-1),(n^-1)*comm(c2^-1,b1)]
#                                 print F.simplified().gap()