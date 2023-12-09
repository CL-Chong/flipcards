import functools
import inspect


class ModuleTree:
    def __init__(self, name=None, value=None, children=None):
        self.name = name
        self.value = value
        if children is None:
            self.children = {}
        else:
            self.children = children

    def setname(self, newname):
        self.name = newname
        return

    def setvalue(self, newvalue):
        self.value = newvalue
        return

    def addchildren(self, child_dict):
        self.children.update(child_dict)
        return

    def find_children_mdl(self):
        mdls = [
            mdl
            for _, mdl in inspect.getmembers(self.value, inspect.ismodule)
            if not mdl.__name__.startswith(self.name + "._")
        ]
        self.addchildren(
            {mdl.__name__: ModuleTree(name=mdl.__name__, value=mdl) for mdl in mdls}
        )

    def find_children_cls(self):
        clss = [
            cls
            for _, cls in inspect.getmembers(self.value, inspect.isclass)
            if cls.__module__ == self.name
        ]
        self.addchildren(
            {
                cls.__name__: {
                    k: functools.partial(v, cls()) for k, v in cls.dispatcher.items()
                }
                for cls in clss
            }
        )
        return


def get_tree(main_mdl):
    dict_tree = ModuleTree(name=main_mdl.__name__, value=main_mdl)
    dict_tree.find_children_mdl()
    for _, val in dict_tree.children.items():
        val.find_children_mdl()
        for _, xalue in val.children.items():
            xalue.find_children_cls()

    return dict_tree


def clean_dict(mdl_tree, separator=None):
    clean_dict = {}
    for _, v in mdl_tree.children.items():
        for k2, v2 in v.children.items():
            for k3, v3 in v2.children.items():
                kstr = k2 + "." + k3
                kstr = kstr[len(mdl_tree.name) + 1 :]
                if separator is not None:
                    kstr = kstr.replace(".", separator)
                # print(kstr)
                clean_dict.update({kstr: v3})
    return clean_dict
