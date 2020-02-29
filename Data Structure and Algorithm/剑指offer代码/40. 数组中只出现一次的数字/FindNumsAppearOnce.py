# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    # def FindNumsAppearOnce(self, array):
    #     # write code here
    #     num_dic = {}
    #     result_list = []
    #     for item in array:
    #         if item in num_dic.keys():
    #             num_dic[item] = num_dic[item] + 1
    #         else:
    #             num_dic[item] = 1
    #
    #     for item, count in num_dic.items():
    #         if count == 1:
    #             result_list.append(item)
    #
    #     return result_list


    def FindNumsAppearOnce(self, array):
        # write code here
        result_list = []
        for item in array:
            count = array.count(item)
            if count == 1:
                result_list.append(item)

        return result_list



if __name__ == "__main__":
    input_array = [2, 4, 3, 6, 3, 2, 5, 5]
    sol = Solution()
    print(sol.FindNumsAppearOnce(input_array))
