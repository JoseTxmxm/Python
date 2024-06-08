class Test:
      ...


def main():
        test = get_test()
        print(f"{test.name} from {test.house}")
def get_test():
    test = Test()
    test.name = input("Name: ")
    test.house = input("House: ")
    return test

if __name__ == "__main__":
      main()

