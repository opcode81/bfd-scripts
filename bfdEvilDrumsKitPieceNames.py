import re
import glob
import os
import shutil
import sys
from pathlib import Path


def process(info_file_path: Path):
    print(info_file_path)

    orig_path = info_file_path.parent / "Info.xml.orig"
    if not os.path.exists(orig_path):
        print(f"  Creating backup: {info_file_path} -> {orig_path}")
        shutil.copy(info_file_path, orig_path)

    with open(orig_path) as f:
        content = f.read()

    m = re.search(r'kpi_manufacturer="(.*?)"', content)
    if not m:
        raise ValueError("No manufacturer")
    manufacturer = m.group(1)
    print(f"  Manufacturer: {manufacturer}")

    m = re.search(r'kpi_model="(.*?)"', content)
    if m:
        model = m.group(1)
    else:
        model = ""
    print(f"  Model: {model}")

    manufacturer = manufacturer.replace("Drum Workshop", "DW")
    model = model.replace(" (tm)", "")
    model = model.replace("Glamoflage", "Glamouflage")
    model = model.replace("Glamoflauge", "Glamouflage")
    model = model.replace("  ", " ")
    full_model = manufacturer
    if model != "":
        full_model += " " + model.strip()
    print(f"  Full model: {full_model}")

    m = re.search(r'kpi_name="EJB Kit (\d) (.*?)"', content)
    if m:
        old = m.group(0)
        new = f'kpi_name="EJB Kit {m.group(1)} {m.group(2)} {full_model}"'
    else:
        m = re.search(r'kpi_name="EJB Xtra \w+ (.*?)"', content)
        if m:
            old = m.group(0)
            new = f'kpi_name="EJB Xtra {m.group(1)} {full_model}"'
        else:
            raise ValueError("no match")

    print(f"  {old} -> {new}")

    content = content.replace(old, new)
    with open(info_file_path, "w") as f:
        f.write(content)


if __name__ == '__main__':
    if not os.path.exists("Audio"):
        print(f"Folder 'Audio' not found in current working directory ({os.path.abspath('.')})")
        sys.exit(1)

    paths = glob.glob("Audio/*/*/Info.xml")
    for path in paths:
        process(Path(path))

    input("Execution complete. Press Enter to continue...")