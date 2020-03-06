class Solution:
    def IsContinuous(self, numbers):
        if numbers == None or len(numbers) < 5:
            return False

        numbers.sort()

        zero_count = numbers.count(0)

        if zero_count == 4:
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


if __name__ == '__main__':
    sol = Solution()
    numbers = [1, 3, 5, 0, 0]
    # numbers = [1, 3, 0, 7, 0]
    # numbers = [1, 0, 0, 5, 0]
    # numbers = [3, 0, 0, 0, 0]
    print(sol.IsContinuous(numbers))
