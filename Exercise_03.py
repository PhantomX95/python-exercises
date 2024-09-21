# You have this sets:
# a = {5, 12, 52, 0, 8}
# b = {2, 5, 1, 9, 8}
# c = {4, 5, 6, 0, 10}
# Find the union of the three sets, then find the intersections between them. After that, determine the differences: first from set A, then from set B, and finally from set C.

# Algorithm:
# print the unions between the sets
# print the intersections between the sets
# print the differences between the sets

a = {5, 12, 52, 0, 8}
b = {2, 5, 1, 9, 8}
c = {4, 5, 6, 0, 10}

print(f"The union between all sets is: {a.union(b, c)}")
print(f"The intersections between all the sets is: {a.intersection(b, c)}")
print(f"The differences between 'a' and the other sets is: {a.difference(b, c)}")
print(f"The differences between 'b' and the other sets is: {b.difference(a, c)}")
print(f"The differences between 'c' and the other sets is: {c.difference(a, b)}")
