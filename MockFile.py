class MockFile:
    def __init__(self, filename):
        self.filename = filename
        self.content = []

    def write(self, string):
        self.content.append(string.strip())

    def read(self):
        if len(self.content) == 0:
            return self.content
        index0 = self.content[0]
        if index0.startswith('//'):
            return self.content[1:]
        return self.content
