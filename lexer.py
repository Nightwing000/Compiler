class Lexer:
    def __init__(self, source):
        self.source_code = source.code
        self.position = 0
        self.line = 1
        self.operators = {"+", "-", "*", "/", "=","==","!=", "<=", ">=", "+=", "-=", "*=","/=","&&","||"}
        self.single_char_tokens = {'(',')','{','}',';',','}
        self.tokens =  []

    
    
    def peek(self):
        if self.position < len(self.source_code):
            return self.source_code[self.position]
        return None

    def advance(self):
        if self.position < len(self.source_code):
            char = self.source_code[self.position]
            self.position +=1
            if char == "\n":
                self.line += 1
            return char

        return None
    def consume_comment(self):
        if self.peek() == '/':  
            while self.peek() is not None and self.peek() != '\n':
                self.advance()
       

    def consume_identifier(self):
        
        start_pos = self.position
        while self.peek() is not '\0' and (self.peek().isalnum() or self.peek() == '_'):
            self.advance()
        value = self.source_code[start_pos:self.position]
        if value in {'int', 'if', 'else', 'return', 'while', 'for', 'true', 'false'}:  
            return ('KEYWORD', value, self.line)
        return ('IDENTIFIER', value, self.line)
    
    def consume_operator(self):
        start_pos = self.position
        char = self.advance()

        next_char = self.peek()
        if next_char and (char+ next_char) in self.operators:
            self.advance()
            return("OPERATOR", char+ next_char, self.line)
        return ("OPERATOR", char, self.line)

    def consume_number(self):
        
        start_pos = self.position
        while self.peek() is not '\0' and self.peek().isdigit():
            self.advance()
        return ('NUMBER', self.source_code[start_pos:self.position], self.line)

    def tokenise(self):
        while self.peek() is not '\0':
            char = self.peek()

            if char.isspace():
                self.advance()
            elif char.isalpha():
                self.tokens.append(self.consume_identifier())
            elif char.isdigit():
                self.tokens.append(self.consume_number())
            elif char in self.operators:
                self.tokens.append(self.consume_operator())
            elif char in self.single_char_tokens:
                self.tokens.append((char,char,self.line))
                self.advance()
        return self.tokens

