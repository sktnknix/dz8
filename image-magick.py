# -*- coding: utf-8 -*-

import subprocess, os

if not os.path.exists('Result'):
    os.makedirs('Result')
_iter = 0
for file in os.listdir('Source'):
    subprocess.call('convert.exe Source\\' + file + ' -resize 200 Result\\output' + str(_iter) + '.jpg')
    _iter += 1

