def my_abs(number):
    """
    returns the absolute value of any number.
    number:an int.
    """ #docstring:documentation
    if number<0:
        return 0-number
    else:
        return number

def main(): #print(my_abs(a))
    #wrap test code in this function
    a=-10
    abs_a=my_abs(a) #ctrl+my_abs
    print(abs_a)


if __name__=='__main__':
    #this will only be excuted when running this file
    #it does not affect other files that import current modules
    main()