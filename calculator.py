def add(*args):
    for each in args:
        try:
            int(each)
        except:
            raise TypeError(f'You can only add numbers in this digital calculator. {each} found.')
    return sum(args)

def multiply(*args):
    product=1
    for each in args:
        try:
            int(each)  
        except:
            raise TypeError('You can only multiply numbers in this calculator.')
        product *= each
    return product
