CC = clang   # This variable is which compiler to use, we will use the variable later by $(CC)
CFLAGS = -Wall  # this variable is command line arguments
CFILES = my_bst.c my_bst_printer.c my_bst_util.c bst_main.c # this variable is the list of files to compile

all: bst  #runs target if is nothing is passed into make

bst: $(CFILES) # this is the target, and the dependency
    # this is the command to run, it compiles the files in CFILES and outputs the executable to bst.out  
	$(CC) $(CFLAGS) -o bst.out $(CFILES) 


clean: #this is a clean target, it removes all the .out files, called via "make clean"
	rm  *.out