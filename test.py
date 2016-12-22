f = open('/users/GG/Desktop/Python/python_abaqus/3Node.txt','r')
l_line=f.readlines()
Mat=[]
for i in range(len(l_line)):
    ls=l_line[i].split(',')
    for i in range(len(ls)):
        ls[i]=float(ls[i])
##        print(ls)
    Mat.append(ls)
  
D=open('/users/GG/Desktop/Python/python_abaqus/Data.txt','w')
for i in Mat:
    k= ',   '.join([str(j) for j in i])
    D.write(k+"\n")
D.close()
f.close()
