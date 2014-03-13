#!/usr/bin/python

import os
import sys


dest_path = sys.argv[1]

print 'Checking for .git/config files without an [user]...\n'

for path, dirs, files in os.walk(dest_path):
    for filename in files:

        if filename == 'config' and path.find('.git') > -1:
            has_config = False
            fullpath = os.path.join(path, filename)

            with open(fullpath, 'r') as f:
                for line in f:

                    if line.find('[user]') > -1:
                        has_config = True

            if not has_config:
                print fullpath
