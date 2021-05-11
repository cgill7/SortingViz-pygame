import time
import random
from abc import ABCMeta, abstractmethod

class algo(metaclass=ABCMeta):
    def __init__(self, name):
        self.array = random.sample(range(512), 512)
        self.name = name
    
    def update_display(self, swap1=None, swap2=None):
        import sortingviz
        sortingviz.update(self, swap1, swap2)
        
    def run(self):
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed
 
#   
@abstractmethod
def algorithm(self):
    raise TypeError(f"Algorithm.algorithm() has not been overwritten.")
#

class bsort(algo):
    def __init__(self):
        super().__init__("BubbleSort")
    
    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)-1-i):
                if (self.array[j] > self.array[j+1]):
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
            self.update_display(self.array[j], self.array[j+1])
            
class mergesort(algo):
    def __init__(self):
        super(mergesort, self).__init__("MergeSort")
    
    def algorithm(self, array = []):
        if (array == []):
            array = self.array
        if (len(array) < 2):
            return array
        mid = len(array) // 2 
        left = self.algorithm(array[:mid])
        right = self.algorithm(array[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if (left[i] < right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            self.update_display()
        result += left[i:]
        result += right[j:]
        self.array = result
        self.update_display()
        return result
    
class selectionsort(algo):
    def __init__(self):
        super().__init__("SelectionSort")
    
    def algorithm(self):
        for i in range(len(self.array)):
            min_indx = i 
            for j in range(i+1, len(self.array)):
                if (self.array[min_indx] > self.array[j]):
                 min_indx = j
        self.array[i], self.array[min_indx] = self.array[min_indx], self.array[i]
        self.update_display(self.array[i], self.array[min_indx])
                
class quicksort(algo):
    def __init__(self):
        super().__init__("QuickSort")

    def algorithm(self, array=[], start=0, end=0):
        if array == []:
            array = self.array
            end = len(array) - 1
        if start < end:
            pivot = self.partition(array,start,end)
            self.algorithm(array,start,pivot-1)
            self.algorithm(array,pivot+1,end)

    def partition(self, array, start, end):
        x = array[end]
        i = start-1
        for j in range(start, end+1, 1):
            if array[j] <= x:
                i += 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                    self.update_display(array[i], array[j])
        return i
    
class inssort(algo):
    def __init__(self):
        super().__init__("InsertionSort")
    
    def algorithm(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i-1
            while j >= 0 and key < self.array[j]:
                self.array[j+1] = self.array[j]
                j -= 1
            self.array[j +1] = key
            self.update_display(self.array[j], self.array[i])