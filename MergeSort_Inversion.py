#This was the merge sort class we made
class MergeSort_Inversion:
    def __init__(self):
        self.inversion_count = 0
    #This here is the mergesort method that will do mergesort
    #This also houses the inversion counter this part was easier then the rest since merge to me is better for inversion
    #This counts how many there is then it shows if i <  j swap them and put them in the right position
    def merge_sort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            left_half = array[:mid]
            right_half = array[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    array[k] = left_half[i]
                    i += 1
                else:
                    array[k] = right_half[j]
                    j += 1
                    self.inversion_count += (len(left_half) - i)
                k += 1

            while i < len(left_half):
                array[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                array[k] = right_half[j]
                j += 1
                k += 1

    def count_inversions_in_file(self, inputFilename):
        with open(inputFilename, 'r') as file:
            array = [int(line) for line in file.readlines()]

        self.inversion_count = 0
        self.merge_sort(array)

        return self.inversion_count


# Usage
#This just houses where you will put in the file address/ path and then it will output to the screen
if __name__ == "__main__":
    #You put the file address here
    inputFilename = "/Users/izzyababy/Desktop/Project1/source1.txt"

    inversion_counter = MergeSort_Inversion()
    inversions = inversion_counter.count_inversions_in_file(inputFilename)
    print("Inversion Count:", inversions)
