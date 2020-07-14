file = open('abc.txt','w')
d = {}

while True:
    print('=>')
    print('1. 建立辭彙')
    print('2. 列出所有單字')
    print('3. 英翻中')
    print('4. 中翻英')
    print('5. 測驗學習成果')
    print('6. 離開系統')
    
    sel = input('what do you want to do: ')

    if sel=='1':
        while True:
            voc = input('input new word(按0跳出): ')
            if voc == '0':
                break
            if voc not in d:
                m = input('輸入中文解釋: ')
                d[voc] = m
            else:
                print('you already have that word')
    elif sel=='2':
        lk = sorted(d)
        for item in lk:
            print(item, '是', d[item])
    elif sel=='3': 
        voc = input('what do you want to find (english: ')
        if voc == '0':
            break
        if voc in d: 
            print(d[voc])
        else:
            print('defind')
    elif sel=='4': 
        got=False
        ch = input('what do you want to find (chinese: ')
        if ch == '0':
            break
        for k,v in d.items():
            if ch==v:
                print(ch,'的英文是',k)
                got=True
        if not got:
            print('defind')                                      
    elif sel=='5': 
        score=0
        print('The total score is', len(d), 'points')
        for k, v in d.items():
            print(v, ':')
            ans = input()
            if ans == k:
                score += 1
                print('correct! you got', score, 'points now')
            else:
                print('wrong! you got', score, 'points now')
    elif sel=='6':
        file.close()
    else:
        print('sorry')
