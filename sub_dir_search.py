""" 하위 디렉토리 검색하기 (특정 확장자만 출력) """
import os


def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):  # 파일 안에 폴더가 더 있는 경우 탐색
                search(full_filename)
            else:
                extension = os.path.splitext(full_filename)[-1]  # 파일 확장자 선택
                if extension == ".py":
                    print(full_filename)
    except PermissionError as e:
        pass


search("D:/")
