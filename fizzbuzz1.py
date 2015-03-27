n = 101
print "_" * 10
print "FizzBuzz counting up to %d" % (100)
print "_" * 10
for num in range(1, n):
  if num % 15 == 0:
    print "FizzBuzz"
  elif num % 5 == 0:
    print "Buzz"
  elif num % 3 == 0:
    print "Fizz"
  else:
    print num