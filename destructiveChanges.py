# This script dynamically generates XML called destructiveChanges.xml. Reads the list of files that is generated from git log that are deleted from repository for  a specified range of dates

import lxml.etree as ET
# This structure defines for the specified object types. At this point of time (06 June 2020), it is hard coded of object types
structure = {
    "aura" : "AuraDefinitionBundle", 
    "classes" : "ApexClass", 
    "customMetadata" : "CustomMetadata", 
    "flexipages" : "FlexiPage", 
    "labels" : "CustomLabel", 
    "layouts" : "Layout", 
    "lwc" : "LightningComponentBundle", 
    "objects" : "CustomObject", 
    "profiles" : "Profile", 
    "remoteSiteSettings" : "RemoteSiteSetting", 
    "reports" : "Report", 
    "triggers" : "ApexTrigger", 
}

data_dict = {"aura" :  [], "classes" :  [], "customMetadata" :  [], "flexipages" :  [], "labels" :  [], "layouts" :  [], "lwc" :  [], "objects" :  [], "profiles" :  [], "remoteSiteSettings" :  [], "reports" :  [], "triggers" :  []}

# Reading list of files to delete in the target environment
def process_file():
    with open("destruct.txt", "r") as f:
        lines = [line.rstrip() for line in f.readlines()]
        for line in lines:
            line = line.split("/")
            num_level = (len(line))
            cls_name = line[num_level-1].split(".")
            if line[3] == "aura":
                data_dict["aura"].append(cls_name) if (len(cls_name) > 3) else data_dict["aura"].append(cls_name[0])
            elif line[3] == "classes":
                data_dict["classes"].append(cls_name) if (len(cls_name) > 3) else data_dict["classes"].append(cls_name[0]) 
            elif line[3] == "customMetadata":
                data_dict["customMetadata"].append(cls_name) if (len(cls_name) > 3) else data_dict["customMetadata"].append(cls_name[0])      
            elif line[3] == "flexipages":
                data_dict["flexipages"].append(cls_name) if (len(cls_name) > 3) else data_dict["flexipages"].append(cls_name[0])
            elif line[3] == "labels":
                data_dict["labels"].append(cls_name) if (len(cls_name) > 3) else data_dict["labels"].append(cls_name[0])
            elif line[3] == "layouts":
                data_dict["layouts"].append(cls_name) if (len(cls_name) > 3) else data_dict["layouts"].append(cls_name[0])			
            elif line[3] == "lwc":
                data_dict["lwc"].append(cls_name) if (len(cls_name) > 3) else data_dict["lwc"].append(cls_name[0])
            elif line[3] == "objects":
                data_dict["objects"].append(cls_name) if (len(cls_name) > 3) else data_dict["objects"].append(cls_name[0])			
            elif line[3] == "profiles":
                data_dict["profiles"].append(cls_name) if (len(cls_name) > 3) else data_dict["profiles"].append(cls_name[0])
            elif line[3] == "remoteSiteSettings":
                data_dict["remoteSiteSettings"].append(cls_name) if (len(cls_name) > 3) else data_dict["remoteSiteSettings"].append(cls_name[0])	
            elif line[3] == "reports":
                data_dict["reports"].append(cls_name) if (len(cls_name) > 3) else data_dict["reports"].append(cls_name[0])
            elif line[3] == "triggers":
                data_dict["triggers"].append(cls_name) if (len(cls_name) > 3) else data_dict["triggers"].append(cls_name[0])
    return data_dict.items()

# This function is to add members and names list to the XML 
def add_member(key, val, cls_name):
    types = ET.SubElement(data, "types")
    name = ET.SubElement(types, "name")
    name.text = structure.get(cls_name)
    for cl in val:
        if isinstance(cl, str):
            member = ET.SubElement(types, "members")
            member.text = cl
    
# This function generates XML and writes to destructiveChanges.xml
def generate_xml(data):
    with open("destructiveChanges.xml", "wb") as f:
        for key, val in process_file():
            if key == "aura":
                add_member(key, val, "aura")
            elif key == "classes":
                add_member(key, val, "classes")
            elif key == "customMetadata":
                add_member(key, val, "customMetadata")
            elif key == "flexipages":
                 add_member(key, val, "flexipages")
            elif key == "labels":
                add_member(key, val, "labels")
            elif key == "layouts":
                add_member(key, val, "layouts")
            elif key == "objects":
                add_member(key, val, "objects")
            elif key == "lwc":
                add_member(key, val, "lwc")
            elif key == "profiles":
                add_member(key, val, "profiles")
            elif key == "remoteSiteSettings":
                add_member(key, val, "remoteSiteSettings")
            elif key == "reports":
                add_member(key, val, "reports")
            elif key == "triggers":
                add_member(key, val, "triggers")
        vers = ET.SubElement(data,"version")
        vers.text = "46.0"
        data = ET.tostring(data, xml_declaration=True, pretty_print=True, encoding="utf-8")
        f.write(data)
       
    



if __name__ == "__main__":
    data = ET.Element("Package", xmlns="http://soap.sforce.com/2006/04/metadata")
    generate_xml(data)
   
    
