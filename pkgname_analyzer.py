#!/usr/bin/python3

import args_parser
parser = args_parser.get_parser()
args = parser.parse_args()
#print(args)

is_debug = False


def debug(s):
    if is_debug or args.debug:
      print("[DEBUG] %s" % (s))

def info(s):
    if is_debug or args.debug:
      print("[INFO] %s" % (s))

def warn(s):
    if is_debug or args.debug:
      print("[WARN] %s" % (s))

#===================================================

import re
re_version = r"^[0-9]+([\.][0-9a-zA-Z]+)*"
re_start_of_non_version = r"[\.][a-zA-Z]"

def trim_rpm_name(name):
    r = name
    l = [".rpm", ".x86_64", ".aarch64", ".arm64", ".noarch", ".ppc64le", ".i686", ".s390x"]
    for e in l:
        r = r.replace(e, "")
    return r

def strip_after_dist(name):
    """
    Strip after distro (el8, el9 ...) 
    """
    r = name
    index_last_occur_dash = r.rfind("-")
    index_first_non_digit = -1
    if index_last_occur_dash != -1:
        # Starting from the right most dash, find first occur of non-digit
        r_re_start_of_non_version = re.search(re_start_of_non_version, r[index_last_occur_dash+1:])
        if r_re_start_of_non_version:
            # (pos at last occur dash) + 1 + (pos at start of non-version rpm name in substring after dash)
            real_pos_start_of_non_version = index_last_occur_dash + 1 + r_re_start_of_non_version.start()
            return r[:real_pos_start_of_non_version]
    return r

def analyze_pkgname(p, t):
    if p == "repodata":
        return

    rpmname = strip_after_dist(p)
    l_pkgname = []
    l_version = []

    # Split by -, filter and add to l_pkgname and l_version
    l_rpmname = rpmname.split("-")
    for e in l_rpmname:
        r_re_find_version = re.match(re_version, e)
        if r_re_find_version:
            l_version.append(e)
        else:
            l_pkgname.append(e)
    
    if t == "name":
        return "-".join(l_pkgname)
    elif t == "version":
        return "-".join(l_version)
    elif t == "longver":
        ver_rest = p.replace("-".join(l_pkgname)+"-", "")
        return trim_rpm_name(ver_rest)
    else:
        warn("[ERROR] Unknown action type: " + str(t))

def main():
    print(analyze_pkgname(args.package, args.action))

if __name__ == "__main__":
    main()
