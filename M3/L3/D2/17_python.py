# Descomposición de una condición compleja: año bisiesto

year = 2024

es_divisible_por_4 = (year % 4 == 0)
es_siglo = (year % 100 == 0)
es_divisible_por_400 = (year % 400 == 0)

es_bisiesto = (es_divisible_por_4 and not es_siglo) or es_divisible_por_400

if es_bisiesto:
    print(year, "es bisiesto")
else:
    print(year, "no es bisiesto")