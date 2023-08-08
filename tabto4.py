""" 탭을 4개의 공백으로 바꾸기 """
import sys

# python tabto4.py a.txt b.txt


def tabTo4():
    src = sys.argv[1]
    dest = sys.argv[2]

    try:
        f = open(src)
    except Exception as e:
        print(e)
    else:
        tab_content = f.read()
        space_content = tab_content.replace("\t", " " * 4)
        f.close()

        f = open(dest, "w")
        f.write(space_content)
        f.close()


tabTo4()
