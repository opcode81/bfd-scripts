import os
import re


def readfile(path):
    with open(path, "r") as f:
        return f.read()


def onerror(e):
    print(e)


for root, dirs, files in os.walk(".", followlinks=True, onerror=onerror):
    for fn in files:
        if fn == "BFDInfo.xml":
            path = os.path.join(root, fn)
            dirName = os.path.split(root)[1]
            subclass = None
            if dirName[:3] == "Tom":
                subclass = list(filter(lambda x: x in dirName, ("Hi", "Mid", "Floor")))
                if len(subclass) == 1:
                    subclass = subclass[0]
                    if subclass == "Hi":
                        subclass = "High"
            if "Crash" in dirName or "Cym A Custom 17" in dirName:
                subclass = "Crash"
            if "Ride" in dirName or "Swish" in dirName: 
                subclass = "Ride"
            if "Chin" in dirName:
                subclass = "China"
            if "Splash" in dirName:
                subclass = "Splash"
            if subclass is not None:
                print(path)
                content = readfile(path)
                if "kpi_subclass" not in content:
                    print("  Subclass '%s' added" % subclass)
                    content = content.replace('kpi_pitchHz', 'kpi_subclass="%s" kpi_pitchHz' % subclass)
                    with open(path, "w") as f:
                        f.write(content)
                else:
                    m = re.search('kpi_subclass="(.*?)"', content)
                    subclass_found = m.group(1)
                    if subclass_found == subclass:
                        print("  No action needed (subclass '%s' already present)" % subclass)
                    else: 
                        print("  Subclass '%s' found, but determined '%s'" % (subclass_found, subclass))

input("Execution complete. Press Enter to continue...")