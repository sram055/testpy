import lxml.etree as ET

structure = {
    "classes": "ApexClass",
    "lwc": "light weightning component",
    "flows": "layout",
}

data_dict = {"classes": [], "lwc": [], "flows": []}


def process_file():
    with open("destruct.txt", "r") as f:
        lines = [line.rstrip() for line in f.readlines()]
        for line in lines:
            line = line.split("/")
            cls_name = line[2].split(".")
            if line[1] == "classes":
                data_dict["classes"].append(cls_name) if (len(cls_name) > 2) else data_dict["classes"].append(cls_name[0])
            elif line[1] == "lwc":
                data_dict["lwc"].append(cls_name) if (len(cls_name) > 2) else data_dict["lwc"].append(cls_name[0])
            elif line[1] == "flows":
                data_dict["flows"].append(cls_name) if (len(cls_name) > 2) else data_dict["flows"].append(cls_name[0])
    return data_dict.items()


def add_member(key, val, cls_name):
    types = ET.SubElement(data, "types")
    name = ET.SubElement(types, "name")
    name.text = structure.get(cls_name)
    for cl in val:
        if isinstance(cl, str):
            member = ET.SubElement(types, "members")
            member.text = cl


def generate_xml(data):
    with open("destructiveChanges.xml", "wb") as f:
        for key, val in process_file():
            if key == "classes":
                add_member(key, val, "classes")
            elif key == "lwc":
                add_member(key, val, "lwc")
            elif key == "flows":
                add_member(key, val, "flows")
        data = ET.tostring(data, xml_declaration=True, pretty_print=True, encoding="utf-8")
        f.write(data)


if __name__ == "__main__":
    data = ET.Element("Package", xmlns="http://soap.sforce.com/2006/04/metadata")
    generate_xml(data)
