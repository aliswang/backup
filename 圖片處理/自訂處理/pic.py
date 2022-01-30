import math
import numpy as np
import cv2
import os
import tensorflow as tf
import multiprocessing
from sklearn.cluster import DBSCAN
from copy import deepcopy
from matplotlib import pyplot as plt
from IPython.display import clear_output

class pic_appraisal():
    def __init__(self,img_path,size=(128,128),eps=2,min_samples=2):
        """
        inputs:
            img_path : 圖片位置/含圖片檔案的位置
            size : analysis用形狀, appraisal固定64x64x3
            eps : analysis用距離 參數
            min_samples : analysis用最小集合點數 參數
        function:
            def analysis : 計算DBSCAN計算色塊色差等參數
            def appraisal : 給分,評分等級S,A,B,C
        初始化含圖片整形縮放
        """
        def fill_square(img, size):
            tmp = np.zeros((max(img.shape),max(img.shape),3)).astype('uint8')
            s_x = math.floor((max(img.shape)*2-img.shape[0]-img.shape[1])/2)
            e_x = (max(img.shape)-math.ceil((max(img.shape)*2-img.shape[0]-img.shape[1])/2))
            try:
                tmp[s_x:e_x,:,:] = img
            except:
                tmp[:,s_x:e_x,:] = img
            tmp = cv2.resize(tmp, size, interpolation=cv2.INTER_AREA)
            img = tmp
            return img
        
        self.img_path = img_path
        self.size = size
        self.eps = eps
        self.min_samples = min_samples
        try:
            self.img = plt.imread(str(self.img_path))[:,:,:3]
            self.tag = "one"
        except:
            file_data = []
            for root, dirs, files in os.walk(img_path):
                for file in files:
                    if (file.endswith(".jpg") or file.endswith(".png")):
                        file_data.append(os.path.join(root,file))
            if(file_data):
                self.tag = "folder"
            else:
                self.tag = "nothing"
        if(self.tag == "one"):
            self.img = fill_square(self.img, size=self.size)
        elif(self.tag == "folder"):
            self.img_data = np.zeros((len(file_data),self.size[0],self.size[1],3)).astype('uint8')
            for i in range(len(file_data)):
                img_i = plt.imread(str(file_data[i]))[:,:,:3]
                img_i = fill_square(img_i,size = self.size)
                self.img_data[i] = img_i
        else:
            print("erro no find pic\nneed .jpg or .png")
   
    def analysis(self,return_mode="return"):
        """
        input:
            return_mode : "return" ->回傳數值
                          "show"   ->顯示結果(含圖)
        return/print:
            與原圖差距:與色塊平均後與原圖差距(含雜訊)
            真實差距:與色塊平均後與原圖差距(不含雜訊)
            平均差:真實差距/總像素
            色塊數:分類數量
            平均色塊:分類數量/總像素
        """
        def analysis_main(img, return_mode="return"):
            X = deepcopy(img).reshape(-1,3)
            clustering = DBSCAN(eps=self.eps, min_samples=self.min_samples).fit(X)
            img_out = np.zeros_like(X)
            label = clustering.labels_.tolist()
            all = 0
            for i in range(max(label)):
                r = 0
                g = 0
                b = 0
                for j in range(len(label)):
                    if(i == label[j]):
                        r+=X[j][0]
                        g+=X[j][1]
                        b+=X[j][2]
                c = label.count(i)
                r = r/c
                g = g/c
                b = b/c
                for j in range(len(label)):
                    if(i == label[j]):
                        all += abs(img_out[j][0]-r)+abs(img_out[j][1]-g)+abs(img_out[j][2]-b)
                        img_out[j][0] = r
                        img_out[j][1] = g
                        img_out[j][2] = b
            if(return_mode == "return"):
                return np.sum(img_out.reshape(img.shape)-img)/(len(label)-label.count(-1)),\
                       all,\
                       all/(len(label)-label.count(-1)),\
                       max(label),\
                       max(label)/(len(label)-label.count(-1))
            elif(return_mode == "show"):
                plt.subplot(221)
                plt.imshow(img)
                plt.subplot(222)
                plt.imshow(img_out.reshape(img.shape))
                plt.show()
                print("與原圖差距:",np.sum(img_out.reshape(img.shape)-img)/len(label))
                print("真實差距:",all)
                print("平均差:",all/(len(label)-label.count(-1)))
                print("色塊數",max(label))
                print("平均色塊:",max(label)/(len(label)-label.count(-1)))

        if(self.tag == "one"):
            if(return_mode == "return"):
                return analysis_main(self.img, return_mode)
            else:
                return analysis_main(self.img, return_mode)
        elif(self.tag == "folder"):
            if(return_mode == "return"):
                out = []
                for i in self.img_data:
                    out.append(analysis_main(i, return_mode))
                return out
            else:
                for i in self.img_data:
                    analysis_main(i, return_mode)
        else:
            print("no img")
        
    def appraisal(self,model_link="./pic_model.h5"):
        """
        input:
            model_link : 模組位置
        return:
            判斷結果(S,A,B,C)
        """
        ANS_list = ["S","A","B","C"]
        
        inp = tf.keras.Input((64,64,3))
        x = tf.keras.layers.Conv2D(64,(3,3),padding='SAME',use_bias=False)(inp)
        x = tf.keras.layers.Conv2D(64,(3,3),padding='SAME',use_bias=False)(x)
        x = tf.keras.layers.Conv2D(64,(3,3),padding='SAME',use_bias=False)(x)
        x = tf.nn.relu(x)
        x = tf.nn.dropout(x,0.3)
        xb = tf.keras.layers.Conv2D(64,(3,3),padding='SAME',use_bias=False)(inp)
        xb = tf.keras.layers.Conv2D(64,(3,3),padding='SAME',use_bias=False)(xb)
        xb = tf.nn.dropout(xb,0.3)
        xh = tf.keras.layers.Conv2D(64,(1,1),padding='SAME',use_bias=False)(inp)
        x = x + xh + xb
        x1 = tf.keras.layers.MaxPool2D()(x)

        x = tf.keras.layers.Conv2D(128,(3,3),padding='SAME',use_bias=False)(x1)
        x = tf.keras.layers.Conv2D(128,(3,3),padding='SAME',use_bias=False)(x)
        x = tf.keras.layers.Conv2D(128,(3,3),padding='SAME',use_bias=False)(x)
        x = tf.nn.relu(x)
        x = tf.nn.dropout(x,0.3)
        xb = tf.keras.layers.Conv2D(128,(3,3),padding='SAME',use_bias=False)(x1)
        xb = tf.keras.layers.Conv2D(128,(3,3),padding='SAME',use_bias=False)(xb)
        xb = tf.nn.dropout(xb,0.3)
        xh = tf.keras.layers.Conv2D(128,(1,1),padding='SAME',use_bias=False)(x1)
        x = x + xh + xb
        x2 = tf.keras.layers.MaxPool2D()(x)

        x = tf.keras.layers.Conv2D(256,(3,3),padding='SAME',use_bias=False)(x2)
        x = tf.keras.layers.Conv2D(256,(3,3),padding='SAME',use_bias=False)(x)
        x = tf.keras.layers.Conv2D(256,(3,3),padding='SAME',use_bias=False)(x)
        x = tf.nn.relu(x)
        x = tf.nn.dropout(x,0.3)
        xb = tf.keras.layers.Conv2D(256,(3,3),padding='SAME',use_bias=False)(x2)
        xb = tf.keras.layers.Conv2D(256,(3,3),padding='SAME',use_bias=False)(xb)
        xb = tf.nn.dropout(xb,0.3)
        xh = tf.keras.layers.Conv2D(256,(1,1),padding='SAME',use_bias=False)(x2)
        x = x + xh + xb

        x = tf.keras.layers.Flatten()(x)
        x = tf.keras.layers.Dense(4096)(x)
        x = tf.nn.dropout(x,0.3)
        x = tf.nn.relu(x)
        x = tf.keras.layers.Dense(2048)(x)
        x = tf.nn.dropout(x,0.3)
        x = tf.nn.relu(x)
        x = tf.keras.layers.Dense(2048,kernel_regularizer=tf.keras.regularizers.l1(0.))(x)
        x = tf.keras.layers.Dense(4)(x)
        out = tf.nn.softmax(x)
        model = tf.keras.Model(inputs=[inp],outputs=[out])
        model.load_weights(model_link,by_name=True)
        
        if(self.tag == "one"):
            img = cv2.resize(self.img, (64, 64), interpolation=cv2.INTER_AREA)
            return ANS_list[np.argmax(model(img.reshape(1,64,64,3),training=False))]
        elif(self.tag == "folder"):
            img_inp = np.zeros((self.img_data.shape[0],64,64,3))
            for i in range(self.img_data.shape[0]):
                img_i = cv2.resize(self.img_data[i], (64, 64), interpolation=cv2.INTER_AREA)
                img_inp[i] = img_i
            return np.choose(np.argmax(model(img_inp,training=False),axis=-1), ANS_list)
        else:
            print("no img")