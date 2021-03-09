#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 20:12:46 2021

@author: isaaclello-smith
"""

# # Problem 1
# ----------------
# def fancy_divide(numbers,index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#     except IndexError:
#         print("-1")
#     else:
#         print("1")
#     finally:
#         print("0")
        
# fancy_divide([0,2,4],0)

# I originally thought this would print error, 0
# but it prints 0, error
# evidently, it runs through finally before processing the error that isn't caught

# # Problem 2
# ----------------
# def fancy_divide(numbers, index):
#     try:
#         denom = numbers[index]
#         for i in range(len(numbers)):
#             numbers[i] /= denom
#         print('Executing division')
#     except IndexError:
#         fancy_divide(numbers, len(numbers) - 1)
#         print('threw Index Error')
#     except ZeroDivisionError:
#         print("-2")
#     else:
#         print("1")
#     finally:
#         print("0")
        
# fancy_divide([0,2,4],4)

# I originally thought this would print 0, 1, 0 
# but it prints, 1, 0, 0
# Evidently, it processes the error handling that catches the specified error type before the finally 

# # Problem 3
# ----------------
# def fancy_divide(numbers, index):
#     try:
#         try:
#             denom = numbers[index]
#             for i in range(len(numbers)):
#                 numbers[i] /= denom
#         except IndexError:
#             fancy_divide(numbers, len(numbers) - 1)
#         else:
#             print("1")
#         finally:
#             print("0")
#     except ZeroDivisionError:
#         print("-2")
        
# fancy_divide([0,2,4],4)

# I originally thought this would print 1, 0 but it prints 1, 0, 0 
# Evidently, it processes the error handling that catches the specified error type before the finally in that function call

# # # Problem 4
# # ----------------
# def fancy_divide(list_of_numbers, index):
#     try:
#         try:
#             raise Exception("0")
#         finally:
#             denom = list_of_numbers[index]
#             for i in range(len(list_of_numbers)):
#                 list_of_numbers[i] /= denom
#     except Exception as ex:
#         print(ex)
        
# fancy_divide([0, 2, 4], 0)

# I originally thought this would throw a division by zero error. But it gets caught in the outer try except statement

# # # Problem 5
# # ----------------
# def fancy_divide(list_of_numbers, index):
#     try:
#         try:
#             denom = list_of_numbers[index]
#             for i in range(len(list_of_numbers)):
#                 list_of_numbers[i] /= denom
#         finally:
#             raise Exception("0")
#     except Exception as ex:
#         print(ex)
        
# fancy_divide([0, 2, 4], 0)

# Interesting that this doesn't throw a div by zero exception. Because the inner try / finally does not specifically catch a div by zero exception, the finally executes first, which raises a different exception that gets printed. Notable that this could mask errors if you were to write logic like this. 

# Helpful notes from python.org: https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions

# "
# If an exception occurs during execution of the try clause, the exception may be handled by an except clause. If the exception is not handled by an except clause, the exception is re-raised after the finally clause has been executed.

# An exception could occur during execution of an except or else clause. Again, the exception is re-raised after the finally clause has been executed.

# If the try statement reaches a break, continue or return statement, the finally clause will execute just prior to the break, continue or return statement’s execution.

# If a finally clause includes a return statement, the returned value will be the one from the finally clause’s return statement, not the value from the try clause’s return statement.
# "

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

# no error in try clause, executes else and finally
divide(2, 1)

# error in try clause that is caught in exception, executes exception and then finally
divide(2, 0)

# error in try clause that is not caught in exception, executes finally and then error
divide("2", "1")
