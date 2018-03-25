def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        l = []
        for x in L:
            l.append((x,x))
        numMin = L[0]
        numMax = L[0]
        for tmpMin,tmpMax in l:
            if tmpMin < numMin:
                numMin = tmpMin
            if tmpMax > numMax:
                numMax = tmpMax
        return (numMin, numMax)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
