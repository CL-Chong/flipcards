from sympy import symbols, diff, sin, cos, exp, log, latex, expand
from fractions import Fraction
import sys
from matplotlib.backend_bases import MouseButton
import numpy as np
import matplotlib.pyplot as plt


def question_generator(qname):
    # [question,answer] = genq(qname)
    # input: qname - string of question name
    # outputs: question - string of question, formatted in latex
    #          answer - string of answer, formatted in latex

    x = symbols("x")

    if qname == "quickdiff0":
        T = np.random.randint(1, 5, size=[3])
        sgn = np.random.choice([1, -1])

        fcn = T[0] * (x ** Fraction(sgn * T[1], T[2]))
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = diff(fcn, x)
        answer = "$" + latex(dfcn) + "$"
    elif qname == "quickdiff1":  # polynomial differentiation
        A = np.random.randint(0, high=6, size=[3])
        B = np.random.randint(-9, high=9, size=[3])
        A.sort()
        A = A[::-1]

        fcn = B[0] * (x ** A[0]) + B[1] * (x ** A[1]) + B[2] * (x ** A[2])
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = diff(fcn, x)
        answer = "$" + latex(dfcn) + "$"
    elif qname == "quickdiff2":  # fractional and negative indices differentiation
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
    elif qname == "elediff1":  # derivatives of elementary non-polynomial functions
        S = [sin(x), cos(x), exp(x), log(x)]
        B2 = np.random.randint(-9, high=9, size=[2])

        fcn = B2[0] * np.random.choice(S) + B2[1] * np.random.choice(S)
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = diff(fcn, x)
        answer = "$" + latex(dfcn) + "$"
    elif qname == "diffuv1a":  # product rule 1 - polynomial * non-polynomial elementary
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
    elif qname == "diffuv1b":  # product rule 1b - elementary functions
        U = np.random.choice([sin(x), cos(x), exp(x), log(x)], replace=False, size=2)
        w = np.random.randint(1, 9) * x ** Fraction(
            np.random.randint(1, 5), np.random.randint(1, 4)
        )

        fcn = np.random.choice([U[0] * U[1], U[0] * w])
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = expand(diff(fcn, x))
        answer = "$" + latex(dfcn) + "$"
    elif qname == "diffuqv1":  # quotient rule 1 - elementary and monomials
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
    elif qname == "diffuqv2":  # quotient rule 2 - polynomial/polynomial
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
    elif (
        qname == "diffuqv2b"
    ):  # quotient rule 2b - polynomial/elementary or elementary/polynomial
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
    elif qname == "diffchain1a":  # chain rule 1 - elementary with linear coefficients
        a = np.random.randint(1, 9)
        sgn = np.random.choice([-1, 1])
        g = a * sgn * x

        fcn = np.random.choice([sin(g), cos(g), exp(g), a ** (g), log(a * x)])
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = expand(diff(fcn, x))
        answer = "$" + latex(dfcn) + "$"
    elif qname == "diffchain1b":  # chain rule 1b - elementary with powers
        T = np.random.randint(1, 5, size=[3])
        sgn = np.random.choice([1, -1])
        g = np.random.choice([sin(x), cos(x), exp(x), log(x)])

        fcn = T[0] * (g ** Fraction(sgn * T[1], T[2]))
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = diff(fcn, x)
        answer = "$" + latex(dfcn) + "$"
    elif qname == "diffchain2a":  # chain rule 2 - composed elementary functions
        g = np.random.choice([sin(x), cos(x), exp(x), log(x)])

        fcn = np.random.choice([sin(g), cos(g), exp(g), log(g)])
        question = "$\\frac{{d}}{{dx}}\\left(" + latex(fcn) + "\\right)$"
        dfcn = diff(fcn, x)
        answer = "$" + latex(dfcn) + "$"
    elif qname == "diffchain2b":  # chain rule 2b - polynomial inside elementary/power
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

    return [question, answer]


def main():
    # List of questions - comment out the questions you don't want
    listq = [
        "diffchain2b",  # chain rule 2b - polynomial inside elementary/power
        "diffchain2a",  # chain rule 2 - composed elementary functions
        "diffchain1b",  # chain rule 1b - elementary with powers
        "diffchain1a",  # chain rule 1 - elementary with linear coefficients
        "diffuqv1",  # quotient rule 1 - elementary and monomials
        "diffuqv2",  # quotient rule 2 - polynomial/polynomial
        "diffuv1b",  # product rule 2 - non-elementary * non-elementary/fractional index
        "diffuv1a",  # product rule 1 - polynomial * non-polynomial elementary
        "elediff1",  # elementary function differentiation 1
        "quickdiff2",  # fractional and negative indices
        "quickdiff1",  # polynomials
        "quickdiff0",  # basic monomial with fractional/negative index
    ]

    fig, ax = plt.subplots(figsize=(8, 8))
    plt.rcParams["text.usetex"] = True
    text_specs = {
        "fontsize": 25,
        "horizontalalignment": "center",
        "verticalalignment": "center",
    }

    # right-click to exit
    def click_handler(event):
        if event.button is MouseButton.RIGHT:
            sys.exit(0)

    while 1:
        ax.axis("off")
        [question0, answer0] = question_generator(np.random.choice(listq))
        ax.text(0, 1, question0, **text_specs)
        ax.text(
            0,
            1.6,
            "left-click for answer/next question, right-click to quit",
            **text_specs
        )
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        plt.connect("button_press_event", click_handler)
        plt.draw()
        plt.waitforbuttonpress()
        ax.text(0, -1, answer0, **text_specs, color="red")
        plt.draw()
        plt.waitforbuttonpress()
        ax.cla()


if __name__ == "__main__":
    main()
