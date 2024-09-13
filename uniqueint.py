#!/usr/bin/python3

class UniqueInt:
    @staticmethod
    def processFile(input_file_path, output_file_path):
        """
        Reads all unique integers from the specified file path and store
        the sorted result into the specified output file path
        """
        integers = UniqueInt.readUniqueIntegers(input_file_path)
        UniqueInt.sort(integers)

        with open(output_file_path, 'w') as file:
            for integer in integers:
                file.write(str(integer) + "\n")

        print(f"Processed the unique integers from {
              input_file_path} to {output_file_path}")

    @staticmethod
    def readUniqueIntegers(file_path):
        """
        Reads all the unique integers from the specified file path
        """
        unique_integers = []
        with open(file_path, 'r') as file:
            for line in file:
                # Process the current line
                integer = UniqueInt.processLine(line)
                if integer is not None and not UniqueInt.contains(unique_integers, integer):
                    unique_integers.append(integer)
        return unique_integers

    @staticmethod
    def processLine(line):
        """
        Processes a line into an integer, by first removing all surrounding
        whitespace and returning an integer if the line contains a valid
        integer
        """
        stripped_line = UniqueInt.strip(line)

        # Skip empty lines
        if not stripped_line:
            return None

        print(f"h{stripped_line}h")
        print(UniqueInt.is_integer(stripped_line))

        # Try to convert the line to an integer
        if UniqueInt.is_integer(stripped_line):
            return int(stripped_line)

        return None

    @staticmethod
    def ask_user():
        """
        This function kicks of the program by asking the user for an input
        file's path, loading the unique integers, sort them and then store them
        in the specified output file path
        """
        input_file_path = input("Enter the input file path: ")

        output_file_path = input("Enter the output file path: ")

        UniqueInt.processFile(input_file_path, output_file_path)

    # Standard functions

    @staticmethod
    def is_integer(s):
        """
        This function checks whether a string (which may contain a number sign
        as prefix) is a valid integer
        """
        # may contain a number sign as prefix
        if s[0] in ('-', '+'):
            return s[1:].isdigit()

        return s.isdigit()

    @staticmethod
    def strip(s):
        """
        Remove all starting and trailing whitepsce from a string
        """
        result = ""
        i = 0
        space_characters = (' ', '\t', '\n')
        while i < len(s) and (s[i] in space_characters):
            i += 1
        j = len(s) - 1
        while j >= 0 and (s[j] in space_characters):
            j -= 1
        for k in range(i, j + 1):
            result += s[k]
        return result

    @staticmethod
    def split(s):
        """
        Strip a string into multiple parts separated by a space or tab
        character
        """
        parts = []
        part = ""
        for char in s:
            if char == ' ' or char == '\t':
                if part:
                    parts.append(part)
                    part = ""
            else:
                part += char
        if part:
            parts.append(part)
        return parts

    @staticmethod
    def contains(arr, value):
        """
        Checks whether a given item is included in the array
        """
        for item in arr:
            if item == value:
                return True
        return False

    @staticmethod
    def sort(arr):
        """
        Sort an array using a simple bubble sort algorithm
        """
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

UniqueInt.processFile("hello.txt", "world.txt")

"""
if __name__ == "__main__":
    UniqueInt.ask_user()
"""

"""
if __name__ == "__main__":
    input_folder = "/home/kellia/UniqueInt/inputs"
    output_folder = "/home/kellia/UniqueInt/results"
    
    unique_int_processor = UniqueInt()

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{filename}_results.txt")

            # Timing for each file
            start_time = time.time()
            unique_int_processor.process_file(input_path, output_path)
            end_time = time.time()

            print(f"Processed {filename} in {end_time - start_time:.4f} seconds")
"""
