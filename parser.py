from lexer import *
import sys

class Parser:
    def __init__(self, lexer):
        self.lexer=lexer
        self.currTok=None
        self.nxTok=None
        self.nextTok()
        self.nextTok()

    # Return true if the current token matches.
    def checktok(self, kind):
        if kind==self.currTok.kind:
            return True
        else:
            return False

    # Return true if the next token matches.
    def peektok(self, kind):
        if kind==self.nxTok.kind:
            return True
        else:
            return False

    def match(self, kind):
        if self.checktok(kind):
            self.nextTok()
        else:
            self.abort("Expected token:"+kind.name+"Current Token:"+self.currTok.kind)

    def nextTok(self):
        self.currTok=self.nxTok
        self.nxTok=self.lexer.getToken()
        
    def abort(self, message):
        sys.exit("Error. " + message)

    def prog(self):
        while self.checktok(TokenType.newline):
            self.nextTok()
        while not self.checktok(TokenType.EOF):
            self.clss()

    def clss(self):
        if self.match(TokenType.Public)       
            