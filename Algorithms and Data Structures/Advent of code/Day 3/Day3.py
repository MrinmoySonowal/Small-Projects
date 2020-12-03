class TobogganTrajectory:
    def __init__(self, right_steps, down_steps):
        self.file = open('input.txt', 'r')
        self.line_size = len(self.file.readline()) - 1  # Since line ends with a new line
        self.right_steps = right_steps
        self.down_steps = down_steps
        self.file.seek(0, 0)

    def count_trees_map(self):
        index = count = line_no = 0
        for line in self.file:
            if line_no % self.down_steps == 0:
                count += line[index % self.line_size] == '#'
                index += self.right_steps
            line_no += 1
        self.file.close()
        return count


slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
product = 1
for slope in slopes:
    product *= TobogganTrajectory(slope[0], slope[1]).count_trees_map()
print(product)
