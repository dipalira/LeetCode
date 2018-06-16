M = [[1,1,1],[1,0,1],[1,1,1]]
import math
direction =  ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1))
le = len(M)
b = len(M[0])
for i,row in enumerate(M):
    for j,ele in enumerate(row):
        s = 0
        coun =0
        for l,r in direction:
            #print("index1 ",i+l, "index2 ", j+r  )
            print("l",l,"r",r)
            print("ele", ele,"index1 ",i+l, "index2 ", j+r  )
            if i+l >0 and j+r >0 and i+l < b and j+r <le :
                #print("ele", ele,"index1 ",i+l, "index2 ", j+r  )
                s += M[i+l][j+r ] 
                coun += 1
                
        s+= ele
        break
        print(s,coun+1)