import random
secret = random.randint(1, 100)
count = 0
while True:
    guess =int(input("猜一个1到100的数字："))
    count+=1
    if guess == secret:
        print("right")
        print("你一共猜了", count, "次")
    elif guess > secret:
        print("大了")
    elif guess<secret:
        print("小了")