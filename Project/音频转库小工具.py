# encoding="utf-8"
import numpy as np
import random
import pyttsx3
'''
total = 7
li = [i for i in range(total)]
res = []
num = 7

print( random.sample(li, num))


Interval = ['纯一度','小二度','大二度','小三度','大三度','纯四度','减五度','纯五度','小六度','大六度','小七度','大七度','纯八度',]
musical_alphabet= ['C','D','E','F','G','A','B',]
roll_call= ['do','re','mi','fa','sol','la','si']

musical_alphabet_12 = ["C","♭C","D","#E","E","F","♭F","G","♭G","A","#B","B"]
roll_call_12 = ["do","♭do","re","#mi","mi","fa","♭fa","sol","♭sol","la","#si","si"]
num_list = ["1","♭1","2","#3","3","4","♭4","5","♭5","6","#7","7"]

roll_call_v= ['哆','ruai','咪','发','嗖','拉','西']
roll_call_12_v = ["哆","降哆","来","升咪","咪","发","降发","嗖","降嗖","拉","升西","西"]
musical_alphabet_12_v = ["C","降C","D","升E","E","F","降F","G","降G","A","升B","B"]


for i in musical_alphabet:
    engine = pyttsx3.init()
    engine.save_to_file(i,'D:\Desktop\\'+str(i)+'.wav')
    engine.runAndWait()
'''

import os
import base64
import pyaudio
import wave
from io import BytesIO


"""二进制文件转存为python模块

bin_file    - 二进制文件名
py_file     - 生成的模块文件名，默认使用二进制文件名，仅更改后缀名
"""
all_list=["C","降C","D","升E","E","F","降F","G","降G","A","升B","B",'纯一度','小二度','大二度','小三度','大三度','纯四度','减五度','纯五度','小六度','大六度','小七度','大七度','纯八度',"哆","降哆","来","升咪","咪","发","降发","嗖","降嗖","拉","升西","西"]
name_list=["C","drop_C","D","Rise_E","E","F","drop_F","G","drop_G","A","Rise_B","B",'Pure_first', 'minor_second', 'major_second', 'minor_third', 'major_third', 'pure_fourth', 'minus_fifth', 'pure_fifth', 'minor_sixth' , 'major_sixth','minor_seventh','major_seventh','Pure_Octave',"1","drop_1","2","Rise_3","3","4","drop_4","5","drop_5","6","Rise_7","7"]

for i in range(len(all_list)):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate+5)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume+1)
    engine.save_to_file(all_list[i],'D:\Desktop\\'+name_list[i]+'.wav')
    engine.runAndWait()


content=[]
for i in range(len(all_list)):

    py_file = "D:\Desktop\speak.py"

    with open("D:\Desktop\\"+name_list[i]+".wav", 'rb') as fp:
        con = fp.read()
        
      
    content.append(base64.b64encode(con).decode('utf-8') )
    
 
with open(py_file, 'w') as fp:
    fp.write('# -*- coding: utf-8 -*-\n\n')
    fp.write('import base64\n')
    fp.write('from io import BytesIO\n\n')
    fp.write('import pyaudio\n')
    fp.write('import wave\n')
    

    fp.write('content = %s \n\n' % content)
    fp.write('name_list=%s \n\n' % name_list) 
    fp.write('d = dict(zip(name_list,content))\n')
    
    
    fp.write('def speak(name):\n')
    fp.write('    chunk=1024\n')
    fp.write('    wf = wave.open(BytesIO(base64.b64decode(d[name].encode("utf8"))))\n')
    fp.write('    p = pyaudio.PyAudio()\n')
    fp.write('    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),rate=wf.getframerate(), output=True)\n')
    fp.write('    data = wf.readframes(chunk)\n')   
    fp.write("    while data != b'':\n") 
    fp.write('        stream.write(data)\n')  
    fp.write('        data = wf.readframes(chunk)\n')     
    fp.write('    stream.stop_stream()\n')  
    fp.write('    stream.close()\n')  
    fp.write('    p.terminate()\n\n')  

        
        

fp.close()
print('已生成')
for i in range(len(all_list)): 
    os.remove('D:\Desktop\\'+name_list[i]+'.wav')
    
    
