from lab3 import *
import unittest
import sys
import os
class mTest(unittest.TestCase):
    def test_v(self):
        self.assertEqual(v(),sys.version)
    def test_path(self):
        res=os.getcwd()+"\\a.txt"
        list=[]
        list.append(res)
        self.assertEqual(path(["a.txt"]),list)
    def test_cat(self):
        cat("w",["catw.txt","this is a test"])
        r=cat("r", ["catw.txt"])
        self.assertEqual(r,"this is a test")
        cat("c",["catw.txt","catc.txt"])
        r2 = cat("r", ["catc.txt"])
        self.assertEqual(r,r2)
    def test_stringToInt(self):
        self.assertEqual(stringToInt("1"),1)
    def test_help(self):
        s = "command:[-v] [-h] [-p] [-c w|r|c] [-s]\n"
        s += "sub-commands:\n"
        s += "\t\t-c w: Write data to file \n"
        s += "\t\t-c r: Read data from  file \n"
        s += "\t\t-c c: Copy file 1 data to file 2 \n"
        s += "position arguments:\n"
        s += "\t\t-p: Print the absolute path of the file  \n"
        s += "named arguments:\n"
        s += "\t\t-v: Print system version information \n"
        s += "\t\t-s: Converts a string to a number \n"
        s += "\t\t-h: Print method information \n"
        self.assertEqual(help(),s)










unittest.main()