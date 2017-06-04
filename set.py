s = set("cheeseshop")
t = set("bookshop")

print s | t
print s.union(t)

print s & t
print s.intersection(t)

print s - t
print s.difference(t)

print s ^ t
print s.symmetric_difference(t)
sss = (s ^ t)
sss.update(s & t)
print sss


print set([1,2,3])

s -= set("cheese")
print s
