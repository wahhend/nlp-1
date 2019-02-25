import re

# regex = r"\n(<[a-z]>)*([\w\.\?\-\,\s !&:'\"$\*]{1,})(<\/[a-z]>)*\n{2}"
regex = r"\n([^>]+?)\n{2}"

subtitle = open('subtitle.srt', 'r')
subtitle = subtitle.read()
subtitle = re.sub('<[a-z]>', '', subtitle)
subtitle = re.sub('<\/[a-z]>', '', subtitle)

matches = re.finditer(regex, subtitle, re.MULTILINE)

d_subtitle = open('d_subtitle.txt', 'w')

for idx, match in enumerate(matches, start=1):
    d_subtitle.write(match.group(1)+'\n')