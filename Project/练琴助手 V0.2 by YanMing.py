import threading
import PySimpleGUI as sg
import time
import random
import speak

Break =False
Interval = ['纯一度','小二度','大二度','小三度','大三度','纯四度','减五度','纯五度','小六度','大六度','小七度','大七度','纯八度',]
musical_alphabet= ['C','D','E','F','G','A','B',]
roll_call= ['do','re','mi','fa','sol','la','si']

musical_alphabet_12 = ["C","♭C","D","#E","E","F","♭F","G","♭G","A","#B","B"]
roll_call_12 = ["do","♭do","re","#mi","mi","fa","♭fa","sol","♭sol","la","#si","si"]
num_list = ["1","♭1","2","#3","3","4","♭4","5","♭5","6","#7","7"]

Interval_v=['Pure_first', 'minor_second', 'major_second', 'minor_third', 'major_third', 'pure_fourth', 'minus_fifth', 'pure_fifth', 'minor_sixth' , 'major_sixth','minor_seventh','major_seventh','Pure_Octave',]
roll_call_v= ["1","2","3","4","5","6","7"]
roll_call_12_v = ["1","drop_1","2","Rise_3","3","4","drop_4","5","drop_5","6","Rise_7","7"]
musical_alphabet_v = ['C','D','E','F','G','A','B',]
musical_alphabet_12_v = ["C","drop_C","D","Rise_E","E","F","drop_F","G","drop_G","A","Rise_B","B",]



def time_update(DY,YC):
    while True:
        if DY is True:
            time2 = time.time()
            current_time = time2 - time1
            Time=str(int(current_time // 60 // 60)) + " 时  " + str(int(current_time // 60 % 60)) + " 分  " + str(round(current_time % 60)) + " 秒"
            window['-1计时-'].update(Time)
            time.sleep(0.5)
            if Break == True:
                break
            
                
        
        elif YC is True:
            time2 = time.time()
            current_time = time2 - time1
            Time=str(int(current_time // 60 // 60)) + " 时  " + str(int(current_time // 60 % 60)) + " 分  " + str(round(current_time % 60)) + " 秒"
            window['-2计时-'].update(Time)
            if Break == True:
                break




def DY():
    frequency= float(values['-1频率-'])
    
    if values['-音数-'] =='七音':
        total = 7
        list = [i for i in range(total)]
       
        if values['-1显示名称-'] =='音名':
            while True:
                for num in random.sample(list, total):
                    time.sleep(frequency)
                    window['-1显示-'].update(musical_alphabet[num])
                    if vice == True:    
                        speak.speak(musical_alphabet[num])
                    if Break == True :
                        break
                if Break == True :
                    window['-1显示-'].update('请开始')
                    break

        if values['-1显示名称-'] =='唱名':
            while True:
                for num in random.sample(list, total):
                    time.sleep(frequency)
                    window['-1显示-'].update(roll_call[num])
                    if vice == True: 
                        speak.speak(roll_call_v[num])
                    if Break == True :
                        break
                if Break == True :
                    window['-1显示-'].update('请开始')
                    break


        if values['-1显示名称-'] =='数字':
            while True:
                for num in random.sample(list, total):
                    time.sleep(frequency)
                    num_str=str(num+1)
                    window['-1显示-'].update(num_str)
                    if vice == True: 
                        speak.speak(num_str)
                    if Break == True :
                        break
                if Break == True :
                    window['-1显示-'].update('请开始')
                    break
                    
    elif values['-音数-'] =='十二':
        total = 12
        list = [i for i in range(total)]
        if values['-1显示名称-'] =='音名':
            while True:
                for num in random.sample(list,total):
                    time.sleep(frequency)
                    window['-1显示-'].update(musical_alphabet_12[num])
                    if vice == True: 
                        speak.speak(musical_alphabet_12_v[num])
                    if Break == True :
                        break
                if Break == True :
                    window['-1显示-'].update('请开始')
                    break

        if values['-1显示名称-'] =='唱名':
            while True:
                for num in random.sample(list,total):
                    time.sleep(frequency)
                    window['-1显示-'].update(roll_call_12[num])
                    if vice == True: 
                        speak.speak(roll_call_12_v[num])
                    if Break == True :
                        break
                if Break == True :
                    window['-1显示-'].update('请开始')
                    break


        if values['-1显示名称-'] =='数字':
            while True:
                for num in random.sample(list,total):
                    time.sleep(frequency)
                    
                    window['-1显示-'].update(num_list[num])
                    if vice == True: 
                        speak.speak(roll_call_12_v[num])
                    if Break == True :
                        break
                if Break == True :
                    window['-1显示-'].update('请开始')
                    break
        
    
def YC():
    frequency= float(values['-2频率-'])
    while True:
        total = 12
        list = [i for i in range(total)]

        for num in random.sample(list,total):
            time.sleep(frequency)
            
            window['-2显示-'].update(Interval[num])
            if vice == True: 
                speak.speak(Interval_v[num])          
            if Break == True :
                break
        if Break == True :
            window['-1显示-'].update('请开始')
            break
            


sg.theme('SystemDefaultForReal')

DY_layout = [
    [sg.Text('计时：',size=(5,1), pad=((20, 0), (20, 10))),
    sg.Text('日积月累！',key='-1计时-',size=(12,1), pad=((5, 0), (20, 10)), justification='center',background_color='black',text_color='red',),
    sg.Text('频率：',size=(5,1), pad=((20, 0), (20, 10))),
    sg.Input('0.2',key='-1频率-',size=(3,1), pad=((0, 0), (20, 10)), justification='center',background_color='black',text_color='red',),
    sg.Text('秒',size=(2,1), pad=((0, 0), (20, 10))),
    sg.Checkbox('语音', default=True, enable_events=True, key='-1语音-',tooltip='请双击！', pad=((20, 0), (20, 10))),],
    
    
    [sg.Text('请开始',size=(6,1),font=('黑体',90), key='-1显示-', justification='center',pad=((20, 20), (10, 10)), background_color='black',text_color='green')],
             
    [sg.Text('显示名称：',size=(8,1), pad=((20, 0), (10, 10))),
    sg.Combo(['音名','唱名','数字'],key='-1显示名称-',default_value='音名',size=(4,1), pad=((5, 0), (10, 10)),readonly=True,),
    sg.Text('音数：',size=(4,1), pad=((20, 0), (10, 10))),
    sg.Combo(['七音','十二'],key='-音数-',default_value='七音',size=(4,1), pad=((5, 0), (10, 10)),readonly=True,),
    sg.Button('开始', key='-1开始-', disabled=False, size=(4, 1), pad=((40, 0), (10, 10))),
    sg.Button('结束', key='-1结束-', disabled=False, size=(4, 1), pad=((20, 0), (10, 10))),
    ],
   ]
   
YC_layout = [
    [sg.Text('计时：',size=(5,1), pad=((20, 0), (20, 10))),
    sg.Text('日积月累！',key='-2计时-',size=(12,1), pad=((5, 0), (20, 10)), justification='center',background_color='black',text_color='red',),
    sg.Text('频率：',size=(5,1), pad=((20, 0), (20, 10))),
    sg.Input('0.2',key='-2频率-',size=(3,1), pad=((0, 0), (20, 10)), justification='center',background_color='black',text_color='red',),
    sg.Text('秒',size=(2,1), pad=((0, 0), (20, 10))),
    sg.Checkbox('语音', default=True, enable_events=True, key='-2语音-',tooltip='请双击！', pad=((20, 0), (20, 10)))],
    
   
    [sg.Text('请开始',size=(6,1),font=('黑体',90), key='-2显示-', justification='center',pad=((20, 20), (10, 10)), background_color='black',text_color='green')],
             
    [sg.Button('开始', key='-2开始-', disabled=False, size=(4, 1), pad=((285, 0), (10, 10))),
    sg.Button('结束', key='-2结束-', disabled=False, size=(4, 1), pad=((20, 0), (10, 10))),
    ],
   ]


layout=[[sg.TabGroup([[ sg.Tab('单音',DY_layout,),sg.Tab('音程',YC_layout) ]],selected_title_color='red',selected_background_color='black',)]]

# 3) 创建窗口
window = sg.Window('练琴助手 V0.2 by YanMing', layout, icon="练琴助手图标.ico",finalize=True)

# 4) 事件循环
while True:


    event, values = window.read()  # 窗口的读取，有两个返回值(1.事件  2.值)
    if event == None:  # 窗口关闭事件
        break
        
    if values['-1语音-'] ==True:
        window['-2语音-'].update(value=True)
        vice=True
    
    if values['-1语音-'] ==False:
        window['-2语音-'].update(value=False)
        vice=False
        
    if values['-2语音-'] ==True:
        window['-1语音-'].update(value=True)
        vice=True
    
    if values['-2语音-'] ==False:
        window['-1语音-'].update(value=False)
        vice=False
        
    
    
    if event == '-1开始-':
        time1=time.time()
        window['-1开始-'].update(disabled=True)
        window['-2开始-'].update(disabled=True)
        
        Break = False
        threading.Thread(target=time_update,args=(True,False,), daemon=True, ).start()
        threading.Thread(target=DY, daemon=True, ).start()
    
    if event == '-1结束-':
        Break =True
        window['-1开始-'].update(disabled=False)
        window['-2开始-'].update(disabled=False)
       
    if event == '-2开始-':
        time1=time.time()
        window['-1开始-'].update(disabled=True)
        window['-2开始-'].update(disabled=True)
        
        Break = False
        threading.Thread(target=time_update,args=(False,True,), daemon=True, ).start()
        threading.Thread(target=YC, daemon=True, ).start()
    
    if event == '-2结束-':
        Break =True
        window['-2开始-'].update(disabled=False)
        window['-1开始-'].update(disabled=False)

        # 5) 关闭窗口
window.close()


# conda create -n 虚拟环境名字 python==3.6 #创建虚拟环境
# conda activate 虚拟环境名字 #激活虚拟环境
# conda deactivate #退出虚拟环境
# conda remove -n aotu--all  # 删除虚拟环境
# (picture_pdf) D:\Users\lixue>cd D:\Desktop\python小工具
# Pyinstaller -F -w -i ico.ico 图片转PDF工具_V1.3.py
# python -m pysimplegui-exemaker.pysimplegui-exemaker # 打包程序



'''
import os
import base64
import pyaudio
import wave
from io import BytesIO

def bin2module(bin_file, py_file=None):
    """二进制文件转存为python模块

    bin_file    - 二进制文件名
    py_file     - 生成的模块文件名，默认使用二进制文件名，仅更改后缀名
    """

    fpath, fname = os.path.split(bin_file)
    fn, ext = os.path.splitext(fname)
    if not py_file:
        py_file = os.path.join(fpath, '%s.py' % fn)

    with open(bin_file, 'rb') as fp:
        content = fp.read()

    content = base64.b64encode(content)
    content = content.decode('utf8')

    with open(py_file, 'w') as fp:
        fp.write('# -*- coding: utf-8 -*-\n\n')
        fp.write('import base64\n')
        fp.write('from io import BytesIO\n\n')
        fp.write('content = """%s"""\n\n' % content)
        fp.write('def get_fp():\n')
        fp.write('    return BytesIO(base64.b64decode(content.encode("utf8")))\n\n')
        fp.write('def save(file_name):\n')
        fp.write('    with open(file_name, "wb") as fp:\n')
        fp.write('        fp.write(base64.b64decode(content.encode("utf8")))\n')
        fp.write('        fp.close()')

    fp.close()

if __name__ == '__main__':
    """测试代码"""

    # 将图像文件转存为img_demo.py
    bin2module("D:\Desktop\野狼disco.wav", 'demo.py')

    # 导入刚刚生成的demo模块
    import demo



    chunk=1024
    wf = wave.open(demo.get_fp())
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                    rate=wf.getframerate(), output=True)

    data = wf.readframes(chunk)  # 读取数据
    print(data)
    while data != b'':  # 播放
        stream.write(data)
        data = wf.readframes(chunk)
        print('while循环中！')
        print(data)
    stream.stop_stream()  # 停止数据流
    stream.close()
    p.terminate()  # 关闭 PyAudio





# sox "D:\Desktop\WJ159.wav" -b 16 -e signed-integer "D:\Desktop\W.wav"


    # 保存为本地文件，验证demo模块的save()：保存文件

'''






