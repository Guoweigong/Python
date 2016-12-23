class Node(object):
          
    def __init__(self,Filepath):
        f = open(Filepath, 'r')
        self.l_line = f.readlines()  ## list of文本每一行
            
        self.Mat = []             ## 节点坐标矩阵
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
                ls[0] = int(ls[0])         ##节点序号转成整数
            self.Mat.append(ls)

    ##节点坐标数据写出到指定文件
    def write(self,Dstpath):
        D = open(Dstpath,'w+')
        strMat=[]
        for i in self.Mat:          ##节点坐标矩阵转换成字符串
            k = ',   '.join([str(j) for j in i])
            k += '\n'
            strMat.append(k)
                
        for i in range(self.Nstart, self.Nend):
            j = i-self.Nstart
            self.l_line[i] = strMat[j]    ##字符串替换原始节点坐标
        D.writelines(self.l_line)
        D.close()

    ##移动指定节点的坐标
    def shift(self, nodeid, dx, dy, dz):
        if str(nodeid) == 'All':
            for i in range(0,len(self.Mat)):
                self.Mat[i][1] += dx
                self.Mat[i][2] += dy
                self.Mat[i][3] += dz
        else:
            self.Mat[nodeid][1] += dx
            self.Mat[nodeid][2] += dy
            self.Mat[nodeid][3] += dz

    ##设置NSET名称，nset新名称
    def nsetname(self,nset):
        namepos=self.l_line[self.Nstart-1].find('=')+1           ##NSET名称起始位置
        self.l_line[self.Nstart-1] =self.l_line[self.Nstart-1][0:namepos] + nset + '\n'




