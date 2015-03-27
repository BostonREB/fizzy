import sys

while True:
  if len(sys.argv) == 1:
    number = raw_input("Please enter the number to play up to --->  ")
  else:
    number = sys.argv[1:]
    number = number[0]
  try:
    x = int(number)
  except ValueError:
    print "You did not enter a valid number"
    number = raw_input("Please enter the number to play up to --->  ")
    continue
  else:
    break
number = int(number)
print "_" * 10
print "FizzBuzz counting up to %d" % (number)
print "_" * 10
for num in range(1, number):
  if num % 15 == 0:
    print "FizzBuzz"
  elif num % 5 == 0:
    print "Buzz"
  elif num % 3 == 0:
    print "Fizz"
  else:
    print num