CC = clang   # This variable is which compiler to use, we will use the variable later by $(CC)
CFLAGS = -Wall  # this variable is command line arguments
CFILES = adj_matrix.c adj_list.c converter.c adj_fun.c # this variable is the list of files to compile

all: myprogram  #runs target myprogram is nothing is passed into make

myprogram:  # this is the target, and the dependency
    # this is the command to run, it compiles the files in CFILES and outputs the executable to dfs_print.out  
	$(CC) $(CFLAGS) -o adj_fun.out $(CFILES) 


clean: #this is a clean target, it removes all the .out files, called via > make clean
	rm  *.out