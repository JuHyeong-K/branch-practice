def print_hello(): 
    for i in range(1, 10+1):
        if i % 2 == 0:
            print('Hello Git for {}th time(s)!'.format(i))
        else:
            print('nope, i is odd..')

if __name__ == '__main__':
    print_hello()
