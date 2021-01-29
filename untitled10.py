def MultiplicationTable():
    g=int(input('where do you want to stop:'))
    for i in range(g):
        for s in range(10):
            k=i*s
            print(k*s,k)
    
    
print(MultiplicationTable())
