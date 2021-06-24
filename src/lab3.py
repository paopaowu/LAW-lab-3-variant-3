import sys

def v():
    print(sys.version)
def main():
    for arg in sys.argv:
        if arg=="-v":
            v()

if __name__ == '__main__':
    main()