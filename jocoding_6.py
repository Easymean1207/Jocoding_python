import math
import sys
import os


# 구구단 프로그램
def GuGuDan(n):
    result = []
    for i in range(1, 10):
        result.append(n * i)
    return result


result = int(input("몇 단? "))
print(GuGuDan(result))


# 3과 5의 배수 합치기
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


# 게시판 페이징하기
def getTotalPage(total_posts, posts_per_page):
    return total_posts / posts_per_page


print(getTotalPage(10, 5))


# 간단한 메모장 만들기
def makeMemo():
    option = sys.argv[1]

    if option == "-w":
        memo = sys.argv[2]
        f = open("memo.txt", "w")
        f.write(memo + "\n")
        f.close()

    elif option == "-a":
        memo = sys.argv[2]
        f = open("memo.txt", "a")
        f.write(memo)
        f.close()

    elif option == "-r":
        try:
            f = open("memo.txt", "r")
        except Exception as e:
            print(e)
        else:
            data = f.read()
            print(data)
            f.close()
    else:
        print("not valid mode")


makeMemo()


# 탭을 4개의 공백으로 바꾸기
def tabTo4():
    src = sys.argv[1]
    dest = sys.argv[2]

    try:
        f = open(src, "r")
    except Exception as e:
        print(e)
    else:
        tab_content = f.read()
        space_content = tab_content.replace("\t", "    ")
        f.close()

        f = open(dest, "w")
        f.write(space_content)
        f.close()


tabTo4()


# 하위 디렉토리 검색하기 (특정 확장자만 출력)
def search(dir_name):
    try:
        files = os.listdir(dir_name)
        for filename in files:
            full_filename = os.path.join(dir_name, filename)

            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == ".py":
                    print(full_filename)
    except Exception as e:
        pass


search("D:/")
