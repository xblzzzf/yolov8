import xml.etree.ElementTree as ET
from pathlib import Path

# NEU-DET 专用转换脚本
xml_dir = Path(r"D:\NEU-DET\NEU-DET\ANNOTATIONS")
img_dir = Path(r"D:\NEU-DET\NEU-DET\IMAGES")
out_dir = Path(r"D:\NEU-DET\NEU-DET\labels")
out_dir.mkdir(exist_ok=True)

# NEU-DET 真实类别（顺序固定）
classes = ["crazing", "inclusion", "patches", "pitted_surface", "rolled-in_scale", "scratches"]

for xml_file in xml_dir.glob("*.xml"):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    w = int(root.find(".//width").text)
    h = int(root.find(".//height").text)

    txt_file = out_dir / f"{xml_file.stem}.txt"
    with open(txt_file, "w") as f:
        for obj in root.findall(".//object"):
            cls = obj.find("name").text
            if cls not in classes:
                continue
            cid = classes.index(cls)
            box = obj.find("bndbox")
            x1 = float(box.find("xmin").text)
            y1 = float(box.find("ymin").text)
            x2 = float(box.find("xmax").text)
            y2 = float(box.find("ymax").text)
            xc = ((x1 + x2) / 2) / w
            yc = ((y1 + y2) / 2) / h
            bw = (x2 - x1) / w
            bh = (y2 - y1) / h
            f.write(f"{cid} {xc:.6f} {yc:.6f} {bw:.6f} {bh:.6f}\n")

    print(f"完成: {xml_file.name}")

print(f"全部完成，共转换 {len(list(xml_dir.glob('*.xml')))} 个文件")
