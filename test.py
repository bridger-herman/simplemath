import random as r
from poly import Poly

# Makes a polynomial with n terms
def make_poly(n):
    d = {}
    for i in range(n):
        cvars = ""
        vrs = r.randint(0, 4)
        vrs = "".join([chr(r.randint(97,122)) for n in range(vrs)])
        cvars += str(r.randint(-100, 100)) + ";" + vrs
        degs = [r.randint(-10, 10) for i in range(len(vrs))]
        d[cvars] = degs
    return Poly(d)

if __name__ == '__main__':
    c = make_poly(10000)
    f = open("polys-test.txt", "w")
    for p in c.poly:
        f.write(p + "\t" + str(c.poly[p]) + "\t" + str(Poly({p:c.poly[p]})) + "\n")
    f.close()
