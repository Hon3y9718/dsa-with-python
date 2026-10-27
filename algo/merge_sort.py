class MergeSorter:
    def sort(self, arr: list) -> list:
        """Recursively sorts the array using the merge sort algorithm."""
        # Base case: arrays with 0 or 1 element are already sorted
        if len(arr) <= 1:
            return arr
        
        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = self.sort(arr[:mid])
        right_half = self.sort(arr[mid:])
        
        # Merge the sorted halves back together
        return self._merge(left_half, right_half)
    
    def _merge(self, left: list, right: list) -> list:   ## _ means this function is private
        """Combines two sorted sub-arrays into a single sorted array."""
        sorted_arr = []
        i = j = 0
        
        # Compare elements from both sub-arrays and append the smaller one
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1

        # Append any remaining elements (one of the lists will be exhausted)
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])
        
        return sorted_arr

# --- Example Usage ---
if __name__ == "__main__": ### -> Entry Point (Code execution Starts here)
    sorter = MergeSorter()
    numbers = [38, 27, 43, 3, 9, 82, 10]
    
    print(f"Original: {numbers}")
    sorted_numbers = sorter.sort(numbers)
    print(f"Sorted:   {sorted_numbers}")
