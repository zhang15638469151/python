a = int(input('请输入你期望消费的总额:'))
while True:
    # a = int(input('请输入你期望消费的总额:'))
    buy=[]
    goods=[{'name':'电脑','price':1999},
           {'name':'鼠标','price':10},
           {'name':'游艇','price':20},
           {'name':'美女','price':998}]
    for i,j in enumerate(goods):
        print(i+1,j)

    b=int(input('请输入你要买的产品序号:'))
    # for i,j in enumerate(goods):
        if b==1:
            buy.append(goods[0])
            print('已加入购物车')
        elif b==2:
            buy.append(goods[1])
            print('已加入购物车')
        elif b==3:
            buy.append(goods[2])
            print('已加入购物车')
        elif b==4:
            buy.append(goods[3])
            print('已加入购物车')
        if b=='exit':
            print('已选好商品并加入到购物车')

    # c=input('是否进入购物车购买所选商品:')
    # if c=='是':
    #     print(buy)
    # else:
    #     c.pop(0)
    # pay=input('是否购买此商品:')
    # if pay=='是':
    #     sum=0
    #     for m,n in enumerate(buy):
    #         sum+=j['price']
    #     if sum<a:
    #         print('购买成功')
    #         print()
    #         break
    #     else:
    #         print('余额不足请充值')
    #         recharge=int(input('输入充值金额：'))
    #         a+=recharge
    #         print('充值成功')

#
#
#
#
#
#
#
#
#
a=int(input('输入总资产'))
b=[{'name':'电脑','price':1999},
  {'name':'鼠标','price':10},
 {'name':'游艇','price':20},
 {'name':'美女','price':998}]
for i,j in enumerate(b):
    print(i+1,j)
c=[]
for d in range(1,10):
    e=int(input('大兄弟买啥就点啥，买完按5'))
    if e<5:
        c.append(e)
    if e==5:
        print('小哥哥，结账')
        break
# print(c)
s=0
for f in c:
    g=b[f-1]['price']
    s+=g
print(s)
if s>a:
    print('小哥哥，钱不够，可以卖身吗？')
    h=int(input('1卖身换钱2忍着心痛减少商品'))
    if h==1:
        for k in range(66):
            l=int(input('卖身换的钱'))
            a+=l
            m=int(input('1继续卖身2虚了不卖了'))
            if m==1:
                print('扁扁的钱包')
                print(a)
                continue
            if m==2:
                print('哼，卖身后有钱了')
                print(a)
                break
    if h==2:
        for n in range(6):
            o=int(input('忍痛减少购物车'))
            q=b[o-1]['price']
            s=s-q
            c.remove(o)
            print('商品总价')
            print(s)
            print('钱包余额')
            print(a)
            if c==[]:
                print('没有商品')
            n=int(input('1继续减少购物车2不减购买'))
            if n == 1:
                print('购物车价格')
                print(s)
                continue
            if n == 2:
                if s>a:
                    print('钱还是不够，呜呜呜，继续减少商品')
                    print('购物车价格')
                    print(s)
                if s<=a:
                    print('商品价格')
                    print(s)
                    print('余额')
                    print(a-s)
                    print('购买成功')
                    break
if s<=a:
    print('商品价格')
    print(s)
    print('余额')
    print(a-s)
    print('好开心哟，又把购物车清了')




