# from fractions import Fraction
# import functools
# import inspect
import sys
import tkinter

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backend_bases import MouseButton

import questions
import questions._utils as utils

# from types import FunctionType


def main():
    full_dict = utils.clean_dict(utils.get_tree(questions), separator=" ")

    q_dict = {}
    root = tkinter.Tk()
    root.geometry("400x400")
    vars_dict = {}
    tkinter.Label(root, text="Options").place(x=5, y=0)
    placement = 20
    for k, _ in full_dict.items():
        vars_dict.update({k: tkinter.IntVar()})
        tkinter.Checkbutton(
            root, text=k, variable=vars_dict[k], onvalue=1, offvalue=0
        ).place(x=5, y=placement)
        placement += 20

    def _submit():
        for k, v in full_dict.items():
            if vars_dict[k].get() == 1:
                q_dict.update({k: v})
        root.destroy()

    tkinter.Button(root, text="Submit", command=_submit).place(x=300, y=20)

    root.mainloop()

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


if __name__ == "__main__":
    main()
