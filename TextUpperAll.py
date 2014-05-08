# TextupperAll
#dwane@dsdraughting.com
#2014
#
#import libraries and reference the RevitAPI and RevitAPIUI
import clr
import math
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')

# to access all the Name-spaces in the RevitAPI & UI, we import them all using *
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Architecture import *
from Autodesk.Revit.DB.Analysis import *

#set the active Revit application and document
uidoc = __revit__.ActiveUIDocument
doc = __revit__.ActiveUIDocument.Document
selection = __revit__.ActiveUIDocument.Selection.Elements

#define a transaction variable and describe the transaction
t = Transaction(doc, 'convert all text to upper case') 

#start a transaction in the Revit database 
t.Start()

#perform some action here...
#select all the text elements using a collector
txtInstancesFilter = ElementClassFilter(clr.GetClrType(TextElement))
collector = FilteredElementCollector(doc)
textsId = collector.WherePasses(txtInstancesFilter).ToElementIds()
selection.Clear()

#add there id's to a selection set
for id in textsId:
	selection.Add(doc.GetElement(id))
	print str(id)
#convert selection to upper / lower case
for el in uidoc.Selection.Elements:	
	el.Text=el.Text.upper()	

#commit the transaction to the Revit database
t.Commit()

#close the script window
__window__.Close()
