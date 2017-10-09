line = ""
cursor = 0
token = None


class Interpreter(object):
    def __init__(self):
        self.line = ""
        self.cursor = 0
        self.token = None

    def skip_whitespace(self):
        while self._is_in_line() and self._char().isspace():
            self._inc()

    def match_keyword(self):
        self.skip_whitespace()
        if not self._is_in_line() or not self._is_alpha():
            return False

        mark = self.cursor
        while self._is_in_line() and self._is_alpha():
            self._inc()

        self.token = self.line[mark:self.cursor]
        return True

    def match_number(self):
        self.skip_whitespace()
        if not self._is_in_line() or not self._is_digit():
            return False

        mark = self.cursor
        while self._is_in_line() and self._is_digit():
            self._inc()

        self.token = self.line[mark:self.cursor]
        return True


    def match_string(self):
        self.skip_whitespace()
        if not self._is_in_line() or self._char() != '"':
            return False

        mark = self.cursor
        self._inc()
        while self._char() != '"':
            self._inc()
            if not self._is_in_line():
                raise IndexError("Unclosed string")

        self._inc()

        self.token = self.line[mark + 1:cursor - 1]
        return True

    def match_varname(self):
        self.skip_whitespace()
        if not self._is_in_line() or not self._is_alpha():
            return False

        mark = self.cursor
        while self._is_in_line() and self._is_alpnum():
            self._inc()

        self.token = self.line[mark:self.cursor]
        return True


    def _char(self):
        return self.line[self.cursor]

    def _inc(self):
        self.cursor += 1

    def _is_alnum(self):
        return self._char().isalnum()

    def _is_alpha(self):
        return self._char().isalpha()

    def _is_digit(self):
        return self._char().isdigit()

    def _is_in_line(self):
        return self.cursor < len(self.line)
