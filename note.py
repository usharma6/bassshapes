notes = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F':6, 'G':7}

class Note:
    def __init__(self, length, pitch)
        self.length = length
        self.pitch = notes[pitch]

    def __str__(self):
        return "length: " + self.length + "\n" + "pitch: " + self.pitch + "\n"
