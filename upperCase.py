def upperCase(lCase):
    print(lCase.upper())

def main():
    lCase = input("Enter the lowerCase:")
    assert lCase == lCase.lower()
    upperCase(lCase)
main()
