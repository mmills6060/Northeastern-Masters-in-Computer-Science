1a)
In order to prove that the output is guaranteed to be a 2 approximation, 
we need to create a minimum weight spanning tree, and complete a TSP tour. 

Since the TSP tour is a hamiltonian cycle, which means that the algoirhtm must visit all vertices,
or in this case cities, we can say that the cost of the MST is a lower bound. We then multiply the
MST by two. This, in other words, means that every edge or city is visited twice. Next, we will use 
the triangle inequality to take a direct path from A to C, while we are skipping B. This is an
interesting concept because the total cost will not increase when using the triangle inequality.
With that being said, we can see that APP <= 2 x MST. We now have two different inequalities,
MST <= OPT and APP <= 2 x MST. We can combine both of these inequalities to APP <= 2 x OPT.


1b)
In order to complete a TSP tour, we should start at  any vertex, and continue adding edges.
Once complete, we will have a TSP tour that looks like the following. 

A,D,F,B,E,C,G,A

The total cost of this tour will be 3023. Since the optimal tour cost is 51, we can see that 
this is clearly not a 2 approximation. The reason why this is not a 2 approximation is because
of the weights that have been added to the missing edges.  This primarily shows how important
it is to assume that the triangle inequality holds and how this assumption can break when
the triangle inequality doesnt in fact hold true. 


1c)

In this problem, we can create an algorithm that will determine the distance between two points when
they are not yet defined. A popular way to do this is to use the Floyd-Warshall algorithm. Now that
we have these distances, we now have a graph that satisfies that triangle inequality. This is a
crucial step in determining a 2 approximation, as it will now work due to the fact that the triangle
inequality now holds. We can now apply the same algorithm to the same TSP instance, and we will
receive the following path.

A,D,F,B,E,C,G,A

With this particular path, we will receive a total cost of 74. Since 74 <= 2 x 51 = 102, we now 
see that this is in fact a 2 approximation. 

1d)

The best way to prove this is by contradiction. With that being said, we can assume that there is 
an optimal TSP tour where two edges actually do intersect. Once we assume thijs, we can show 
that when the edges cross, the tour isn't optimal. The fact that this contradicts will show that
this cannot be the case.

To begin, we will consider a quadrilateral with edges A,B,C,D. We can then make the assumption
that this distances A,C + B,D < A,B + C,D. We can assume this due to the fact that the direct path
will always be shorter than when it crosses over. This is simple geometry. If we replace the
intersecting edges, we can see that we now have a new tour, but with a total distance that is 
shorter than the original. Since the tour has a smaller total distance than the original,
we can see that the original is not the optimal solution. With that being said, we can now 
see that the edges cannot cross. 


2c)
My algorithm performs better with smaller cities in general. As it gets to later cities,
it gradually takes longer and longer to calculate. I believe we are receiving a relative approximation
due to the fact that we are measuring results based on the number of runs it takes, I believe it 
is safe to assume that we are working with a relative approximation. 
