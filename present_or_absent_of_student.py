def roll_no(n):
     s = 0
     for i in range(1,k+1):
          if n == i:
               s = i

     if s == n:
          print("present")
     else:
          print("absent")
k = int(input("enter the strength of the class: "))
n = int(input("enter the roll no. of student: "))
out = roll_no(n)