import time
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
    time_result_label_text = StringVar()
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
                                     command=Gui.set_active_screen_approximation)
        geneticButton = Button(text="Genetic Programming", padx=10, fg="blue",
                               command=Gui.set_active_screen_genetic)
        uploadFileButton = Button(text="Upload Matrix File", padx=10, fg="blue",
                                  command=Gui.uploadFile)

        branchAndBoundButton.grid(row=1, column=1, sticky="ew")
        antColonyButton.grid(row=1, column=2, sticky="ew")
        bruteForceButton.grid(row=1, column=3, sticky="ew")
        dynamicButton.grid(row=1, column=4, sticky="ew")
        edgeBranchAndBoundButton.grid(row=1, column=5, sticky="ew")
        greedyButton.grid(row=1, column=6, sticky="ew")
        approximationButton.grid(row=1, column=7, sticky="ew")
        geneticButton.grid(row=1, column=8, sticky="ew")
        geneticButton.grid(row=1, column=8, sticky="ew")
        Gui.space1Label.grid(row=3, column=0, sticky="ew")
        uploadFileButton.grid(row=4, column=0, sticky="ew")

        active_screen_label = Label(Gui.root, textvariable=Gui.active_screen_text)
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        active_screen_label.grid(row=2, column=0, sticky="ew")

        uploadLabel = Label(Gui.root, textvariable=Gui.upload_label_text)
        Gui.upload_label_text.set("Filename: none")
        uploadLabel.grid(row=4, column=1, columnspan=8, sticky="ew")

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
    def set_active_screen_genetic():
        Gui.activeScreen = Gui.CONST_GENETIC
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        print(Gui.activeScreen)
        return
    @staticmethod
    def set_active_screen_approximation():
        Gui.activeScreen = Gui.CONST_APPROXIMATION
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        print(Gui.activeScreen)
        return

    @staticmethod
    def uploadFile():
        uploaded_file = filedialog.askopenfilename(initialdir="./", title="Matrix file",
                                                   filetypes=(("Excel Files", "*.xlsx"),))
        Gui.upload_label_text.set("Filepath: " + uploaded_file)
        Gui.uploaded_file_name = uploaded_file

        # select module base on active screen
        if Gui.activeScreen == Gui.CONST_BRANCH_AND_BOUND:
            from branch_and_bound import matr
            start_time = time.time()
            response = matr(uploaded_file)
            end_time = time.time()
            time_taken = end_time-start_time
            response.append(time_taken)
            Gui.set_screen_content(response)
        if Gui.activeScreen == Gui.CONST_ANT_COLONY:
            from ant_colony_optimization import compute
            start_time = time.time()
            response = compute(uploaded_file)
            end_time = time.time()
            time_taken = end_time - start_time
            response.append(time_taken)
            Gui.set_screen_content(response)
        if Gui.activeScreen == Gui.CONST_GENETIC:
            from genetic_approach import geneticApproach
            start_time = time.time()
            response  = geneticApproach(uploaded_file)
            end_time = time.time()
            time_taken = end_time - start_time
            response.append(time_taken)
            Gui.set_screen_content(response)
        if Gui.activeScreen == Gui.CONST_APPROXIMATION:
            from approximation_mst import approximationMST
            start_time = time.time()
            response  = approximationMST(uploaded_file)
            end_time = time.time()
            time_taken = end_time - start_time
            response.append(time_taken)
            Gui.set_screen_content(response)           
        return

    @staticmethod
    def set_screen_content(result):
        frame = LabelFrame(Gui.root, )
        frame.grid(row=5, column=0, columnspan=9, rowspan=9, sticky="nsew", padx=2, pady=2)

        cost_result_label = Label(frame, textvariable=Gui.cost_result_label_text)
        path_result_label = Label(frame, textvariable=Gui.path_result_label_text)
        time_label = Label(frame, text="Time Taken:")
        time_result_label = Label(frame, textvariable=Gui.time_result_label_text)
        matrix_label = Label(frame, textvariable=Gui.matrix_label_text)

        Gui.cost_result_label_text.set("Minimum Cost : " + str(result[0]))
        Gui.path_result_label_text.set("Path Taken: " + result[1])
        Gui.time_result_label_text.set(str(result[3]) + " Seconds")
        Gui.matrix_label_text.set("Matrix: ")

        cost_result_label.grid(row=0, column=0)
        path_result_label.grid(row=0, column=1)
        time_label.grid(row=1, column=0)
        time_result_label.grid(row=1, column=1)
        matrix_label.grid(row=2, column=0)

        matrix = Text(frame, width=40, height=10, font=("Helvetica", 10))
        matrix.grid(row=2, column=1, pady=10)

        matrix.insert(END, str(result[2]))
        return


if __name__ == '__main__':
    Gui().main()
