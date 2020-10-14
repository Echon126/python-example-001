import cv2
import math
import numpy as np
import os
import pdb
import xml.etree.ElementTree as ET
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageEnhance

class ImgAugemention():
    def __init__(self):
        self.angle = 90

    # rotate_img
    def rotate_image(self, src, angle, scale=1.):
        w = src.shape[1]
        h = src.shape[0]
        # convet angle into rad
        rangle = np.deg2rad(angle)  # angle in radians
        # calculate new image width and height
        nw = (abs(np.sin(rangle) * h) + abs(np.cos(rangle) * w)) * scale
        nh = (abs(np.cos(rangle) * h) + abs(np.sin(rangle) * w)) * scale
        # ask OpenCV for the rotation matrix
        rot_mat = cv2.getRotationMatrix2D((nw * 0.5, nh * 0.5), angle, scale)
        # calculate the move from the old center to the new center combined
        # with the rotation
        rot_move = np.dot(rot_mat, np.array([(nw - w) * 0.5, (nh - h) * 0.5, 0]))
        # the move only affects the translation, so update the translation
        # part of the transform
        rot_mat[0, 2] += rot_move[0]
        rot_mat[1, 2] += rot_move[1]
        # map
        return cv2.warpAffine(
            src, rot_mat, (int(math.ceil(nw)), int(math.ceil(nh))),
            flags=cv2.INTER_LANCZOS4)

    def rotate_xml(self, src, xmin, ymin, xmax, ymax, angle, scale=1.):
        w = src.shape[1]
        h = src.shape[0]
        rangle = np.deg2rad(angle)  # angle in radians
        # now calculate new image width and height
        # get width and heigh of changed image
        nw = (abs(np.sin(rangle) * h) + abs(np.cos(rangle) * w)) * scale
        nh = (abs(np.cos(rangle) * h) + abs(np.sin(rangle) * w)) * scale
        # ask OpenCV for the rotation matrix
        rot_mat = cv2.getRotationMatrix2D((nw * 0.5, nh * 0.5), angle, scale)
        # calculate the move from the old center to the new center combined
        # with the rotation
        rot_move = np.dot(rot_mat, np.array([(nw - w) * 0.5, (nh - h) * 0.5, 0]))
        # the move only affects the translation, so update the translation
        # part of the transform
        rot_mat[0, 2] += rot_move[0]
        rot_mat[1, 2] += rot_move[1]
        # rot_mat: the final rot matrix
        # get the four center of edges in the initial martix，and convert the coord
        point1 = np.dot(rot_mat, np.array([(xmin + xmax) / 2, ymin, 1]))
        point2 = np.dot(rot_mat, np.array([xmax, (ymin + ymax) / 2, 1]))
        point3 = np.dot(rot_mat, np.array([(xmin + xmax) / 2, ymax, 1]))
        point4 = np.dot(rot_mat, np.array([xmin, (ymin + ymax) / 2, 1]))
        # concat np.array
        concat = np.vstack((point1, point2, point3, point4))
        # change type
        concat = concat.astype(np.int32)
        print(concat)
        rx, ry, rw, rh = cv2.boundingRect(concat)
        return rx, ry, rw, rh

    def process_img(self, imgs_path, xmls_path, img_save_path, xml_save_path, angle_list):
        # assign the rot angles
        for angle in angle_list:
            for img_name in os.listdir(imgs_path):
                # split filename and suffix
                n, s = os.path.splitext(img_name)
                # for the sake of use yolo model, only process '.jpg'
                if s == ".jpg":
                    img_path = os.path.join(imgs_path, img_name)
                    img = cv2.imread(img_path)
                    rotated_img = self.rotate_image(img, angle)
                    save_name = n + "_" + str(angle) + "d.jpg"
                    # 写入图像
                    cv2.imwrite(img_save_path + save_name, rotated_img)
                    print("log: [%sd] %s is processed." % (angle, img))
                    xml_url = img_name.split('.')[0] + '.xml'
                    # xml_path = os.path.join(xmls_path, xml_url)
                    # tree = ET.parse(xml_path)
                    # file_name = tree.find('filename').text  # it is origin name
                    # path = tree.find('path').text  # it is origin path
                    # change name and path
                    # tree.find('filename').text = save_name  # change file name to rot degree name
                    # tree.find('path').text = save_name  # change file path to rot degree name
                    # root = tree.getroot()
                    # for box in root.iter('bndbox'):
                    #     xmin = float(box.find('xmin').text)
                    #     ymin = float(box.find('ymin').text)
                    #     xmax = float(box.find('xmax').text)
                    #     ymax = float(box.find('ymax').text)
                    # x, y, w, h = self.rotate_xml(img, xmin, ymin, xmax, ymax, angle)
                    # change the coord
                    # box.find('xmin').text = str(x)
                    # box.find('ymin').text = str(y)
                    # box.find('xmax').text = str(x+w)
                    # box.find('ymax').text = str(y+h)
                    # box.set('updated', 'yes')
                    # write into new xml
                    # tree.write(xml_save_path + n + "_" + str(angle) + "d.xml")
                print("[%s] %s is processed." % (angle, img_name))

    def qz(self,image_path):
        img = cv2.imread(image_path)

        dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

        plt.subplot(121), plt.imshow(img)
        plt.subplot(122), plt.imshow(dst)
        plt.show()

    def sharpening_processing(self,imagePath):
        # 原始图像
        image = Image.open(imagePath)
        image.show()
        # 亮度增强
        enh_bri = ImageEnhance.Brightness(image)
        brightness = 1.5
        image_brightened = enh_bri.enhance(brightness)
        image_brightened.show()
        # 色度增强
        enh_col = ImageEnhance.Color(image)
        color = 1.5
        image_colored = enh_col.enhance(color)
        image_colored.show()
        # 对比度增强
        enh_con = ImageEnhance.Contrast(image)
        contrast = 1.5
        image_contrasted = enh_con.enhance(contrast)
        image_contrasted.show()
        # 锐度增强
        enh_sha = ImageEnhance.Sharpness(image)
        sharpness = 3.0
        image_sharped = enh_sha.enhance(sharpness)
        image_sharped.show()






if __name__ == '__main__':
    img_aug = ImgAugemention()
    imgs_path = r'C:\Users\ZKTT\Desktop\image\process'
    xmls_path = './xml/'
    img_save_path = r'C:\Users\ZKTT\Desktop\image\process\data/'
    xml_save_path = './xml_rot/'
    angle_list = [60, 90, 120, 150, 210, 240, 300]

    # img_aug.process_img(imgs_path, xmls_path, img_save_path, xml_save_path, angle_list)
    # img_aug.qz(r'C:\Users\ZKTT\Desktop\image\process\f.jpg')
    img_aug.sharpening_processing(r'C:\Users\ZKTT\Desktop\image\process\f.jpg')
