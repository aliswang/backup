import numpy as np
class music():
    def __init__(self,music_list_data="12音節檔案列表.txt", em_path="music_em_data2.txt", nd_path="all_music.npy"):
        """
        input:
            music_list_data : 音樂名列表
            em_path : 音樂能量檔案位置
            nd_path : 音樂壓縮檔案位置
        function:
            def search ： 尋找音樂名/序列位置
            def get_em : 尋找該序列位置的音樂能量
            def em_search :尋找位於範圍內音樂能量的音樂
            def near_list : 尋找壓縮後最近音樂
        """
        self.music_list_data = music_list_data
        self.em_path = em_path
        self.nd_path = nd_path
    def search(self,str_inp="", index_inp=None):
        """
        input:
            str_inp : 搜尋含有該輸入的檔案名
            index_inp : 搜尋檔案名的序列位置
        
        print:
            全部符合上述條件中一個的結果
        """
        index = 0
        with open(self.music_list_data,"r",encoding="utf-8") as r:
            line = r.readline()
            while(line):
                if(str_inp != ""):
                    if(str_inp in line):
                        print("第"+str(index)+"個: "+line.strip("\n"))
                elif(index_inp != None):
                    if(index == index_inp):
                        print("第"+str(index)+"個: "+line.strip("\n"))
                else:
                    print("erro")
                line = r.readline()
                index += 1
    def get_em(self,index_inp):
        """
        input:
            index_inp : 檔案名的序列位置
        return:
            音樂能量數值
        """
        index = 0
        with open(self.em_path,"r",encoding="utf-8") as r:
            line = r.readline()
            while(line):
                if(index == index_inp):
                    return float(line.split(",")[-1])
                line = r.readline()
                index += 1
    def em_search(self,low=0.1, high=0.3):
        """
        input:
            low : 搜尋能量下限
            high : 搜尋能量上限
        print:
            全部符合上述音樂能量範圍之音樂名
        """
        with open(self.em_path,"r",encoding="utf-8") as r:
            line = r.readline()
            while(line):
                em = float(line.split(",")[-1])
                if(low <= em <= high):
                    print(line.split(",")[0])
                line = r.readline()
    def near_list(self,index_inp):
        """
        input:
            index_inp : 檔案名的序列位置
        return:
            arange_list : 由關聯到不關聯的檔案序列位置
            dist_list : 由關聯到不關聯的距離
        """
        all_data = np.load(self.nd_path)
        select_data = all_data[index_inp]
        dist_list = []
        for i in range(all_data.shape[0]):
            dist_list.append(np.sum(abs(all_data[i] - select_data)))
        arange_list = np.arange(0,all_data.shape[0],1).tolist()
        dist_list, arange_list = zip(*sorted(zip(dist_list, arange_list)))
        return arange_list, dist_list