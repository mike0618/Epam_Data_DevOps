from typing import Union


def task2(nums: Union[list[int], range]):
    """
    :type nums: list[int]
    """
    for num in nums:
        if type(num) != int:
            print('Not a number appeared in the list')
        elif not num % 2:
            print(num)
            if num == 254:
                break


if __name__ == '__main__':
    task2(range(300))
    task2([1, 2, '3', 4, 254, 11, 12])
