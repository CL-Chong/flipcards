# from fractions import Fraction
import functools
import inspect
import sys
from types import FunctionType

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backend_bases import MouseButton

import questions


def main():
    q_dict = {}
    mdls = [
        mdl
        for _, mdl in inspect.getmembers(questions, inspect.ismodule)
        if not mdl.__name__.startswith("questions._")
    ]

    for mdl in mdls:
        is_mdl = input(f"Use {mdl.__name__}? (y/n) ")
        if is_mdl in ("Y", "y"):
            submdls = [
                submdl for _, submdl in inspect.getmembers(mdl, inspect.ismodule)
            ]
            for submdl in submdls:
                is_submdl = input(f"Use {submdl.__name__}? (y/n) ")
                if is_submdl in ("Y", "y"):
                    clss = [
                        cls
                        for _, cls in inspect.getmembers(submdl, inspect.isclass)
                        if cls.__module__ == submdl.__name__
                    ]
                    for cls in clss:
                        is_cls = input(f"Use {submdl.__name__}.{cls.__name__}? (y/n) ")
                        if is_cls in ("Y", "y"):
                            q_dict.update(
                                {
                                    cls.__name__: {
                                        k: functools.partial(v, cls())
                                        for k, v in cls.dispatcher.items()
                                    }
                                }
                            )

    # diffq_cls_pl = [
    #     cls
    #     for _, cls in inspect.getmembers(
    #         questions.differentiation.singlevariable, inspect.isclass
    #     )
    #     if cls.__module__ == questions.differentiation.singlevariable.__name__
    # ]

    # for mycls in diffq_cls_pl:
    #     is_mycls = input(f"Include questions from {mycls}? (y/n) ")
    #     if is_mycls == "Y" or is_mycls == "y":
    #         q_dict.update(
    #             {k: functools.partial(v, mycls()) for k, v in mycls.dispatcher.items()}
    #         )

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
        key_j = np.random.choice(list(q_dict[key_i].keys()))
        question0, answer0 = q_dict[key_i][key_j]()
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
