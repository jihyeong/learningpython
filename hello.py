print("hello world")
#x=input("what should I set x to?\n")

#print("x is", x)

y=2**3
print("y=", y)

x = True
if (y<=5 and True) or (False):
    print("Y is greater than five!")
elif False:
    print("This prints if the previous cndition is false AND",\
    "This one is true")
else :
    print("This prints if all others are false")
if True:
    if True:
        print("Both of the previous conditions must be true")

# List!
x= [1, 2, 3, 4]
print(x)
print(x[2])


x.append(5)
print(x)

x[2]=20
print(x)

del x[2]
print(x)


z=x.pop(0)
print(x)
print(z)

x.insert(2,50)
print(x)

#This is a tuple - you can't change a tuple!
x=(5,6,7,8)
print(x)
print(x[1])
#x[1] = 100 # this does't work! you can't change a tuple

# This is a set! A set stores only uique values
# Order is not guaranteed; they are randomly ordered
x= {"one", "two", "two", "three"}
print(x)

# Dictionary! A dictionary consists of keys and values
x = {
    "key": "value",
    "jeehyeon": "beege"
}
print(x)
print(x["jeehyeon"])

x["coding"] = "fun"
print(x)

print(x.get("coding"))
print(x.get("fake key", "default value"))

# dict_keys of keys in dictionary
print(x.keys())
print(list(x.keys()))
print(str(5))
print(int("5"))
# print(int("a")) #a is not an integer, so we can't convert it

x = ["loops", "are", "CRAAAAZY"]
for item in x:
    print(item)

for count in range(10):
    print (count)

for count in range(20, 25):
    print(count)

for count in range(50, 100, 10):
    print(count)

for count in range(10, 0, -2):
    print(count)

x = list(range(0, 100, 10))
print(x)
print(x[:5])
print(x[3:7])
print(x[7:3:-1])

#list comprehension
y= [a*10 for a in x[5:8]]
print(y)

#generator comprehension
y=(a*10 for a in x[5:8])
print(y)
for value in y:
    print(value)

for newValue in y:
    print(newValue)

import sys
print(sys.executable)
# *ececutable=path
import weather
print(weather.weather_options)

#argv is variable arguments
print(sys.argv)
if(len(sys.argv)>=3):
    print(sys.argv[1] + sys.argv[2])
    print(int(sys.argv[1]) + int(sys.argv[2]))

def add(a,b):
    return a+b #return is output
print(add(2,4))

x=add(10,20)
print(x)
