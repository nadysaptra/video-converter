from os import listdir
from os.path import isfile, join
import os
import subprocess
mypath    = '/the-path-to-video/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
quality   = 24
for f in onlyfiles:
    print('files %s' % (f))
    os.system('ffmpeg -i /the-path-to-video/%s -vcodec libx264 -crf %d /the-path-to-results/convert/%s' % (f, quality, f))
