# -*- encoding: utf-8 -*-

import sympy


def solve(*equalities):
    if len(equalities) == 1:
        return sympy.solve(equalities[0])
    return sympy.solve_poly_system(equalities)


x = sympy.Symbol("x")
form = x ** 2
print('Производная: ')
diff = sympy.diff(form)
sympy.pprint(diff)
sympy.plot(diff)
print('Интеграл: ')
integr = sympy.integrate(form)
sympy.pprint(integr)
sympy.plot(integr)

y = sympy.Symbol("y")
eq1 = sympy.Equality(3 , x ** 2 - x * y)
eq2 = sympy.Equality(-2, y ** 2 - x * y)
eq3 = sympy.Equality(x**2, -2)
sympy.pprint(solve(eq1, eq2))
sympy.pprint(solve(eq3))

#Complete
