import answers


with open("best.py", "w") as f:
    f.write("import random\n\n\n")
    f.write("class Best:\n\n")
    for value in answers.answers:
        f.write(f"    {value} = {repr(answers.answers[value])}" + "\n")
    f.write("\n")
    f.write("    def __getattribute__(self, name):\n")
    f.write("        # Return random value in list\n")
    f.write("        return random.choice(self.name)\n")
