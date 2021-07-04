friends = {"david", "artie", "louis"}
abroad = {"liane", "lulu", "bob", "louis"}

local_friends = friends.difference(abroad)
print(local_friends)

all_friends = friends.union(abroad)
print(all_friends)

intersect_friends = friends.intersection(abroad)
print(intersect_friends)