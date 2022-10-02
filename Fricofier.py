from docx import Document
from docx.shared import Pt
from docx.shared import RGBColor

import sys
import os   

if(len(sys.argv)<=1):
    print("No document argument")
    exit()


one = sys.argv[1]

try:
    doc = Document(one)
except:
    print("incorrect file")
    exit()


for pa in doc.paragraphs:
    for run in pa.runs:
        run.font.name = 'freecofont Courier'

name = sys.argv[1]
name = name[0:name.index(".")] + "_Fricofied.docx"


print("document saved as " +  name)
doc.save(name)
