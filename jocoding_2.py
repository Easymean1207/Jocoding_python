""" list,tuple """
# list -> a = [1,2,3] can change
# ex) append, del, replace ... etc)
# tuple -> b = (1,2,3) unchangable!!!!

# tuple_1 = (1, 2, 3, "a", "b", "c")
# print(tuple_1)
# tuple_1 = tuple_1 + (4, 5)
# print(tuple_1)

""" dictionary """
# dictionary -> key:value의 형태로 된 자료구조
# ex) hash, map(hashMap), object, json

# dict_1 = {"name": "john", "age": 15, "city": "NewYork"}
# dict_1["school"] = "middle_school"

# print(dict_1.keys())  # dictionary안의 key 반환
# print(dict_1.values())  # dictionary안의 value 반환
# print(dict_1.items())  # dictionary안의 key,value쌍을 tuple 형태로 반환

# for key, value in dict_1.items():
#     print("key:" + str(key) + "," + "value:" + str(value))


# print("name" in dict_1)

# # find key using value
# for key, value in dict_1.items():
#     if value == "john":
#         print(key)

""" set """
# # set(집합 자료형) -> 중복 허용 x, 순서 없음
# set_1 = set([1, 2, 3, 4, 5, 6])  # set_1 ={1, 2, 3, 4, 5, 6}
# set_2 = set([4, 5, 6, 7, 8, 9])

# intersection = set_1.intersection(set_2)  # set_1 & set_2
# print(intersection)

# union = set_1.union(set_2)  # set_1 | set_2
# print(union)

# differ_s1 = set_1.difference(set_2)  # set_1 - set_2
# print("s1 differ:" + str(differ_s1))
# differ_s2 = set_2 - set_1  # set_2.difference(set_1)
# print("s2 differ:" + str(differ_s2))

# set_1.add(7)  # add
# print(set_1)
# set_1.update([10, 11, 12])  # upadate (multiple add)
# print(set_1)
# set_1.remove(1)  # remove
# print(set_1)

""" bool(boolean) """
isTrue = True
print("value:", isTrue, type(isTrue))
isFalse = False
print("value:", isFalse, type(isFalse))
