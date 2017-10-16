# coding=utf-8
import sys
import numpy as np
sys.path.append('../')
from lib import *


class TwoSum(object):
    """docstring for Two Sum"""
    def __init__(self):
        super(TwoSum, self).__init__()
        self.twosum()

    def twosum(self, random_list=None, target=None):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.random_list = random_list
        self.target = target

        if self.random_list is None:
            self.random_list = np.random.randint(2017, size=2000)
        if self.target is None:
            self.target = self.random_list[0] + self.random_list[-1]

    @time_cost
    def solution1(self):
        # solution1 : Brute Force
        for index1, number1 in enumerate(self.random_list):
            for index2, number2 in enumerate(self.random_list):
                if (number1 + number2 == self.target) and index1 != index2:
                    return index1, index2

    @time_cost
    def solution2(self):
        # solution2 : Hash map
        self.random_list = list(self.random_list)
        for number1 in self.random_list:
            number2 = self.target - number1
            if number2 in self.random_list:
                # index1 = np.where(self.random_list == number1)
                # index2 = np.where(self.random_list == number2)
                index1 = self.random_list.index(number1)
                index2 = self.random_list.index(number2)
                return index1, index2


instan = TwoSum()
print instan.solution1()
print instan.solution2()

