from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
import selenium.webdriver.support.ui as ui

# dr = webdriver.Chrome()             #打开浏览器
# dr.get('https://www.baidu.com') #请求网址
# sleep(2)     #休眠两秒
# #获取网站的标题    #做断言使用：某个网站的标题是否符合预期结果
# print(dr.
# title)
#
# #获取网站的网址
# print(dr.current_url)
#
# #设置浏览器的大小:为了保证测试用例都在同一环境下测试
# dr.set_window_size(400,400)
#
# #设置浏览器打开后的位置：:为了保证测试用例都在同一环境下测试
# dr.set_window_position(500,500)
# sleep(5)
#
# dr.quit()    #关闭浏览器
#
# dr.maximize_window()  #浏览器最大化
# dr.minimize_window()  #浏览器最小化
#
# #浏览器的前进和后退
# dr.get('http://www.jd.com')
# sleep(4)
# dr.back()
# sleep(4)
# dr.forward()
#
#
# #selenium定位方法：1，id属性：webdriver模拟人的行为
# #通过id属性定位（括号里写id属性的值）
# dr.find_element_by_id('kw').send_keys('大猪蹄子')  #定位到id=kw的位置   1、输入：send_keys
# sleep(3)
# dr.find_element_by_id('su').click()     #2、点击：click
# sleep(3)



#2、class name
# dr.find_element_by_class_name('s_ipt').send_keys('大猪蹄子')
# sleep(3)
# dr.find_element_by_class_name('bg s_btn btnhover').click()


#3、name
# dr.find_element_by_name('wd').send_keys('大猪蹄子')
# sleep(3)
# dr.find_element_by_id('su').click()

# dr.find_element_by_name('tj_trnews').click()


#4、link text:通过文本来定位(只能找呈现在网页上的超文本来定位而且是唯一的超文本，不包括下拉的文本）网页的部分定位
# dr = webdriver.Chrome()
# dr.get('http://www.moore.ren/')
# sleep(3)
# dr.find_element_by_link_text('企业').click()
#
# dr.find_element_by_link_text('登录').click()





#5、partial link text：通过超文本来定位（模糊文本来匹配）可以摘取文本的一部分就可以匹配到，并且要保证唯一性
# dr = webdriver.Chrome()
# dr.get('http://www.moore.ren/')
# sleep(3)
# dr.find_element_by_partial_link_text('登').click()

#6、tag name：通过标签的名称去定位，通常用于多个元素的定位
# dr = webdriver.Chrome()
# dr.get('http://www.moore.ren/')
# sleep(3)
# dr.find_element_by_tag_name('').click()



#7、xpath:路径标记语言，去xml（可扩展标记语言）找资源的。包括绝对路径和相对路径
#xml：可扩展标记语言，跟HTML内容一样但是功能不一样。xml是传输和存储数据的
# dr = webdriver.Chrome()
# dr.get('http://www.moore.ren/')
# sleep(3)
# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
#
# dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/dl/dd[1]/a').click()


#8、css selector:层叠样式表

# dr = webdriver.Chrome()
# dr.get('http://www.moore.ren/')
# sleep(3)
# dr.find_element_by_css_selector('#user-nomal > div.login-wrap > div.before-login > li.no-login').click()




#二、定位多个元素（一组）
#1、定位多个class属性值的元素
# dr = webdriver.Chrome()
# dr.get('http://www.moore.ren/')
# sleep(3)
# wd = dr.find_elements_by_class_name('menu-box')     #wd的数据类型为列表
# for i in wd:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)


# dr = webdriver.Chrome()
# dr.get('https://www.jd.com/?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=32277499332_0_bf70ae8472334b7d9c39e5127c9fe2ef')
# sleep(3)
# wd = dr.find_elements_by_class_name('cate_menu_item')     #wd的数据类型为列表
# for i in wd:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)


#2、层级定位:可以多层定位

# dr = webdriver.Chrome()
# dr.get('https://www.jd.com')
# sleep(3)
# wd = dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_tag_name('li')     #wd的数据类型为列表
# # print(len(wd))
# for i in wd:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)


#3、获取某个属性的值
# dr = webdriver.Chrome()
# dr.get('http://www.moore.ren/')
# sleep(3)
# wd = dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a')
# print(wd.get_attribute('rel'))         #获取元素的某个属性的值


# dr = webdriver.Chrome()
# dr.get('http://www.moore.ren/')
# sleep(3)
# wd = dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').text
# print(wd)





#防火墙的自动登录
# dr = webdriver.Chrome()
# dr.get('http://192.168.0.254')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').clear()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').send_keys('administrator')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# sleep(2)
# b = dr.find_element_by_xpath('//*[@id="checkinfo"]').find_elements_by_class_name('nobody')
# for i in b:
#     c = i.get_attribute('src')
#     dr.find_element_by_xpath('//*[@id="input1"]').send_keys(c[-5])
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()



#携程定位酒店级别
# dr = webdriver.Chrome()
# dr.get('http://www.ctrip.com')
# wd = dr.find_element_by_xpath('//*[@id="searchHotelLevelSelect"]').click()
# sleep(2)





















#切换窗口(句柄)
# dr=webdriver.Chrome()
# dr.get('http://www.moore.ren/')
# sleep(2)
# print(dr.current_window_handle)            #获取当前窗口的句柄
# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
# sleep(2)
# print(dr.title)
# wd = dr.window_handles    #获取所有窗口句柄(结果为列表)
#
# dr.switch_to.window(wd[1])    #根据句柄切换窗口
# print(dr.title)
#
#
# dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('15638469151')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('zzzz25210')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
# dr.switch_to_window(wd[0])
# print(dr.title)







#框架：镶嵌在web上的一个窗口
#切换框架
# dr=webdriver.Chrome()
# dr.get('https://i.qq.com/?rd=1')
# sleep(2)
# # dr.switch_to.frame('login_frame')       #切换到内嵌框架中，但只能根据id属性值或name属性的值或者定位到框架上来切换
# # dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# # dr.find_element_by_xpath('//*[@id="u"]').send_keys('1874694392')
# # dr.find_element_by_xpath('//*[@id="p"]').send_keys('zzzz25210')
# # dr.find_element_by_xpath('//*[@id="login_button"]').click()
#
# wd = dr.find_element_by_xpath('//*[@id="login_frame"]')
# dr.switch_to.frame(wd)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('1874694392')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('zzzz25210')
# sleep(2)
# # dr.find_element_by_xpath('//*[@id="login_button"]').click()
#
#
#
# dr.switch_to.default_content()     #退出到原始页面
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# dr.switch_to.parent_frame()         #切换到上一层框架













#弹出框（alert）
# dr = webdriver.Chrome()
# dr.get('http://192.168.0.254')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').clear()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').send_keys('administrator')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# sleep(2)
# b = dr.find_element_by_xpath('//*[@id="checkinfo"]').find_elements_by_class_name('nobody')
# for i in b:
#     c = i.get_attribute('src')
#     dr.find_element_by_xpath('//*[@id="input1"]').send_keys(c[-5])
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# sleep(2)
# wd = dr.switch_to_alert()         #切换到弹出框
# sleep(2)
# print(wd.text)                    #获取弹出框上的文本
# sleep(2)
# wd.accept()            #点击确定
# wd.dismiss()           #点击取消
# wd.send_keys()         #像弹出框输入内容







#喔图云摄影
# dr = webdriver.Chrome()
# dr.get('http://www.alltuu.com/v')
# dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[1]/div/ul/li[6]/div/div/div/a[1]').click()
# sleep(1)
#
# dr.find_element_by_xpath('//*[@id="loginUsername"]').send_keys('15638469151')
# sleep(1)
# wd = dr.find_element_by_class_name('eui_emailsuggest').find_elements_by_tag_name('li')
# for i in wd:
#     if '15638469151' in i.text:
#         i.click()
#
# dr.find_element_by_xpath('//*[@id="loginPassword"]').send_keys('zzzz25210')
# dr.find_element_by_xpath('//*[@id="login"]').click()







#防火墙
# dr = webdriver.Chrome()
# dr.get('http://192.168.0.254/')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# sleep(2)
# wd = dr.find_element_by_xpath('//*[@id="checkinfo"]').find_elements_by_class_name('nobody')
# sleep(2)
# for i in wd:
#     c = i.get_attribute('src')
#     dr.find_element_by_xpath('//*[@id="input1"]').send_keys(c[-5])
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# sleep(2)
# wd1 = dr.switch_to_alert()
# wd1.accept()
#
# sleep(10)
# dr.switch_to.frame('left')
# dr.find_element_by_xpath('//*[@id="04"]/span[2]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="041"]/span').click()
# dr.switch_to.default_content()
#
# dr.switch_to.frame('mainFrame')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="content"]/form[2]/table/tbody/tr/td[2]/div/div/a').click()
# sleep(2)
# # dr.switch_to.default_content()
# #
# # dr.switch_to.frame('mainFrame')
# dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div[1]/a').click()








# dr = webdriver.Chrome()
# dr.get('http://www.alltuu.com/v')
# dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[1]/div/ul/li[6]/div/div/div/a[1]').click()
# sleep(1)
#
# dr.find_element_by_xpath('//*[@id="loginUsername"]').send_keys('15638469151')
# sleep(1)
# wd = dr.find_element_by_class_name('eui_emailsuggest').find_elements_by_tag_name('li')
# for i in wd:
#     if '15638469151' in i.text:
#         i.click()
# dr.find_element_by_xpath('//*[@id="loginPassword"]').send_keys('zzzz25210')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login"]').click()
# sleep(2)

#下拉页面
#1、根据页面的高度来移动的滚动条
# 移动滚动条:属于浏览器的，不属于当前访问页面的（属于JavaScript语言的滚动条的功能的脚本）
# js = "var q=document.documentElement.scrollTop=10000"   #控制滚动条的JavaScript代码       10000表示的是：页面的高度，数字越大，滚动条越往下
# dr.execute_script(js)           #执行JavaScript语句     并把滚动条从最顶部滚到最底部
# sleep(2)


# 2、根据定位的元素来移动滚动条

# wd = dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[2]/div[4]/div/div[1]/p[1]')
#
# js = "arguments[0].scrollIntoView()"            #JavaScript代码
#
# dr.execute_script(js,wd)



#3、拖拉
# from selenium.webdriver.common.action_chains import  ActionChains（动作链）
# dr=webdriver.Chrome()
# dr.get('https://i.qq.com/?rd=1')
# sleep(2)
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('1101303023')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('zzzz25210')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# wd1 = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
# dr.switch_to_frame(wd1)
# sleep(2)
# start = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
# sleep(2)
# ActionChains(dr).drag_and_drop_by_offset(start,191,0).perform()
# sleep(5)

#ActionChains(dr).drag_and_drop_by_offset(start,191,0)  命令
#perform()      执行





#4、设置控制器等待
#强制等待
# sleep(2)


#智能等待

dr = webdriver.Chrome()
dr.get('http://www.moore.ren/')
# until = ui.WebDriverWait(dr,10)
# until.until(lambda dr:dr.find_element_by_xpath('//*[@id="kw"]').is_displayed())
# dr.quit()


#.is_displayed() 判断元素是否显示在屏幕上，结果为布尔值
#.is_enabled()   判断是否为灰化状态，结果为布尔值（true、false）

# u = until.until(lambda dr:dr.find_element_by_xpath('//*[@id="user-nomal"]/div[1]/a/img').is_displayed())
# print(u)

#5、截图功能
# dr.get_screenshot_as_png()   #截图
# dr.save_screenshot('jietu.png')  #保存

dr.get_screenshot_as_file('jiet.png')
