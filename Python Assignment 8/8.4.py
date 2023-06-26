# This is problem to convert all the negative coordinates to a positive coordinates;
# The agenda is to get all the coordinates in 0 or positive values keeping the relative distance same;
# We can add or delete any number from the coordinates ; however graph should not be changed;

# Input: [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
# Output : [(9,6), (6, 12), (7,7),(0, 5), (8, 12), (18,5)]


input_coordinates = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]

result= []

for point in input_coordinates:
    print(point[0])

min_x = -(min(point[0] for point in input_coordinates))

# print(min_x)

for i in input_coordinates:
    list1 = []
    for j in i:
        j = j+min_x
        list1.append(j)
    result.append(tuple(list1))

print("The Positive co-ordinates are: ", result)
