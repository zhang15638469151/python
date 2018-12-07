# while True:
#     a = int(input('请输入你期望消费的总额:'))
#     buy=[]
#     goods=[{'name':'电脑','price':1999},
#            {'name':'鼠标','price':10},
#            {'name':'游艇','price':20},
#            {'name':'美女','price':998}]
#     for i,j in enumerate(goods):
#         print(i+1,j['name'],j['price'])
#
#     for b in range(1,6):
#         c = int(input('请输入你要买的产品序号(选完请输入5即可):'))
#         if c < 5:
#             buy.append(c)
#             print('已加入购物车')
#         if c == 5:
#             print('您已选好商品')
#             break
#
#     d=input('是否进入购物车购买所选商品')
#     if d =='是':
#         # print(buy)
#         s = 0
#         for f in buy:
#             g = goods[f - 1]['price']
#             s += g
#         print(s)
#         if s>a:
#             print('余额不足')
#             q=print(input('充值输1减少购物车商品输2'))
#             if q==2:
#                 print(buy)
#                 for h,k in enumerate(buy):
#                     l = int(input('请输入删除的商品号'))
#                     for w in range(4):
#                         if h==w:
#                             buy.remove(a[h])
#                     print('删除成功')
#
#             if q==1:
#                 f=print('请输入充值金额')
#                 a+=f
#                 print('充值成功')
#                 if s<a:
#                     print('充值成功')
#
#
#         if s<a:
#             print('购买成功')
#             buy.clear()
