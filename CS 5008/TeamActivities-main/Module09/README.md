# Team Activity: Explore Hash Algorithms and Collisions  

For this team activity, you will explore hashing algorithms and collisions. When working with Hashmaps,
there will be collisions, but the depth of the lists (or even trees as you will explore in future weeks),
is often very small. This is why even with large numbers, such as near a million items, you still get effectively
$O(1)$ access time. 

## Review The Code

In your group, review the provided code in [hashing.h](hashing.h) and [hash_test.c](hash_test.c). 
Explain to each other the various lines. `hash_test.c` probably has code that looks more familiar to you.
The code that may look unique (though used in past test files), is the code that includes function pointers.

```c
uint32_t (*hash[])(char*) = {
    simple_hash,
    djb2,
    fnv_hash,
    jenkins_one_at_a_time_hash    
};
```

What this array stores is a pointer to each function, but also defines that the functions will return an `uint32_t` and are 
required to take in a `char *` (string) as a parameter. If you want to call `simple_hash` it would be `simple_hash[0]`.

Later in your code, you will see:

```c
for (int i = 0; i < ALGO_SIZE; i++)
{
      uint32_t loc = (hash[i](buffer)) % SIZE;
      collisions[i][loc]++;
}
```
This means that for every algorithm, call the hash, mod it by the `SIZE` of the 'hashmap' (really just an array in this case), and increment a counter to track the number of collisions that happen. Since the `collisions[i]` is initialized with 0, it will just continue to count up for everything a key wants to be stored in that position. 

Then later in `void printCollisionsOnly(int *array, int size)` it prints out the stats of the collisions array for each algorithm in order. 

This code is setup so you can get a better feel of how hashmaps work in practice, even if we are not storing the full key-value pairs. 



### *.txt files
There are a number of .txt files. If you open them you will find the files with ids in the name contain values such as `tt0000001`, where as the titles contain the corresponding movie titles, like the `The Princess Bride` which is on line 53,321. The ids and titles are pulled from the open IMDB dataset, and filtered for US only movies with IMDB ratings to reduce it down from the 32 million points to only 925,174 titles. Then using `head -n #` smaller test files were developed at 1000, 10,000, and 100,000. 

### Running the Code
You should be able to run the code with:

```console
> clang -Wall hash.test.c 
> ./a.out movie_ids_us_1000.txt
```

You can also run more than one file at a time chaining the results:

```console
> ./a.out movie_ids_us_1000.txt movie_titles_us_1000.txt movie_ids_us_10000.txt movie_titles_us_10000.txt movie_ids_us_100000.txt movie_titles_us_100000.txt movie_ids_us_unique.txt movie_titles_us_unique.txt 
```
The above is all one line, but auto wraps in display. 

You should go ahead and run the code. When running it, you will see something like (depending on how many files you test against):

```text
movie_ids_us_1000.txt...
Collisions: 1000, Highest: 1000, Average Length > 1: 1000.00, Filled Spots: 1, Load: 0.00000
Collisions: 1000, Highest: 1000, Average Length > 1: 1000.00, Filled Spots: 1, Load: 0.00000
Collisions: 0, Highest: 0, Average Length > 1: -nan, Filled Spots: 1000, Load: 0.00050
Collisions: 0, Highest: 0, Average Length > 1: -nan, Filled Spots: 1000, Load: 0.00050

movie_titles_us_1000.txt...
Collisions: 1000, Highest: 1000, Average Length > 1: 1000.00, Filled Spots: 1, Load: 0.00000
Collisions: 1000, Highest: 1000, Average Length > 1: 1000.00, Filled Spots: 1, Load: 0.00000
Collisions: 22, Highest: 2, Average Length > 1: 2.00, Filled Spots: 989, Load: 0.00049
Collisions: 22, Highest: 2, Average Length > 1: 2.00, Filled Spots: 989, Load: 0.00049
```
The first two lines are high because those functions are not implemented yet, so only returning 0. 

> Discussion: What does each value represent out of Collisions, Highest, Average Length > 1, Filled Spots, and Load. Make sure to discuss together what is the ideal load balance num.


## 👉🏽 **Task**: Write Simple Hash

Using your notes from the class videos or on your own, write a simple hash that that adds the ASCII value of the characters. As a reminder, just casting a character as an int gives you the ascii value, so you can loop through every character in the string, and
just add the values of those characters.

> Discussion: How effective is the "simple hash" compared to the other
two hashes that are implemented - for this particular dataset"? 


## 👉🏽 **Task**: Write djb2 Hash

Now work on the djb2 hash, which as a reminder, is:

```text
hash = 5381
for c in string:
    hash = hash * 33 + c
```

We encourage you to look at a more efficient implementation than using multiplication. 

> Discussion: How effective is the djb2 compared to others for this particular dataset? 
>
> Second: What is a more efficient implementation? Do you think they picked 33 for this reason? 
> Why would this matter? (reflect back to your assembly team activity). 

## Tests

Look at the file, and run various tests.

* What happens when you change SIZE?
* Is there an optimal number/size, that increases your load factor but not too much (0.5-0.7)?
* What are the differences between the various functions?
  * Number of operations?
  * Types of operations? 
  * Do the ones that perform better come at an increased cost?
* Would prime numbers be useful staring points?

If you don't recall what some operators do - look them up! Discuss them (particular the XOR and the shifts). Why would these be useful? 
As a reminder, hash algorithms care more about the binary bits, which thinking about it in a form of binary may help better understand why they may use those. 

For example, take 5 in binary (101) and apply the operations to that small value, to get a better idea of the transformations that are happening. You can always either write a small see program, or perform the same operations in the python interactive interrupter to see what is going on! 

```python
>>>bin(5)
'0b101'
>>>bin(5<<2) 
'0b10100'
>>>bin(5*4)
'0b10100'
```

## Final Discussion

You will never find a perfect hash, and there is often a cost of performance the more complicated your transformation. As such, those who define hashmaps are often searching for a "good enough" hash algorithm, and then they provide a way to let people change the default implementation so they can be more specific for their domain. 

For object oriented languages such as Java, those are built into the objects themselves to determine their hash. 

> Discussion: 
> Discuss a hashmap design. See if you can explain to each other how it is designed, and why it is effectively $O(1)$.  
> Can you also generate a case where access/insert/delete are $O(n)$?

## Leet Code Practice
Take time practicing some of the past modules leet code. While you may not have time for everyone to do this, have a couple people practice "live coding". Live coding is a skill in interviews were you are asked to describe code **while** you are writing it. It can be a challenging skill, and it takes practice. I recommend that you setup a rotation of people to practice this skill within your team, ideally a couple every week. The other teams members can offer support, and then do a code review after a solution is generated. Discuss pros/cons of the leet code solution as well as other potential ways to solve the problem.

## 📚 Resources
* [Left/Right Shift Operators in C](https://www.geeksforgeeks.org/left-shift-right-shift-operators-c-cpp/)
* [List of Hash algorithms](https://en.wikipedia.org/wiki/List_of_hash_functions#Non-cryptographic_hash_functions)
* [djb2 Hash explained](https://theartincode.stanis.me/008-djb2/)
