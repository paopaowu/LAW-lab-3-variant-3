import sys
import os
def v():
    print(sys.version)

def path(s):
    print(os.getcwd()+"\\"+s)










def main():
    for a in sys.argv:
        print(a)
    if sys.argv[1]=="-v":
        v()
    elif sys.argv[1]=="-p":
        path(sys.argv[2])
if __name__ == '__main__':
    main()