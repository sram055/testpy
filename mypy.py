
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
import xml.etree.ElementTree as xml


def GenerateXML(fileName):
    root=xml.Element("Package")
    
    cl=xml.Element("types")
    root.append(cl)

    Amount1=xml.SubElement(cl,"members")
    Amount1.text = "AccountGeneratorTest"

    type1=xml.SubElement(cl,"name")
    type1.text="ApexClass"

    tree=xml.ElementTree(root)

    with open(fileName, "wb") as files:
       tree.write(files)  
       newline = "\n".encode("utf-8")
       files.write(newline)
        
if __name__=="__main__":
    GenerateXML("hero.xml") 
	
