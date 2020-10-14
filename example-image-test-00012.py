import os
import cv2
import matplotlib.pyplot as plt
import numpy as np

"""
  基于RGB空间亮度调整算法：
  主要是对RGB空间进行亮度调整。计算出调整系数后，调整手段主要有两种：
    1) 基于当前RGB值大小进行调整，即R、G、B值越大，调整的越大，
    例如：当前像素点为(100,200,50),调整系数1.1,则调整后为(110,220,55)；
    2) 不考虑RGB值大小的影响，即始终对各个点R、G、B值进行相同的调整，
    例如：当前像素点为(100,200,50),调整系数10/255,则调整后为(110,210,60)。
"""


def RGBAlgorithm(rgb_img, value=-1, basedOnCurrentValue=True):
    img = rgb_img * 2.0
    img_out = img

    # 基于当前RGB进行调整（RGB*alpha）
    if basedOnCurrentValue:
        # 增量大于0，指数调整
        if value >= 0:
            alpha = 1 - value
            alpha = 1 / alpha

        # 增量小于0，线性调整
        else:
            alpha = value + 1

        img_out[:, :, 0] = img[:, :, 0] * alpha
        img_out[:, :, 1] = img[:, :, 1] * alpha
        img_out[:, :, 2] = img[:, :, 2] * alpha

    # 独立于当前RGB进行调整（RGB+alpha*255）
    else:
        alpha = value
        img_out[:, :, 0] = img[:, :, 0] + 255.0 * alpha
        img_out[:, :, 1] = img[:, :, 1] + 255.0 * alpha
        img_out[:, :, 2] = img[:, :, 2] + 255.0 * alpha

    img_out = img_out / 255.0

    # RGB颜色上下限处理(小于0取0，大于1取1)
    mask_3 = img_out < 0
    mask_4 = img_out > 1
    img_out = img_out * (1 - mask_3)
    img_out = img_out * (1 - mask_4) + mask_4

    return img_out


"""
  基于HSV空间亮度调整算法：
  主要是对HSV空间的亮度V值进行调整。计算出调整系数后，调整手段主要有两种：
    1) 基于当前V值大小进行调整，即V值越大，调整的越大，
    例如：当前像素点V值为200,调整系数1.1,则调整后为220；
    2) 不考虑V值大小的影响，即始终对各个V值进行相同的调整，
    例如：当前像素点V值为200,调整系数10/255,则调整后为210。
"""


def HSVAlgorithm(rgb_img, value=0.5, basedOnCurrentValue=True):
    hsv_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2HSV)
    img = hsv_img * 1.2
    img_out = img

    # 基于当前亮度进行调整（V*alpha）
    if basedOnCurrentValue:
        # 增量大于0，指数调整
        if value >= 0:
            alpha = 1 - value
            alpha = 1 / alpha

        # 增量小于0，线性调整
        else:
            alpha = value + 1
        img_out[:, :, 2] = img[:, :, 2] * alpha

    else:
        alpha = value
        img_out[:, :, 2] = img[:, :, 2] + 255.0 * alpha

    # HSV亮度上下限处理(小于0取0，大于1取1)
    img_out = img_out / 255.0
    mask_1 = img_out < 0
    mask_2 = img_out > 1
    img_out = img_out * (1 - mask_1)
    img_out = img_out * (1 - mask_2) + mask_2
    img_out = img_out * 255.0

    # HSV转RGB
    img_out = np.round(img_out).astype(np.uint8)
    img_out = cv2.cvtColor(img_out, cv2.COLOR_HSV2RGB)
    img_out = img_out / 255.0

    return img_out


path = './resource/fruit.bmp'
value = 0.3  # 范围-1至1
basedOnCurrentValue = True  # 0或者1


def read_Image(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        img = cv2.imread(file_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_rgb = RGBAlgorithm(img, value, basedOnCurrentValue)
        img_hsv = HSVAlgorithm(img, value, basedOnCurrentValue)
        plt.figure("img_original")
        plt.imshow(img / 255.0)
        plt.axis('off')

        plt.figure("img_light_rgb")
        plt.imshow(img_rgb)
        plt.axis('off')

        plt.figure("img_light_hsv")
        plt.imshow(img_hsv)
        plt.axis('off')

        plt.show()


# run : python Lightness.py (path) (value) (basedOnCurrentValue)
if __name__ == "__main__":
    path = r'C:\Users\ZKTT\Desktop\python\demo'
    read_Image(path)
