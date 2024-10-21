

def q1(): 
  num1 = int(input("In: "))
  num2 = int(input("In: "))
  num3 = int(input("In: "))

  if num1 >= num2 or num1 >= num3:
      if num2 >= num3:
          print(num3)
      else:
          print(num2)
  else:
      print(num1)
  #Write Assignment code here


def q2(): 
  num4 = int(input("In: "))
  if not num4%4:
      if not num4%100:
          if not num4%400:
              print("Is a leap year")
          else:
              print("Is not a leap year")
      else:
          print("Is a leap year")
  else:
      print("Is not a leap year")
  #Write Assignment code here



#Do not alter the following code
#Comment out the following code when running your tests

# q1()
# q2()
