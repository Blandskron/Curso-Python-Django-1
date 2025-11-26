# index comienza en 0
# el final del index es -1
a = [5, 1, 4, 9, 0]
# No es una lista b = range(3, 10) + range(20, 23)
c = [[1, 2], [3, 4, 5], [6, 7]]
d = ['perro', 'gato', 'jirafa', 'elefante']
e = ['a', a, 2 * a]

print("solucion 1: ", a[2])
print("solucion 2: Error no es una lista b[9]")
print("solucion 3: ", c[1][2])
print("solucion 4: ", e[0] == e[1])
print("solucion 5: ", len(c))
print("solucion 6: ", len(c[0]))
print("solucion 7: ", len(e))
print("solucion 8: ", c[-1])
print("solucion 9: ", c[-1][+1])
print("solucion 10: ", c[2:] + d[2:])
print("solucion 11: ", a[3:10])
print("solucion 12: ", a[3:10:2])
print("solucion 13: ", d.index('jirafa'))
print("solucion 14: ", e[c[0][1]].count(5))
print("solucion 15: ", sorted(a)[2])
print("solucion 16: es un error la b no es una lista complex(b[0], b[1])", )

"""
solucion 1:  4
solucion 2: Error no es una lista b[9]
solucion 3:  5
solucion 4:  False
solucion 5:  3
solucion 6:  2
solucion 7:  3
solucion 8:  [6, 7]
solucion 9:  7
solucion 10:  [[6, 7], 'jirafa', 'elefante']
solucion 11:  [9, 0]
solucion 12:  [9]
solucion 13:  2
solucion 14:  2
solucion 15:  4
solucion 16: es un error la b no es una lista complex(b[0], b[1])
"""