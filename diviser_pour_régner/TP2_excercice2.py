def positive_negative(num1,num2):
    if num1 >= 0 and num2>=0:
        return True
    else:
        if num1 < 0 and num2 < 0:
            return True
        else:
            return False

print(positive_negative(2,3))