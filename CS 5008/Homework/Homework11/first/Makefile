CC = clang   # This variable is which compiler to use, we will use the variable later by $(CC)
CFLAGS = -Wall  # this variable is command line arguments
CFILES =  # this variable is the list of files to compile - UPDATE THIS LINE with your files

all: myprogram  #runs target myprogram is nothing is passed into make

myprogram: # it needs to compile out to >>>map.out<<<!
	$(CC) $(CFLAGS) -o map.out $(CFILES)  
	


clean: #this is a clean target, it removes all the .out files, called via > make clean
	rm  *.out