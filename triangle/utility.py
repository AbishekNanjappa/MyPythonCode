def triangle_type(a,b,c):       #Where a,b and c are the lengths of the sides of the triangle
    result = "0000"
    if a + b > c and b + c > a and c + a > b:
        if a == b and b == c:
            result = "Equilateral"
        elif a != b and b != c and c != a:
            result = "Scalene"
        else:
            result = "Iscoceles" 
    else:
        result = "NA"
    return result