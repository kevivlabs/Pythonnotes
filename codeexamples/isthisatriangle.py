def is_triangle(a, b, c):
        # Triangle Inequality Theorem
        # sum of any 2 sides of a triangle must be greater than the 3rd side
    if (a+b) >c and (b+c) > a and (c+a) > b:
        return True
    else: 
        return False
      
# yeah if you dont know the Triangle Inequality Theorem, you can just keep thinking as long as you want :/ 
