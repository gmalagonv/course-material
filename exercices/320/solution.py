al=("abcdefghijklmnopqrstuvwxyz")
al2 = al.upper()
al3 = al+al2
dic={}
for i in al3:
    dic[i]=0
print(dic)
f = open('words2', 'r')
for line in f:
    for h in line:
        if h in dic:            
            dic[h]=dic[h]+1
print(dic)
        
        
    
    
#f = open('words', 'r')
#for line in f:
 #   for h in line:
  #      if h in al3:
            
   #             c = c + 1
    #print(k,c)     
            