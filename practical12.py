tuple1 = (10, 20, 30)
tuple2 = ("Apple", "Banana", "Mango")
tuple3 = (5, 15, 25, 35, 45)


print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("Tuple 3:", tuple3)

print("\nIndexing:")
print(tuple1[0])       
print(tuple2[1])       
print(tuple3[-1])
   


print("\nSlicing:")
print(tuple1[0:2])     
print(tuple2[1:3])     
print(tuple3[1:4])     


print("\nReverse:")
print(tuple1[::-1])
print(tuple2[::-1])
print(tuple3[::-1])

print("\nUnpacking:")
a,b,c=tuple1
print(a)
print(b)
print(c)
fruit1,fruit2,fruit3=tuple2
print(fruit1)
print(fruit2)
print(fruit3)


p,q,r,s,t=tuple3
print(p)
print(q)
print(r)
print(s)
print(t)

#oprations
print("\nCountOperation")
print(tuple1.count(10))
print(tuple2.count("Apple"))
print(tuple3.count(15))
print("\nchecking elements are in or not")
print(20 in tuple1)
print(100 in tuple1)





#checking mutability
print("\nChecking mutability")
tuple1[0]=100