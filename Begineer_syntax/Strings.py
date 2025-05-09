a = "Hello world"
print(a[1])

#looping in a string
for x in "banana":
    print(x)

#string length
b = "Hello world"
print(len(b))

#check the string
txt = "The best things in life are free!"
print("free" in txt)

print("expensive" not in txt)

#slicing a string
c = "Hello world"
print(c[2:5])

#slicing from the start
print(c[:5])

#slicing to the end
print(b[2:])

#negative indexing
print(c[-5:-2])


#modfying Stings
d = "hello world"
print(d.upper())

#remove the white spaces
print(d.strip())

#replace string
print(a.replace("H","J"))

#spilt the string
print(a.split(","))

#concertination
m = "Hello"
n = "World"
k = m + n
print(k)