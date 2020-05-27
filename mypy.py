from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree

def GenerateXML(fileName):
      root=Element("Customers")
      tree=ElementTree(root)
      cl=Element("customer")
      root.append(cl)
    #  type1=SubElement(cl,"Place")
    #  type1.text="UK"
    #  Amount1=SubElement(cl,"Amount")
    #  Amount1.text = "5000"
    #  print etree.tostring(root)
      with open(fileName, "w") as files:
         tree.write(files)
if __name__=="__main__":
    GenerateXML("Custard.xml") 
