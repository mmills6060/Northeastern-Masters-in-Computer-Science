# Research Paper
Name: Michael Mills
Semester: Summer 2023
Topic: Combinatorial Optimization Algorithms
Link The Repository: https://github.com/Su23-CS5008-Online-Lionelle/finalresearchpaper-mmills6060

## Introduction
For my final project, I decided to implement a few algorithms that are directly related to a project that I have been working on for the greater part of the year. I have been working on an application that aims to improve the way that we are able to access files. Currently, it is often the case that we will subscribe to some cloud storage service. This costs a lot of money, and the files are also stored in some unknown location. This project aims to decentralize cloud storage, so we can seamlessly access our files across all of our devices, without the need for some expensive cloud subscription plan. The cool thing about this project is that there are many strategies that can be used to determine what would be the best way to store all of these files. Should we store all of the files on just one device and leave the rest empty? Should we store the same file on multiple different devices? Should we split up files to multiple different devices, so device has one entire file? These problems are where my algorithms are able to come into play. 

For this particular problem, I decided to look at Combinatorial Optimization Algorithms. These types of algorithms are beneficial for when we need to find an optimal solution from a finite number of combinations. In other words, there are a large number of combinations that are available, however which one would happen to be the best? There are many famous problems that are associated with this type of algorithm, such as the Traveling Salesman Problem, the Minimum Spanning Tree Problem, and the Knapsack Problem. I believe that the algorithm that I chose to implement most closely resembles the Knapsack Problem. More specifically, the Knapsack problem with multiple Knapsacks, or notably "The Multiple Knapsack Problem."

![Knapsack_picture
](https://github.com/mmills6060/Northeastern-Masters-in-Computer-Science/blob/main/CS%205008/Final/knapsack_picture.png)

The Multiple Knapsack Algorithm is essentially an algorithm that solves a problem where you have multiple different items of different weights, and multiple different knapsacks with different capacities, and we need to find an optimal allocation of items for each knapsack, such that the total carrying capacity of each knapsack is maximized. It does this by using a dynamic programming approach. This means that it will use a nested loop and iterate over each of the items and each of the knapsacks. Then, the algorithm will determine whether or not it should include the current item by looking at the current value of the knapsack, and see if there is enough room to fit the curent item being evaluated. 

![Knapsack_picture
](https://github.com/mmills6060/Northeastern-Masters-in-Computer-Science/blob/main/CS%205008/Final/knapsack_equation.png)


In terms of best, worst, and average case scenarios, the best case scenario will be when the algorithm is able to quickly determine that the item cannot be added to the knapsack. Even though this is a best case scenario, we will still see this time complexity to be O(n * m). As for a worst case scenario, this is when the algorithm needs to consider all possible items in a knapsack, especially when the knapsack is close to full. Because this algorithm is constant, the time complexity is still O(n * m). In terms of the average case scenario, the algorithm still needs to consider all possible scenarios, which would still lead to O(n * m).  (Schrijver, 1995)

Algorithms used to solve many various Combinatorial Optimization problems have mostly been prevalent since the early 1900s. Despite most being mostly prevalent in the 1900s, the very first attempt at solving a similar problem occured in 1736. This is when a man by the name of Leonhard Euler worked on the Seven Bridges of Konigsberg Problem. This was a problem where a city consisted of seven bridges, and Euler wanted to figure out how he could create a walk through the city that would allow the traveler to go over each of the bridges just one time. (Kőnig–Egerváry theorem, n.d.)




In 1931, a man by the name of Denes Konig worked on a problem where there are a certain number of tasks, and a certain number of workers, and only one task should be assigned to one worker. In order to solve this problem Denes came up with the Konig-Egervary theorem. This theorem essentially explains that the maximum number of tasks that can be completed is equal to the minimum number of workers that are needed to complete all of the tasks. (Kőnig–Egerváry theorem, n.d.)


In 1947, a man by the name of George Dantzig worked on solving various linear programming problems. While working as a research assistant, he was given the task to solve a certain linear programming problem. He realized that he could solve the problem through an algorithm called the Simplex Method. The simplex method is essentially starting off with a solution that works, and then iteratively coming up with a better solution until the solution becomes optimal. (George Dantzig, n.d.)

In the 1950s and 1960s, there was a sharp increase in popularity in solving something called the traveling salesman problem. The traveling salesman problem is essentially a problem in which there is a salesman that needs to go to various locations, and there are multiple different orders in which the salesman may visit each city. For example, should he go from Boston to New York, or should he stop in Philadelphia before he goes to New York? This problem, and the subsequent algorithms that were developed for it aim to determine the best possible route for the traveling salesman. (Travelling salesman problem, n.d.)

Another popular problem is the minimum spanning tree problem. This is a problem that aims to determine a tree of a graph, while maintaining the smallest total edge weight possible. This problem is particularly important in a number of different situations. For example, it can be incredibly helpful when we are thinking about and designing efficient networks. These networks don't just have to be computer networks, they can be any type of network, such as a road system when planning a new city. 

Another popular problem in the realm of ocmputer science is the Knapsack Problem. This was mostly prevalent in the late 1950s and 1960s. The Knapsack Problem is essentially a problem in which there are a certain amount of items that consit of various weights. We are looking to find the best way to pack the knapsack. This problem works by implementing a dynamic programming approach. Additionally, this problem is mostly solved using a greedy approach, which means that each item is determined one at a time, and there is no backtracking involved. (Salkin & De Kluyver, 1975)


Now that we have learned about the history of Combinatorial Optimization Algorithms and their history, it is time to give a brief summary of what the rest of this paper will look like. To begin, I will be giving an analysis of the Algorithm, including the time complexity, space complexity, and general analysis. Next, I will be providing an empirical analysis. Next, I will discuss the application of the algorithm, including what it's used for, some real world examples of how its used, and why it can be helpful. Next, I will discuss my implementation of the algorithm, the language that I used, the libraries I used, some challenges I faced, and finally some key points. 

Finally, I will provide an overall summary of what I found, what I learned, and how it helped me become a better computer scientist. 

## Analysis of Algorithm/Datastructure

For these algorithms, there are multiple different parts of each algorithm that have different time complexities. In other words, each algorithm can be broken down into 3 different sections, sorting the files, sorting the devices, and the nested loop. As for sorting the files, this will normally have a time complexity of O(n log n). In this particular scenario, n will be the number of files. As for sorting the devices, this will normally have a time complexity of O(m log m). In this particular scenario, m will be the number of devices. Finally, as for the nested loop, this will normally have a time complexity of O(n * m) where again n is the number of files and m is the number of devices. Since the overall algorithm is a combination of these smaller pieeces, we are able to add all three of these time complexities together, which would be O(n log n + m log m + n * m). We are then able to simplify this to an overall time complexity of O(n * m). 

As for the space complexity, there doesn't seem to be much wrong with the algorithm. I certainly learned a lot in this part of the project, as this was the first time that I had worked with analyzing memory in a python program. I ended up copying all of the algorithm functions to the test_space_complexity.py file, as the memory profiler doesn't review the memory of the function that is called from another file. For the most part, it seems as if the memory is mostly sound. Of course, there are variables that are assigned that will require memory. In my experience, even with incredibly high numbers for the number of files, number of devices, etc., the memory does not seem to be bad at all. In fact, I thought there was something wrong with the profiler as it was showing zeroes across the board, and I had to increase the workload in order to get it to show anything. 

Overall I think that this is a very interesting algorithm, and probably has a lot of use cases. I think overall the algorithm works especially with large workloads and large datasets specifically because it is considered to be a greedy algorithm. In other words, the algorithm doesn't backtrack and look to change which knapsack to store the file in after it has already been placed. I think this is the sole reason why it is able to work with large numbers. 

## Empirical Analysis

As for the time complexity, I wanted to measusure the amount of time it would take to run the algorithm, depending on the number of files and the number of devices. My theory was that this particular algorithm would take a greater amount of time to complete the greater the number of devices or files are actually in the dataset. I also made the prediction that there isn't really any difference in speed when comparing number of devices and number of files. However, both variables matter when it comes to measuring the time complexity. With these assumptions, I made the conclusion that these particular algorithms would follow a time complexity of O(n * m). I ran through the code a few times and struggled with receiving a constant time complexity. My initial thought was that this was ue to the fact that the dataset was not large enough. I then came to the conclusion that the code that I had written to measure the amount of time that had elapsed was restarting the start time after every loop. This is what caused the constant time complexity, which makes sense, since this algorithm resembles a greedy algorithm, which would have relatively the same speed for each loop, no matter how many loops there are. 

![Time Complexity](CS 5008\Final\time_complexity.png)

As for the space complexity, I wanted to measure the amount of memory that was used per line of code that I had written. In order to do this, I went ahead and used the memory_profiler module, which is a popular module used to measure memory in Python. My prediction for this was that the overall program should run relatively smoothly, however whenever I assigned a variable to something, it would use memory. In my initial testing, I was really confused because it was showing there being zero memory being used. I then did some thinking and came to the conclusion that there is probably some limit to the number of decimal places that the memory profiler uses. I did some research, and came to the ocnclusion that I was correct in my assumption. My next plan of attack was to see if there was some sort of way that I can change the profiler so that it presented more than two decimal places. I quickly came to the conclusion that this was not the correct plan of attack as it would probably require me going into the profiler module and editing the module. I then came to the conclusion that instead of figuring out how to create more decimal places, I should try to figure out a way to make the numbers larger, so they would appear desipte the low number of decimal places. I then decided that increasing the size of the dataset would be the best way for me to increase the amount of memory that is being used. After modifying the dataset to make it larger, I was actually able to get numbers to show for the amount of memory used. Not only that, but the numbers were showing in the exact lines that I would expect it to be, where I am assigning variables to things. 

In the below screenshot, I am running the very first algorithm which is to just allocate the files, without any additional functionality. 
![Space Complexity](https://github.com/mmills6060/Northeastern-Masters-in-Computer-Science/blob/main/CS%205008/Final/space_complexity1.png)

In this second screenshot, I am running the algorithm that will not only allocate the files accoridngly, but also include the duplication functionality. I found it interesting how the increment in memory usage seems to be dramatically in the negatives here. I think that this is mostly because I am iterating thorugh all of the files, and it is dumping the memory used for each file. 
![Space Complexity](https://github.com/mmills6060/Northeastern-Masters-in-Computer-Science/blob/main/CS%205008/Final/space_complexity2.png)

In this third screenshot,  I am running the algorithm that will not only allocate the files accordingly, but also use the file sharing functionality as well. It well take the files and split them up into multiple pieces and allocate them accordingly. I believe that this is running as expected, as the only time that memory is allocated is when I am assigning a value to a variable or adding a particular value to a list. 
![Space Complexity](https://github.com/mmills6060/Northeastern-Masters-in-Computer-Science/blob/main/CS%205008/Final/space_complexity3.png)

As for the fourth screenshot, I am running the algorithm that will include all of the functionalities. I believe that the memory is working as expected in this algorithm as well. My theory is that the python interpreter is reusing the datastructure that was used in the previous algorithms, and that is why I am seeing zero memory. 
![Space Complexity](https://github.com/mmills6060/Northeastern-Masters-in-Computer-Science/blob/main/CS%205008/Final/space_complexity4.png)

As for the final scrrenshot, I am running the main, which is the block of code that is calling all of the other algorithms. The memory also makes sense in this screenshot as well as the only time memory is being allocated is when I am assigning a value to a variable. It looks like the memory allocated when calling the different algorithms correlates with what was happening in the actual algorithms themselves, which makes sense. 
![Space Complexity](https://github.com/mmills6060/Northeastern-Masters-in-Computer-Science/blob/main/CS%205008/Final/space_complexity5.png)


## Application

The algorithms I wrote are primarily used to determine the optimal allocation of files across devices. The algorithms have a number of different variables such as priority, duplication of files across multiple devices, and splitting files into pieces across devices. For example, say for instance that we have a word document that we open for work every single day. This is an important document that requires the highest level of priority. Now say for instance we also have a wedding video, which is still a really important file, but we don't think we will be using it as frequently as the document we pull up for work every day. In terms of devices, we have a laptop, desktop, Apple Watch, iphone, two Roku devices, an iPad, and a Meta Quest 2.  With that being said, this algorithm will determine the optimal allocation for these two files, such that the files with the highest priority will be allocated first, and the files with the lowest priority will be allocated last. 

There are many other examples of Combinatorial Optimization Algorithms. For example, Google Maps could use an algorithm to determine the fastest point from A to B. Another example is Amazon. Amazon could certainly use an algorithm like this when shipping products. It could be incredibly beneficial to determine what products they should ship together, and which ones would be more profitable to ship separately. Is it cheaper to ship one particular package to Philadelphia before going to New York? Or is it cheaper to go straight to New York. 

## Implementation

For this project, I decided to implement most if not all of my work in Python. I chose Python for a number of reasons. One of which is due to the fact that I don't have to worry about memory management. This makes life much easier for when I am writing code, as I don't have to constantly think about allocating and freeing memory. I also think that Python is just an easier language to use. The syntax makes more sense and is incredibly simple. Python seems to be one of the only languages where I may not know exactly what the syntax is for a particular line of code, and when I just randomly guess what it might be, I have someone of a decent chance of being correct. Another reason why I enjoy Python is because I don't have to worry about compilers and compiling all of my code. I can just simply run the python scripts and it works. It doesn't seem like a lot, but in reality it is twice the amount of keystrokes to compile a project before you run it, and that can add up. 

As for the libraries I used, I really did not use many libraries. I really only used libraries for the testing portion of the code such as Time and memory profiler. I found this one repository on github that I could have used that implemented all of the algorithms automatically without having to write them all out, but I decided not to use that. I also seemed to have some very specific and custom requirements for some of the algorithms that I wrote. One library that I did use, which is not incredibly important is the tkinter library. I basically just used this as a GUI to go ahead and select which directory or file I am interested in uploading and scanning. This just eliminates the need to manually write out the file path of what directory you are looking to scan. 

One challenge I faced was uploading large directories. I essentially designed the program in a way where the program would go through each individual level of folders from a top down approach until all of the files have been scanned. This means that each individual file is given a CID, and information about the CID's are stored in a directory on your computer. The problem was that the process of uploading files to IPFS seemed to slow down after 15,000 files. This is primarily because every time a CID is added, it is also added to a directory on the local computer. I am assuming this means that after 15,000 files or so, adding another CID would mean that it needs to search through 15,000 files. My immediate solution to this problem is to not give a CID to every single file on the computer, and only give CID's to directories, which seems to be possible. I am interested in going into this deeper to determine if there is anything else causing it to slow down. Another problem I had was related to actually developing the algorithms. I had many issues/bugs in many different instances. One of which was the fact that it would only pack a few files in the "knapsack," and leave a large majority of the files unpacked, despite the fact that there was still space left. Another issue I had was the fact that the file sizes would go to some crazy decimal number. This caused the algorithm to just leave those files alone and not place them in a "knapsack." Rounding the file size to a certain decimal fixed this. 

Overall, I really enjoyed working on these algorithms. I am interested to see how I can improve these algorithms in the future. I feel as if the base model of the algorithm, where it just simply places files in devices almost mindlessly seems to be a little bit of a waste. However, I think once I started to incorporate different variables into the algorithm, that's when it really started to get interesting. I think theres a lot of room for improvement as well. For example, we could take into account the frequency that a file is visited or used. We could also take into account how fast the internet is for each individual device. If one particular device has terrible internet speed, you could shift all of the files or some of the files to another device that may be faster. I also think the priorty functionality is a really interesting concept as well, and could influence how many devices a particular file is on. I think the most interesting part of all, is how I would be able to implement all of these variables into one algorithm.

## Summary

Overall, I learned a lot not only with this project but also in this class. Before this class, I had a good general understanding of algorithms and why they are important in the realm of computer science. Taking this class helped make me more aware of the concept of data structures and algorithms within applications, and how important they can be. I heard people talk about time complexities such as O(n) before this class, but now I have a solid understanding of what it means. 

## References

Schrijver, A. (1995). The History of Combinatorial Optimization. In Handbook of Combinatorial Optimization, Volume 1.

Kőnig–Egerváry theorem. (n.d.). In Wikipedia. Retrieved from https://en.wikipedia.org/wiki/K%C5%91nig%E2%80%93Egerv%C3%A1ry_theorem

George Dantzig. (n.d.). In Wikipedia. Retrieved from https://en.wikipedia.org/wiki/George_Dantzig

Travelling salesman problem. (n.d.). In Wikipedia. Retrieved from http://en.wikipedia.org/wiki/Travelling_salesman_problem

Salkin, H. M., & De Kluyver, C. A. (1975). The knapsack problem: A survey. Naval Research Logistics, 22, 127-144. https://doi.org/10.1002/nav.3800220110

Kleywegt, A. J., & Papastavrou, J. D. (1998). The Dynamic and Stochastic Knapsack Problem. Operations Research, 46(1), 17-35.