from sympy import symbols, diff, sin, cos, exp, log, latex, expand
import numpy as np
from fractions import Fraction

x = symbols("x", real=True)


def quickdiff0():
    T = np.random.randint(1, 5, size=[3])
    sgn = np.random.choice([1, -1])

    fcn = T[0] * (x ** Fraction(sgn * T[1], T[2]))
    question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
    dfcn = diff(fcn, x)
    answer = "$" + latex(dfcn) + "$"
    return question, answer


def quickdiff1():  # polynomial differentiation
    A = np.random.randint(0, high=6, size=[3])
    B = np.random.randint(-9, high=9, size=[3])
    A.sort()
    A = A[::-1]

    fcn = B[0] * (x ** A[0]) + B[1] * (x ** A[1]) + B[2] * (x ** A[2])
    question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
    dfcn = diff(fcn, x)
    answer = "$" + latex(dfcn) + "$"
    return question, answer


def elediff1():  # derivatives of elementary non-polynomial functions
    S = [sin(x), cos(x), exp(x), log(x)]
    B2 = np.random.randint(-9, high=9, size=[2])

    fcn = B2[0] * np.random.choice(S) + B2[1] * np.random.choice(S)
    question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
    dfcn = diff(fcn, x)
    answer = "$" + latex(dfcn) + "$"
    return question, answer


def quickdiff2():  # fractional and negative indices differentiation
    A = np.random.randint(-6, high=6, size=[2])
    B = np.random.randint(-9, high=9, size=[2])
    if B[0] == 0 and B[1] == 0:
        B[0] = B[0] + 1
    C = np.random.randint(1, high=4, size=[2])
    A.sort()
    A = A[::-1]

    fcn = B[0] * (x ** Fraction(A[0], C[0])) + B[1] * (x ** Fraction(A[1], C[1]))
    question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
    dfcn = diff(fcn, x)
    answer = "$" + latex(dfcn) + "$"
    return question, answer


def diffuv1a():  # product rule 1 - polynomial * non-polynomial elementary
    A = np.random.randint(0, high=6, size=[2])
    B = np.random.randint(-9, high=9, size=[2])
    if B[0] == 0 and B[1] == 0:
        B[0] = B[0] + 1
    A.sort()
    A = A[::-1]

    u = B[0] * (x ** A[0]) + B[1] * (x ** A[1])
    v = np.random.choice([sin(x), cos(x), exp(x), log(x)])
    fcn = u * v
    question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
    dfcn = expand(diff(fcn, x))
    answer = "$" + latex(dfcn) + "$"
    return question, answer


def diffuv1b():  # product rule 1b - elementary functions
    U = np.random.choice([sin(x), cos(x), exp(x), log(x)], replace=False, size=2)
    w = np.random.randint(1, 9) * x ** Fraction(
        np.random.randint(1, 5), np.random.randint(1, 4)
    )

    fcn = np.random.choice([U[0] * U[1], U[0] * w])
    question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
    dfcn = expand(diff(fcn, x))
    answer = "$" + latex(dfcn) + "$"
    return question, answer


def diffuqv1():  # quotient rule 1 - elementary and monomials
    U = np.random.choice([sin(x), cos(x), exp(x), log(x)], replace=False, size=2)
    np.append(
        U,
        np.random.randint(0, 9)
        * x ** Fraction(np.random.randint(1, 5), np.random.randint(1, 4)),
    )
    [u, v] = np.random.choice(U, replace=False, size=2)

    fcn = u / v
    question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
    dfcn = expand(diff(u, x) * v - diff(v, x) * u) / (v**2)
    answer = "$" + latex(dfcn) + "$"
    return question, answer


def diffuqv2():  # quotient rule 2 - polynomial/polynomial
    A = np.random.randint(0, high=3, size=[2])
    B = np.random.randint(-9, high=9, size=[2])
    if B[0] == 0 and B[1] == 0:
        B[0] = B[0] + 1
    A.sort()
    A = A[::-1]

    u = B[0] * (x ** A[0]) + B[1] * (x ** A[1])
    A2 = np.random.randint(0, high=4, size=[2])
    B2 = np.random.randint(-9, high=9, size=[2])
    if B2[0] == 0 and B2[1] == 0:
        B2[0] = B[0] + 1
    A2.sort()
    A2 = A2[::-1]

    v = B2[0] * (x ** A2[0]) + B[1] * (x ** A2[1])
    fcn = u / v
    question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
    dfcn = expand(diff(u, x) * v - diff(v, x) * u) / (v**2)
    answer = "$" + latex(dfcn) + "$"
    return question, answer


def diffuqv2b():  # quotient rule 2b - polynomial/elementary or elementary/polynomial
    A = np.random.randint(0, high=4, size=[2])
    B = np.random.randint(-9, high=9, size=[2])
    if B[0] == 0 and B[1] == 0:
        B[0] = B[0] + 1
    A.sort()
    A = A[::-1]

    u = B[0] * (x ** A[0]) + B[1] * (x ** A[1])
    v = np.random.choice([sin(x), cos(x), exp(x), log(x)])
    if np.random.uniform(0, 1) > 0.5:
        u, v = v, u
    fcn = u / v
    question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
    dfcn = expand(diff(u, x) * v - diff(v, x) * u) / (v**2)
    answer = "$" + latex(dfcn) + "$"
    return question, answer


def diffchain1a():  # chain rule 1 - elementary with linear coefficients
    a = np.random.randint(1, 9)
    sgn = np.random.choice([-1, 1])
    g = a * sgn * x

    fcn = np.random.choice([sin(g), cos(g), exp(g), a ** (g), log(a * x)])
    question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
    dfcn = expand(diff(fcn, x))
    answer = "$" + latex(dfcn) + "$"
    return question, answer


def diffchain1b():  # chain rule 1b - elementary with powers
    T = np.random.randint(1, 5, size=[3])
    sgn = np.random.choice([1, -1])
    g = np.random.choice([sin(x), cos(x), exp(x), log(x)])

    fcn = T[0] * (g ** Fraction(sgn * T[1], T[2]))
    question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
    dfcn = diff(fcn, x)
    answer = "$" + latex(dfcn) + "$"
    return question, answer


def diffchain2a():  # chain rule 2 - composed elementary functions
    g = np.random.choice([sin(x), cos(x), exp(x), log(x)])

    fcn = np.random.choice([sin(g), cos(g), exp(g), log(g)])
    question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
    dfcn = diff(fcn, x)
    answer = "$" + latex(dfcn) + "$"
    return question, answer


def diffchain2b():  # chain rule 2b - polynomial inside elementary/power
    A = np.random.randint(0, high=6, size=[2])
    B = np.random.randint(-9, high=9, size=[2])
    if B[0] == 0 and B[1] == 0:
        B[0] = B[0] + 1
    A.sort()
    A = A[::-1]
    g = B[0] * (x ** A[0]) + B[1] * (x ** A[1])
    g2 = np.absolute(B[0]) * (x ** A[0]) + B[1] * (x ** A[1])

    fcn = np.random.choice(
        [sin(g), cos(g), exp(g), log(g2), g ** (1 / 2), g**3, g**4, g**5]
    )
    question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
    dfcn = diff(fcn, x)
    answer = "$" + latex(dfcn) + "$"
    return question, answer
