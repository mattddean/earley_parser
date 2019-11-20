class Rule:
    def __init__(self, begin, ends, terminal, part_of_speech):
        self.begin = begin # piece that we start with
        self.ends = ends # array of things it can go to
        self.terminal = terminal
        self.part_of_speech = part_of_speech
    def __str__(self):
        return str({
            "begin": self.begin,
            "ends": self.ends,
            "terminal": self.terminal
        })