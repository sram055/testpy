import xml.etree.ElementTree as xml
from git import *
import git

repo = git.Repo("/home/runner/work/testpy/testpy")
commits = list(repo.iter_commits('master'))
print(commits[0])
print(commits[0].stats.total)
print(commits[0].stats.files)

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
