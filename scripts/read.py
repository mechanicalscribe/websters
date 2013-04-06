import re
import os
import json
import random
import codecs
import pie

websters = open(os.getcwd() + "/texts/websters.txt", 'r').read().decode('iso-8859-1').encode('utf8')

#normalize the linebreaks in memory

websters = re.sub(" +", " ", websters)
websters = re.sub("[\r\n]+", "  ", websters)

definitions = [
    ("word", r"\s{2}([[A-Z][A-Z\s-]*)\s{2}"),
    ("origin", r"\([A-z]{2,6}\.\)"),
    ("etymology", r"\bEtym: \[(.*?)\]"),
    ("source", r"(?:\.|\])\s([A-Z][A-z]{3,15}\.)\s\s"),
    ("definition", r"\d{1,2}\. (.+?)(?:\d|\s{2})"),
    ("definition", r"Defn: (.+)")
]

PIE = pie.PIE_Parser()

#grab a snippet of the text on which to test our patterns
def sample(text, margin=5000):
    bookmark = random.randint(0, len(websters) - margin)
    return text[bookmark: bookmark + margin]

t = sample(websters, 2000)


for c in range(len(definitions)):
    t = PIE.parse(definitions[c][0], definitions[c][1], t)


t = t.replace("\n", "")

f = open(os.getcwd() + "/data/test.json", 'w')
f.write(json.dumps({ "text": t}))
f.close()