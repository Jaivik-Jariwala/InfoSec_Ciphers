buffer_size = 10  # Set the buffer size 10 characters at a time

with open('buffered_example.txt', 'w', buffering=buffer_size) as file:
    for i in range(1, 6):
        file.write(f"This is line {i}\n")

print("Task4: Buffering is done")

'''
 Buffering allows you to accumulate data in memory and then write it in larger chunks, reducing 
 the number of system calls required to write the data.

 Here's what happens in the loop:
 The loop iterates from 1 to 5.
 In each iteration, it writes a line of text to the file, and the data is buffered in memory.
 Once the buffer is filled with 10 characters (or a newline character \n is encountered), 
 the buffered data is flushed (written) to the file.
 The primary use of buffering is to improve the efficiency of data transfer, processing and improving latency.
 buffering can have performance implications and can affect the behavior of your code, 
 so it's important to choose an appropriate buffering strategy based on your specific requirements. 
 In real-world scenarios, you might choose a buffer size that balances performance and memory 
 consumption based on the nature of your application.'''