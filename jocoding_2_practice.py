# Q1
""" score = {"korean": 80, "english": 75, "math": 55}
sum, i = 0, 0

for key, value in score.items():
    sum = sum + value
    i = i + 1

avg = sum / i
print(avg) """


# Q2
""" def isOdd(input):
    if input % 2 == 0:
        return False
    else:
        return True


test_var1 = 5
test_var2 = 4

result = isOdd(test_var2)
print(result) """


# Q3
""" RRN = "881120-1068234"  # RRN(Resident Registration Number)
birthday = RRN[:6]
private_id = RRN[7:]

print(birthday)
print(private_id) """


# Q4
""" print(RRN[7:8]) """


# Q5
""" str_1 = "a:b:c:d"
replaced = str_1.replace(":", "#")
print(replaced) """


# Q6
""" list_1 = [1, 3, 5, 4, 2]
list_1.sort()
reversed = list_1[::-1]
print(reversed) """


# Q7
""" test_list = ["Life", "is", "too", "short"]
merged = " ".join(test_list)
print(merged) """


# Q8
""" tuple_1 = (1, 2, 3)
tuple_to_list = list(tuple_1)
tuple_to_list.append(4)
list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple) """

# Q10
""" dict_a = {"A": 90, "B": 80, "C": 70}
result = dict_a.get("B", "not found")
print(result) """

# Q11
list_a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
set_a = set(list_a)
print(set_a)
