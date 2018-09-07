"""Math functions for calculator."""


def add(nums):
    """Return the sum of the two inputs."""
    total = 0
    for num in nums:
        total = total + num
    return total


def subtract(nums):
    """Return the second number subtracted from the first."""
    
    for num in nums:
        total = total - num
    return total

def multiply(nums):
    """Multiply the two inputs together."""
    total = 1
    for num in nums:
        total = total * num
    return total

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    return num1 / num2

def square(num1):
    """Return the square of the input."""
    return num1 * num1

def cube(num1):
    """Return the cube of the input."""
    return num1 * num1 * num1

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return num1 ** num2

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    return num1 % num2

def add_mult(num1, num2, num3):
    """Add first and second numbers and multiply the result with third"""
    return (num1 + num2) * num3

def add_cubes(num1, num2):
    """Adds cube of num1 to cube of num2"""
    return cube(num1) + cube(num2)


    
