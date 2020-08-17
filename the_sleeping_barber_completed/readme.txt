In this readme I will be going over the following:
    My approach to the problem
    How did I test this code?
    What bugs remain?
    Limitations

After many days of draeing out plans, i decided that the threads were going to represent a customer entered and then workiing their way through the shop.
I had drawn out the many scenerios, all the if's and elses and decided that my code was clean enough to implement. 

I used recursion for my haircut function to keep my code tidy.

The first thing I did was get my code working with a single thread. Ths program was extremely slow and I soon saw the importance of the threading module.

The most effieciant way i used to test the code and its behaviour was by having good output give me back all the information i needed. The next big test was the actual purpose of the threads.
Was it actually speeding up my program? Using time module I found that yes it was. I did this all the way through the 40, 60 anf finally 100 percent solution.
If at any time my tests wernt going to plan, I would go back to pencil and paper and retrace my steps. The keyboard was always the last thing used, until I thought
my way through my solution. I used the random module to cover a wide range of tests fast. Also by doing this I wanted to insure thst the user of the program
would easily be able to change just about anything; number of customers, time rnages between them, time taken for the trim and how many barbers(freechairs) there are available.

The tried to address the flaws one by one as the program was being built. I originally built the program in lcasses across multiple files but then reverted back to a
 simpiler one file format as I didnt think it was necessary. I think there is many bugs, many unknown to me. I believe this because I didnt find a use for mutex which 
 I had researched but could find no useful implementation in my code. Because my barbers were a variable, it was changed quite fast and the threads( in my testing ) never got 
 to it at the same time. A bug I did find though is that in my output. I have tried to keep it as clean as possible. For some reason it only 
 appears sometimes. When the program is run and I state "customer + str(customer) + " is now getting their haircut", it sometimes prints
 the customers number(desired output) but then sometimes it print the threads.getName() value. Another bug os that "Customer 0" always returns 
 as customer Thread-1, while the rest remain 1, 2, 3, 4.... After much googling and python documentation I couldn't understand this.

 I understand that my solution mught be a bit messy but I made a great effort to not view any sleeping barber examples. This was made solely 
 off the project spec and this is the solution and method that made most sense to me.

The last thing I did was comment the code and tidy up the output. Comment in and out the print statements if needed, I have it set up to illustrate the behaviour of my program best.
