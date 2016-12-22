f = open('/users/GG/Desktop/Python/python_abaqus/node.inp','r')
l_line=f.readlines() ## list of文本每一行
Mat=[]               ## 节点坐标矩阵

for i in range(len(l_line)):
    if l_line[i].startswith('*NODE')==1:       ##判断节点坐标开始行数
        Nstart=i+1
        break
    
for i in range(Nstart,len(l_line)):
    if l_line[i].startswith('*')==1:   ##判断节点坐标结束行数
        Nend=i
        break
    
##节点坐标读入
for i in range(Nstart,Nend):
    ls=l_line[i].split(',')                    ##字符串去掉分隔符逗号
    for i in range(len(ls)):
        ls[i]=float(ls[i]) 
    Mat.append(ls)

D=open('/users/GG/Desktop/Python/python_abaqus/Data.inp','w')
for i in Mat:
    k= ',   '.join([str(j) for j in i])
    D.write(k+"\n")
D.close()
f.close()

