def task1(seq=''):
    while True:
        sequence = seq
        if not seq:
            sequence = input('Enter a sequence of comma-separated numbers:\n')
        sequence = sequence.replace(' ', '')
        seq_lst = sequence.split(',')
        lst = []
        for s in seq_lst:
            if not s:
                continue
            elif s.replace('.', '', 1).replace('-', '', 1).isnumeric():
                lst.append(float(s))
            else:
                print('Please, use only numbers for your sequence!\n')
                break
        else:
            print(lst, tuple(lst))
            return True


if __name__ == '__main__':
    task1('1,2,3,4,5')  # Test 1
    task1('1,2.2,-3,.4')  # Test 2
    task1('11,12, 13, 14.5 , 15,-16,17,,')  # Test 3
    task1()
