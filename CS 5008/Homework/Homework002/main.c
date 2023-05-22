/**
 * This program runs the various cpractice.c functions. While it is essentially
 * a test, it does not do a full test of the functions. You should write your
 * own tests in tests.c.
 * 
 * Student Name: Michael Mills
 * Semester: Summer
*/

#include <stdio.h>  // basic input and output
#include <stdlib.h> // standard library

#include "cpractice.h" // header file for cpractice.c

/**
 * Sample run of swap
*/
void swap_practice() {
    printf("Practicing Swap\n");
    int a = 5;
    int b = 10;
    printf("Before Swap: a = %d, b = %d\n", a, b);
    swap(&a, &b);
    printf("After Swap: a = %d, b = %d\n", a, b);
    printf("\n");
}

/**
 * Sample runs of array practice. notice how some of them are called
*/
void array_practice() {
    printf("Practicing Arrays\n");
    int* arr = create_array_of_ints_fib(12);
    print_array(arr, 12);

    // printing array where it loops around
    printf("printing loop standard: ");
    int return_size;
    int* arr2 = copy_array_start_end_loop(arr, 12, 3, 8, &return_size);
    print_array(arr2, return_size);
    free(arr2);

    printf("printing loop with wrap around: ");
    int* arr3 = copy_array_start_end_loop(arr, 12, 8, 3, &return_size);  // you will want to draw this out. 
    print_array(arr3, return_size);
    free(arr3);

    printf("printing array that is in the reverse order: ");
    // reverse array
    reverse_array(arr, 12); // notice this modifies the original array!
    print_array(arr, 12);

    printf("printing array that is double the size: ");
    // double size
    double_array_size(&arr, 12); //this replaces the original array with a new one
    print_array(arr, 24);

    // free array from memory
    free(arr); 
    printf("\n");

}

/**
 * Sample run dealing with structs and polygons
*/
void struct_practice(){
    printf("Practicing Structs\n");
    // point test
    Point* p1 = create_point(5, 10);
    print_point(p1);
    printf("\n");
    free(p1); // free memory

    // rectangle test
    Polygon* rect = create_rectangle(5, 10);
    print_polygon(rect);

    double area = calculate_polygon_area(rect);
    printf("Area of rectangle: %.2f\n", area);
    free_polygon(rect);

    // triangle test
    Polygon* tri = create_triangle(5, 10);
    print_polygon(tri);

    area = calculate_polygon_area(tri);
    printf("Area of triangle: %.2f\n", area);
    free_polygon(tri);

    Polygon* hexagon = create_polygon(6);
    hexagon->points[0] = create_point(12, 10);
    hexagon->points[1] = create_point(11, 12);
    hexagon->points[2] = create_point(9, 12);
    hexagon->points[3] = create_point(8, 10);
    hexagon->points[4] = create_point(9, 8);
    hexagon->points[5] = create_point(11, 8); 

    print_polygon(hexagon);
    area = calculate_polygon_area(hexagon);
    printf("Area of hexagon: %.2f\n", area);
    free_polygon(hexagon);


}

/**
 * Main entry point for the program. 
 * You may also want to focus
 * on writing your own tests in tests.c **First** 
 * and then coming here to run
 * the final program. 
*/
int main(int argc, char const *argv[])
{
    swap_practice();
    array_practice();
    struct_practice();
    return 0;
}
