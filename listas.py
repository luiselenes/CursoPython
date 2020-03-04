a= ["pepe", "jose", "carlos,maria"]
print (a)
print(a[1])
#  agregar un elemento al final en la lista A
a.append("luis")
# para insertar un elemento en una pocicion
a.insert (2,"fernanda")
# agrega elementos al final de la lista varios
a.extend(["benjamin,veronica"])
# remueve un elemento de la lista
a.remove("jose")

print(a[2:])
print(a[4:5])
print(a)