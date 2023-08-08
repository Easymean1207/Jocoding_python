import math
import sys
import os


""" 구구단 프로그램 """


def GuGuDan(n):
    result = []
    for i in range(1, 10):
        result.append(n * i)
    return result


user_input = int(input("몇 단? "))
print(GuGuDan(user_input))


""" 3과 5의 배수 합치기 """


def addThreeAndFive():
    three_list = []
    five_list = []
    for i in range(1, 1000):
        if i % 3 == 0:
            three_list.append(i)
        elif i % 5 == 0:
            five_list.append(i)
        else:
            continue

    result_list = list(set(three_list + five_list))
    sum_of_result = sum(result_list)
    return sum_of_result


print(addThreeAndFive())


""" 게시판 페이징하기 """


def getTotalPage(total_posts, posts_per_page):
    return math.ceil(total_posts / posts_per_page)


print(getTotalPage(1, 5))
