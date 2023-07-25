#!/usr/bin/python3

def convert_s_to_html(r):
    l_r = r.split(sep="\n")
    return "<br>".join(l_r)

def is_later_pkg_version(v1, v2):
    l_v1 = v1.split("-")
    l_v2 = v2.split("-")
    for n in range(len(l_v1)):
        if l_v2[n] > l_v1[n]:
            return True
