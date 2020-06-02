
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
from xml.dom import minidom
import xml.etree.ElementTree as etree
import xml.etree.ElementTree as xml
import xml.dom as xmly

root = xml.Element('Package', xmlns={"http://soap.sforce.com/2006/04/metadata"})
 


tree_out  =  xml.tostring(root,  xml_declaration=True, encoding="UTF-8")
tree_out_pretty=(xmly.minidom.parseString(tree_out).toprettyxml(indent=" ", encoding="UTF-8"))
print(tree_out_pretty)

ctr=0
objectmemberline=[]
files = open("destuctive1.xml", "wb")  

with open('destruct.txt', 'r') as filehandle:
    for line in filehandle:
        lines = [current_lines.rstrip() for current_lines in filehandle.readlines()] 
	#print(lines)
        currentlines = line[:-1]
        #currentlines = line[]
        lines.append(currentlines)
        
ctr=(len(lines))
typeline=""
elementline=""
print(ctr)   
ind=0
prev=" "
while ind<ctr:
    x=lines[ind]
    x = x.split("/")
    file=x[2].split(".")
    print(ind)   	
    curr=x[1]
    ind+=1  
    
    if x[1] == "classes":
        typeline="ApexClass"
        elementline=file[0]
    elif x[1] == "lwc":
        typeline="light weightning component"
        elementline=file[0]     
    elif x[1] == "flows":
        typeline="layout"
        elementline=file[0]

    if prev==curr:
       Amount1=xml.SubElement(cl,"members")
       string1=elementline
       Amount1.text = string1 
       prev=curr       
    else:
        prev=curr   
        cl=xml.Element("types")
        type1=xml.SubElement(cl,"name")
        type1.text=typeline
        Amount1=xml.SubElement(cl,"members")
        string1=elementline
        Amount1.text = string1 
        root.append(cl)
tree=xml.ElementTree(root)     
tree.write(files)        

        
        













	
