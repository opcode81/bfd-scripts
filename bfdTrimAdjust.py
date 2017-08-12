import os
import re
import sys

adjustTrim = True # if False, demo only (no files written)

argv = sys.argv[1:]
if len(argv) != 1:
    print "\n usage: bfdTrimAdjust <new trim value (dB)>"
    sys.exit(1)
newTrim = argv[0]

def replace(m):
    print "  adjusting trim: '%s' -> '%s'" % (m.group(1), newTrim)
    return newTrim

for root, dirs, files in os.walk("."):
    for fn in files:
        if fn == "BFDArticTweaks.xml":
            path = os.path.join(root, fn)
            print path
            with file(path, "r") as f:
                content = f.read()
            content = re.sub(r'dbTrim="(.*?)"', replace, content)
            if adjustTrim:
                with file(path, "w") as f:
                    f.write(content)
