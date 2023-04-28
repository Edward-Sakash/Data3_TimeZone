"""a = 10
b = 0
c = a/b
print(c)"""


"""try:
    x = int(input('Please give a number'))
    print(x/0)
    #print(1/x)
    print('Hello world')
except (ValueError):
    print('give me the right value')
except ZeroDivisionError:
    print('do not divide by zero')"""

"""try:
    x = int(input('Please give a number'))
    print(1/x)
except:
    print('error')"""

"""try:
    x = int(input('Please give a number'))
    print(1/x)
except Exception as e:
    print('error', e)"""
      

"""try:
    1 + 'Hallo'
finally:
    print('Goodbye, cruel world!')
print('This will not be executed.')"""

"""def bool_return():
    try:
        return True
    finally:
        return False
    
print(bool_return())  """

def dangerous_call(num):
    print(1+num)

def after_call(num):
    print('everything is alright')

try:
    dangerous_call('2')
    after_call()
except TypeError:
    print('Type Error')

try:
    raise NameError('Hi there')
except NameError:
    print('An exception flew by!')
    raise           