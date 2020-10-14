import cv2
import pytesseract
from PIL import Image

img = Image.open(r"C:\Users\ZKTT\Desktop\example-001\111.png")
text = pytesseract.image_to_string(img, lang='chi_sim')
print(text)

import matplotlib.pyplot as plt
import tensorflow as tf

# 读入二进制文件
image_raw = tf.gfile.FastGFile('test.jpg', 'rb').read()

# 解码为tf中的图像格式
img = tf.image.decode_jpeg(image_raw)  # Tensor

with tf.Session() as sess:
    img_ = img.eval()
    print(img_.shape)

plt.figure(1)
plt.imshow(img_)
plt.show()


def tensorflowMethod():
    image_raw = tf.gfile.FastGFile(r"C:\Users\ZKTT\Desktop\example-001\111.png", 'rb').read()
    img = tf.image.decode_jpeg(image_raw)
    with tf.Session() as sess:
        img_ = img.eval()
        print(img_.shape)


plt.figure()
plt.imshow(img_)
plt.show()

if __name__ == '__main__':
    tensorflowMethod()
