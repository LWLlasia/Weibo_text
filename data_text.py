# -*- coding: utf-8 -*-
import re
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



content = open("./content_01.html", "r").read()

html = etree.HTML(content)



def match_WB_name(ori_str):
    name = ori_str.xpath('div[@class="WB_info"]/a[1]/text()')
    return name

def match_WB_TIME(ori_str):
    time = ori_str.xpath('div[@class="WB_from S_txt2"]/a[1]/text()')
    return time

def match_WB_source(ori_str):
    source = ori_str.xpath('div[@class="WB_from S_txt2"]/a[2]/text()')
    return source

def match_WB_comment(ori_str):
    # re_str = r'<div class>="WB_text W_f14" node-type="feed_list_content">(.*?)<img class="W_img_face".*?title="(.*?)".*?>(.*?)<a target="_blank" render="ext" suda-uatrack=".*?>(.*?)</a>'

    comment = ori_str.xpath('div[@class="WB_text W_f14"]/text()')

    # info =ori_str.xpath('div[@class="WB_text W_f14"]')
    # info_1 = info[0].xpath('string(.)').strip()
    # comment = "".join([each.strip() for each in info_1])
    # print comment


    return comment


def match_WB_man(ori_str):
    man = ori_str.xpath('div[@node-type="feed_list_content"]/a/text()')
    return man

def match_WB_img(ori_str):
    img = ori_str.xpath('div[@class="WB_text W_f14"]/img/@title')
    return img

def match_WB_if_like(ori_str):
    id = ori_str.xpath('//div[@layout-shell="false"]/div/p/img/@alt')
    return id


'''====================================================='''







def data_WB_write():
    i = 0
    id = match_WB_if_like(html)
    for e in html.xpath('//div[@node-type="feed_list"]//div[@node-type="feed_content"]/div[@class="WB_detail"]'):
        name = match_WB_name(e)
        time = match_WB_TIME(e)
        source = match_WB_source(e)
        comment = match_WB_comment(e)
        man = match_WB_man(e)
        img = match_WB_img(e)

        if len(comment) > 0:
            i = i+1
            print i
            if id == name[0]:
                print 'data'
            else :
                print 'like'

            print name[0]

            if len(time) < 1:
                print 'null'
            else:
                print time[0]
            if len(source) < 1:
                print 'null'
            else:
                print source[0]
            for a in range(len(comment)):
                print comment[a].replace('\n', '').replace('\t', '').replace(' ', '')
            # print comment
            if len(img) < 1:
                print 'img : null'
            else:
                print "/".join(img)
            if len(man) < 1:
                print 'null'
            else:
                print "/".join(man)

            print "==================================================="
        else :
            continue

data_WB_write()









