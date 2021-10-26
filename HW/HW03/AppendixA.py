'''Code from Appendix A of Assignment 3'''

debug = True

def applied_load(load, position, L_beam, W_beam):
    '''Define forces applied to truss based on hoist position and loads.

    Input:  load     - scalar weight of load on hoist plus the hoist [kN]
            position - scalar float position of hoist along beam [meters]
            L_beam   - scalar length of the I beam that the hoist transits [meters]
            W_beam   - scalar weight of the I beam
    Output: f        - 1D numpy float array of applied forces at joints [kN]

    Define 14x1 right side vector of applied forces at joints.

    The weight of the I beam is assumed to be equally shared at the
    two joints F and D.

    The weight of the load (including the hoist) is assumed to be linearly
    distributed between the two joints F and D.  For example,
     - position = 0        => 100% of load is at joint F,   0% at joint D;
     - position = L_beam/4 =>  75% of load is at joint F,  25% at joint D;
     - position = L_beam   =>   0% of load is at joint F, 100% at joint D.
    '''

    # figure out the equations to specify the elements of f, and then make f

    if (debug):
        print("hoist load [kN] =", load)
        print("hoist position [m] =", position)
        print("I beam length [m], weight [kN] =", L_beam, W_beam)
        print("truss load vector f [kN]:")
        print(f)
        print()

    return f
