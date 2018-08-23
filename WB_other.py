# -*- coding: utf-8 -*-
import re
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

content = open("./content_40.html", "r").read()
html = etree.HTML(content)


def match_WB_other_name(ori_str):
    name = ori_str.xpath('div[@class="WB_info"]/a/text()')
    return name


def match_WB_other_comment(ori_str):
    info = ori_str.xpath('div[@class="WB_text"]')
    if len(info)>0:
        info_1 = info[0].xpath('string(.)').strip()
        comment = "".join([each.strip() for each in info_1])

        # comment = ori_str.xpath('div[@class="WB_text"]/text()')
        return comment
    else:
        return 0

def match_WB_other_time(ori_str):
    time = ori_str.xpath('div[@class="WB_func clearfix"]/div[@class="WB_from S_txt2"]/a[1]/text()')
    return time


def math_WB_other_source(ori_str):
    source = ori_str.xpath('div[@class="WB_func clearfix"]/div[@class="WB_from S_txt2"]/a[2]/text()')
    return source


def math_WB_other_man(ori_str):
    man = ori_str.xpath('div[@node-type="feed_list_reason"]//a[@extra-data="type=atname"]/text()')
    return man

def match_WB_other_img(ori_str):
    img = ori_str.xpath('div[@class="WB_text"]/img/@title')
    return img


def match_WB_if_like(ori_str):
    id = ori_str.xpath('//div[@layout-shell="false"]/div/p/img/@alt')
    return id


'''成功'''
# name = match_WB_other_name(html)
# for i in range(len(name)):
#     print name[i]

# comment = match_WB_other_comment(html)
# for i in range(len(comment)):
#     print comment[i].replace('\n', '').replace('\t', '').replace(' ', '')

#
# time = match_WB_other_time(html)
# for i in range(len(time)):
#     print time[i]

# source = math_WB_other_source(html)
# for i in range(len(source)):
#     print source[i]

#
# man = math_WB_other_man(html)
# for i in range(len(man)):
#     print man[i]


for e in html.xpath('//div[@node-type="feed_content"]/div[@class="WB_detail"]/div[@class="WB_feed_expand"]/div[@node-type="feed_list_forwardContent"]'):
    name = match_WB_other_name(e)
    comment = match_WB_other_comment(e)
    source = math_WB_other_source(e)
    time = match_WB_other_time(e)
    man = math_WB_other_man(e)
    img = match_WB_other_img(e)
    fs = open("./data/WB_data_other_40.txt", "a+")
    id = match_WB_if_like(html)
    if comment==0:
        continue
    else:
        # fs.write('<id>'+id[0]+'</id>'+'\n')
        #
        # fs.write("<repost_list>" + '\n')
        # fs.write("<repost>" + '\n')
        print comment
        # fs.write("<repost_weibo>"+comment+"</repost_weibo>" + '\n')

        if len(source) < 1:

                print 'null'

                # fs.write("<repost_origin>"+"</repost_origin>" + '\n')
        else:

                print source[0]

                # fs.write("<repost_origin>" +source[0]+ "</repost_origin>" + '\n')
            # print name[0]
            #     fs.write("<repost_id>" +name[0]+ "</repost_id>" + '\n')
        if len(man) < 1:

                print 'null'
                #
                # fs.write("<repost_@>" + "</repost_@>" + '\n')
        else:

                print man[0]
                #
                # fs.write("<repost_@>" +man[0]+ "</repost_@>" + '\n')
        if len(time) < 1:

                print 'null'
        #
        #         fs.write("<repost_time>" + "</repost_time>" + '\n')
        else:

                print time[0]
                #
                # fs.write("<repost_time>"+time[0] + "</repost_time>" + '\n')

        if len(img) < 1:

                print 'img : null'

                # fs.write("<repost_emo>"+ "</repost_emo>" + '\n')
        else:

                print img[0]

        #         fs.write("<repost_emo>" +img[0]+ "</repost_emo>" + '\n')
        # fs.write("</repost>"+'\n'+'</repost_list>'+'\n')
        print "==================================================="


