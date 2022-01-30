if __name__ == '__main__':
  #參數
  """
  上圖尾部與下圖頂部假設模糊化的情況下
  會產生相似的資料分佈
  Path - 輸入檔案路徑
  OutputPath - 輸出檔案路徑
  CatchWidth - 視窗抓取寬度大小
  VagueWidth - 模糊視窗寬度大小
  VagueDot - 模糊視窗長度比例
  BlankNorm - 空白結尾視窗抓取大小
  PearsonrCriterion - 相似度標準(0->最小 1->最大)
  """
  Path = "./combine_input"
  OutputPath = "./combine_output"
  CatchWidth = 5
  VagueWidth = 5
  VagueDot = 0.1
  BlankNorm = 1
  PearsonrCriterion = 0.7
  import cv2
  import numpy as np
  import os
  from scipy.stats import pearsonr

  #讀檔
  FileNameList = []
  for root, dirs, files in os.walk(Path):
    for file_name in files:
      if file_name.endswith(".jpg"):
        FileNameList.append(os.path.join(root,file_name))
  #執行
  for i in FileNameList:
    PrePic = cv2.imread(i)
    if(np.sum(abs(PrePic[BlankNorm*-1:,:] - np.average(PrePic[BlankNorm*-1:,:]))) < 10000):
      print("空白結尾\nPass By ",i)
      continue
    VagueSize = (int(PrePic.shape[1]*VagueDot), VagueWidth)
    PreVag = cv2.resize(PrePic[CatchWidth*-1:,:], VagueSize)
    for j in FileNameList:
      if(i != j):
        Pic = cv2.imread(j)
        if(PrePic.shape[1] == Pic.shape[1]):
          PicVag = cv2.resize(Pic[:CatchWidth,:], VagueSize)
          if(pearsonr(PreVag.reshape(-1), PicVag.reshape(-1))[0] > PearsonrCriterion):
            OutPic = np.vstack((PrePic,Pic))
            if(OutPic.shape[0] >= 50000):
              print("圖片檔案過大")
            else:
              PreName = i.split("\\")[-1].split(".")
              NextName = j.split("\\")[-1].split(".") 
              OutFileName = OutputPath + "/" + PreName[0] + "_" + NextName[0] + "." + PreName[1]
              print(OutFileName)
              cv2.imwrite(OutFileName, OutPic)