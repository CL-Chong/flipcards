from fractions import Fraction

import numpy as np
from sympy import cos, diff, exp, expand, integrate, latex, log, sin, symbols

from questions._classtemplate import QuestionBank

# conventions:
# all classes must have metaclass QuestionBank
# Class: declare all symbolic variables used in questions in __init__
# questions: implemented as instance methods. Need class reference "self" to get relevant symbolic variables
#            must take self as input and output question, answer


class Basic(metaclass=QuestionBank):
    def __init__(self):
        self._x = symbols("x", real=True)

    def quickint0(self):
        tt = np.random.randint(1, 5, size=[3])
        sgn = np.random.choice([1, -1])

        fcn = tt[0] * (self._x ** Fraction(sgn * tt[1], tt[2]))
        question = f"$\\int {latex(fcn)} \\ dx$"
        ifcn = integrate(fcn, self._x)
        answer = f"${latex(ifcn)} + C$"
        return question, answer

    def quickint1(self):  # polynomial integration
        aa = np.random.randint(0, high=6, size=[3])
        bb = np.random.randint(-9, high=9, size=[3])
        aa.sort()
        aa = aa[::-1]

        fcn = (
            bb[0] * (self._x ** aa[0])
            + bb[1] * (self._x ** aa[1])
            + bb[2] * (self._x ** aa[2])
        )
        question = f"$\\int {latex(fcn)} \\ dx$"
        ifcn = integrate(fcn, self._x)
        answer = f"${latex(ifcn)} + C$"
        return question, answer

    def eleint1(self):  # integrals of elementary non-polynomial functions
        ss = [sin(self._x), cos(self._x), exp(self._x), log(self._x)]
        bb2 = np.random.randint(-9, high=9, size=[2])

        fcn = bb2[0] * np.random.choice(ss) + bb2[1] * np.random.choice(ss)
        question = f"$\\int {latex(fcn)} \\ dx$"
        ifcn = integrate(fcn, self._x)
        answer = f"${latex(ifcn)} + C$"
        return question, answer

    def quickint2(self):  # fractional and negative indices integration
        aa = np.random.randint(-6, high=6, size=[2])
        bb = np.random.randint(-9, high=9, size=[2])
        if bb[0] == 0 and bb[1] == 0:
            bb[0] = bb[0] + 1
        cc = np.random.randint(1, high=4, size=[2])
        aa.sort()
        aa = aa[::-1]

        fcn = bb[0] * (self._x ** Fraction(aa[0], cc[0])) + bb[1] * (
            self._x ** Fraction(aa[1], cc[1])
        )
        question = f"$\\int {latex(fcn)} \\ dx$"
        ifcn = integrate(fcn, self._x)
        answer = f"${latex(ifcn)} + C$"
        return question, answer
