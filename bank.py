# 1. 로그인
#       로그들
#       1. 입금
#           금액 입력
#           이유
#       2. 출금
#           금액 입력
#           이유
#       3. 계좌이체
#           아이디
#           이유
#           금액
# 2. 새로등록
#       로그인 페이지
# 3. 종료

# member.txt (id 와 비밀번호를 기억하는 파일)
import time
def reverse(l) :
    x = []
    for a in l :
        x = [a] + x 
    return x

def load_members(): #아이디,비밀번호가 있는 파일을 불러온다.
    file = open("member.txt","r")#계정과 비밀번호 파일을 읽는다.
    ms = {}#사전을 만들기 위해 빈{}를 만든다. 
    for line in file :#읽어온 파일에서 1줄씩 반복문을 통해서 읽는다. 
        n,p = line.strip('\n').split(',')#파일의 구성이 n,p 아이디와 비밀번호로 되어있고, 콤마를 1개 이후에 줄을 바꿔준다.
        ms[n] = p#ms[n]의 키워드는 n이고  내용은 p로 구성되어있다. 
    file.close#파일을 닫는다. 
    return ms

def load_user(id):#사용자의 계좌파일을 읽어온다. 
    file = open(id+".txt","r")#사용자의 아이디에 맞는 텍스트 파일을 읽어온다. 
    list1 = []#사전을 만들기 위해 ms{}를 만든다 
    for line in file :#읽어온 파일을 1줄씩 반복문을 통해서 사전에 담는다. 
        t,m,tm,log = line.strip('\n').split(',')
        list1 = list1 + [(t,m,tm,log)]#ms사전에 키워드는 시간이고 안에 들어갈 내용은 m,tm,log이다.
    file.close
    return list1
    
def store_members(ms):#사전에 아이디랑 키를 저장하는 함수. 
    file = open("member.txt","w")#아이디와 비밀번호가 저정된 파일을 읽어온다
    names = ms.keys()#사전의 키를 names에저장한다. 
    for name in names :
        p = ms[name]#아이디 키에 비밀번호를 저장한다. 
        line = name+","+p+'\n'#line은 이름과 ,콤마와 비밀번호를 저장하고 줄바꿈해준다.
        file.write(line)
    file.close
    return None

def store_user(list1,id): #
    file = open(id+".txt","w")#사용자의 아이디와 파일을 쓰기위해 w를 쓴다.
    # names = list1.keys()#___.keys() -> [key,key,key]
    for name in list1 :# 
        (t,m,tm,log) = name#list1은 value는 3개의 튜플이다.
        line = t+","+m+","+tm+","+log+'\n'#line은 이름,돈의금액,총금액과 내용을 저장한다.
        file.write(line)
    file.close
    return None


    

def get_time():#입력한 시간을 알려주는 함수 
    t = time.gmtime(time.time())
    return time.asctime(t)

def main() :#메인함수
    print("혜리 가계부 !")
    while(True) :#프로그램이 시작되면 1.로그인,2.새로등록,3.종료로 이렇게 나눠지고 번호를 입력받도록 한다. 이외의 번호가 입력되면 다시 입력을 받도록 한다. 
        i = input("입력해주세요(1.로그인, 2.새로등록, 3.종료)")#1.로그인,2.새로등록,3종료의 숫자를 입력받는다. 
        if (i=="1") :#만약 1.로그인을 입력받으면
            ms = load_members()#ms(아이디와,비밀번호를)load_members()함수를 사용한다. load_members()함수는 아이디와 비밀번호를 입력받는다. 
            n = input("아이디를 입력 : ")# 아이디를 입력받는다.
            while(True) :
                if (n in ms) :#입력받은 아이디가 ms에서 존재하는 아이디라면 멈추고 다음으로 넘어간다.
                    break
                else :
                    n = input("아이디를 입력 : ")#members.txt에 없는 아이디라면 다시 재입력받는다. 
            #ms=아이디랑 비밀번호가 있는 사전 
            #n=아이디 key가 아이디,value 비밀번호 
            
            p = ms[n] # 사전에서 key값을 가진 value의 값을 받아와서 p에 저장 (그 키값의 value를 꺼내와서 저장하는 것. )
            pd = input("비밀번호를 입력 : ")#비밀번호를 입력받는다. 
            while(True) :
                if p == pd :#비밀번호가  사전에 있는 비밀번호와 일치하면 
                    print("로그인 성공")#로그인 성공이라고 메세지를 준다. 
                    break#로그인 성공시에 다음 단계로 진행한다. 
                else :
                    pd = input("비밀번호를 입력 : ") #비밀번호가 일치하지 않을경우 다시 입력을 받는다 
            list1 = load_user(n)#ms는 사용자 계좌파일을 저장한다.?? 
            print("로그를 보여드립니다.")
            for time in list1 :
                (t,m,tm,log) = time
                print(t,m,tm,log)
            while(True):
                i = input("1.입금 2.출금 3.계좌이체 4.아무거나 입력")
                if (i=="1"):
                    im = input("입금할 금액 입력 : ") #m 금액
                    # a=(-1)*im
                    log = input("입금 로그 입력 : ")#내용
                    t = get_time()
                    tm = int(tm) +int(im)
                    list1= list1 + [(t,im,str(tm),log)]#추가update
                    store_user(list1,n)#store_user함수는 key값을t로가지고,value를 ()
                elif(i=="2"):
                    im = input("출금할 금액 입력 : ") #m 금액
                    log = input("출금 로그 입력 : ")#내용
                    t = get_time()
                    tm = int(tm) - int(im)
                    list1= list1 + [(t,im,str(tm),log)]#추가update
                    store_user(list1,n)#store_user함수는
                elif(i=="3"):
                    print("계좌이체 코너입니다.")
                    send=input("보내실 계좌번호를 입력해주세요.")
                    ms = load_members()
                    while(True) :
                        if (send in ms) :#입력받은 아이디가 ms에서 존재하는 아이디라면 멈추고 다음으로 넘어간다.
                            break
                        else :
                            send = input("아이디를 찾을 수 없습니다. 다시 입력해 주세요. : ")#members.txt에 없는 아이디라면
                    a1=send
                    print(send)
                    im = input("송금 금액 입력 : ") #m 금액
                    im2= (im)
                    log = input("송금 로그 입력 : ")#내용
                    log2=log
                    t = get_time()
                    tm = int(tm) - int(im)
                    list1= list1 + [(t,im,str(tm),log)]#추가update
                    store_user(list1,n)
                    #여기부터 상대방 계좌
                    list2 = load_user(a1)#ms는 사용자 계좌파일을 저장한다.?? 
                    print("받는 사람의 계좌입니다.")
                    for time in list2 :
                        (t,m,tm,log) = time
                        print(t,m,tm,log)
                    im=im2
                    log=log2
                    t = get_time()
                    tm = int(tm) + int(im)
                    list2= list2 + [(t,im,str(tm),log)]#추가update
                    store_user(list2,a1)#store_user함수는
                    
                else :
                    break
            # 로그인 무조건 성공 !
            
        elif (i=="2") :
            # 새로등록 부분
            ms = load_members()
            n = input("아이디를 입력 : ")
            while(True) :
                if (n in ms) :
                    n = input("아이디를 입력 : ")
                else :
                    break
            p = input("비밀번호를 입력 : ")
            ms[n] = p
            store_members(ms)
            file = open(n+".txt","w")
            t = get_time()
            s = t+","+"10000"+","+"10000"+","+"계좌생성"
            file.write(s)
            file.close
        else :
            break
    return
main()
