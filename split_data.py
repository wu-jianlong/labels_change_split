import os
import random
import shutil
from os import listdir, getcwd

def split(trainval_percent=0.1,train_percent = 0.9,xml_file_path='xml' ,txt_save_path='ImageSets'):
    total_xml = os.listdir(xml_file_path)
    num = len(total_xml)
    list = range(num)
    tv = int(num * trainval_percent)
    tr = int(tv * train_percent)
    trainval = random.sample(list, tv) #从所有list中返回tv个数量的项目
    train = random.sample(trainval, tr)
    if not os.path.exists(txt_save_path):
        os.makedirs(txt_save_path)
    ftrainval = open(txt_save_path+'/trainval.txt', 'w')
    ftest = open(txt_save_path+'/test.txt', 'w')
    ftrain = open(txt_save_path+'/train.txt', 'w')
    fval = open(txt_save_path+'/val.txt', 'w')
    for i in list:
        name = total_xml[i][:-4] + '\n'
        if i in trainval:
            ftrainval.write(name)
            if i in train:
                ftest.write(name)
            else:
                fval.write(name)
        else:
            ftrain.write(name)
    ftrainval.close()
    ftrain.close()
    fval.close()
    ftest.close()

    sets = ['train', 'trainval']
    wd = getcwd()
    print(wd)
    for image_set in sets:
        image_ids = open('ImageSets/%s.txt' % (image_set)).read().strip().split()
        # print(image_ids)
        image_list_file = open('images_%s.txt' % (image_set), 'w')
        labels_list_file = open('labels_%s.txt' % (image_set), 'w')
        for image_id in image_ids:
            image_list_file.write('%s.png\n' % (image_id))
            labels_list_file.write('%s.xml\n' % (image_id))
        image_list_file.close()
        labels_list_file.close()

def copy_file(new_path,path_txt,search_path):#参数1：存放新文件的位置  参数2：为上一步建立好的train,val训练数据的路径txt文件  参数3：为搜索的文件位置
    if not os.path.exists(new_path):
        os.makedirs(new_path)
    with open(path_txt, 'r') as lines:
        filenames_to_copy = set(line.rstrip() for line in lines)
        # print('filenames_to_copy:',filenames_to_copy)
        # print(len(filenames_to_copy))
    for root, _, filenames in os.walk(search_path):
        # print('root',root)
        # print(_)
        # print(filenames)
        for filename in filenames:
            if filename in filenames_to_copy:
                shutil.copy(os.path.join(root, filename), new_path)

if __name__ == '__main__':
    split()
    #按照划分好的训练文件的路径搜索目标，并将其复制到yolo格式下的新路径
    copy_file('./images_data/train/','./images_train.txt','./images')
    copy_file('./images_data/val/','./images_trainval.txt','./images')
    copy_file('./labels_data/train/','./labels_train.txt','./xml')
    copy_file('./labels_data/val/','./labels_trainval.txt','./xml')


