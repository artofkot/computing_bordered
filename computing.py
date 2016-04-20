from algebra_and_DA import A,Identity_DA,DA_bimodule

def init_m_Dehn_twist_DA_bimodule(A):
    gen_by_name=AttrDict({
                "p": Generator("x"),
                "q": Generator("y"),
                "r": Generator("r")
                })
    gen_by_name.p.add_idems(A.idem.i0,A.idem.i0)
    gen_by_name.q.add_idems(A.idem.i1,A.idem.i1)
    gen_by_name.r.add_idems(A.idem.i1,A.idem.i0)

    arrows=Set([
        # from p to q
        Arrow(              gen_by_name.p,(A.gen_by_name.r1,),
                A.gen_by_name.r1,gen_by_name.q),
        Arrow(              gen_by_name.p,(A.gen_by_name.r123,),
                A.gen_by_name.r123,gen_by_name.q),
        Arrow(              gen_by_name.p,(A.gen_by_name.r3,A.gen_by_name.r23),
                A.gen_by_name.r3,gen_by_name.q),

        # from p to r 
        Arrow(              gen_by_name.p,(A.gen_by_name.r12,),
                A.gen_by_name.r123,gen_by_name.r),
        Arrow(              gen_by_name.p,(A.gen_by_name.r3,A.gen_by_name.r2),
                A.gen_by_name.r3,gen_by_name.r),

        #from r to p
        Arrow(              gen_by_name.r,(),
                A.gen_by_name.r2,gen_by_name.p),

        #from r to q
        Arrow(              gen_by_name.r,(A.gen_by_name.r3,),
                1,gen_by_name.q),

        #from q to r
        Arrow(              gen_by_name.q,(A.gen_by_name.r2,),
                A.gen_by_name.r23,gen_by_name.r),

        #from q to q
        Arrow(              gen_by_name.q,(A.gen_by_name.r23,),
                A.gen_by_name.r23,gen_by_name.q)
    ])

    return DA_bimodule(gen_by_name,arrows,A)

m_Dehn_twist_DA_bimodule=init_m_Dehn_twist_DA_bimodule(A)
m_Dehn_twist_DA_bimodule.show()
m_Dehn_twist_DA_bimodule.check()