import numpy as np
from PIL import Image
from wordcloud import WordCloud
import  matplotlib.pyplot as plt
import random


# 打开存放项目名称的txt文件
with open('web.txt','r') as f:
    word= (f.read())
    f.close()

# 图片模板和字体
image=np.array(Image.open('firstname.png'))


# 关键一步
my_wordcloud = WordCloud(mask=image,background_color='white',
                         max_words = 100,max_font_size = 40).generate(word)

#显示生成的词云
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()

#保存生成的图片
my_wordcloud.to_file('result.jpg')