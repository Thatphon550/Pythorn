from tkinter import *

class graph_display:
    def __init__(self):
        window = Tk()
        window.title("Display a Graph")

        self.canvas = Canvas(window, width= 300, height=250)
        self.canvas.pack()

        self.x = 40
        self.y = 40
        self.i = 0
        self.distance = 80
        self.pos_of_vertices = []

        infile = open("graph.txt", "r")
        self.display_graph(infile)


        infile.close()
        window.mainloop()

    def display_graph(self, infile):
        for i, line in enumerate(infile):
            if i == 0:
                continue
            self.display_vertices()
        infile.seek(0)

        for j, line in enumerate(infile):
            if j == 0:
                continue
            self.display_lines(j, line)


    def display_vertices(self):
        if self.i % 2 == 0:
            self.canvas.create_oval(
                self.x - 3, self.y - 3,
                self.x + 3, self.y + 3,
                fill= "black"
            )
            self.canvas.create_text(
                self.x - 5, self.y - 9,
                text=self.i
            )
            self.pos_of_vertices.append([self.x, self.y])
        else:
            self.canvas.create_oval(
                self.x + self.distance - 3, self.y - 3,
                self.x + self.distance + 3, self.y + 3,
                fill= "black"
            )
            self.canvas.create_text(
                self.x + self.distance - 5, self.y - 9,
                text=self.i
            )
            self.pos_of_vertices.append([self.x + self.distance, self.y])
            self.y += self.distance
        self.i += 1

    def display_lines(self, j, line):
        for i in line.split()[3:]:
            self.canvas.create_line(
                self.pos_of_vertices[j - 1][0], self.pos_of_vertices[j - 1][1],
                self.pos_of_vertices[int(i)][0], self.pos_of_vertices[int(i)][1]
            )

graph_display()
