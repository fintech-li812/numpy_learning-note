correct_password = "123456"
chance = 3
while chance>0:
    pwd = input(f"请输入你的密码,剩余{chance}次机会")
    if pwd==correct_password:
        print("密码正确")
        break
    chance-=1
else:
        print("你的机会已用完")