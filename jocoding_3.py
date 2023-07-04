""" 제어문 """


def isSufficient(money):
    if money >= 10000:
        return True
    else:
        return False


def hasCreditCard(credit_card):
    if credit_card == "Y":
        return True
    elif credit_card == "N":
        return False


def canTakeTaxi(money, credit_card):
    if money == False and credit_card == False:
        print("걸어가라")
    else:
        print("택시를 타고 가라")


money = int(input("잔액을 입력하세요: "))
credit_card = input("카드가 있나요?(Y/N): ")

canTakeTaxi(isSufficient(money), hasCreditCard(credit_card))

pocket = ["smartphone", "document", "glass_cleaner"]
card = True

""" 조건부 표현식(삼항 연산자의 python 형식) """
print("택시를 타고 가라") if "money" in pocket or card == True else print("걸어가라")


"""' 반복문 """


def chopWood(tree_hit):
    while tree_hit < 10:
        tree_hit = tree_hit + 1
        if tree_hit < 5:
            print("뛰발 5번도 안 찍어놓고 나무가 넘어가길 바래? %d번 찍었다" % tree_hit)
        elif tree_hit < 10:
            print("좀 치네? 좀만 더 쳐봐. %d번 찍었다" % tree_hit)
        else:
            print("넘어간다~")


tree_hit = 0
chopWood(tree_hit)


def sellCoffee(money, coffee):
    while coffee > 0:
        if money > 3000:
            coffee = coffee - 1
            money = money - 3000
            print("주문하신 아이스 아메리카노 나왔습니다~ 현재 남은 커피는 %d개입니다." % coffee)
        else:
            print("잔액이 부족합니다. 현재 잔액 %d원입니다." % money)
            return -1
    print("오늘 준비한 커피가 모두 소진되었습니다. 감사합니다.")


money = 10000
coffee = 10

sellCoffee(money, coffee)

test_list = ["one", "two", "three"]
for i in test_list:
    print(i)

tuple_in_list = [(1, 2), (3, 4), (5, 6)]
for first, last in tuple_in_list:
    print(first + last)


# python의 for문은 다른 언어의 for문과 조금 다름.
# for item in list -> index없이 list에 있는 item을 순차적으로 꺼내옴


def calGrade(scores, student):
    for score in scores:
        student = student + 1
        if score >= 70:
            print(f"{student}번 학생은 {score}점이고 우수 장학생으로 선정되었습니다.")
        elif score >= 40 and score < 70:
            print(f"{student}번 학생은 {score}점이고 합격입니다.")
        elif score >= 20 and score < 40:
            continue
        else:
            continue


scores = [90, 25, 67, 45, 80]
number = 0

calGrade(scores, number)

# range(a,b) -> a 이상 b 미만

result = []
for i in range(2, 10):
    for j in range(1, 10):
        result.append(i * j)
print(result)
