import glob


def test():
    file_list = glob.glob("*.*")
    for fileName in file_list:
        print(fileName)
    someWrongName=2.13
    return
