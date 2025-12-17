ton_to_kg = lambda t: t * 1000
kg_to_g = lambda kg: kg * 1000
g_to_mg = lambda g: g * 1000
mg_to_p = lambda mg: mg * 0.00000220462

def weight_converter(weight, conv_type, func):
    print(weight, conv_type, "=", func(weight))

w = float(input("Enter weight in tonns: "))

weight_converter(w, "tonns to kg", ton_to_kg)

kg = ton_to_kg(w)
weight_converter(kg, "kg to g", kg_to_g)

g = kg_to_g(kg)
weight_converter(g, "g to mg", g_to_mg)

mg = g_to_mg(g)
weight_converter(mg, "mg to pounds", mg_to_p)
