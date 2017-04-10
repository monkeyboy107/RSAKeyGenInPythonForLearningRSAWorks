import functools
import decimal

def lamb(p, q):
  p = p - 1
  q = q -1 
  value = lcm(p, q)
  return value

def gcd(*numbers):
    """Return the greatest common divisor of the given integers"""
    from fractions import gcd
    return functools.reduce(gcd, numbers)

def lcm(*numbers):
    """Return lowest common multiple."""    
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    return functools.reduce(lcm, numbers, 1)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def rsaEncrypt(message, encypt):
  print("Encrypting")
  print(message, encypt)
  cipher = pow(decimal.Decimal(message), decimal.Decimal(encypt))
  print("Done encypting")
  return cipher 

def rsaDecrypt(cipher, decrypt, n):
  print("Decyrpting")
  print(cipher, decrypt, n)
  message = pow(decimal.Decimal(cipher), decimal.Decimal(decrypt))
  #message = decimal.Decimal(message) * decimal.Decimal(n)
  print("Done decrypting")
  return message

def keyGen():
  print("Generating Key")
  p = 61
  q = 53
  value = lamb(p, q)
  randNum = 17
  encyption = randNum
  decryption = modinv(encyption, value)
  print("Done generating key")
  return encyption, decryption, value

def unitTest(message):
    keys = keyGen()
    encyption = keys[0]
    decryption = keys[1]
    n = keys[2]
    cipher = rsaEncrypt(message, encyption)
    unencrypted = rsaDecrypt(cipher, decryption, n)
    print(((encyption * decryption) * n))
    print(decryption, cipher, unencrypted)

def main():
  unitTest(107)

main()
