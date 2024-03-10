# Future-Proofing Computer Behavior: Predictive Modeling of Computer Performance


## What is it about?

This project dives into the world of predictive analytics, specifically focusing on the way that our computers behave throughout the day.
There are a lot of metrics that we can look at to evaluate how our computer is performing. For example, we can look at wifi upload and download
speeds to determine how fast our computer is currently communicating with the internet. We can also look at GPU, CPU, and RAM load usage to determine 
the current load on our computer and how hard it is currently working in order to complete a certain task. We can look at the device downtime,
which is the time that the computer is not able to be reached. These are just a few metrics that can be looked at. An idea that I had was to
take this data and use it to predict the future behavior of the computer. For example, if a particular user consistently shuts their computer off
at 6:00PM, eventually we should be able to generate an inference that will essentially say that there is a high probability that this device will 
not be able to be reached  after 6:00PM. 

Predicting system performance like this is important in cloud computing. If we can make accurate predictions when a particular server will 
have a low network speed, or when the CPU will have a high load, we can make better decicions about how we can properly allocate resources
and ultimately create a better user experience.

## Related Works

There are a number of papers that related to this topic, however I have not found any that have done exactly what I am proposing. The first 
paper is called Predictive Analysis of Cloud Systems. This paper investigates various methods for predictive analysis of cloud systems. It looks
at how we can create a self-adaptive system that will be able to predict certain performance metrics that may happen in the future, and adapt itself
accordingly. This paper also looks at variosu quality of service metrics that are used to evaluate the performance of cloud systems. Another paper 
that I have found is called The Impact of Big Data in Predictive Analytics Towards Technological Development in Cloud Computing. This was an interesting
paper which started off by giving a perspective of how important cloud computing is. It gave certain statistics such as the fact that there are 2.5
quintillion bytes of data generated every day. This paper also discusses the present applications and challenges of big data in predictive analytics. In
addition, it looks at the future and what sort of applications and challenges might arise in the future as well. My third and final paper that I reviewed
was a paper called Energy Efficiency for Cloud Computing System Based on Predictive Optimization. When thinking about this project, I realized that 
of course something like this may be able to help with things like user experience and profitability for a company. However, I also was thinking about
the amount of energy that could be saved as well. If we can predict when a server won't need to be running, we could potentially turn it off and 
save that energy that's being used. This paper looks at just that. It looks at power consumption in the realm of computer science. It also 
proposes an energy efficient solution for resource orchestration in cloud computing. This solution, although is not exactly what I am proposing,
offers a similar motive in the sense that it is trying to save energy by predicting when a server will not be needed.
## Aims and Contributions

My overall goal for this project is to create a solution for a faster, cheaper, more consistent, and more energy efficient cloud computing service.
For example, I want to create a solution that will take in a certain time of day, and be able to predictive the wifi upload and download speed.
In addition, I want to be able to predict many other metrics such as GPU, CPU, and RAM usage. Finally, I want to create a solution that will
make informed decisions about how to self-optimize itself. 

## Methodolody

In order to achieve this goal, I will need to collect a lot of data. Specifically, I will need to collect wifi speeds, GPU, CPU, and RAM usage.
In addition to that, I will need to collect the time that this data is collected. In order to collect this data, I will need to create a relay
server that will send out pings to various devices every 20 minutes or so. This relay server will then collect the data and store it in a database.
Once I have enough data, I will then be able to use this data to train a model.  I will have to remove outliers, for example, if a particular device 
is offline, I will have to remove that data point. A potential model that I am looking at using is a Recurrent Neural Network. I have chosen this 
model primarily because it is especially good at working with time-series datasets. I plan on evaluating the model by using the Root Mean Square Error,
which essentially calculates ther square root of the average squared differences between the predicted value and actual value. 

## Desired Results

In terms of desired results, I hope to be able to predict wifi speeds within 50mb/s. I also hope to see reasonable trends in the inferences. For example,
I hope to see that the p[redicted load time of a CPU is lower in the middle of the night and higher during the day when I am actually using the computer.
Finally, I hope to be able to create a program that will be able to make informed decisions about how to self-optimize itself.
