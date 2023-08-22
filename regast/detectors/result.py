from regast.parsing.ast_node import ASTNode


class Result:
    def __init__(
        self,
        fname: str,
        source: str,
        start_line: int,
        end_line: int
    ):
        self.fname: str = fname
        self.source: str = source
        self.start_line: int = start_line
        self.end_line: int = end_line

    @staticmethod
    def from_node(source: str, node: ASTNode) -> "Result":
        return Result(
            node.fname,
            source,
            node.start_line + 1,
            node.end_line + 1
        )

    @staticmethod
    def from_line(fname: str, source: str, start_line: int, end_line: int) -> "Result":
        return Result(fname, source, start_line, end_line)
    
    @property
    def is_multiline(self) -> bool:
        return self.start_line != self.end_line

    @property
    def code(self) -> str:
        lines = self.source.splitlines()

        s = ''
        for line_number in range(self.start_line - 1, self.end_line):
            s += str(line_number + 1).rjust(4, ' ') 
            s += ': '
            s += lines[line_number]
            s += '\n'
        
        return s
    
    def __str__(self):
        lines = self.source.splitlines()
        return '\n'.join(lines[self.start_line - 1:self.end_line])
    
