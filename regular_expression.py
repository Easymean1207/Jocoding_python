""" 정규 표현식 """
import re

# match 객체로 return 함 ->

# match
p = re.compile("[a-p]+")
m = p.match("deserter pursuit")  # 0번 index부터 매칭이 되는 인덱스까지 return
# print(m)


# search
p2 = re.compile("[a-z]+")
m2 = p2.search("3 python")  # match와 유사하지만 첫번째가 일치하지 않아도 일치하는 구문이 있다면 return
# print(m2)


# findall
p3 = re.compile("[a-z]+")
m3 = p3.findall("life is too short")  # 일치하는 string을 list에 담아서 return
# print(m3)


# finditer
p4 = re.compile("[a-z]+")
m4 = p4.finditer("we need python")
# for i in m4:
#     print(i)


# match 객체의 메서드
p5 = re.compile("[a-z]+")
m5 = p5.match("python")

# print(m5.group())
# print(m5.start())
# print(m5.end())
# print(m5.span())


# DOTALL, S
p6 = re.compile("a.b", re.DOTALL)  # \n이 있어도 객체가 매치됨
m6 = p6.match("a\nb")
# print(m6)

# IGNORECASE, I
p7 = re.compile("[a-z]", re.IGNORECASE)  # 대,소문자를 무시하고 매칭 여부를 판단

# print(p7.match("python"))
# print(p7.match("Python"))
# print(p7.match("PYTHON"))


# MULTILINE, M
p8 = re.compile(
    "^python\s\w+", re.MULTILINE  # MULTILINE 옵션을 주면 여러 줄을 매칭
)  # python이라는 글자가 제일 처음 나오고(^) 공백이 있고(\s) 뒤에 단어가 1개 이상 있음(\w+)

data = """python one
life is too short
python two
you need python
python three"""

print(p8.findall(data))
