# -*- coding: utf-8 -*-
import urllib
import re
import os

baseUrl = 'http://res.wx.qq.com/voice/getvoice?mediaid='
status = 0
print 'Specification'
print u'说明书：'
print "This feature is limited to the daily poetry of the Emanna public number."
print u'该程序仅限于Emanna公共号码的日常诗歌。'
print "Please open the poem interface in WeChat, click the copy link address, and then paste the address below to enter."
print u'请打开Emanna诗歌界面，点击右上角复制链接地址，然后粘贴地址到程序里面按回车。'
print 'Paste it in the program instead of pressing Ctrl + C, click on the icon in the upper-left corner of the box, and select edit - > paste.'
print u'粘贴到程序里是不要按Ctrl+C，点击程序框左上角图标，选择编辑—>粘贴'
print "If you want to exit, please enter 'exit' manually."
print u'如果您想退出，请手动输入“exit”。'

def downloadHymns(a):
    print ' '
    if a == 0:
        print u'请粘贴你复制诗歌的链接'
    elif a == 1:
        print u'请继续粘贴你复制诗歌的链接'
    elif a == 2:
        print u'请确认诗歌链接后再复制粘贴'
    htmlUrl = raw_input("Please paste the poem's website: ")
    try:
        if htmlUrl == "exit":
            os._exit(0)
            return
        if not os.path.exists('D:/Music'):
            os.mkdir('D:/Music')
        htmlDom = urllib.urlopen(htmlUrl).read()
        reg = r'voice_encode_fileid="(.*)" play_length'
        regTitle = r'<title>(.*)</title>'
        urlRe = re.compile(reg)
        urlReTitle = re.compile(regTitle)
        urlList = re.findall(urlRe, htmlDom)
        urlTitle = re.findall(urlReTitle, htmlDom)
        print baseUrl + urlList[0]
        print urlTitle[0]
        urllib.urlretrieve(baseUrl + urlList[0], 'D://Music//' + urlTitle[0].decode('utf-8') + '.mp3')
        status = 1
        print "Download successfully, the download file in D:/Music folder."
    except:
        print "Copy url error, please copy again and paste it."
        status = 2
    downloadHymns(status)

downloadHymns(status)
