from fractions import Fraction

import numpy as np
from sympy import (
    cancel,
    cos,
    diff,
    exp,
    expand,
    latex,
    log,
    simplify,
    sin,
    symbols,
    tan,
)

from questions._classtemplate import QuestionBank

# conventions:
# all classes must have metaclass QuestionBank
# Class: declare all symbolic variables used in questions in __init__
# questions: implemented as instance methods. Need class reference "self" to get relevant symbolic variables
#            must take self as input and output question, answer


class Basic(metaclass=QuestionBank):
    def __init__(self):
        self._t = symbols("t", real=True)

    def polypoly(self):
        idxs = np.random.randint(1, 5, size=[5])
        coeffs = np.random.randint(-5, 5, size=[5])
        if coeffs[0] * coeffs[1] * coeffs[2] == 0:
            coeffs[0] += 1
        if coeffs[3] * coeffs[4] == 0:
            coeffs[3] += 1
        xfcn = (
            coeffs[0] * self._t ** idxs[0]
            + coeffs[1] * self._t ** idxs[1]
            + coeffs[2] * self._t ** idxs[2]
        )
        yfcn = coeffs[3] * self._t ** idxs[3] + coeffs[4] * self._t ** idxs[4]
        if xfcn == 0:
            xfcn += self._t
        question = f"$x(t) = {latex(xfcn)}, \\ y(t) = {latex(yfcn)}$. \\ Find $\\frac{{dy}}{{dx}}$."
        dxfcn = diff(xfcn, self._t)
        dyfcn = diff(yfcn, self._t)
        ansfcn = cancel(dyfcn / dxfcn)
        answer = f"$\\frac{{dy}}{{dx}} = {latex(ansfcn)}$"
        return question, answer

    def powers(self):
        tt = np.random.randint(1, 5, size=[5])
        sgn = np.random.choice([1, -1])
        sgn2 = np.random.choice([1, -1])

        xfcn = tt[0] * (self._t ** Fraction(sgn * tt[1], tt[2]))
        yfcn = tt[3] * self._t ** (sgn2 * tt[4])

        question = f"$x(t) = {latex(xfcn)}, \\ y(t) = {latex(yfcn)}$. \\ Find $\\frac{{dy}}{{dx}}$."
        dxfcn = diff(xfcn, self._t)
        dyfcn = diff(yfcn, self._t)
        ansfcn = cancel(dyfcn / dxfcn)
        answer = f"$\\frac{{dy}}{{dx}} = {latex(ansfcn)}$"
        return question, answer

    def ele(self):
        uu = np.random.choice(
            [sin(self._t), cos(self._t), exp(self._t), log(self._t)],
            replace=False,
            size=2,
        )
        np.append(
            uu,
            np.random.randint(0, 9)
            * self._t ** Fraction(np.random.randint(1, 5), np.random.randint(1, 4)),
        )
        [xfcn, yfcn] = np.random.choice(uu, replace=False, size=2)
        question = f"$x(t) = {latex(xfcn)}, \\ y(t) = {latex(yfcn)}$. \\ Find $\\frac{{dy}}{{dx}}$."
        dxfcn = diff(xfcn, self._t)
        dyfcn = diff(yfcn, self._t)
        ansfcn = cancel(dyfcn / dxfcn)
        answer = f"$\\frac{{dy}}{{dx}} = {latex(ansfcn)}$"
        return question, answer
