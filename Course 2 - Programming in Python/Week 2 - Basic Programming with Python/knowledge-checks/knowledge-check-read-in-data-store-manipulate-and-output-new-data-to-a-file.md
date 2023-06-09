# Knowledge Check: Read in data, store, manipulate and output new data to a file

1. What function allows reading and writing files in Python?
   - open()
   - read_write()
   - input()
   - output()
   ```
   Answer: open()
   Explanation: open() both reading and writing of files.
   ```

2. Which method allows reading of only a single line of a file containing multiple lines?
   - ead()
   - readall()
   - readline()
   - readlines()
   ```
   Answer: readline()
   Explanation: Readline allows the reading of a single line of a file.
   ```

3. What is the default mode for opening a file in python?
   - read mode
   - read and write
   - copy mode
   - write mode
   ```
   Answer: read mode
   Explanation: By default the file is opened in read mode.
   ```

4. What is the difference between write and append mode?
   - Nothing, they are both the same.
   - Write mode overwrites the existing data. Append mode adds new data to the existing file.
   - Write mode will append data to the existing file. Append will overwrite the data. 
   - Write mode will not allow edits if content already exists. Append mode will add new data to the file.
   ```
   Answer: Write mode overwrites the existing data. Append mode adds new data to the existing file.
   Explanation: Both write and append mode serve different usecases!
   ```

5. What error is returned if a file does not exist?
   - FileNotFoundError
   - LookupError
   - Exception
   - AssertionError 
   ```
   Answer: FileNotFoundError
   Explanation: The FileNotFoundError is returned when a file cannot be found.
   ```
