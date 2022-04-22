#def narcissistic( value ):
#  j=0
#  for i in str(value):
#    j += int(i)** len(str(value))
#  return j == value

def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
