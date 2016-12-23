class Node(object):
          
    def __init__(self,Filepath):
        f = open(Filepath, 'r')
        self.l_line = f.readlines()  ## list of文本每一行
            
        self.Mat=[]             ## 节点坐标矩阵
        for i in range(len(self.l_line)):
            if self.l_line[i].startswith('*NODE') == 1:  ##判断节点坐标开始行数
                self.Nstart = i + 1
                break

        for i in range(self.Nstart, len(self.l_line)):
            if self.l_line[i].startswith('*') == 1:  ##判断节点坐标结束行数
                self.Nend = i
                break

                ##节点坐标读入
        for i in range(self.Nstart, self.Nend):
            ls = self.l_line[i].split(',')  ##字符串去掉分隔符逗号
            for i in range(len(ls)):
                ls[i] = float(ls[i])
            self.Mat.append(ls)


    def write(self,Dstpath):
        D=open(Dstpath,'w+')
       
        strMat=[]
        for i in self.Mat:          ##节点坐标矩阵转换成字符串
            k= ',   '.join([str(j) for j in i])
            k+='\n'
            strMat.append(k)
                
        for i in range(self.Nstart, self.Nend):
            j=i-self.Nstart
            self.l_line[i]=strMat[j]    ##替换原始节点坐标
            
        D.writelines(self.l_line)
        D.close()


    def shift(self,nodeid,dx,dy,dz):
        pass

        
