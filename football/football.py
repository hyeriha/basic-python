import random
# user = 0
# computer =0

#사용자공격#
# def userattack () :
#     user1 = input("1~8까지의 숫자를 입력해주세요.")
#     while not (user1.isdigit() and (0<int(user1)<9)):
#         user1=input("1:1~8까지의 숫자를 입력해주세요.")
#     return int(user1)
    # user1 = u1
    # user2 = input("2n:1~8까지의 숫자를 입력해주세요.")
    #     user2 i
#점수비교

# input … -> (user,computer)
#컴퓨터방어


# user1 = userattack()
# user2 = userattack()
# user,computer = counter(user1,user2,com1,com2,user,computer)


#컴퓨터 공격 
def computerattack (): 
    com1 = random.randint(1,8)
    com2 = random.randint(1,8) 
    while com1== com2 : 
        com2= random.randint(1,8)
    return (com1,com2)


def user_input(): 
    u1 = input("1~8까지의 숫자를 입력해주세요.")
    while not (u1.isdigit() and (0< int(u1) < 9)): 
        u1 = input("1:1~8까지의 숫자를 입력해주세요.")
    return int(u1)

def compare(per1,com1,com2) : 
    return per1 == com1 or (per1 == com2)
def compare2(p1,p2,c1,c2):
    return p1==c1 and p2==c2

def main (): 
    game = 0
    game+= 1
    print("사용자가 공격,컴퓨터가 방어자")
    user = 0
    computer =0
    i=0 
    while i <3:
        i+=1
        print("사용자가 공격",i,"번째")
        a1,b2 = computerattack()
        print(a1,b2)
        u1 = user_input()
        if compare(u1,a1,b2) : 
            user+=1
        else : 
            u2 = user_input()
            if compare(u2,a1,b2) : 
                user+=1
            else :
                computer+=1 
    print ("user:",user,"computer:",computer)
    print("*-------------------------------------*")
    k=0
    print("컴퓨터가 공격합니다.")
    while k <3 :
        k+=1
        print("컴퓨터가 공격",k,"번째")
        c1,c2 = computerattack ()
        print(c1,c2)
        human1 = user_input()
        human2 = user_input()
        if compare2(human1,human2,c1,c2):
            computer+=1
        else : 
            user+= 1
    print ("user:",user,"computer:",computer)

def start():
    print("게임을 시작합니다\n 처음에는 사용자가 공격합니다. 1~8까지 숫자를 입력하세요. \n 다음에 컴퓨터가 공격합니다. 각각 여섯번씩(공격3,방어3) 4번의 게임을 하게됩니다. \n 사용자가 공격시 숫자를 입력합니다.\n 입력한 첫번째수나 두번째수가 컴퓨터가 방어한 숫자 둘중 하나라도 일치하면 사용자의 승리가 됩니다.\n")
    o=0
    while o<4 :
        o+=1
        main()

start()