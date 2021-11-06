from tkinter import *


class Gui(object):
    root = Tk()

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

    # create a label widget
    titleLabel = Label(root, text="Advanced algorithm Project")
    categoriesLabel = Label(root, text="Categories:")

    # add the widget to the screen
    # titleLabel.pack() #window will be only as big as its content
    titleLabel.grid(row=0, column=0)
    categoriesLabel.grid(row=1, column=0)

    def main(self):
        # create menu buttons
        branchAndBoundButton = Button(text="Branch And Bound", padx=10,
                                      # command=Gui.set_active_screen(self, Gui.CONST_BRANCH_AND_BOUND))
                                      command=Gui.set_active_screen_branch_and_bound)
        antColonyButton = Button(text="Ant Colony Optimization", padx=10,
                                 command=Gui.set_active_screen_aco)
        bruteForceButton = Button(text="Brute Force", padx=10,
                                  command=Gui.set_active_screen_branch_and_bound)
        dynamicButton = Button(Gui.root, text="Dynamic Programming", padx=10)
        edgeBranchAndBoundButton = Button(text="Edge Branch and Bound", padx=10,
                                          command=Gui.set_active_screen_branch_and_bound)
        greedyButton = Button(text="Greedy", padx=10, command=Gui.set_active_screen_branch_and_bound)
        approximationButton = Button(text="MST Approximation", padx=10,
                                     command=Gui.set_active_screen_branch_and_bound)
        geneticButton = Button(text="Genetic Programming", padx=10,
                               command=Gui.set_active_screen_branch_and_bound)

        branchAndBoundButton.grid(row=1, column=1)
        antColonyButton.grid(row=1, column=2)
        bruteForceButton.grid(row=1, column=3)
        dynamicButton.grid(row=1, column=4)
        edgeBranchAndBoundButton.grid(row=1, column=5)
        greedyButton.grid(row=1, column=6)
        approximationButton.grid(row=1, column=7)
        geneticButton.grid(row=1, column=8)


        active_screen_label = Label(Gui.root, textvariable=Gui.active_screen_text)
        Gui.active_screen_text.set("Active: " + Gui.activeScreen)
        active_screen_label.grid(row=2, column=0)

        Gui.root.mainloop()

    def set_active_screen(self, screen_name):
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

    def set_screen_content(self, active_screen_name):
        if active_screen_name == Gui.CONST_BRANCH_AND_BOUND:
            print('NOTHING')

        return


if __name__ == '__main__':
    Gui().main()
