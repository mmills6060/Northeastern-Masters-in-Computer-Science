#include "hashmap.h"


/** use this file for tests. 
 * 
 * Below isn't actually any 'real' tests, it
 * just simply is a sample run. 
*/

int main() {
  /*  hashmap map = map_create(1);

    map_put(map, "Apple", 2.08);
    map_put(map, "Orange", 3.01);
    map_put(map, "Orange", 2.50);

    map_print(map);


    printf("Dread is %.2f\n", map_get(map, "Orange"));

    map_del(map, "Apple");
    map_del(map, "Pineapple");
    map_print(map);

    map_free(map);
    */
       hashmap* map = map_create(10);
    
    // Test map_put and map_get
    map_put(map, "apple", 2.5);
    map_put(map, "banana", 1.8);
    map_put(map, "orange", 3.2);
    
    printf("Testing map_put and map_get:\n");
    printf("Apple Value: %.2f\n", map_get(map, "apple"));     // Expected: 2.5
    printf("Banana Value: %.2f\n", map_get(map, "banana"));   // Expected: 1.8
    printf("Organge Value: %.2f\n", map_get(map, "orange"));   // Expected: 3.2
    printf("Grape Value: %.2f\n", map_get(map, "grape"));     // Expected: -1.0


    // Test map_del
    float deleted_value = map_del(map, "banana");
    printf("\nTesting map_del:\n");
    if (deleted_value != -1.0F) {
        printf("Deleted value for 'banana': %.2f\n", deleted_value);   // Expected: 1.8
    } else {
        printf("Key 'banana' not found.\n");
    }
    printf("Value for 'banana' after deletion: %.2f\n", map_get(map, "banana"));   // Expected: -1.0

    // Test map_print
    printf("\nTesting map_print:\n");
    map_put(map, "grape", 0.9);
    map_put(map, "watermelon", 4.6);
    map_put(map, "kiwi", 2.1);
    map_put(map, "mango", 3.7);
    map_print(map);   // Expected: {apple : 2.50}, {orange : 3.20}, {grape : 0.90}, {watermelon : 4.60}, {kiwi : 2.10}, {mango : 3.70}

    // Test map_free
    printf("\nTesting map_free:\n");
    map_free(map);
    printf("Map freed successfully.\n");
    
    return 0;
}
