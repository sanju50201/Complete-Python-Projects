import random

# create a MadLibs class


class MadLibs:
    def __init__(self, filename):
        self.filename = filename
        self.word_list = []

    # create a method to read the file

    def read_file(self):
        with open(self.filename, 'r') as f:
            self.word_list = f.read().split()

    # method to generate story

    def generate_story(self):
        story = ""
        with open(self.filename, 'r') as f:
            for line in f:
                for word in line.split():
                    if word.startswith("<") and word.endswith(">"):
                        story += " " + random.choice(self.word_list)
                    else:
                        story += " " + word
        return story


# create an instance of the class
if __name__ == "__main__":
    madlibs = MadLibs('./resources/madlibs.txt')
    madlibs.read_file()
    print(madlibs.generate_story())
