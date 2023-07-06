""" immutable -> 정수, 실수, 문자열, 튜플 """
""" Mutable -> 리스트, 딕셔너리, 집합 """


def vartest(a):
    a = a + 1


def vartest2(b):
    b = b.append(4)


a = 1
print(a)

b = [1, 2, 3]
vartest2(b)
print(b)


""" 클래스 """


class Calculator:
    # 생성자(Constructor)
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setData(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


value_cal = Calculator(1, 2)
value_cal.setData(10, 2)
sum_result = value_cal.sum()
sub_result = value_cal.sub()
mul_result = value_cal.mul()
div_result = value_cal.div()


# 상속(inheritance)
class ScientificCalculator(Calculator):
    def pow(self):
        result = self.first**self.second
        return result

    def div(self):
        try:
            result = self.first / self.second
        except ZeroDivisionError as e:
            return e
        else:
            return result


value_cal2 = ScientificCalculator(1, 0)
print(value_cal2.pow())
print(value_cal2.div())


# 클래스 변수, 객체 변수
class Family:
    # 클래스 변수 -> 클래스에서 미리 정의해 놓은 클래스 공통적으로 적용되는 변수
    last_name = "김"


Family.last_name = "박"
print(Family.last_name)

family_1 = Family()
family_2 = Family()
print(family_1.last_name)
print(family_2.last_name)


""" 모듈 -> 미리 만들어 놓은 .py 파일(함수, 변수, 클래스) """
import mod1

# from mod1 import add -> mod1에서 add함수만 선택적으로 가져옴

print(mod1.sum(2, 5))

""" 패키지 -> 모듈 여러 개를 모아놓은 것 """

""" 
exception handling(예외처리)

    try:
        예외가 발생할 수 있는 구문
    except Exception as e:
        예외가 발생할 때 동작 코드
    else:
        예외가 발생하지 않을 때 동작 코드
    finally:
        무조건 마지막에 실행되는 코드
"""

try:
    f1 = open("none.txt", "r")
except Exception as e:
    print(e)
else:
    data = f1.read()
    print(data)
    f1.close()

f2 = open("exist.txt", "w")
try:
    data = f2.read()
except Exception as e:
    print(e)
else:
    print(data)
finally:
    f2.close()

try:
    f3 = open("none.txt", "r")
except Exception as e:
    print(e)
    pass
else:
    data = f3.read()
    print(data)
    f3.close()


class Bird:
    def fly(self):
        raise NotImplementedError  # -> 상속하는 클래스가 무조건 해당 기능을 구현해야 함(java의 interaface)


class Eagle(Bird):
    def fly(self):
        print("very fast")


eagle = Eagle()
eagle.fly()

"""
    내장함수: python이 기본적으로 내장하고 있는 함수
    외장함수: 라이브러리 함수, import해서 쓰는 것
"""
print(dir([1, 2, 3]))  # dir -> 자체적으로 가지고 있는 함수나 변수 보여줌
print(divmod(7, 3))  # divmod -> 몫과 나머지를 tuple의 형태로 반환

# enumerate -> 리스트를 key,value 형태(dictonary)로 반환
for i, name in enumerate(["body", "hand", "foot"]):
    print(i, name)


# filter -> 실행 후 결과값이 참인 것만 반환
def isEven(num):
    return num % 2 == 0


filter_list = list(filter(isEven, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(filter_list)
