

# values = [1, 23, 42, "asdfg"]
# transformation = lambda x: x
# transformed_values = list(map(transformation, values))
#
# if values == transformed_values:
#     print("ok")
# else:
#     print("fail")

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
#
#
# def find_farthest_orbit(list):
#     temp = 0
#     for k, v in list:
#         if k != v and k * v > temp:
#             temp = k * v
#     return temp
# print(find_farthest_orbit(orbits))
def same_by(f, list):
    if not list:
        return True
    a = f(list[0])
    for i in list:
        if f(i) != a:
          return False

    return True


values = []
if same_by(lambda x: x % 2, values):
        print("‘same’")
else:
    print("‘different’")


