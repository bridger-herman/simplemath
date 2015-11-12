** Notes: **
+ Everything is to be represented as a polynomial object
  + Still need to decide what this will be. Probably similar to the one in existence

# Polynomials
## Representation
+ ** Options: **
  1. Dictionary of degree:coefficient
  + Dictionary of degree:List of coefficients *useful for multivariable things?*
  + Dictionary of string of variables:list of degrees
    + Note: this would require a string parsing thing which we would need anyway
    + Examples:
    + `'2,xy':[0, 1, 1]` == 2 x y
    + `'5,yz':[0, 2, 2]` == 5 y^2 z^2
    
## Operations
+ +
  + Given option 3:
    + Get variables after the comma in string, and match degrees
    + If degrees match, add coefficients before commas together and give result
+ -
  + Given option 3: same as + except subtract
+ *
  + Given option 3:
    + Get coefficients and multiply them together
    + See what variables don't overlap and add them to the second part of the string
    + Add corresponding coefficients together
+ /
  + Long division of polynomials?
+ %
  + Does this even make sense? Ask Emmie
