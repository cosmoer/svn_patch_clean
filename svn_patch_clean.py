# -*- coding: utf-8 -*-

import sys

fp = open(sys.argv[1], 'r')
content = fp.readlines()
fp.close()

diff_block = []
index = 0

tmp_str = None
for line in content:
    if line.startswith('Index:'):
        if tmp_str:
            diff_block.append(tmp_str)
        tmp_str = line
    else:
        tmp_str += line
diff_block.append(tmp_str)

head_list = []
result = []

for line in diff_block:
    index = line.find('\n', 0)
    if line[0:index] not in head_list:
        head_list.append(line[0:index])
        result.append(line)
    else:
        print '%s ---delete'%(line[0:index])

print '----------result---------------'
for line in head_list:
    print line

outfile_name = '%s-clean.patch'%(sys.argv[1])
fp = open(outfile_name, 'w')
fp.write("".join(result))
fp.close()
