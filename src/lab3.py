import sys
import os
def v():
    print(sys.version)

def path(s):
    print(os.getcwd()+"\\"+s)
def cat(sc,p1,p2):
    if sc=='w':
        f1 = open(p1, 'w')
        f1.write(p2)
        f1.close()
    elif sc=="c":
        f1 = open(p1, "r")
        f2 = open(p2, "w")
        f2.write(f1.read())
        f1.close()
        f2.close()
    elif sc=="r":
        f1 = open(p1, "r")
        print(f1.read())
        f1.close()

def main():
    for a in sys.argv:
        print(a)
    if sys.argv[1]=="-v":
        v()
    elif sys.argv[1]=="-p":
        path(sys.argv[2])
    elif sys.argv[1]=="-c":
        cat(sys.argv[2],sys.argv[3],sys.argv[4])

if __name__ == '__main__':
    main()