def km_to_m(km):
    return km*1000

def m_to_cm(m):
    return m*100

def cm_to_mm(cm):
    return cm*10

def ft_to_in(ft):
    return ft * 12

def in_to_cm(i):
    return i * 2.54

def distance_converter(d, name, fun):
    print(name, "=", fun(d))

d = float(input("Enter distance: "))

distance_converter(d, "km to m", km_to_m)
distance_converter(d, "m to cm", m_to_cm)
distance_converter(d, "cm to mm", cm_to_mm)
distance_converter(d, "feet to inches", ft_to_in)
distance_converter(d, "inches to cm", in_to_cm)    