/**
 * Student Name:
 * Semester:
 * 
 * C Practice
 * This assignment is to help you practice using C. Is is setup to
 * a set of various functions that tests the ideas you are learning.
 * 
 * In addition to this file, you will need to create a test file, that tests
 * every function!
 * 
 * This is called a 'header' library, meaning it is a collection of functions
 * that can be used in other files. This is the standard way of creating
 * libraries in C. In this case, the functions are implemented in the header file (.h)
 * but sometimes they are separated between header declarations (.h) and source files (.c)
 * which  you will explore in other assignments. 
*/

#ifndef C_PRACTICE_H
#define C_PRACTICE_H

#include <stdio.h> // basic input and output
#include <stdlib.h> // standard library

/**
 * Basic struct to hold two coordinates
*/
typedef struct {
    int x;
    int y;
} Point;


/**
 * Basic struct to hold a list of points - this list could be a polygon, 
 * but no checking for complexity is done.
*/
typedef struct {
    Point **points;
    int size;
} Polygon;


/**
 * Swaps the values of a and b. Makes use of pointers to change the values
 * of the variables in the calling function. 
**/
void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

/**
 * Prints an array of integers to the screen. Has a space after each value, and new line at the end
 * so an array of [1, 3, 2] would be
 * 1 3 2 
 * (notice there is a hidden space at the end of the 2 before the \n )
*/
void print_array(int *arr, int size)
{
    for(int i = 0; i < size; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

/**
 * Creates an array based on the fibonacci sequence.
 * The size is the number of elements in the array.
 *
 * For example, if size is 5, then the array should be [1, 1, 2, 3, 5]
 * if the size is 1, then the array should be [1]
 * if the size is <= 0, then NULL should be returned.
 *
 * As a reminder, the fibonacci sequence is:
 * is the value of the two previous values added together.
 *
 * So the first two values [0], [1] are 1, 1.
 * The third value is 1 + 1 = 2
 * The fourth value is 1 + 2 = 3
 * The fifth value is 2 + 3 = 5
 *
 * This means, you can set the first two values of the array to 1, 1,
 * and then start your loop forward.
 *
 * You can assume the size is less than 95, so you don't have to worry about
 * integer overflow.
 *
 * here is a quick list of numbers: https://www.math.net/list-of-fibonacci-numbers
 **/

int* create_array_of_ints_fib(int size) {
    if (size <= 0) {
        return NULL;  // Return NULL for size <= 0
    }

    int* arr = (int*)malloc(size * sizeof(int));  // Allocate memory for the array

    // Set the first two values of the array to 1
    arr[0] = 1;
    arr[1] = 1;

    // Generate Fibonacci sequence for the rest of the values
    for (int i = 2; i < size; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
    }
    // return array
    return arr;  

}


/**
 * Reverses an array *in place* (meaning you don't copy into another array)
 * 
 * For example, if the array is [1, 2, 3, 4, 5] then the array should be
 * [5, 4, 3, 2, 1]
 * 
 * To receive full points, you should only loop through *half* of the array. (size/2). 
 * Consider using swap. 
*/
void reverse_array(int *arr, int size){


/*  */
    if (arr == NULL || size <= 0) {
        return;
    }

    for (int i = 0; i < size / 2; i++) {
        int temp = arr[i];
        arr[i] = arr[size - 1 - i];
        arr[size - 1 - i] = temp;
    }
}
   


 
/**
 * Doubles the size of an array, and copies all previous values into the new array.
 * All other values should be set to 0.
 * 
 * You may want to look at calloc to help with this, to confirm all values are set to 0.
 * though you don't have to, if you want to loop through and set them to 0 yourself.
 * 
 * Notice, it is a pointer to the array that is being passed in (so you can modify the original
 * pointer location). As a reminder, you may need to do things like
 * 
 * new_arr[i] = (*arr)[i];
 * 
 * and then later *arr = new_arr;
 * 
 * don't forget to free(*arr); before you set it to the new array.
*/
void double_array_size(int **arr, int size){
     if (arr == NULL || size <= 0) {
        return;
    }

    int* new_arr = (int*)calloc(2 * size, sizeof(int));
    if (new_arr == NULL) {
        return;
    }

    for (int i = 0; i < size; i++) {
        new_arr[i] = (*arr)[i];
    }

    free(*arr);
    *arr = new_arr;
}   


/**
 * Copies elements of an array from start to end (inclusive) into a new array.
 * 
 * Returns the new array. However, if end is less than start, it loops around copying
 * elements from the beginning of the array.. (thus picture your array as a circle).
 * 
 * if start or end are invalid (less than 0, or greater than or equal to size), then
 * return NULL.
 * 
 * Example: assume an array is [1, 2, 3, 4, 5]
 * if make start = 1, and end = 3, then the new array should be [2, 3, 4]
 * if make start = 3, and end = 1, then the new array should be [4, 5, 1, 2]
 * 
 * Notice, new_size is a pointer, so you can set the size of the new array in your function. This
 * is commonly done in C, as a way to have multiple return values. (both the return, and the modified parameter)
 * 
 * In the two examples above, new_size would be set to 3, and then 4 respectively.
 * 
 * You will want to remember pointer arithmetic here. You can't say something like new_size = steps (where steps
 * is your new calculated size based on start to end), instead you have to say *new_size = steps)
 * 
 * Make sure to test this function, this is probably the hardest of the batch! 
*/

int* copy_array_start_end_loop(int* arr, int size, int start, int end, int* new_size) {
      if (arr == NULL || size <= 0 || start < 0 || end >= size) {
        *new_size = 0;
        return NULL;
    }

    int newLength;
    if (start <= end) {
        newLength = end - start + 1;
    } else {
        newLength = size - (start - end - 1);
    }

    int* newArr = (int*)malloc(newLength * sizeof(int));

    int j = 0;
    for (int i = start; j < newLength; i = (i + 1) % size, j++) {
        newArr[j] = arr[i];
    }

    *new_size = newLength;
    return newArr;
}
Point* create_point(int x, int y) {
     Point* point = (Point*)malloc(sizeof(Point));
    if (point != NULL) {
        point->x = x;
        point->y = y;
    }
    return point;
}

  //
/**
 * Creates a point with the given x and y values. Allocates it on the heap. (malloc)
 * and returns the new point
*/

/**
 * Creates a polygon with the given size. Allocates it on the heap. (malloc)
 * and returns the new polygon
 * 
 * For the points, you are creating the array of points, but you do not have too allocate
 * the point values. it is just a polygon of eventual size, and an array of empty points. 
*/
Polygon* create_polygon(int size){
  Polygon* p = malloc(sizeof(Polygon));
  if (p == NULL) {
    printf("Memory allocation failed.\n");
    return NULL;
  }

  p->points = malloc(size * sizeof(Point));
  if (p->points == NULL) {
    printf("Memory allocation failed.\n");
    free(p);
    return NULL;
  }

  p->size = size;

  return p;
}


/**
 * Frees the memory used by the polygon, make sure to loop through
 * all the points, to free them, free the array, and then free the polygon itself.
*/
void free_polygon(Polygon *p){
   if (p == NULL) {
    return;
  }

  free(p->points);
  free(p);
}   

/**
 * Creates a rectangle of width and height, using the polygon struct and returns it.
 * 
 * You can assume the following order of points
 * 0, 0
 * width, 0
 * width, height
 * 0, height
*/
Polygon* create_rectangle(int width, int height){

    if (width <= 0 || height <= 0) {
        return NULL;
    }

    Polygon* rectangle = create_polygon(4);
    if (rectangle == NULL) {
        return NULL;
    }

    rectangle->points[0] = create_point(0, 0);
    rectangle->points[1] = create_point(width, 0);
    rectangle->points[2] = create_point(width, height);
    rectangle->points[3] = create_point(0, height);

    return rectangle;
}
/**
 * Creates a (right) triangle of width and height, using the polygon struct and returns it.
 * 
 * You can assume the following order of points
 * 0, 0
 * width, 0
 * width, height
*/
Polygon* create_triangle(int width, int height){
    if (width <= 0 || height <= 0) {
        return NULL;
    }

    Polygon* triangle = create_polygon(3);
    if (triangle == NULL) {
        return NULL;
    }

    triangle->points[0] = create_point(0, 0);
    triangle->points[1] = create_point(width, 0);
    triangle->points[2] = create_point(width, height);

    return triangle;
}

/**
 * Prints the point in the format "(x, y) "
*/
void print_point(Point *p){
    printf("(%d, %d)", p->x, p->y);
}

/**
 * Prints the polygon in the format "(x, y) (x, y) (x, y) \n"
*/
void print_polygon(Polygon *p){
    for(int i = 0; i < p->size; i++){
        print_point(p->points[i]);
        printf(" ");
    }
    printf("\n");
}

/**
 * Calculates the area of the polygon using the shoestring formula.
 * 
 * The shoestring formula will loop through every point, and calculates the area by
 * 
 * area +=  i->x * i+1->y - i+1->x * i->y
 * 
 * however, when i+1 is greater than size, you will need to loop back around to the beginning (so think of
 * setting i+1 to j, where j= (i+1) % p->size before running the calculations)
 * 
 * after area is summed across all points, divide by 2.0 and return the area.
*/

double calculate_polygon_area(Polygon *p) {
  double area = 0.0;
  int size = p->size;

  int i, j;
    for (i = 0, j = 1; i < size; i++, j = (j + 1) % size) {
    area += p->points[i]->x * p->points[j]->y - p->points[j]->x * p->points[i]->y;
  }

  area /= 2.0;

  return area;
}


#endif // C_PRACTICE_H

