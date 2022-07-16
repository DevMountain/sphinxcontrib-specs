"""tests.testutil

Pytest helpers.

This is copied from https://github.com/sphinx-doc/sphinx/blob/9e1b4a8f1678e26670d34765e74edf3a3be3c62c/tests/test_build_html.py
"""

import re
from itertools import chain, cycle


def flat_dict(d):
    return chain.from_iterable(
        [zip(cycle([fname]), values) for fname, values in d.items()]
    )


def tail_check(check):
    rex = re.compile(check)

    def checker(nodes):
        for node in nodes:
            if node.tail and rex.search(node.tail):
                return True
        assert False, "%r not found in tail of any nodes %s" % (check, nodes)

    return checker


def check_xpath(etree, fname, path, check, be_found=True):
    nodes = list(etree.findall(path))
    if check is None:
        assert (
            nodes == []
        ), "found any nodes matching xpath " "%r in file %s" % (path, fname)
        return
    else:
        assert (
            nodes != []
        ), "did not find any node matching xpath " "%r in file %s" % (
            path,
            fname,
        )
    if hasattr(check, "__call__"):
        check(nodes)
    elif not check:
        # only check for node presence
        pass
    else:

        def get_text(node):
            if node.text is not None:
                # the node has only one text
                return node.text
            else:
                # the node has tags and text; gather texts just under the node
                return "".join(n.tail or "" for n in node)

        rex = re.compile(check)
        if be_found:
            if any(rex.search(get_text(node)) for node in nodes):
                return
        else:
            if all(not rex.search(get_text(node)) for node in nodes):
                return

        assert (
            False
        ), "%r not found in any node matching " "path %s in %s: %r" % (
            check,
            path,
            fname,
            [node.text for node in nodes],
        )
