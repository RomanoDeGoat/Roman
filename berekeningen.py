import math

def omtrek_cirkel(straal):
    if straal < 0:
        return 0
    return 2 * math.pi * straal

def oppervlakte_rechthoek(lengte, breedte):
    if lengte < 0 or breedte < 0:
        return 0
    return lengte * breedte

def pythagoras(a, b):
    if getallen != type(list):
        return 0
    return sum(getallen) / len(getallen)

assert math.isclose(omtrek_cirkel(1), 2 * math.pi), "Test 1 omtrek_cirkel mislukt"
assert math.isclose(omtrek_cirkel(0), 0), "Test 2 omtrek_cirkel mislukt"
assert omtrek_cirkel(-5) == 0, "Test 3 omtrek_cirkel mislukt"

assert oppervlakte_rechthoek(5, 10) == 50, "Test 1 oppervlakte_rechthoek mislukt"
assert oppervlakte_rechthoek(0, 10) == 0, "Test 2 oppervlakte_rechthoek mislukt"
assert oppervlakte_rechthoek(-5, 10) == 0, "Test 3 oppervlakte_rechthoek mislukt"


def pythagoras_correct(a, b):
    return math.sqrt(a**2 + b**2)

assert math.isclose(pythagoras_correct(3, 4), 5), "Test 1 pythagoras mislukt"
assert math.isclose(pythagoras_correct(5, 12), 13), "Test 2 pythagoras mislukt"
assert math.isclose(pythagoras_correct(0, 0), 0), "Test 3 pythagoras mislukt"

print("Alle tests zijn geslaagd!")
