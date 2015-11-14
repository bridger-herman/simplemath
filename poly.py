# poly.py
# Bridger Herman 2015

import re

class Poly:
    # poly should be a dictionary of the form:
    # {'coefficient;vars':[degrees]}
    def __init__(_, poly):
        if not poly:
            _.poly = {"0;":[]}
        if isinstance(poly, dict):
            _.poly = poly
            for p in _.poly:
                try:
                    cut = p.index(";") + 1
                    if len(p[cut:]) != len(_.poly[p]):
                        raise AttributeError
                except (IndexError, AttributeError):
                    raise AttributeError("Malformed Polynomial")
        elif isinstance(poly, int):
            _.poly = {str(poly) + ";":[]}
        else:
            raise AttributeError("Malformed Polynomial")
        _.simplify()

    # __str__
    # String method
    def __str__(_):
        ts = _.terms()
        astr = ""
        astr += ts[0]
        if len(ts) > 1:
            astr += " "
        for i in range(1, len(ts)):
            if ts[i][0] == "-":
                astr += "- " + ts[i][1:]
            else:
                astr += "+ " + ts[i]
            if i != len(ts) - 1:
                astr += " "
        return astr

    # terms
    # Returns a string list of the terms in a polynomial
    def terms(_):
        alst = []
        astr = ""
        for term in _.poly:
            cvrs = term.split(";")
            c = cvrs[0]
            vrs = cvrs[1]
            astr += c
            if len(vrs) > 0:
                astr += " "
            for i in range(len(vrs)):
                if _.poly[term][i] == 1:
                    astr += vrs[i]
                else:
                    astr += vrs[i] + "^" + str(_.poly[term][i])
                if i != len(vrs) - 1:
                    astr += " "
            alst.append(astr)
            astr = ""
        return alst

    # simplify
    # Simplifies a polynomial
    # TODO add degrees of same variables together
    def simplify(_):
        tmpp = {}
        for p in _.poly:
            cut = p.index(";") + 1
            cvrs = ""
            degs = []
            if p[0] == "0":
                continue
            else:
                cvrs += p[:cut]
            for i in range(len(_.poly[p])):
                if _.poly[p][i] != 0:
                    degs.append(_.poly[p][i])
                    cvrs += p[cut + i]
            tmpp[cvrs] = degs
        _.poly = tmpp

    # from_str
    # Makes a polynomial from a string
    # Returns a Poly object
    def from_str(string):
        # TODO maybe fix this regex to avoid workaround stated below
        coeffs = re.findall(r"([\+\-]? ?((\^\d+)|\d+))", string)
        # Get the first match out of tuple
        # Workaround for my inability to Regex properly
        coeffs = [c[0] for c in coeffs]
        coeffs = [num.replace(" ", "").replace("+","") for num in coeffs]
        cs = []
        for c in coeffs:
            if "^" not in c:
                cs.append(c)
        vr = re.findall(r"[a-zA-Z]\^\d+|[a-zA-Z]|[\+\-]", string)
        i = 0
        # Variable accumulator
        avrs = ""
        # Degree accumulator
        adegs = []
        # Final Degree and Variable lists
        vrs = []
        degs = []
        while i < len(vr):
            if vr[i] in "+-":
                vrs.append(avrs)
                degs.append(adegs)
                avrs = ""
                adegs = []
            elif "^" in vr[i]:
                carat = vr[i].index("^")
                # TODO this may need to be a float
                adegs.append(int(vr[i][carat + 1:]))
                avrs += vr[i][:carat]
            else:
                avrs += vr[i]
                # TODO this may need to be a float
                adegs.append(1)
            i += 1
        degs.append(adegs)
        vrs.append(avrs)
        fvrs = []
        fdegs = []
        print(degs, vrs, cs)
        # Clean up empty strings and lists
        for i in range(len(vrs)):
            if vrs[i] and degs[i]:
                fvrs.append(vrs[i])
                fdegs.append(degs[i])
        # Put all the lists together in the format specified for the Polynomial
        # {'coefficient;vrs':[degrees]}
        poly = {}
        for i in range(len(fvrs)):
            cvstr = cs[i] + ";" + fvrs[i]
            poly[cvstr] = fdegs[i]
        return Poly(poly)

if __name__ == "__main__":
    p = Poly({"0;xy":[-2,3], "-12;abc":[0,2,3]})
    print(p)
