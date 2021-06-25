import sys
import os

def v():
    print(sys.version)
def decoratorForPath(func,com):
    def wrapper():
        if len(com)==1:
            print("The command requires at least one parameter!")
        else :
            func(com[1:])
    return wrapper

def path(list):
    for s in list:
        print(os.getcwd()+"\\"+s)

def decoratorForCat(func,sc,args):
    def wrapper():
        if sc not in ["w","c","r"]:
            print(sc+" is not a valid command!")
        else :
            func(sc,args)
    return wrapper

def cat(sc,args):
    if sc=='w':
        f1 = open(args[0], 'w')
        f1.write(args[1])
        f1.close()
    elif sc=="c":
        f1 = open(args[0], "r")
        f2 = open(args[1], "w")
        f2.write(f1.read())
        f1.close()
        f2.close()
    elif sc=="r":
        f1 = open(args[0], "r")
        print(f1.read())
        f1.close()

def decoratorForStringToInt(func,s):
    def wrapper():
        str_1 = list(s)
        for i in str_1:
            if i.isalpha():
                print("Parameters cannot contain letters!")
        else :
            func(s)
    return wrapper

def stringToInt(s):
    new=int(s)
    print(type(new))

def decoratorForMain(func):
    def wrapper():
        global com
        com=sys.argv[1:]
        if com[0] not in ["-v","-p","-c","-s"]:
            print(com[0]+" is not a valid command!")
        else:
            func()
    return wrapper

def main():
    global com
    if com[0]=="-v":
        v()
    elif com[0]=="-p":
        decoratorForPath(path,com)()
    elif com[0]=="-c":
        decoratorForCat(cat,com[1],com[2:])()
    elif com[0]=="-s":
        decoratorForStringToInt(stringToInt,com[1])
com=[]
if __name__ == '__main__':
    decoratorForMain(main)()
