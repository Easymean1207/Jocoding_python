""" 제어문 """


def isSufficient(money):
    if money >= 10000:
        return True
    else:
        return False


def hasCreditCard(creditCard):
    if creditCard == "Y":
        return True
    elif creditCard == "N":
        return False


def canTakeTaxi(money, creditCard):
    if money == False and creditCard == False:
        print("걸어가라")
    else:
        print("택시를 타고 가라")


# money = int(input("잔액을 입력하세요: "))
# creditCard = input("카드가 있나요?(Y/N): ")

# canTakeTaxi(isSufficient(money), hasCreditCard(creditCard))

pocket = ["smartphone", "document", "glass_cleaner"]
card = True

""" 조건부 표현식(삼항 연산자의 python 형식) """
# print("택시를 타고 가라") if "money" in pocket or card == True else print("걸어가라")


"""' 반복문 """


def chopWood(treeHit):
    while treeHit < 10:
        treeHit = treeHit + 1
        if treeHit < 5:
            print("뛰발 5번도 안 찍어놓고 나무가 넘어가길 바래? %d번 찍었다" % treeHit)
        elif treeHit < 10:
            print("좀 치네? 좀만 더 쳐봐. %d번 찍었다" % treeHit)
        else:
            print("넘어간다~")


# treeHit = 0
# chopWood(treeHit)


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
