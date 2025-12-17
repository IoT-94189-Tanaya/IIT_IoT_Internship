km_to_m = lambda km: km * 1000
m_to_cm = lambda m: m * 100
cm_to_mm = lambda cm: cm * 10
ft_to_in = lambda ft: ft * 12
in_to_cm = lambda inch: inch * 2.54

def distance_converter(distance, conv_type, func):
    print(distance, conv_type, "=", func(distance))


d = float(input("Enter distance: "))

distance_converter(d, "km to m", km_to_m)
distance_converter(d, "m to cm", m_to_cm)
distance_converter(d, "cm to mm", cm_to_mm)
distance_converter(d, "feet to inches", ft_to_in)
distance_converter(d, "inches to cm", in_to_cm)
