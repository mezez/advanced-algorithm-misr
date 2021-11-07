from tkinter import *
from tkinter import filedialog


class Gui(object):
    root = Tk()
    root.geometry("1200x600")
    # root.grid_rowconfigure(0, weight=1)
    # root.grid_columnconfigure(0, weight=1)

    uploaded_file_name = ""

    # SOME CONSTANTS
    CONST_BRANCH_AND_BOUND = "branch_and_bound"
    CONST_ANT_COLONY = "ant_colony"
    CONST_BRUTE_FORCE = "brute_force"
    CONST_DYNAMIC = "dynamic_programming"
    CONST_EDGE_BRANCH_AND_BOUND = "edge_branch_and_bound"
    CONST_GREEDY = "greedy"
    CONST_APPROXIMATION = "approximation"
    CONST_GENETIC = "genetic"

    # default active screen
    activeScreen = CONST_BRANCH_AND_BOUND

    active_screen_text = StringVar()
    upload_label_text = StringVar()
    cost_result_label_text = StringVar()
    path_result_label_text = StringVar()
    matrix_label_text = StringVar()

    # create a label widget
    titleLabel = Label(root, text="Advanced algorithm Project")
    categoriesLabel = Label(root, text="Categories:")
    space1Label = Label(root, text=" ")

    # add the widget to the screen
    # titleLabel.pack() #window will be only as big as its content
    titleLabel.grid(row=0, column=0)
    categoriesLabel.grid(row=1, column=0)

    @staticmethod
    def main():
        # create menu buttons
        branchAndBoundButton = Button(text="Branch And Bound", padx=10, fg="blue",
                                      # command=Gui.set_active_screen(self, Gui.CONST_BRANCH_AND_BOUND))
                                      command=Gui.set_active_screen_branch_and_bound)
        antColonyButton = Button(text="Ant Colony Optimization", padx=10, fg="blue",
                                 command=Gui.set_active_screen_aco)
        bruteForceButton = Button(text="Brute Force", padx=10, fg="blue",
                                  command=Gui.set_active_screen_branch_and_bound)
        dynamicButton = Button(Gui.root, text="Dynamic Programming", padx=10, fg="blue",
                               command=Gui.set_active_screen_branch_and_bound)
        edgeBranchAndBoundButton = Button(text="Edge Branch and Bound", padx=10, fg="blue",
                                          command=Gui.set_active_screen_branch_and_bound)
        greedyButton = Button(text="Greedy", padx=10, fg="blue", command=Gui.set_active_screen_branch_and_bound)
        approximationButton = Button(text="MST Approximation", padx=10, fg="blue",
                                     command=Gui.set_active_screen_branch_and_bound)
        geneticButton = Button(text="Genetic Programming", padx=10, fg="blue",
                               command=Gui.set_active_screen_branch_and_bound)
        uploadFileButton = Button(text="Upload Matrix File", padx=10, fg="blue",
                                  command=Gui.uploadFile)

        branchAndBoundButton.grid(row=1, column=1)
        antColonyButton.grid(row=1, column=2)
        bruteForceButton.grid(row=1, column=3)
        dynamicButton.grid(row=1, column=4)
        edgeBranchAndBoundButton.grid(row=1, column=5)
        greedyButton.grid(row=1, column=6)
        approximationButton.grid(row=1, column=7)
        geneticButton.grid(row=1, column=8)
        geneticButton.grid(row=1, column=8)
        Gui.space1Label.grid(row=3, column=0)
        uploadFileButton.grid(row=4, column=0)

        active_screen_label = Label(Gui.root, textvariable=Gui.active_screen_text)
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        active_screen_label.grid(row=2, column=0)

        uploadLabel = Label(Gui.root, textvariable=Gui.upload_label_text)
        Gui.upload_label_text.set("Filename: none")
        uploadLabel.grid(row=4, column=1)

        Gui.root.mainloop()

    @staticmethod
    def set_active_screen(screen_name):
        Gui.activeScreen = screen_name
        return

    @staticmethod
    def set_active_screen_branch_and_bound():
        Gui.activeScreen = Gui.CONST_BRANCH_AND_BOUND
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        print(Gui.activeScreen)
        return

    @staticmethod
    def set_active_screen_aco():
        Gui.activeScreen = Gui.CONST_ANT_COLONY
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        print(Gui.activeScreen)
        return

    @staticmethod
    def uploadFile():
        uploaded_file = filedialog.askopenfilename(initialdir="C:/", title="Matrix file",
                                                   filetypes=(("Excel Files", "*.xlsx"),))
        Gui.upload_label_text.set("Filepath: " + uploaded_file)
        Gui.uploaded_file_name = uploaded_file
        from branch_and_bound import matr
        response = matr(uploaded_file)
        Gui.set_screen_content(response)

        return

    @staticmethod
    def set_screen_content(result):
        frame = LabelFrame(Gui.root, )
        frame.grid(row=5, column=0, columnspan=6, sticky="ew", padx=2, pady=2)

        cost_result_label = Label(frame, textvariable=Gui.cost_result_label_text)
        path_result_label = Label(frame, textvariable=Gui.path_result_label_text)
        matrix_label = Label(frame, textvariable=Gui.matrix_label_text)
        Gui.cost_result_label_text.set("Minumum Cost : " + str(result[0]) + " |")
        Gui.path_result_label_text.set("Path Taken: " + result[1])
        Gui.matrix_label_text.set("Matrix: ")
        cost_result_label.grid(row=1, column=0)
        path_result_label.grid(row=1, column=1)
        matrix_label.grid(row=1, column=2)

        matrix = Text(frame, width=40, height=10, font=("Helvetica", 10))
        matrix.grid(row=1, column=3, pady=10)

        matrix.insert(END, str(result[2]))
        return


if __name__ == '__main__':
    Gui().main()
