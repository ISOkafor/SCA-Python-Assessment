def Fibbonacci_series(num):
    pass
    print("The Fibbonacci_series of a given number say 10")

    First_Value = 0
    Second_Value = 1
    for i in range(0, num):
        if (i <= 1):
            Next = i
        else:
            Next = First_Value + Second_Value
            First_Value = Second_Value
            Second_Value = Next
        print(Next)

Fibbonacci_series(10)
