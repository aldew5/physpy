"""
1D Motion
"""

import math

def solve_kinematic(v, v0, a, t, x):
    """Takes in at least three known variables, unknown variables should be specified
        as none, and returns a tuple containing the values for all the variables"""
# defining functions to handle every combination of three variables possible to solve for the other two
    def big1(v0, v, t):
        """ returns [x, a]"""
        x = ((v + v0)/2)*t
        a = (v-v0)/t

        return [x, a]

    def big2(v0, v, a):
        """returns [x, t]"""
        t = (v-v0)/a
        x = ((v+v0)/2)*t

        return [x, t]

    def big3(v0, v, x):
        """returns t, a"""
        t = (2*x)/(v+v0)
        a = (v**2 - v0**2)/(2*x)

        return [t, a]

    def big4(v0, t, a):
        """returns v, x"""
        v = v0 + a* t
        x = ((v+v0)/2)*t

        return [v, x]

    def big5(v0, t, x):
        """returns v, a"""
        v = (2*x)/t - v0
        a = (v-v0)/t

        return [v, a]

    def big6(v0, a, x):
        """returns v, t"""
        v = math.sqrt(v0**2 + 2*a*x)
        t = (v-v0)/a

        return [v, t]

    def big7(v, t, a):
        """returns x, v0"""
        x = v0*t + (a*t**2)/2
        v0 = v - a*t

        return [x, v0]

    def big8(v, t, x):
        """returns v0, a"""
        v0 = (2*x)/t - v
        a = (v-v0)/t

        return [v0, a]

    def big9(v, a, x):
        """returns v0, t"""
        v0 = math.sqrt(-2*a*x + v**2)
        t = (v-v0)/a

        return [v0, t]

    def big10(t, a, x):
        """returns v, v0"""
        v0 = x/t - (a*t)/2
        v = v0 + a * t

        return [v, v0]


    var, num_vars = [v0, t, x, a, v], 0

    # check how many variables are missing
    for v in var:
        if v != 'none':
            num_vars += 1

    # if less than three variables were given the others cannot be solved for
    assert num_vars >= 3, "You don't have enough variables to solve"

    # conditionals using all of the 10 equations in the proper instances
    if v0 != 'none' and v != 'none' and t != 'none':
        x = big1(v0, v, t)[0]
        a = big1(v0, v, t)[1]

    elif v0 != 'none' and v != 'none' and a != 'none':
        x = big2(v0, v, a)[0]
        t = big2(v0, v, a)[1]

    elif v0 != 'none' and v != 'none' and x != 'none':
        t = big3(v0, v, x)[0]
        a = big3(v0, v, x)[1]

    elif v0 != 'none' and t != 'none' and a != 'none':
        v = big4(v0, t, a)[0]
        x = big4(v0, t, a)[1]

    elif v0 != 'none' and t != 'none' and x != 'none':
        v = big5(v0, t, x)[0]
        a = big5(v0, t, x)[1]

    elif v0 != 'none' and a != 'none' and x != 'none':
        v = big6(v0, a, x)[0]
        t = big6(v0, a, x)[1]

    elif v != 'none' and t != 'none' and a != 'none':
        x = big7(v, t, a)[0]
        v0 = big7(v, t, a)[1]

    elif v != 'none' and t != 'none' and x != 'none':
        v0 = big8(v, t, x)[0]
        a = big8(v, t, x)[1]

    elif v != 'none' and a != 'none' and x != 'none':
        v0 = big9(v, a, x)[0]
        t  = big9(v, a, x)[1]

    elif t != 'none' and a != 'none' and x != 'none':
        v = big10(t, a, x)[0]
        v0 = big10(t, a, x)[1]
        

    
    return (v, v0, a, t, x)
