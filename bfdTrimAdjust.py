import os
import re
import sys

adjustTrim = True # if False, demo only (no files written)

argv = sys.argv[1:]
newTrim = None
if len(argv) != 1:
    newTrim = raw_input("Enter new trim value in dB (e.g. -5): ")
else:
    newTrim = argv[0]
    
validParams = True
newTrim = newTrim.strip()
try:
    int(newTrim)
except:
    print "Invalid trim value (%s); Integer required" % newTrim
    validParams = False
    
def replace(m):
    print "    adjusting trim: '%s' -> '%s'" % (m.group(1), newTrim)
    return 'dbTrim="%s"' % newTrim

if validParams:
    def onerror(e): print e
    for root, dirs, files in os.walk(".", followlinks=True, onerror=onerror):
        print root
        for fn in files:
            if fn.lower()[-3:] == "xml":
                path = os.path.join(root, fn)
                print "  %s" % path
                if fn == "BFDArticTweaks.xml":     
                    print "  %s" % path
                    with file(path, "r") as f:
                        content = f.read()
                    content = re.sub(r'dbTrim="(.*?)"', replace, content)
                    if adjustTrim:
                        with file(path, "w") as f:
                            f.write(content)

raw_input("Execution complete. Press Enter to continue...")