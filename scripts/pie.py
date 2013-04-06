import re
#TODO
#convert native HTML to entities

class PIE_Parser:
    def __init__(self, tag="div", definitions=[]):
        self.tag = tag
        self.pattern = "(?:^|</%s>)(.*?)(?:$|<%s)" % (tag, tag)
        
    def parse(self, classname, pattern, text):
        #first, get every part of the text that is not marked up
        #that is, by default, text outside the <div> tags that we add as we find matches
        print "==================>", classname, pattern
        print "\n----\n".join(re.findall(self.pattern, text, re.S))
        
        return re.sub(self.pattern, self._sub_regex(classname, pattern), text, re.S)

    #receives each region of text not yet matched and runs the real regex against it
    def _sub_regex(self, name, pattern):
        def repl(match):
            return match.group(0).replace(match.group(1), re.sub(pattern, self._markup(name), match.group(1), re.S))
        return repl
        
    #take matches of the real regex pattern and marks them up with tags
    def _markup(self, name):
        def repl(match):
            #some patterns have submatches, some don't
            if len(match.groups()) == 0:
                print match.group(0) 
                return "<%s class='%s'>%s</%s>" % (self.tag, name, match.group(0), "div")
            print match.groups() 
            try:
                return match.group(0).replace(match.group(1), "<%s class='%s'>%s</%s>" % (self.tag, name, match.group(1), "div"))
            except:
                print "Error", match.groups()
        return repl
    
    