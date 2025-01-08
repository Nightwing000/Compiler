class lexer:
    def __init__(self,source):
        self.source=source + '\n'
        self.curChar=''
        self.curPos=-1
        self.nextChar()

    def nextChar(self):
        self.curPos+=1
        if self.curPos<len(self.source):
            self.curChar=self.source[self.curPos]
        else:
            self.curChar='\0'

    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos+1]

    def skipCow(self):
        while self.curChar in ('\t',' '):
            self.nextChar()

        if self.curChar=='\\' and self.peek() == '\\':
            while self.curChar!='\n':
                self.nextChar()

    def getToken(self):
        pass

class Token    
