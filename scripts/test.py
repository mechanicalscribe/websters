import re

def repl(match):
    return match.group(0).replace(match.group(1), "h" + match.group(1) + "h")

print re.sub("Christopher(.*?)Wilson", repl, "Christopher Emhardt Wilson")