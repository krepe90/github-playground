import glob


def test():
    file_list = glob.glob("*.*")
    for fileName in file_list:
        print(fileName)
    return
