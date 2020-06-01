class Solution:
    def IsContinuous(self, numbers):
        if numbers == None or len(numbers) < 5:
            return False

        numbers.sort()

        zero_count = numbers.count(0)

        if zero_count >= 4:
            return True

        if zero_count > 0:
            numbers = list(filter(lambda x: x != 0, numbers))

        absent_list = self.IsSeries(numbers)

        if zero_count == len(absent_list):
            return True
        else:
            return False

    def IsSeries(self, array):
        absent_list = []
        tempList = list(range(array[0], array[-1] + 1))
        for index, item in enumerate(tempList):
            if item not in array:
                absent_list.append(item)
        return absent_list

    def IsContinuous2(self, numbers):
        if numbers is None or len(numbers) < 5:
            return False

        new_numbers = sorted(numbers)
        count_zero = new_numbers.count(0)

        if count_zero == 0:
            if self.isContinueNum(new_numbers):
                return True
            else:
                return False
        if count_zero == 1:
            # 从第1位到最后1位是连续子序列
            if self.isContinueNum(new_numbers[1:]):
                return True
            # 中间有缺失1个数字
            elif self.fillOne(new_numbers[1:]):
                return True
            else:
                return False
        if count_zero == 2:
            # 从第2位到最后1位是连续子序列
            if self.isContinueNum(new_numbers[2:]):
                return True
            # 中间有缺失1个数字
            elif self.fillOne(new_numbers[2:]):
                return True
            # 中间缺失2个数字
            elif self.fillTwo(new_numbers[2:]):
                return True
            else:
                return False

        if count_zero == 3:
            # 从第3位到最后1位是连续子序列
            if self.isContinueNum(new_numbers[3:]):
                return True
            # 中间有缺失1个数字
            elif self.fillOne(new_numbers[3:]):
                return True
            # 中间缺失2个数字
            elif self.fillTwo(new_numbers[3:]):
                return True
            # 中间缺失3个数字
            elif self.fillThree(new_numbers[3:]):
                return True
            else:
                return False
        if count_zero >= 3:
            return True

    # 判断一个序列是否是连续的数字
    def isContinueNum(self, numbers):
        count = 0
        for i in range(1, len(numbers), 1):
            if numbers[i] - numbers[i - 1] == 1:
                count += 1

        if count == len(numbers) - 1:
            return True
        else:
            return False

    # 填充一个数字能否满足连续序列
    def fillOne(self, numbers):
        for i in range(1, len(numbers), 1):
            if numbers[i] - numbers[i - 1] != 1:
                numbers.insert(i, numbers[i - 1] + 1)
                break

        if self.isContinueNum(numbers):
            return True
        else:
            return False

    # 填充2个数字能否满足连续序列
    def fillTwo(self, numbers):
        count = 0
        for i in range(1, len(numbers) + 2, 1):
            if numbers[i] - numbers[i - 1] != 1:
                if count < 2:
                    numbers.insert(i, numbers[i - 1] + 1)
                    count += 1
                else:
                    break

        if self.isContinueNum(numbers):
            return True
        else:
            return False

    # 填充3个数字能否满足连续序列
    def fillThree(self, numbers):
        count = 0
        for i in range(1, len(numbers) + 3, 1):
            if numbers[i] - numbers[i - 1] != 1:
                if count < 3:
                    numbers.insert(i, numbers[i - 1] + 1)
                    count += 1
                else:
                    break

        if self.isContinueNum(numbers):
            return True
        else:
            return False

    # 方法三： 剑指offer上方法
    def IsContinuous3(self, numbers):
        if not numbers or len(numbers) < 1:
            return False

        numbers.sort()

        # 统计数组中0的个数
        numberOfZero = numbers.count(0)
        numberOfGap = 0

        # 统计数组中的间隔数目
        small = numberOfZero
        big = small + 1
        while big < len(numbers):
            # 两个数相等，有对子，不可能是顺子
            if numbers[small] == numbers[big]:
                return False
            numberOfGap += (numbers[big] - numbers[small] - 1)
            small = big
            big += 1

        return False if numberOfGap > numberOfZero else True


if __name__ == '__main__':
    sol = Solution()
    # numbers = [1, 3, 5, 0, 0]
    # numbers = [1, 3, 0, 7, 0]
    # numbers = [1, 0, 0, 5, 0]
    # numbers = [1, 3, 5, 2, 4]
    # numbers = [3, 0, 0, 0, 0]
    numbers = [1, 3, 2, 6, 4]
    print(sol.IsContinuous3(numbers))
