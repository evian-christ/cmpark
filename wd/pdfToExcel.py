from pypdf import PdfReader
from os import listdir
import csv

data = []
fields = ['court', 'id']
filename = "court_data.csv"

with open(filename, 'w', encoding = 'utf-8-sig', newline = '') as csvfile:
    #writer = csv.DictWriter(csvfile, fieldnames = fields)

    #writer.writeheader()

    for file in listdir("inputs"):
        reader = PdfReader("inputs/" + file)

        page = reader.pages[0]
        text = page.extract_text()
        line = text.splitlines()

        org = line[0]
        num = line[2].split()

        #data.append({"court": org, "id": num[1]})
        
        idd = num[1]

        law_app = []
        on = 0

        for n, page in enumerate(reader.pages):
            text = page.extract_text()
            line = text.splitlines()
            
            if '법령의 적용' in line:
                on = 1
                law_app += line
            elif '피고인 및 변호인의 주장에 관한 판단' in line:
                on = 0
                law_app += line
            elif '양형의 이유' in line:
                on = 0
                law_app += line
            elif on == 1:
                law_app += line
            else:
                continue
        
        print(idd)
        print(law_app)

        x = law_app.index("법령의 적용")
        
        law_app = law_app[x:]

        for i in law_app:
            if i.startswith("1"):
                law_app.remove(i)

        
        #print(law_app)
    #writer.writerows(data)
