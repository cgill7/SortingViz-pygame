import algos
import time
import pygame
import os
import sys

pygame.init()
dimensions = [1050, 512]
window = pygame.display.set_mode((dimensions[0], dimensions[1]))
window.fill((102, 102, 153))

algorithms = {
                "BubbleSort" : algos.bsort(), 
                "MergeSort" : algos.mergesort(), 
                "SelectionSort" : algos.selectionsort(),
                "QuickSort" : algos.quicksort(), 
                "InsertionSort" : algos.inssort()
                }

    
def ifquit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
def dontquit(time, algorithm, window):
    pygame.display.set_caption("SORTING VISUALIZER:)         ALGORITHM USED - {}     TIME ELAPSED - {:.3f}".format(algorithm.name, time))
    running = True
    while running:
        ifquit()
    
        
def update(algorithm, swap1 = None, swap2 = None, window=window):
    window.fill((102, 102, 153))
    pygame.display.set_caption("SORTING VISUALIZER:)         ALGORITHM USED - {}     TIME ELAPSED - {:.3f}".format(algorithm.name, time.time()-algorithm.start_time))
    k = int(dimensions[0]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        colour = (255, 102, 0)
        if swap1 == algorithm.array[i]:
            colour = (0,255,0)
        elif swap2 == algorithm.array[i]:
            colour = (255,0,0)
        pygame.draw.rect(display, colour, (i*k,dimensions[1],k,-algorithm.array[i]))
    ifquit()
    pygame.display.update()
     
def main(val):
    if len(val) < 2:
        print("Algorithm not selected")
    elif val[1] == "menu":
         print("Algorithms:\n\t" + "\n\t".join(algorithms.keys()))
         sys.exit(0)
    else:
        try:
           algorithm = algorithms[val[1]] 
           time_elapsed = algorithm.run() 
           dontquit(time_elapsed, algorithm, window)
        except:
            print("ERROR")
            
if __name__ == "__main__":
    sys.argv.append("BubbleSort")
    main(sys.argv)
