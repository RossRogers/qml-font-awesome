import sys
import os
import re
from shutil import copyfile

update_path_dir = os.path.dirname(os.path.abspath(__file__)) 
outpath = update_path_dir + '/font_awesome.js'
print outpath
out = open(outpath,'w')
out.write('''
/****************************************************************************
**
** The MIT License (MIT)
**
** Copyright (c) 2016 Ross Rogers 
**
** $BEGIN_LICENSE:MIT$
** Permission is hereby granted, free of charge, to any person obtaining a copy
** of this software and associated documentation files (the "Software"), to deal
** in the Software without restriction, including without limitation the rights
** to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
** copies of the Software, and to permit persons to whom the Software is
** furnished to do so, subject to the following conditions:
**
** The above copyright notice and this permission notice shall be included in
** all copies or substantial portions of the Software.
**
** THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
** IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
** FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
** AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
** LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
** OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
** SOFTWARE.
**
** $END_LICENSE$
**
****************************************************************************/    

''')

for l in open(update_path_dir + '/Font-Awesome/less/variables.less','r'):
    #                    @fa-var-500px: "\f26e";
    srch = re.compile(r'^@fa-var-(?P<icon_name>[\w+\-]*): "\\(?P<icon_unicode>[a-fA-F0-9]+)";').search(l)
    if srch:
        out.write('var fa_' + 
            re.sub('-','_',srch.group('icon_name')) +
            ' = "\u'+ srch.group('icon_unicode') + '";\n')
out.write('\n')
