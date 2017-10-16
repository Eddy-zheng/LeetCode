# coding=utf-8
import numpy as np


class TwoSum(object):
    """docstring for Two Sum"""
    def __init__(self):
        super(TwoSum, self).__init__()

    def twosum(self, random_list=None, target=None):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if random_list is None:
            random_list = np.random.randint(2017, size=20)
        if target is None:
            target = random_list[0] + random_list[-1]

        # # solution1 : Brute Force
        # for index1, number1 in enumerate(random_list):
        #     for index2, number2 in enumerate(random_list):
        #         if (number1 + number2 == target) and index1 != index2:
        #             return index1, index2

        # solution2 : Hash map
        random_list = list(random_list)
        for index1, number1 in enumerate(random_list):
            number2 = target - number1
            if number2 in random_list:
                index2 = random_list.index(number2)
                return index1, index2


instan = TwoSum()
print instan.twosum()
