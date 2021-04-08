# -*- coding: utf-8 -*-
"""
Created on Thu April 8 20:30:10 2021
@author: WU-JL
"""

import os
import json
import cv2
import codecs
try: 
  import xml.etree.cElementTree as ET 
except ImportError: 
  import xml.etree.ElementTree as ET 

def json_to_xml(image_path,json_path,save_path):
    if not os.path.exists(save_path):
        os.mkdir(save_path)

    data = json.load(open(json_path))
    for key in data:
        img = cv2.imread(image_path+key)
        img_width=img.shape[1]
        img_height=img.shape[0]
        img_depth=img.shape[2]
        label = data[key]['label']
        left = data[key]['left']
        top = data[key]['top']
        height = data[key]['height']
        width = data[key]['width']
        with codecs.open(save_path + key[0:-4] + '.xml', 'w', 'utf-8') as xml:
            xml.write('\n')
            xml.write('<annotation>')
            xml.write('\t<folder>' + "Annotation" + '</folder>\n')
            xml.write('\t<filename>' + key + '</filename>\n')
            xml.write('\t<path>')
            xml.write('path not record')
            xml.write('\t</path>')
            xml.write('\t<source>\n')
            xml.write('\t\t<database>' + 'Unknown' + '</database>\n')
            xml.write('\t</source>')
            xml.write('\t<size>\n')
            xml.write('\t\t<width>' + str(img_width) + '</width>\n')
            xml.write('\t\t<height>' + str(img_height) + '</height>\n')
            xml.write('\t\t<depth>' + str(img_depth) + '</depth>\n')
            xml.write('\t</size>\n')
            xml.write('\t\t<segmented>0</segmented>\n')
            for i in range(len(label)):
                xmin = str(left[i])
                ymin = str(top[i])
                xmax = str(left[i] + width[i])
                ymax = str(top[i] + height[i])
                label_obj= str(label[i])
                xml.write('\t<object>\n')
                xml.write('\t\t<name>' + label_obj+ '</name>\n')
                xml.write('\t\t<pose>Unspecified</pose>\n')
                xml.write('\t\t<truncated>0</truncated>\n')
                xml.write('\t\t<difficult>0</difficult>\n')
                xml.write('\t\t<bndbox>\n')
                xml.write('\t\t\t<xmin>' + xmin + '</xmin>\n')
                xml.write('\t\t\t<ymin>' + ymin + '</ymin>\n')
                xml.write('\t\t\t<xmax>' + xmax + '</xmax>\n')
                xml.write('\t\t\t<ymax>' + ymax + '</ymax>\n')
                xml.write('\t\t</bndbox>\n')
                xml.write('\t</object>\n')
            xml.write('</annotation>')
            xml.close()
    print('json->xml  Done.')
# json_to_xml('./train_images/','./mchar_train.json','./train_xml/')
json_to_xml('images_path','./.json  path','save_xml_path')







