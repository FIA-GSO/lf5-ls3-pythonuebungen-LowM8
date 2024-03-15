import math
# This is a sample Python script.
# Press Umschalt+F10 to execute it or replace it with your code.

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#---------------------Aufgabe 1 ------------------------------------
def compute_r2d2_population(steps: int) -> tuple[int,int,int]:
    
    young_r2 = 10
    adult_r2 = 10
    old_r2 = 10


    if steps == 0:
        return(young_r2, adult_r2, old_r2)

    
    for _ in range(0, steps):

        temp_adult = adult_r2
        
        adult_r2 = young_r2/2
        young_r2 = temp_adult*4
        young_r2 = young_r2 + old_r2*2
        old_r2 = math.floor(temp_adult/3) 
    
    return(young_r2, adult_r2, old_r2)

#---------------------Aufgabe 2 Streichholz------------------------------
#IMPLEMENT YOUR SOLUTION FOR THE STEICHHOLZSPIEL HERE


streichhölzer = 31

print("Geben Sie Etwas ein")
test = int(input())

print(test)
#---------------------Aufgabe 3 Heron ------------------------------------
def heron_verfahren(area : float, threshold:float) -> float:
    """
        computes the square root using the heron method
    :param area: size of the area e.g.25
    :param threshold: threshold for the heron method e.g. 0.01
    :return:the square root of the given area according to the heron method
    """

    return 0


#---------------------Aufgabe 4 Quersumme------------------------------
#IMPLEMENT, IF NECESSARY, EXERCISE 4 HERE BUT USE A FUNCTION!


#---------------MANAGEMENT----------------------
#-------------COMMENT/UNCOMMENT lines to launch the different exercises
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("You need to adjust this code to run your implementation")

    # Aufgabe 1
    print(f"""
        # R2D2 Population after 5 steps is: 
        # Young: {compute_r2d2_population(5)[0]}
        # Adults: {compute_r2d2_population(5)[1]}
        # Old: {compute_r2d2_population(5)[2]}""")
    # print (compute_r2d2_population(5))

    # Aufgabe 2
    # TO BE IMPLEMENTED

    # Aufgabe 3
    print (f"Die Wurzel für die Fläche 25 und Grenze 0.01 nach Heron ist: {heron_verfahren(25, 0.01)}")

    # Aufgabe 4
    # TO BE IMPLEMENTED

    # Use a breakpoint in the code line below to debug your script.


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
