# Sets are an unordered collection of unique elements, whereas a dictionary is an ordered collection of key-value pairs.
# are mutable. Both sets and dictionaries do not allow duplicate entries.

s = {2, 3, 4, 2}
print(s, type(s))

s1 = {19, "ryt", 4.5, 19}
print(s1)

for i in s1:
    print(i)

# s2 = {}
# s3 = set()
# print(type(s2), type(s3))

s3={"a","b","c"}


#methods
#union and update
print(s.union(s1)) #s will not change here
s.update(s3) #but here s will be updated for forever
print(s)

#other methods

#intersection and intersection_update
#pop
#remove/discard
#adjoint set
#clear
#del