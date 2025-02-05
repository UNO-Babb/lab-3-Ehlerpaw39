#ApproxPi.py
#Name:
#Date:
#Assignment:
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main(): 
 realPi = math.pi
pi = 0
denominator = 1 
sign = 1
  

  #ask user for decimal percision (up to 10)
precision =int(input("Enter the number of decimal places of precision (up to 10): "))
if precision > 10:
  print("precision too high. setting to maximum of 10")
  precision = 10

  target_error = 10 ** (-precision)
               

start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached
while True:
  term = sign / denominator
  pi += term
  denominator += 2
  sign *= -1

end = time.time()

elapsedTime = end - start
print(elapsedTime)
print(f"Approximated pi: {4 * pi:.{precision}f}")
print(f"Real pi: {real_pi:.{precision}}")
print(f"T ime taken: {elapsed_time:.6f}seconds")
if __name__ == '__main__':
  main()
