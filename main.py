# from fractions import Fraction
import functools
import inspect
import sys
from types import FunctionType

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backend_bases import MouseButton

import differentiation.questions as diffq

# from sympy import cos, diff, exp, expand, latex, log, sin, symbols


# x = symbols("x", real=True)


def main():
    q_dict = {}

    diffq_cls_pl = [
        cls
        for _, cls in inspect.getmembers(diffq, inspect.isclass)
        if cls.__module__ == diffq.__name__
    ]

    for mycls in diffq_cls_pl:
        is_mycls = input(f"Include questions from {mycls}? (y/n) ")
        if is_mycls == "Y" or is_mycls == "y":
            q_dict.update(
                {k: functools.partial(v, mycls()) for k, v in mycls.dispatcher.items()}
            )

    if not q_dict:
        print("No questions selected. Exiting.")
        return

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

    while True:
        ax.axis("off")
        key_i = np.random.choice(list(q_dict.keys()))
        question0, answer0 = q_dict[key_i]()
        ax.text(0, 1, question0, **text_specs)
        ax.text(
            0,
            1.6,
            "left-click for answer/next question, right-click to quit",
            **text_specs,
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


# def getdicts(mycls):
#     # clsdict and fundict are dicts with the same keys.
#     # clsdict[key] gives the class object
#     # fundict[key] gives the callable (instance method) from the class
#     fundict = {}
#     clsdict = {}
#     cls = mycls()
#     for name, func in mycls.__dict__.items():
#         if isinstance(func, FunctionType) and not name.startswith("__"):
#             fundict.update({name: func})
#             clsdict.update({name: cls})
#     return clsdict, fundict


if __name__ == "__main__":
    main()
