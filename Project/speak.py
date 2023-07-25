# -*- coding: utf-8 -*-

import base64
from io import BytesIO

import pyaudio
import wave

name_list=['C', 'drop_C', 'D', 'Rise_E', 'E', 'F', 'drop_F', 'G', 'drop_G', 'A', 'Rise_B', 'B', 'Pure_first', 'minor_second', 'major_second', 'minor_third', 'major_third', 'pure_fourth', 'minus_fifth', 'pure_fifth', 'minor_sixth', 'major_sixth', 'minor_seventh', 'major_seventh', 'Pure_Octave', '1', 'drop_1', '2', 'Rise_3', '3', '4', 'drop_4', '5', 'drop_5', '6', 'Rise_7', '7'] 

d = dict(zip(name_list,content))
def speak(name):
    chunk=1024
    wf = wave.open(BytesIO(base64.b64decode(d[name].encode("utf8"))))
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),rate=wf.getframerate(), output=True)
    data = wf.readframes(chunk)
    while data != b'':
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()
