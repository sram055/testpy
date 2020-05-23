import xml.etree.ElementTree as XML

def GenerateXML(fileName):
    root=xml.Element("Customers")
    cl=xml.Element("customer")
    root.append(cl)

    type1=xml.SubElement(c1, "Place")
    type1.text="UK"

    Amount1=xml.SubElement(c1, "Amount1")
    Amount1.text = "5000"

    tree=xml.ElementTree(root)

    with open(fileName, "wb") as files:
       tree.write(files)
if __name__ == __main__:
    GenerateXML("Cust.XML") 
