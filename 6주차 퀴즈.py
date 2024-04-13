db = int(input("몇 단까지 출력할까요?"))

for f in range(1,db+1):
    print("-"*6,"[",f,"단","]","-"*6)
    for c in range(1,20):
        print(f,"x",c,"=",f*c) 