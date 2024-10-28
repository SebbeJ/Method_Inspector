'''
To do:
    Bättre kod: 
    ***Gör automatiska test cases
    -Dela upp i mindre metoder
    *Skriv ordentliga kommentarer

    Utökad funktionalitet:
    *Implementera weight till genomsnitt
    -Ge filer och metoder mer data
        *Kommentarer/docstrings
        -Längd i rader (filer)
        *Average längd
    *Ignorera tomma folders/filer för genomsnittet
    -Gör om till console commands

    Presenteation:
    *Implementera depth
    -Implementera visualisering
'''

class method: 
    '''A class to save information about methods, mostly setter and getters'''
    def __init__(self, name, parent, indent):
        self.name = name
        self.parent = parent
        self.indent = indent
        self.line_count = 0
        self.comments = 0
        self.docstrings = 0
    
    def inc_line_count(self, inc = 1):
        self.line_count += inc

    def get_name(self):
        return self.name
    
    def get_line_count(self):
        return self.line_count
    
    def get_indent(self):
        return self.indent

    def get_parent(self):
        return self.parent

    def inc_comments(self, inc = 1):
        self.comments += inc
    
    def get_comments(self):
        return self.comments

    def inc_docstring(self, inc=1):
        self.docstrings += inc
    
    def get_docstring(self):
        return self.docstrings



