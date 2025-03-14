# chapter video-13

# strings are immutable

a = "Harry"
print(len(a))
print(a.upper())
print(a.lower())

b = "!!!Hello!!! harry"
print(b.rstrip("!"))
print(b.replace("!", "#"))
print(b.split(" "))

c = "heloo world"
print(c.capitalize())
print(c.center(20))
print(c.count("o"))


str1="he is a onset man, he is a den"
print(str1.endswith("is",3,5)) #return true or false
print(str1.find("b")) #if you find then index or -1
print(str1.index("an")) #if substring found then index or error

str5="welcome to console"
print(str5.isalnum())
print(str5.isalpha())
print(str5.isprintable())
print(str5.islower())

print(str5.istitle())
print(str5.title())
print(str5.isspace())
print(str5.swapcase())


