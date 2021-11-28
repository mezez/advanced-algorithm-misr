from utils import convertPath
import numpy as np
import time
from tkinter import *
from tkinter import filedialog
np.random.seed(0)


class Gui(object):
    root = Tk()
    root.geometry("1920x1000")
    uploaded_file_name = ""
    # SOME CONSTANTS
    CONST_BRANCH_AND_BOUND = "branch_and_bound"
    CONST_ANT_COLONY = "ant_colony"
    CONST_BRUTE_FORCE = "brute_force"
    CONST_DYNAMIC = "dynamic_programming"
    CONST_TWO_OPT_ALGORITHM = "two_opt_algorithm"
    CONST_GREEDY = "greedy"
    CONST_APPROXIMATION = "approximation"
    CONST_GENETIC = "genetic"
    # default active screen
    activeScreen = CONST_BRANCH_AND_BOUND
    active_screen_text = StringVar()
    matrix_dimension_text = StringVar()
    matrix_min_bound_text = StringVar()
    matrix_max_bound_text = StringVar()
    upload_label_text = StringVar()
    cost_result_label_text = StringVar()
    path_result_label_text = StringVar()
    time_result_label_text = StringVar()
    matrix_label_text = StringVar()
    matrixDimension = Entry(root, width=1)
    minBound = Entry(root, width=1)
    maxBound = Entry(root, width=1)
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
                                      command=Gui.set_active_screen_branch_and_bound)
        antColonyButton = Button(text="Ant Colony Optimization", padx=10, fg="blue",
                                 command=Gui.set_active_screen_aco)
        bruteForceButton = Button(text="Brute Force", padx=10, fg="blue",
                                  command=Gui.set_active_screen_brute)
        dynamicButton = Button(Gui.root, text="Dynamic Programming", padx=10, fg="blue",
                               command=Gui.set_active_screen_dynamic)
        twoOptAlgorithButton = Button(text="Two Opt Algorithm", padx=10, fg="blue",
                                      command=Gui.set_active_screen_two_opt)
        greedyButton = Button(text="Greedy", padx=10,
                              fg="blue", command=Gui.set_active_screen_greedy)
        approximationButton = Button(text="MST Approximation", padx=10, fg="blue",
                                     command=Gui.set_active_screen_approximation)
        geneticButton = Button(text="Genetic Programming", padx=10, fg="blue",
                               command=Gui.set_active_screen_genetic)
        matrix_dimension_label = Label(
            Gui.root, textvariable=Gui.matrix_dimension_text)
        matrix_min_bound_label = Label(
            Gui.root, textvariable=Gui.matrix_min_bound_text)
        matrix_max_bound_label = Label(
            Gui.root, textvariable=Gui.matrix_max_bound_text)
        generateMatrixButton = Button(text="Generate Random Matrix", fg="blue",
                                      command=Gui.generateMatrix)
        uploadFileButton = Button(text="Upload Matrix File", fg="blue",
                                  command=Gui.uploadFile)
        branchAndBoundButton.grid(row=1, column=1, sticky="ew")
        antColonyButton.grid(row=1, column=2, sticky="ew")
        bruteForceButton.grid(row=1, column=3, sticky="ew")
        dynamicButton.grid(row=1, column=4, sticky="ew")
        twoOptAlgorithButton.grid(row=1, column=5, sticky="ew")
        greedyButton.grid(row=1, column=6, sticky="ew")
        approximationButton.grid(row=1, column=7, sticky="ew")
        geneticButton.grid(row=1, column=8, sticky="ew")
        geneticButton.grid(row=1, column=8, sticky="ew")
        Gui.space1Label.grid(row=3, column=0, sticky="ew")
        Gui.matrixDimension.grid(row=4, column=1, sticky="ew", padx=10,)
        Gui.minBound.grid(row=5, column=1, sticky="ew", padx=10)
        Gui.maxBound.grid(row=6, column=1, sticky="ew", padx=10)
        generateMatrixButton.grid(row=5, column=2, sticky="ew")
        uploadFileButton.grid(row=5, column=4, sticky="ew")
        active_screen_label = Label(
            Gui.root, textvariable=Gui.active_screen_text)
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        active_screen_label.grid(row=2, column=0, sticky="ew")
        Gui.matrix_dimension_text.set("Enter matrix size N: ")
        matrix_dimension_label.grid(row=4, column=0, sticky="ew")
        Gui.matrix_min_bound_text.set("Enter minimum value of cost: ")
        matrix_min_bound_label.grid(row=5, column=0, sticky="ew")
        Gui.matrix_max_bound_text.set("Enter maximum value of cost: ")
        matrix_max_bound_label.grid(row=6, column=0, sticky="ew")
        uploadLabel = Label(Gui.root, textvariable=Gui.upload_label_text)
        Gui.upload_label_text.set("Filename: none")
        uploadLabel.grid(row=5, column=5, columnspan=7, sticky="ew")
        Gui.root.mainloop()

    @staticmethod
    def set_active_screen(screen_name):
        Gui.activeScreen = screen_name
        return

    @staticmethod
    def set_active_screen_branch_and_bound():
        Gui.activeScreen = Gui.CONST_BRANCH_AND_BOUND
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        return

    @staticmethod
    def set_active_screen_aco():
        Gui.activeScreen = Gui.CONST_ANT_COLONY
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        return

    @staticmethod
    def set_active_screen_genetic():
        Gui.activeScreen = Gui.CONST_GENETIC
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        return

    @staticmethod
    def set_active_screen_approximation():
        Gui.activeScreen = Gui.CONST_APPROXIMATION
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        return

    @staticmethod
    def set_active_screen_two_opt():
        Gui.activeScreen = Gui.CONST_TWO_OPT_ALGORITHM
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        return

    @staticmethod
    def set_active_screen_greedy():
        Gui.activeScreen = Gui.CONST_GREEDY
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        return

    @staticmethod
    def set_active_screen_dynamic():
        Gui.activeScreen = Gui.CONST_DYNAMIC
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        return

    @staticmethod
    def set_active_screen_brute():
        Gui.activeScreen = Gui.CONST_BRUTE_FORCE
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        return

    @staticmethod
    def generateMatrix():
        # generate matrix
        matrix_length = int(Gui.matrixDimension.get())
        minBound = int(Gui.minBound.get())
        maxBound = int(Gui.maxBound.get())
        current_row = 0
        cost_matrix = [[0 for x in range(matrix_length)] for y in range(
            matrix_length)]  # initialize node with 0 costs
        for i in range(matrix_length):
            current_column = 0
            for j in range(matrix_length):
                if current_row != current_column:  # change cost if the movement is to a different node, for same node, leave as 0
                    cost_matrix[i][j] = np.random.randint(minBound, maxBound)
                current_column = current_column + 1
            current_row = current_row + 1
        Gui.uploadFile(cost_matrix)

    @staticmethod
    def uploadFile(matrix=None):
        if matrix:
            uploaded_file = matrix
        else:
            uploaded_file = filedialog.askopenfilename(initialdir="./tsp_database", title="Matrix file",
                                                       filetypes=(("Excel Files", "*.xlsx"),))
            Gui.upload_label_text.set("Filepath: " + uploaded_file)
            Gui.uploaded_file_name = uploaded_file
        # select module base on active screen
        if Gui.activeScreen == Gui.CONST_BRANCH_AND_BOUND:
            from branch_and_bound import matr
            start_time = time.time()
            # run computations and return response list
            response = matr(uploaded_file)
            end_time = time.time()
            time_taken = end_time-start_time
            response.append(time_taken)  # time taken for computation
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
            response = geneticApproach(uploaded_file)
            end_time = time.time()
            time_taken = end_time - start_time
            response.append(time_taken)
            Gui.set_screen_content(response)
        if Gui.activeScreen == Gui.CONST_APPROXIMATION:
            from approximation_mst import approximationMST
            start_time = time.time()
            response = approximationMST(uploaded_file)
            end_time = time.time()
            time_taken = end_time - start_time
            response.append(time_taken)
            Gui.set_screen_content(response)
        if Gui.activeScreen == Gui.CONST_TWO_OPT_ALGORITHM:
            from py2opt import compute
            start_time = time.time()
            response = compute(uploaded_file)
            end_time = time.time()
            time_taken = end_time - start_time
            response.append(time_taken)
            Gui.set_screen_content(response)
        if Gui.activeScreen == Gui.CONST_GREEDY:
            from greedy import compute
            start_time = time.time()
            response = compute(uploaded_file)
            end_time = time.time()
            time_taken = end_time - start_time
            response.append(time_taken)
            Gui.set_screen_content(response)
        if Gui.activeScreen == Gui.CONST_DYNAMIC:
            from dynamic_programing import dynamic_programing
            start_time = time.time()
            response = dynamic_programing(uploaded_file)
            end_time = time.time()
            time_taken = end_time - start_time
            response.append(time_taken)
            Gui.set_screen_content(response)
        if Gui.activeScreen == Gui.CONST_BRUTE_FORCE:
            from brute_force import brute_force
            start_time = time.time()
            response = brute_force(uploaded_file)
            end_time = time.time()
            time_taken = end_time - start_time
            response.append(time_taken)
            Gui.set_screen_content(response)
        return

    @staticmethod
    def set_screen_content(result):
        frame = LabelFrame(Gui.root)
        frame.grid(row=7, column=0, columnspan=12,
                   rowspan=12, sticky="nsew", pady=2)
        cost_result_label = Label(
            frame, textvariable=Gui.cost_result_label_text)
        path_result_label = Label(
            frame, textvariable=Gui.path_result_label_text)
        time_result_label = Label(
            frame, textvariable=Gui.time_result_label_text)
        matrix_label = Label(frame, textvariable=Gui.matrix_label_text)
        Gui.cost_result_label_text.set("Minimum Cost : " + str(result[0]))
        Gui.path_result_label_text.set("Path Taken: " + convertPath(result[1]))
        Gui.time_result_label_text.set(
            "Time taken: " + str(result[3]) + " Seconds")
        Gui.matrix_label_text.set("Matrix: ")
        cost_result_label.grid(row=0, column=0)
        path_result_label.grid(row=0, column=1)
        time_result_label.grid(row=1, column=0)
        matrix_label.grid(row=2, column=0)
        matrix = Text(frame, width="100", font=("Helvetica", 10))
        matrix.grid(row=2, column=1, pady=10)
        matrix.insert(END, str(np.array(result[2])))
        return


if __name__ == '__main__':
    Gui().main()
