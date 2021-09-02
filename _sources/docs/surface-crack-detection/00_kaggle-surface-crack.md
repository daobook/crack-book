# ‎Kaggle 表面裂纹数据

参考：[Surface Crack Detection | Kaggle](https://www.kaggle.com/arunrk7/surface-crack-detection)

## 数据集简介

混凝土表面裂缝是土木结构的主要缺陷。建筑物检测是为了评估建筑物的刚度和抗拉强度。裂缝检测在建筑检测中起着重要作用，发现裂缝并确定建筑健康。

这些数据集包含有裂缝和无裂缝的各种混凝土表面的图像。图像数据被分为阴性（negative，无裂缝）和阳性（positive，有裂缝）两类，分别放在不同的文件夹中进行图像分类。每个类别都有 $20\,000$ 张图像，总共有 $40\,000$ 张 $227 \times 227$ 像素的 RGB 通道图像。该数据集由 458 张高分辨率图像（$4032 \times 3024$ 像素）产生，采用 {cite}`7533052` 提出的方法。高分辨率图像在表面处理和光照条件方面发现有很高的差异性。没有应用随机旋转或翻转或倾斜的数据增强。

该数据集取自 [Mendeley Data - Crack Detection](https://data.mendeley.com/datasets/5y9wdsg2zt/2) 网站，由 Çağlar Fırat Özgenel 贡献。引用自：{cite}`10.22260/ISARC2018/0094` 和 {cite}`10.17632/5y9wdsg2zt.2`。

## 数据集使用

参考：[Kaggle 命令行工具 (xinetzone.github.io)](https://xinetzone.github.io/sanstyle-book/docs/basics/kaggle.html) 配置 Kaggle API 到本地。

可以直接获取 Kaggle 数据的根目录：

```python
def kaggle_root():
    import kaggle
    config_values = kaggle.api.config_values
    root = config_values['path']
    return root
```

如果下载下来的数据是 Zip 文件，可以使用如下类直接读取图片：

```python
from zipfile import ZipFile
from PIL import Image
import numpy as np

class ZipImage:
    def __init__(self, Z):
        '''
        Z: 图片的 ZipFile 对象
        '''
        self.Z = Z
        self.name_bunch = {name: name.split('/')[0] for name in self.Z.namelist()}

    def array(self, name):
        with self.Z.open(name) as fp:
            with Image.open(fp) as im:
                img = np.array(im)
        return img

    def __iter__(self):
        for name, label in self.name_bunch.items():
            img = self.array(name)
            yield img, label
```

下载数据集：

```sh
kaggle datasets download -d arunrk7/surface-crack-detection
```

获取数据集的根目录：

```python
root = kaggle_root() + '/datasets/arunrk7/surface-crack-detection/surface-crack-detection.zip'
```

读取图片：

```python
Z = ZipFile(root)
I = ZipImage(Z)
for img, label in I:
    break
```

这里 `img`，`label` 分别是图片的数据及其标签。