"""
Author: Nikita Sinkha
Date: 02/13/2018
File: file_compare.py
"""
import sys

def counters(f1, f2):
    """
    func: counters()
    This function is used to find the difference in the number of lines of both the files.
    param1: f1 -> file to be read.
    param2: f2 -> another file to be read.
    """
    fil1 = open(f1)
    fil2 = open(f2)
    count1 = 0
    count2 = 0
    s = 0
    for d in fil1:
        if d != "":
            count1 += 1
    for k in fil2:
        if k != "":
            count2 += 1
    if count1 > count2:
        s = count1 - count2
    else:
        s = count2 - count1
    return s


def line_by_line(f1, f2):
    """
    func: line_by_line()
    This function compares the files line by line and reports 
    the amount of matching and nonmatching lines in files.
    param1: f1 -> file to be read.
    param2: f2 -> another file to be read.
    """
    match = 0
    nonmatch = 0
    with open(f1) as fd1, open(f2) as fd2:
        for i in fd1:
            a = fd2.readline().strip()
            b = i.strip()
            print("File 1 word:", b)
            print("File 2 word:", a)
            if b == a:
                match += 1
            else:
                nonmatch += 1
    print("")
    print("Number of matching sentances:", match)
    print("Number of non-matching sentances:", nonmatch)
    print("Number of sentances:", match+nonmatch)

def char_by_char(f1, f2):
    """
    func: char_by_char()
    This function is supposed to be used to compare the 
    corresponding positions of both the files for matching and non
    matching characters in a file.
    param1: f1 -> file to be read
    param2: f2 -> another file to be read.
    """
    yes = 0
    no = 0
    fd1 = open(f1)
    fd2 = open(f2)
    st1 = ""
    st2 = ""
    temp = 0
    for i in fd1:
        a = i.strip()
        for x in range(len(a)):
            st1 += a[x]
    for j in fd2:
        b = j.strip()
        for y in range(len(b)):
            st2 += b[y]
    for q in range(len(st1)):
        if len(st1) > len(st2):
            n = st1[q].strip()
            m = st2[q:q+1].strip()
            if n == m:
                yes += 1
            elif n == "" or m == "":
                print("No match found for- ", n, ":", m, sep="")
                no += 1
            else:
                print("no match found for- ", n, ":", m, sep="")
                no += 1
        else:
            n = st1[q:q+1].strip()
            m = st2[q].strip()
            if n == m:
                yes += 1
            elif n == "" or m == "":
                print("No match found for- ", n, ":", m, sep="")
                no += 1
            else:
                print("No match found for- ", n,":",m, sep="")
                no += 1
    print("") 
    print("Number of chars in file 1:", len(st1))
    print("Number of chars in file 2:", len(st2))
    print("Number of matching chars:", yes)
    print("Number of nonmatching chars:", no)
    print("Number of chars:", yes + no)

def counter(f):
    """
    func: counter()
    This function was designed to count the amount of lines 
    per one file
    param1: f -> file to be read
    """
    countf1 = 0
    fd1 = open(f)
    for i in fd1:
        countf1 += 1
    return countf1


def main():
    """
    func: main()
    This function is used to execute the program in order to produce favprable outcome
    """
    f1 = str(input("Enter file 1:"))
    f2 = str(input("Enter file 2:"))
    print("")
    print("File1:", f1)
    print("File2:",  f2)
    print("Running file_compare.py")
    print("")
    print("Unmatched lines 1, 2.")
    print("There are", counter(f1), "lines in file 1")
    print("There are", counter(f2), "lines in file 2")
    line_by_line(f1, f2)
    print("")
    char_by_char(f1, f2)
    

if __name__ == '__main__':
    main()
