def task5(lst: list[int]) -> list[int]:
    """
    Returns top-three integers from a list of integers
    """
    if type(lst) != list:
        print('Invalid input')
        return []
    ints = set()  # if we need a top-three different integers from the original list
    not_int_lst = []
    top_three = []
    for element in lst:
        if type(element) != int:
            not_int_lst.append(element)
        else:
            ints.add(element)
    for _ in range(3):
        if not ints:
            break
        max_elm = max(ints)
        ints.discard(max_elm)
        top_three.append(max_elm)
    if not_int_lst:
        print("You've passed some extra elements that I can't parse:", not_int_lst)
    return top_three


def task5_2(lst: list[int]) -> list[int]:
    """
    Returns top-three integers from a list of integers
    Slightly different function
    The same integers in returned list are allowed
    """
    if type(lst) != list:
        print('Invalid input')
        return []
    ints = []
    not_int_lst = []
    for element in lst:
        if type(element) != int:
            not_int_lst.append(element)
        else:
            ints.append(element)
    if not_int_lst:
        print("You've passed some extra elements that I can't parse:", not_int_lst)
    return sorted(ints, reverse=True)[:3]


if __name__ == '__main__':
    print(task5([5, 15]))  # Test 1
    print(task5([1, 2, 3, 4, 5]))  # Test 2
    print(task5([1, 2, 3, 4, 5, 5, 5, 15, 'hi', 'there', 22.2, [1]]))  # Test 3

    print(task5_2([5, 15]))  # Test 1
    print(task5_2([1, 2, 3, 4, 5, 5, 5, 15, 'hi', 'there']))  # Test 2
