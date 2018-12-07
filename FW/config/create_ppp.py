#!/user/bin/python
#-*- coding:utf-8 -*-
#Author:一土小亘兄
#@Time: 14:21

from selenium import webdriver
import time,re,unittest,paramiko

def create_new(dr,row):
    data=read.create(row)
    dr = login.qhppp(dr)
    dr.find_element_by_xpath('/html/body/table[3]/tbody/tr/td/div/div/a').click()
    windows = dr.window_handles
    dr.switch_to.window(windows[1])
    time.sleep(1)
    if data[1]=='空':
        pass
    else:
        dr.find_element_by_id('com_phy_netiftxt').click()
        msg = dr.find_element_by_id('combo_list').find_elements_by_tag_name('td')
        for i in msg:
            if i.get_attribute(
                    'onclick') == f"com_phy_netif.choose('{data[1]}','{data[1]}',event);com_phy_netif.opslist.style.display='none';":  ####点击eth3
                i.click()
                break
    likename = dr.find_element_by_xpath(
        '/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/input')
    number = likename.get_attribute('value')
    num = str(int(number[-1]) + 1)  #######获取pppoe接口号
    print(num)
    dr.find_element_by_xpath(
        '/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[5]/td[2]/table/tbody/tr/td[2]/input').send_keys(
        f'{data[2]}')  ##输入用户名
    time.sleep(1)
    dr.find_element_by_xpath(
        '/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/table/tbody/tr/td[2]/input').send_keys(
        f'{data[3]}')  ##输入密码
    dr.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]/input').send_keys(f'{data[4]}')
    time.sleep(1)
    dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div[1]/a').click()
    time.sleep(3)
    # dr.switch_to.window(windows[0])  ##切换到原始窗口
    # dr.switch_to.frame('main')  ####记录列表框架
    # time.sleep(1)
    # dr.find_element_by_xpath(f'/html/body/table[2]/tbody/tr[{num}]/td[5]/div[1]/a/img').click()
    return num


def find_port(dr,row):
    data = read.create(row)
    dr = login.qhppp(dr)
    dr.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/a').click()  ####点击查询
    # allwindows=dr.window_handles
    if data[1]=='空':
        pass
    else:
        time.sleep(0.5)####输入名称
        dr.find_element_by_xpath(
        '/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/input').send_keys(f'{data[1]}')
    if data[2]=='空':
        pass
    else:
        time.sleep(0.5)####输入ip地址
        dr.find_element_by_xpath(
        '/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]/input').send_keys(f'{data[2]}')
    if data[3]=='空':
        pass
    else:
        time.sleep(0.5)####输入掩码
        dr.find_element_by_xpath(
        '/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/table/tbody/tr/td[2]/input').send_keys(f'{data[3]}')
    if data[4]=='空':
        pass
    else:
        time.sleep(0.5)#####选择工作模式
        dr.find_element_by_xpath('//*[@id="com_workmode"]/input[3]').click()
        modo = dr.find_element_by_id('combo_list').find_elements_by_tag_name('td')
        for i in modo:
            print(i.get_attribute('onclick'))
            if i.get_attribute(
                    f'onclick') == "com_workmode.choose('1','{data[4]}',event);com_workmode.opslist.style.display='none';":
                i.click()

    time.sleep(1)
    dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div/a').click() ###点击确认
    time.sleep(1)
    return data[5]




#####查找功能数据为真时
def find_true(dr,row):
    data = read.create(row)
    dr = login.qhppp(dr)
    jkname = dr.find_elements_by_class_name('TableTdBg_date')
    yi = []
    # print(len(jkname))
    for l in jkname:
        a = l.find_elements_by_tag_name('td')
        b = []
        for e in a:
            try:
                b.append(e.text)
            except:
                pass
        yi.append(b)
    # print(yi)
    dr.find_element_by_xpath('/html/body/table[1]/tbody/tr/td/a').click()  ####点击查询
    # allwindows=dr.window_handles
    if data[1]=='空':
        pass
    else:
        time.sleep(0.5)####输入名称
        dr.find_element_by_xpath(
        '/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/input').send_keys(f'{data[1]}')
    if data[2]=='空':
        pass
    else:
        time.sleep(0.5)####输入ip地址
        dr.find_element_by_xpath(
        '/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]/input').send_keys(f'{data[2]}')
    if data[3]=='空':
        pass
    else:
        time.sleep(0.5)####输入掩码
        dr.find_element_by_xpath(
        '/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/table/tbody/tr/td[2]/input').send_keys(f'{data[3]}')
    if data[4]=='空':
        pass
    else:
        time.sleep(0.5)#####选择工作模式
        dr.find_element_by_xpath('//*[@id="com_workmode"]/input[3]').click()
        modo = dr.find_element_by_id('combo_list').find_elements_by_tag_name('td')
        for i in modo:
            print(i.get_attribute('onclick'))
            if i.get_attribute(
                    f'onclick') == "com_workmode.choose('1','{data[4]}',event);com_workmode.opslist.style.display='none';":
                i.click()
    time.sleep(1)
    dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div/a').click() ###点击确认
    time.sleep(1)
    jkname = dr.find_elements_by_class_name('TableTdBg_date')
    er = []
    # print(len(jkname))
    for j in jkname:
        a = j.find_elements_by_tag_name('td')
        b = []
        for h in a:
            try:
                b.append(h.text)
            except:
                pass
        er.append(b)
    # print(er)
    return yi,er

