#coding=utf-8
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '10272027'
API_KEY = 'Db0PXoleLRt5GdiZAnOXWphx'
SECRET_KEY = 'FUwa6XFevwSrAVxBlj67oWfCs9IW9TYp'

aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

#读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

#识别本地test.wav文件,
def voiceRecognize():
    a = aipSpeech.asr(get_file_content('test.wav'), 'wav' , 16000 ,{'lan' : 'zh', })#调用百度语音
    if a[u'err_no'] == 0: #没有识别错误
        return a[u'result'][0]
    else:
        print a
    return 1
