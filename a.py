import re
# regex = r"([12][0-9]{3})-([12][0-9]{3}|[a-zA-Z]{0,}):\s{0,}([a-zA-Z0-9\s]{0,})(\n+?)"
regex = r"(\d{1,4})-(\d{1,4}|[a-zA-Z]{0,}):\s{0,}([\w ]{0,})\n+?"

doc1 = open('doc-1.txt', 'r')
doc1 = doc1.read()

matches = re.finditer(regex, doc1, re.MULTILINE)

a_subjudul = open('a_subjudul.txt', 'w')
i=1
for match in matches:
    
    a_subjudul.write(match.group(1)+' s.d. '+match.group(2)+'\t'+match.group(3)+'\n')