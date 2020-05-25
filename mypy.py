import xml.etree.ElementTree as xml
import gitapi
repo = gitapi.Repo("https://github.com/sram055/testpy.git") #existing folder
repo.git_init()
repo.git_add("fold/newfile2") #already created but not added file
repo.git_commit("Adding newfile2", user="sram055")
str(repo['HEAD'].desc)
'Adding newfile2'

def GenerateXML(fileName):
    root=xml.Element("Customers")
    cl=xml.Element("customer")
    root.append(cl)

    type1=xml.SubElement(cl,"Place")
    type1.text="UK"

    Amount1=xml.SubElement(cl,"Amount")
    Amount1.text = "5000"

    tree=xml.ElementTree(root)

    with open(fileName, "wb") as files:
       tree.write(files)
if __name__=="__main__":
    GenerateXML("Custs.xml") 
