import random

words=("victory","awesome","best","bedazzled","baby","deep","show","sweet","serendipity","lucky","sugar","love","yes","alright","please","family","foever","happy","joy","pleasure")

count = 0
while True : 
    rand1 = random.randint(0,19)
#    print (words[rand1])
#    i=0
#단어섞기 
    origin = words[rand1] 
    sorted = ""
    for ochar in origin : 
        index = 0 
        for schar in sorted : 
            if ochar <= schar:
                break
            else : 
                index = index + 1 
        sorted = sorted [:index]+ochar +sorted [index:]
    s=sorted
    r=""
    for c in s : 
        r = c + r 
#    for number in words[rand1]:
#      print (i,end='')
       
#      i+=1
    k=""
    for spel in words[rand1]:
           if spel == ("a") :
               k= k+"?"
           elif spel == ("i"):
               k= k+"?"
           elif spel == ("e"):
               k= k+"?"
           elif spel == ("o"):
               k= k+"?"
           elif spel == ("u"):
               k= k+"?"      
           else:
               k=k+"_"
    while True :         
        count+=1
        print()
        print("시도횟수",count)
        print ("후보문자:",r)
        print("게임보드")
        i=0
        for number in words[rand1]:
           print (i,end='')
       
           i+=1
        print()   
        print (k)
        print()
        location = input("단어의 위치를 입력:")
        while not (location.isdigit() and int(location) <=len(words[rand1])-1):
            location = input ("단어 위치 재입력:")
        stay = int(location)
        again= words[rand1]
        pick = input("단어를 입력:")
        if (again[stay]==pick):
            print ("정답")
            k=k[0:stay]+pick+k[stay+1:]
        else: 
            print ("틀렸습니다.")
        if (k==words[rand1]):
            break
        else : 
            continue 
