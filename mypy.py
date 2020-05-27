
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree
import xml.etree.ElementTree as xml

def GenerateXML(fileName):
    root=xml.Element("Customers")
    
    cl=xml.Element("customer")
    root.append(cl)

    type1=xml.SubElement(cl,"Place")
    type1.text="UK"

    Amount1=xml.SubElement(cl,"Amount")
    Amount1.text = "5000"

    tree=xml.ElementTree(root)
    #print etree.tostring(root)
    tree.write(open(filename,'w'))
if __name__=="__main__":
    GenerateXML("Cutty.xml")
