import os
import sys
import hashlib 
import random

for (dirname, dirs, files) in os.walk('.'):
    print(dirname)
    for filename in files:
        if filename.endswith('.kv') :
            thefile = os.path.join(dirname,filename)
            size = os.path.getsize(thefile)
            if size == 2578 or size == 2565:
                print('T-Mobile: {}'.format(thefile))
                #os.remove(thefile)
                continue
            fhand = open(thefile,'r',encoding='utf-8')
            lines = list()
            for line in fhand:
                lines.append(line)

            data = fhand.read()
            data = data.encode('utf-8')
            checksum = hashlib.md5(data).hexdigest()
            print("checksum: {}".format(checksum))

            hashCode = hashlib.sha256(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
            print("hash code: {}".format(hashCode))

            fhand.close()
            #if len(lines) == 3 and lines[2].startswith('Sent from my iPhone'):
            #    print('iPhone: {}'.format(thefile))
            #    os.remove(thefile)
            #    continue
            if len(lines) > 1:
                print(len(lines), thefile)
                print(lines[:4])