def maxProfit(x):
    buy = []
    sell = []    
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if x[i] >= x[j]:
                continue
            elif x[i] < x[j]:
                buy.append(x[i])
                sell.append(x[j])
    if buy:
        return max(sell) - min(buy)
    else:
        return 0
            
x =   [7,1,5,3,6,4]
print(maxProfit(x))

# def maxProfit(x):
#     buy = []
#     sell = []    
#     for i in range(len(x)):
#         for j in range(i+1, len(x)):
#             if x[i] >= x[j]:
#                 sell.append(0)
#             elif x[i] < x[j]:
#                 buy.append(x[i])
#                 sell.append(x[j])
#     buy_list = []
#     for i in buy:
#         if i != 0:
#             buy_list.append(i)

#     if buy_list:
#         return max(sell) - min(buy_list)
#     else:
#         return 0