from fractions import Fraction

import numpy as np
from sympy import cos, diff, exp, expand, latex, log, sin, symbols

from questions._classtemplate import QuestionBank

# conventions:
# all classes must have metaclass QuestionBank
# Class: declare all symbolic variables used in questions in __init__
# questions: implemented as instance methods. Need class reference "self" to get relevant symbolic variables
#            must take self as input and output question, answer


class Basic(metaclass=QuestionBank):
    def __init__(self):
        self._x = symbols("x", real=True)

    def quickdiff0(self):
        tt = np.random.randint(1, 5, size=[3])
        sgn = np.random.choice([1, -1])

        fcn = tt[0] * (self._x ** Fraction(sgn * tt[1], tt[2]))
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = diff(fcn, self._x)
        answer = "$" + latex(dfcn) + "$"
        return question, answer

    def quickdiff1(self):  # polynomial differentiation
        aa = np.random.randint(0, high=6, size=[3])
        bb = np.random.randint(-9, high=9, size=[3])
        aa.sort()
        aa = aa[::-1]

        fcn = (
            bb[0] * (self._x ** aa[0])
            + bb[1] * (self._x ** aa[1])
            + bb[2] * (self._x ** aa[2])
        )
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = diff(fcn, self._x)
        answer = "$" + latex(dfcn) + "$"
        return question, answer

    def elediff1(self):  # derivatives of elementary non-polynomial functions
        ss = [sin(self._x), cos(self._x), exp(self._x), log(self._x)]
        bb2 = np.random.randint(-9, high=9, size=[2])

        fcn = bb2[0] * np.random.choice(ss) + bb2[1] * np.random.choice(ss)
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = diff(fcn, self._x)
        answer = "$" + latex(dfcn) + "$"
        return question, answer

    def quickdiff2(self):  # fractional and negative indices differentiation
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
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = diff(fcn, self._x)
        answer = "$" + latex(dfcn) + "$"
        return question, answer


class ProductRule(metaclass=QuestionBank):
    def __init__(self):
        self._x = symbols("x", real=True)

    def diffuv1a(self):  # product rule 1 - polynomial * non-polynomial elementary
        aa = np.random.randint(0, high=6, size=[2])
        bb = np.random.randint(-9, high=9, size=[2])
        if bb[0] == 0 and bb[1] == 0:
            bb[0] = bb[0] + 1
        aa.sort()
        aa = aa[::-1]

        u = bb[0] * (self._x ** aa[0]) + bb[1] * (self._x ** aa[1])
        v = np.random.choice([sin(self._x), cos(self._x), exp(self._x), log(self._x)])
        fcn = u * v
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = expand(diff(fcn, self._x))
        answer = "$" + latex(dfcn) + "$"
        return question, answer

    def diffuv1b(self):  # product rule 1b - elementary functions
        uu = np.random.choice(
            [sin(self._x), cos(self._x), exp(self._x), log(self._x)],
            replace=False,
            size=2,
        )
        w = np.random.randint(1, 9) * self._x ** Fraction(
            np.random.randint(1, 5), np.random.randint(1, 4)
        )

        fcn = np.random.choice([uu[0] * uu[1], uu[0] * w])
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = expand(diff(fcn, self._x))
        answer = "$" + latex(dfcn) + "$"
        return question, answer


class QuotientRule(metaclass=QuestionBank):
    def __init__(self):
        self._x = symbols("x", real=True)

    def diffuqv1(self):  # quotient rule 1 - elementary and monomials
        uu = np.random.choice(
            [sin(self._x), cos(self._x), exp(self._x), log(self._x)],
            replace=False,
            size=2,
        )
        np.append(
            uu,
            np.random.randint(0, 9)
            * self._x ** Fraction(np.random.randint(1, 5), np.random.randint(1, 4)),
        )
        [u, v] = np.random.choice(uu, replace=False, size=2)

        fcn = u / v
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = expand(diff(u, self._x) * v - diff(v, self._x) * u) / (v**2)
        answer = "$" + latex(dfcn) + "$"
        return question, answer

    def diffuqv2(self):  # quotient rule 2 - polynomial/polynomial
        aa = np.random.randint(0, high=3, size=[2])
        bb = np.random.randint(-9, high=9, size=[2])
        if bb[0] == 0 and bb[1] == 0:
            bb[0] = bb[0] + 1
        aa.sort()
        aa = aa[::-1]

        u = bb[0] * (self._x ** aa[0]) + bb[1] * (self._x ** aa[1])
        aa2 = np.random.randint(0, high=4, size=[2])
        bb2 = np.random.randint(-9, high=9, size=[2])
        if bb2[0] == 0 and bb2[1] == 0:
            bb2[0] = bb[0] + 1
        aa2.sort()
        aa2 = aa2[::-1]

        v = bb2[0] * (self._x ** aa2[0]) + bb[1] * (self._x ** aa2[1])
        fcn = u / v
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = expand(diff(u, self._x) * v - diff(v, self._x) * u) / (v**2)
        answer = "$" + latex(dfcn) + "$"
        return question, answer

    def diffuqv2b(
        self,
    ):  # quotient rule 2b - polynomial/elementary or elementary/polynomial
        aa = np.random.randint(0, high=4, size=[2])
        bb = np.random.randint(-9, high=9, size=[2])
        if bb[0] == 0 and bb[1] == 0:
            bb[0] = bb[0] + 1
        aa.sort()
        aa = aa[::-1]

        u = bb[0] * (self._x ** aa[0]) + bb[1] * (self._x ** aa[1])
        v = np.random.choice([sin(self._x), cos(self._x), exp(self._x), log(self._x)])
        if np.random.uniform(0, 1) > 0.5:
            u, v = v, u
        fcn = u / v
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = expand(diff(u, self._x) * v - diff(v, self._x) * u) / (v**2)
        answer = "$" + latex(dfcn) + "$"
        return question, answer


class ChainRule(metaclass=QuestionBank):
    def __init__(self):
        self._x = symbols("x", real=True)

    def diffchain1a(self):  # chain rule 1 - elementary with linear coefficients
        a = np.random.randint(1, 9)
        sgn = np.random.choice([-1, 1])
        g = a * sgn * self._x

        fcn = np.random.choice([sin(g), cos(g), exp(g), a ** (g), log(a * self._x)])
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = expand(diff(fcn, self._x))
        answer = "$" + latex(dfcn) + "$"
        return question, answer

    def diffchain1b(self):  # chain rule 1b - elementary with powers
        tt = np.random.randint(1, 5, size=[3])
        sgn = np.random.choice([1, -1])
        g = np.random.choice([sin(self._x), cos(self._x), exp(self._x), log(self._x)])

        fcn = tt[0] * (g ** Fraction(sgn * tt[1], tt[2]))
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = diff(fcn, self._x)
        answer = "$" + latex(dfcn) + "$"
        return question, answer

    def diffchain2a(self):  # chain rule 2 - composed elementary functions
        g = np.random.choice([sin(self._x), cos(self._x), exp(self._x), log(self._x)])

        fcn = np.random.choice([sin(g), cos(g), exp(g), log(g)])
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = diff(fcn, self._x)
        answer = "$" + latex(dfcn) + "$"
        return question, answer

    def diffchain2b(self):  # chain rule 2b - polynomial inside elementary/power
        aa = np.random.randint(0, high=6, size=[2])
        bb = np.random.randint(-9, high=9, size=[2])
        if bb[0] == 0 and bb[1] == 0:
            bb[0] = bb[0] + 1
        aa.sort()
        aa = aa[::-1]
        g = bb[0] * (self._x ** aa[0]) + bb[1] * (self._x ** aa[1])
        g2 = np.absolute(bb[0]) * (self._x ** aa[0]) + bb[1] * (self._x ** aa[1])

        fcn = np.random.choice(
            [sin(g), cos(g), exp(g), log(g2), g ** (1 / 2), g**3, g**4, g**5]
        )
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = diff(fcn, self._x)
        answer = "$" + latex(dfcn) + "$"
        return question, answer
