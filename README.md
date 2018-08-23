# Weibo_text
对微博用户页面进行信息获取，并对信息进行整理（微博页面已被保存为ｈｔｍｌ格式，以下各种操作均为对ｈｔｍｌ文件的操作）


            针对用户页面的每一条微博内容：
            
      个人发的微博和其点赞过的微博
      data_text.py:
                        match_WB_name:微博用户的姓名
                        match_WB_TIME：微博发布的时间
                        match_WB_source：发布微博的客户端
                        match_WB_comment：微博的内容
                        match_WB_man：微博所相关的话题或关键字
                        match_WB_img：微博内容里的表情包
                        match_WB_if_like：判断该微博为用户原创还是用户点赞的
                        
       微博用户转发他人微博，针对他人的微博内容获取数据：
       WB_other.py:
       　　　　　　　　　　match_WB_other_nam:微博用户的姓名
                        match_WB_other_comment:微博的内容
                        match_WB_other_time:微博发布的时间
                        math_WB_other_source:发布微博的客户端
                        math_WB_other_man:微博所相关的话题或关键字
                        match_WB_other_img:微博内容里的表情包
