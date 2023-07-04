""" 함수 """
""" def functionName(parameter): -> parameter is optional
        want_to_excute......
        want_to_excute......
        want_to_excute......
        return return_value -> return is optional """


def hello():
    greeting = input("어느 나라 사람이세요? ")
    if greeting == "한국":
        print("안녕하세요~")
    elif greeting == "미국":
        print("Hello")
    elif greeting == "스페인":
        print("Hola!")
    else:
        print("이 함수에는 해당 언어의 인사말은 없네요... 유감")


# def functionName(*args): -> 받을 수 있는 parameter의 개수를 유동적으로 설정
def sumMany(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum


# def functionName(*kw_args): -> dictionary 형태의 여러 개의 parameter 받음
def printKwargs(**kw_args):
    sum = 0
    for key in kw_args.keys():
        if key == "name":
            print("당신의 이름은 :" + kw_args.get(key, "없는데요?"))


def sayMySelf(**kw_args):
    my_name = kw_args.get("name", "NULL")
    my_age = kw_args.get("age", "0")
    my_gender = "male" in (kw_args.get("gender", "0")).lower()
    print(my_name, my_age, my_gender)


# printKwargs(name="int 조수", b="2")

# print("result is", sumMany(2**100, 2**100))
# hello()

# my_list = [1, 2, 3]
# print(my_list.pop())

# my_info = {"name": "lee_jimin", "age": 26, "gender": "Male"}
# sayMySelf(**my_info)

# lamda 함수 -> def함수의 축약형태,
# def를 못 쓰는 상황에서도 사용 가능 ex)리스트 안

# add = lambda a, b: a + b
# print(add(1, 2))

# lambda_list = [lambda a, b: a + b, lambda a, b: a * b]
# print(lambda_list[0](1, 2))


""" 사용자 입출력 """

# a = input("입력하세요: ")
# print(a)

# print("life" "is" "too" "short")
# print("life", "is", "too short")
# print("life", "is", "too", "short")

# print(출력값, end ='넣고 싶은 값') -> 줄바꿈 x, 출력값 뒤에 붙여서 출력
# for i in range(1, 10):
#     print(i, end=" ")

# EOF(파일 끝)까지 읽기
f = open("new_file.txt", "r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
# f.close()

# readlines로 파일 끝까지 읽기
# lines = f.readlines()
# for line in lines:
#     print(line, end="")
# f.close()

# read로 파일 통째로 읽기
data = f.read()
print(data)
f.close()

# append mode
f2 = open("new_file.txt", "a")
for i in range(11, 20):
    new_data = f"line {i} \n"
    f2.write(new_data)
f2.close()

# with문을 이용한 파일 입출력 -> close 필요 x
with open("life.txt", "w") as f3:
    f3.write("life is too short, you need python")
