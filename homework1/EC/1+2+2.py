import matplotlib.pyplot as plt
import numpy
import random


# 循环次数
tryTimes = 30
# 基因个数（个体个数）
geneNum = 1000
# 基因长度（1000位）
geneLength = 200
# 变异的基因个数
changeTime = 10
# 比率 精英与平民的个体
rate = [0.2, 0.8]
# 比率 精英与平民与失败者的个体
rate2 = [0.2, 0.6, 0.2]
# 函数一的x的范围
range1 = [-5.12, 5.12]
# 函数二的x的范围
range2 = [-2.048, 2.048]

#
# function y = dejong1(x1, x2)
#     y = x1.^2 + x2.^2;
# end
#
# % -5.12<= x <= 5.12
def dejong1(x1,x2):
    return x1**2 + x2 ** 2
#
# function y = dejong2(x1, x2)
#     y = 100*(x1.^2 - x2).^2 + (1-x1).^2;
# end
#
# % -2.048<= x <= 2.048

def dejong2(x1,x2):
    return 100*(x1**2 - x2)**2 + (1-x1)**2

def getrand():
    list = []
    for i in range(0, geneLength):
        list.append(random.randint(0, 1))
    return list

def decode(list, beginNum, endNum):
        sum = 0
        rate = 1
        for i in range(0, geneLength):
            sum += list[i]* rate
            rate *= 2
        # print(rate)
        ans = (sum / rate) * (endNum- beginNum) + beginNum
        return ans
def crossover(list1, list2):
    crossoverlist = []
    for i in range(0, geneLength):
        if list1[i] == list2[i]:
            crossoverlist.append(list1[i])
        else:
            crossoverlist.append(random.randint(0,1))
    return crossoverlist

def crossover2(list1, list2):
    crossoverlist2 = []
    spot = random.randint(0,len((list1))-1)
    head = random.randint(0,1)
    for i in range(0, spot):
        if(head == 0):
            crossoverlist2.append(list1[i])
        else:
            crossoverlist2.append(list2[i])
    for i in range(spot, len(list1)):
        if(head == 0):
            crossoverlist2.append(list2[i])
        else:
            crossoverlist2.append(list1[i])
    return crossoverlist2

def crossover3(list1, list2):
    crossoverlist2 = []
    spot = (int)(len(list1)/2)
    head = random.randint(0,1)
    for i in range(0, spot):
        if(head == 0):
            crossoverlist2.append(list1[i])
        else:
            crossoverlist2.append(list2[i])
    for i in range(spot, len(list1)):
        if(head == 0):
            crossoverlist2.append(list2[i])
        else:
            crossoverlist2.append(list1[i])
    return crossoverlist2

def change(list):
    changedlist = list
    for i in range(0,changeTime):
        changePos = random.randint(0, geneLength-1)
        changedlist[changePos] = 1-changedlist[changePos]
    return changedlist


def getRandNum(list, begin):
    numList = []
    sum = 0.0
    for i in range(begin, len(list)):
        sum += list[i][3]
    # print(sum)
    i = begin
    while (i < len(list)):
        # 精英-平民-失败者模型
        # tt = (int)(0.0005/(1.0*list[i][3]/sum))
        # 精英-平民模型
        tt = (int)(0.0001 / (1.0 * list[i][3] / sum))
        for j in range(0,tt):
            numList.append(i)
        i+=1

    # print(numList)
    n = len(numList)-1
    return numList[random.randint(0,n)]

def mymain():
    listbest = []
    list1 = []
    list2 = []
    for i in range(0, geneNum):
        listTmp1 = getrand()
        list1.append(listTmp1)
        listTmp2 = getrand()
        list2.append(listTmp2)
    # print(list1)
    # print(list2)
    for i in range(0,tryTimes):
        listBestN = []
        listtmp = []
        for i in range(0, geneNum):

            # dejong1
            # x1 = decode(list1[i], range1[0], range1[1])
            # x2 = decode(list2[i], range1[0], range1[1])
            # y = dejong1(x1, x2)

            # dejong2
            x1 = decode(list1[i], range2[0], range2[1])
            x2 = decode(list2[i], range2[0], range2[1])
            y = dejong2(x1, x2)
            listtmp = (i,x1,x2,y)
            listBestN.append(listtmp)
        # print(listBestN)
        rankListBestN = sorted(listBestN, key=lambda x:x[3], reverse=False)
        # print(rankListBestN)
        print("best:   " + (str)(rankListBestN[0][3]))
        listbest.append(rankListBestN[0][3])


        # 精英-平民模型
        bestNum = (int)(geneNum*(rate[0])/(rate[0]+rate[1]))
        restNum = geneNum - bestNum


        nextGenList1 = []
        nextGenList2 = []
        for i in range(0, bestNum):
            nextGenList1.append(list1[rankListBestN[i][0]])
            nextGenList2.append(list2[rankListBestN[i][0]])
        for i in range(0, restNum):
            # 随机
            # list11 = list1[rankListBestN[random.randint(bestNum,geneNum-1)][0]]
            # list12 = list1[rankListBestN[random.randint(bestNum,geneNum-1)][0]]

            # # 轮盘赌
            num1 = getRandNum(rankListBestN,bestNum)
            num2 = getRandNum(rankListBestN,bestNum)
            list11 = list1[num1]
            list12 = list1[num2]




            # 相同情况下出同，相异则随机法3
            # nextGenList1.append(change(crossover(list11 , list12)))
            # 中间截断分为前后法2
            nextGenList1.append(change(crossover2(list11, list12)))
            # 中间截断分为前后法1
            # nextGenList1.append(change(crossover3(list11, list12)))


            # 随机
            # list21 = list2[rankListBestN[random.randint(bestNum, geneNum - 1)][0]]
            # list22 = list2[rankListBestN[random.randint(bestNum, geneNum - 1)][0]]
            #
            list21 = list2[num1]
            list22 = list2[num2]
            # 相同情况下出同，相异则随机法3
            # nextGenList2.append(change(crossover(list21, list22)))
            # 中间截断分为前后法2
            nextGenList2.append(change(crossover2(list21, list22)))
            # 中间截断分为前后法1
            # nextGenList2.append(change(crossover3(list21, list22)))
        # print(nextGenList1)
        # print(nextGenList2)




        list1 = nextGenList1
        list2 = nextGenList2
    # plt.plot(listbest)
    # plt.show()

    return listbest

if __name__ == '__main__':
    finalbestlist = []
    finallist = []
    for i in range(0, 30):
        listtmp = mymain()
        print(i)
        print(listtmp[-1])
        finallist.append(listtmp)
        finalbestlist.append(listtmp[-1])
    print("average")
    print(numpy.mean(finalbestlist))
    print("方差：")
    print(numpy.std(finalbestlist, ddof=1))