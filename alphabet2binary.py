lp = []
result = []
def split(alp):
  return [char for char in alp]

input = str(input('enter any alphabet:'))
char = split(input)
for a in char:
  if a.islower():
    lp.append('011')
    a = ord(a)-96
  elif a.isupper():
    lp.append('010')
    a = a.lower()
    a = ord(a)-96
  elif a == ' ':
    lp.append('001')
    a = 0
  n5 = a//16
  ns5 = a%16
  n4 = ns5//8
  ns4 = ns5%8
  n3 = ns4//4
  ns3 = ns4%4
  n2 = ns3//2
  ns2 = ns3%2
  lp.append(n5)
  lp.append(n4)
  lp.append(n3)
  lp.append(n2)
  lp.append(ns2)
  lp = [str(ints) for ints in lp]
  val = ''.join(lp)
  result.append(val)
  lp = []
print('-'.join(result))
