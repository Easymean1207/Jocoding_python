import math


def isExist(inputStr, want_to_find):
    if inputStr.find(want_to_find) != -1:
        print(str(inputStr.find(want_to_find)) + " 번째에 있음")
    else:
        print("not found")


str_1 = "hello, my name is 'lee_jimin'"
str_2 = "123456789"

today = "7/3"
grade = 3

userInput = "a"
isExist(str_1, userInput)

# 문자열 슬라이싱:
# 문자열[처음 위치(이샹):끝 위치(미만):몇 스텝으로?(음수면 역값 반환)]
print(str_1[::-1])

gcu = ["michael", "porter", "lucy", "daniel"]
gcu.append("lucas")
print(sorted(gcu))
