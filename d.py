import re

# regex = r"\n(<[a-z]>)*([\w\.\?\-\,\s !&:'\"$\*]{1,})(<\/[a-z]>)*\n{2}"
regex = r"\n([^>]+?)\n{2}"

subtitle = open('subtitle.srt', 'r')
subtitle = subtitle.read()
subtitle = re.sub('<[a-z]>', '', subtitle)
subtitle = re.sub('<\/[a-z]>', '', subtitle)

matches = re.finditer(regex, subtitle, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

with open('subtitle-clean.srt', 'w') as file:
    file.write(subtitle)