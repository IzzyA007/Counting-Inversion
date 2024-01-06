class Quicksort_Inversion:
    def __init__(self):
        #This is the inversion counter
        self.inversion_count = 0
    #This is the quick sort algo
    #This will start the process for the inversion
    #But first we need the quicksort

    #I then made the quick sort method to implimate the sorting
    #this part was fine just because of the history in data sturtures
    def quick_sort(self, array, start, end):
        if start < end:
            pivot_index, inversions = self.partition(array, start, end)
            self.inversion_count += inversions

            self.quick_sort(array, start, pivot_index - 1)
            self.quick_sort(array, pivot_index + 1, end)
    #This starts the inversions process with the array
    def partition(self, array, start, end):
        pivot = array[end]
        i = start - 1
        #this will store the count of the inversions
        inversions = 0

        #This is the inversion formula that will make a inversion and swap the correct numbers in the right places in order
        for j in range(start, end):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
                inversions += (j - i)

        array[i + 1], array[end] = array[end], array[i + 1]
        return i + 1, inversions

    def count_inversions_in_file(self, input_filename):
        with open(input_filename, 'r') as file:
            array = [int(line) for line in file.readlines()]

        self.inversion_count = 0
        self.quick_sort(array, 0, len(array) - 1)
        #This will then return the value of the inversion and put it in inversion object
        return self.inversion_count


# Usage
if __name__ == "__main__":
    #This is where you will put in the address/path of the file that you would like to input and run the inversions
    #You can put any file in there
    inputFilename = "/Users/izzyababy/Desktop/Project1/source5.txt"
    #this will then pull the code from the quicksort class I made
    inversion_counter = Quicksort_Inversion()
    inversions = inversion_counter.count_inversions_in_file(inputFilename)
    #This will print how many inversion there are and will output it in the screen
    print("Inversion Count:", inversions)
