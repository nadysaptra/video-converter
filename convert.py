from os import listdir
from os.path import isfile, join
import os
import subprocess
cur_dir     = os.path.dirname(os.path.realpath(__file__))
mypath      = '%s/files' % cur_dir
if not os.path.exists('%s/convert' % mypath ):
    os.makedirs('%s/convert' % mypath)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
quality   = 24
for f in onlyfiles:
    print('files %s' % (f))
    path        = '%s/%s' % (mypath, f)
    result_path = '%s/convert/%s' % (mypath, f)
    os.system('ffmpeg -i %s -vcodec libx264 -crf %s %s' % (path, quality, result_path))
