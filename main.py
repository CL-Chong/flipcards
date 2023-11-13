from sympy import symbols, diff, sin, cos, exp, log, latex, expand
from fractions import Fraction
import sys
from matplotlib.backend_bases import MouseButton
import numpy as np
import matplotlib.pyplot as plt
import importlib

x = symbols("x", real=True)


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

    diff = importlib.import_module("differentiation.methods")
    diff_dict = vars(diff)

    while True:
        ax.axis("off")
        question0, answer0 = diff_dict[np.random.choice(listq)]()
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
