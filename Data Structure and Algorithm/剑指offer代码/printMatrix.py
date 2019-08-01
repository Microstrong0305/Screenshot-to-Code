class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        rows = len(matrix)
        columns = len(matrix[0])
        if matrix == None or rows <= 0 or columns <=0:
            return
        start = 0
        while columns > start * 2 and rows > start *2:
            endX = columns - 1 -start
            endY = rows - 1 -start
            # 从左到右打印一行
            for i in range(start,endX+1):
                res.append(matrix[start][i])
            # 从上到下打印一行
            if start < endY:
                for i in range(start+1, endY+1):
                    res.append(matrix[i][endX])
            # 从右到左打印一行
            if start < endX and start < endY:
                for i in range(endX-1, start-1, -1):
                    res.append(matrix[endY][i])
            # 从下到上打印一列
            if start < endX and start < endY - 1:
                for i in range(endY-1, start, -1):
                    res.append(matrix[i][start])

            start += 1

        return res

sol = Solution()
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix = [[1],[2],[3],[4],[5]]
print(sol.printMatrix(matrix))

