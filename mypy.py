from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as etree

def GenerateXML(fileName):
      root=xml.Element("Customers")
      tree=xml.ElementTree(root)
      cl=xml.Element("customer")
      root.append(cl)
      type1=xml.SubElement(cl,"Place")
      type1.text="UK"
      Amount1=xml.SubElement(cl,"Amount")
      Amount1.text = "5000"
      with open(fileName, "w") as files:
         tree.write(files)
if __name__=="__main__":
    GenerateXML("Custard.xml") 
