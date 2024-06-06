from pypdf import PdfReader
from os import listdir

reader = PdfReader("창원지방법원진주지원-2023고정165.pdf")

court = ""
cid = ""

lawapp = []

for p, page in enumerate(reader.pages):
    text = page.extract_text()
    words = text.split()
    lines = text.split("\n")

    if p == 0:
        court = words[0]
        cid = words[4]
    
    if not lawapp == []:
        lawapp += lines

    if '법령의 적용' in lines:
        lawapp += lines[lines.index("법령의 적용"):]

    #if 법령의 적용이 끝난다면:
        #break

for n, i in enumerate(lawapp):
    if i.startswith("1. "):
        lawapp.pop(n)
 
lawapp = lawapp[1:] # '법령의 적용' 제거
lawapp = ' '.join(lawapp)

erase = 0
n = 0
for i in lawapp:
    if i == '(' or (i == '출' and lawapp[n+1] == '처'):
        erase = n
    if erase:
        lawapp = lawapp[:erase] + lawapp[erase+1:]
    else:
        n += 1
    if i == ')' or (i == '-'):
        erase = 0

print(lawapp)
