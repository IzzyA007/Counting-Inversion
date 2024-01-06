#This is the Insertion sort class
class InsertionSort_Inversion:
    def __init__(self):
        self.inversion_count = 0
    #this is the method for the insertion sort I picked this one just cause I was more good with it
    #Inside here also the inversion counter is started swaping around the numbers that are in the wrong order
    #The numbers are then rearange around and put in the write place
    #The len will count the numbers in the array to then sort with using the inversion formula
    def insertion_sort(self, array):
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
                self.inversion_count += 1
            array[j + 1] = key
    #This then here will count the inversion in the file this process is key since we need it to run the source code
    def count_inversions_in_file(self, input_filename):
        with open(input_filename, 'r') as file:
            array = [int(line) for line in file.readlines()]

        self.inversion_count = 0
        self.insertion_sort(array)

        return self.inversion_count


# Usage
#From here the project wraps around to the end using the input file
#You can put the source address of the input file to then check how many inversion there are
#This will then print the output to the screen
if __name__ == "__main__":
    input_Filename = "/Users/izzyababy/Desktop/Project1/source1.txt"

    inversion_counter = InsertionSort_Inversion()
    inversions = inversion_counter.count_inversions_in_file(input_Filename)
    print("Inversion Count:", inversions)
