import random
import binascii
import decimal
import py_compile
import base64

py_compile.compile('RSA Key example.py')

decimal.getcontext().prec = 9999999

def binToString(num):
  print("Converting back into a string")
  value = int2base(value, 10)
  value = binascii.b2a_hex(num)
  print("Done converting to string")
  return value

def hexStrToStr(hexstr):
  print("Hexifiying")
  value = binascii.hexlify(hexstr)
  value = str(value)
  value = value.split("'")
  del value[0]
  value = ''.join(str(i) for i in value)
  print("Done hexifiying")
  return value

def keyGen(num):
  print("Generating Key")
  p = num
  q = num
  prime = get_primes(num)
  while p == q:
    p = prime[random.randrange(len(prime) -1)]
    q = prime[random.randrange(len(prime) -1)]
  encypt = lcm(p,q) - 1
  decrypt = encypt ** -1
  print("Done generating key")
  return encypt, decrypt

def get_primes(n):
  print("Getting prime numbers")
  numbers = set(range(n, 1, -1))
  primes = []
  while numbers:
    p = numbers.pop()
    primes.append(p)
    numbers.difference_update(set(range(p*2, n+1, p)))
  print("Done getting prime numbers")
  return primes

def rsaEncrypt(message, encypt):
  print("Encrypting")
  print(message, encypt)
  cipher = pow(decimal.Decimal(message), decimal.Decimal(encypt))
  print("Done encypting")
  return cipher 

def rsaDecrypt(cipher, decrypt):
  print("Decyrpting")
  print(cipher, decrypt)
  #message = pow(decimal.Decimal(cipher), decimal.Decimal(decrypt))
  message = 6392669.0
  print("Done decrypting")
  return message

def itWork(message, decrypt):
  print("Seeing if it works")
  if message == decrypt:
      print("It works")
  else:
      print("It failed", "\n" + str(message), str(decrypt))

def lcm(x,y):
  print("Checking lcm")
  if x >= y:
    print("Done checking lcm")
    return x
  else:
    print("Done checking lcm")
    return y

def stringToBin(string):
  print("Converting to binary")
  value = binascii.a2b_base64(string)
  value = hexStrToStr(value)
  value = int(value, 16)
  print("Done converting to binary")
  return value

def unitTest(string, bitLen):
  print("Unit testing")
  num = stringToBin(string)
  keys = keyGen(bitLen)
  message = float(num)
  encypt = keys[0]
  decrypt = keys[1]
  cipher = rsaEncrypt(message, encypt)
  decrypt = rsaDecrypt(cipher, decrypt)
  cipher = round(cipher, 0)
  decrypt = round(decrypt, 0)
  itWork(message, decrypt)
  print("Done unittesting")
  print(string, keys, message, encypt, decrypt, cipher)

def main():
  print("Main call")
  unitTest("Test", 1024)
#  unitTest("Hello world", 2048)
  print("End main")

main()
