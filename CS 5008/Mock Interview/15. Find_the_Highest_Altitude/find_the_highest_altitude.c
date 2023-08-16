// time complexity: O(n)
// space complexity O(1)


int largestAltitude(int* gain, int gainSize)
{
    // maintain a max and sum variable
    int maxal=0;
    int sum=0;
    // find sum for each node
    for(int i=0;i<gainSize;i++)
    {
        sum = sum + gain[i];
        // check if it surpasses the max value
        if(sum>maxal)
        {
            maxal = sum;
        }
    }
    return(maxal);

}