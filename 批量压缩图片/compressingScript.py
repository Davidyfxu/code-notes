# -*- coding: utf-8 -*-
""" 
__author__= 'Du' 
__creation_time__= '2018/1/5 10:06' 
"""

import os
from PIL import Image
import glob

DIR = r'./'


class Compress_Picture(object):
    def __init__(self):
        # 图片格式，可以换成.bpm等
        self.file = '.jpg'

    # 图片压缩批处理
    def compressImage(self):
        for filename in glob.glob('%s%s%s' % (DIR, '*', self.file)):
            # print(filename)
            # 打开原图片压缩
            sImg = Image.open(filename)
            w, h = sImg.size
            print(w, h)
            # 设置压缩尺寸和选项，注意尺寸要用括号
            dImg = sImg.resize((w//2, h//2), Image.ANTIALIAS)

            # 如果不存在目的目录则创建一个
            comdic = "%scompress/" % DIR
            if not os.path.exists(comdic):
                os.makedirs(comdic)

            # 压缩图片路径名称
            f1 = filename.split('/')
            f1 = f1[-1].split('\\')
            f2 = f1[-1].split('.')
            f2 = '%s%s1%s' % (comdic, f2[0], self.file)
            # print(f2)
            dImg.save(f2)  # save这个函数后面可以加压缩编码选项JPEG之类的
            print("%s compressed succeeded" % f1[-1])


if __name__ == "__main__":
    obj = Compress_Picture()
    obj.compressImage()
