import podstawy_punkty_losowe as points
from matplotlib import pyplot as plt

A = [0,3]
B = [2,4]
ODCHYLENIE_STANDARDOWE_A = 0.8
ODCHYLENIE_STANDARDOWE_B = 1.0

p1 = [points.random_point(A, ODCHYLENIE_STANDARDOWE_A)
          for _ in range(0,500)]

p2 = [points.random_point(B, ODCHYLENIE_STANDARDOWE_B)
          for _ in range(0,500)]

points.plot_list_of_points(p1, 'red')
points.plot_list_of_points(p2, 'blue')
plt.axis('equal')
plt.show()

punkty_po_klasyfikacji_A = []
punkty_po_klasyfikacji_B = []

for p in p1 + p2:
    if points.distance(A, p) < points.distance(B, p):
        punkty_po_klasyfikacji_A.append(p)
    else:
        punkty_po_klasyfikacji_B.append(p)

points.plot_list_of_points(punkty_po_klasyfikacji_A, 'red')
points.plot_list_of_points(punkty_po_klasyfikacji_B, 'blue')
plt.axis('equal')
plt.show()

## Zobacz co się stanie jak wywołasz:
# help(random_points)
# Python automatycznie stworzył dokumentację do modułu na podstawie komentarzy!
