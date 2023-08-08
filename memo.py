""" 간단한 메모장 만들기 """
# python memo.py -a "Life is too short"
import sys


def makeMemo():
    option = sys.argv[1]

    if option == "-w":
        f = open("memo.txt", "w")
        memo = sys.argv[2]
        f.write(memo + "\n")
        f.close()

    elif option == "-a":
        f = open("memo.txt", "a")
        memo = sys.argv[2]
        f.write(memo + "\n")
        f.close()

    elif option == "-r":
        f = open("memo.txt", "r")
        data = f.read()
        print(data)
        f.close()
    else:
        print("not valid mode")

makeMemo()