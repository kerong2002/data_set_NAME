from torch.utils.data import Dataset    ##torch常用工具中引入Dataset
from PIL import Image   ##讀取圖片
import os   ##處理相關路徑的庫

class MyData(Dataset):  ##創建一個MyData繼承Dataset

    def __init__(self,root_dir,label_dir): ##初始化(包含全局變量)
        self.root_dir = root_dir    ##self使變量可以互相使用-全局變量
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir,self.label_dir)   ##利用join將兩個函數路徑相加
        self.img_path = os.listdir(self.path)   ##獲得所有圖片的一個列表
    def __getitem__(self,idx): ##索引數據
        img_name = self.img_path[idx]   ##讀去一個對應名稱
        img_item_path = os.path.join(self.root_dir,self.label_dir,img_name) #圖片檔案位置
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label
    def __len__(self):  #列表長度
        return len(self.img_path)


root_dir = "dataset/train"
ants_label_dir = "ants"
bees_label_dir = "bees"
ants_dataset = MyData(root_dir,ants_label_dir)  #螞蟻數據集
bees_dataset = MyData(root_dir,bees_label_dir)  #蜜蜂數據集
train_dataset = ants_dataset + bees_dataset