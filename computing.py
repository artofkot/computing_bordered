from algebra_and_DA import A,Identity_DA,DA_Bimodule

def init_m_Dehn_twist_DA_bimodule(A):
    gen_by_name=AttrDict({
                "p": Generator("x"),
                "q": Generator("y"),
                "r": Generator("r")
                })
    gen_by_name.p.add_idems(torus_algebra.idem.i0,torus_algebra.idem.i0)
    gen_by_name.q.add_idems(torus_algebra.idem.i1,torus_algebra.idem.i1)
    gen_by_name.r.add_idems(torus_algebra.idem.i1,torus_algebra.idem.i0)

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