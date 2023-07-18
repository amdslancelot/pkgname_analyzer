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
re_version = r"^[0-9]+([\.][0-9])*"

def trim_rpm_name(name):
    r = name
    l = [".rpm", ".x86_64", ".aarch64", "arm64"]
    for e in l:
        r = r.replace(e, "")
    return r

def analyze_pkgname(p, t):
    rpmname = trim_rpm_name(p)
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
    


    #pos_first_digit = re.search(r"\d", rpmname).start()-1
    #pkgname = rpmname[:pos_first_digit]
    #pkgname_rest = rpmname[(pos_first_digit+1):]
    #debug(pkgname_rest)
    
    if t == "name":
        return "-".join(l_pkgname)
    elif t == "version":
        #re_search_end_digit = re.search(r"[a-zA-Z]", pkgname_rest)

        #if pos_end_digit:
        #    version = pkgname_rest[:re_search_end_digit.start()-1]
        #    return version
        #else:
        #    warn("[ERROR] Invalid version format: " + pkgname_rest)

        version = "-".join(l_version)
        pos_el = re.search(r"el", version)
        return version[:pos_el.start()-1]
    else:
        warn("[ERROR] Unknown action type: " + str(t))

def main():
    print(analyze_pkgname(args.package, args.action))

if __name__ == "__main__":
    main()
