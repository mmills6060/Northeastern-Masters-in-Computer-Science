# Downloading the dataset

In order to download the Dataset I had to sign up for a huggingface account. They recently removed functionality for username and password so I had to input a token where it says to put in your password. This can be found under settings on the hugginface website. 

Link to the dataset: https://huggingface.co/datasets/bigcode/the-stack-dedup

I haven't put a whole lot of time into implementing the dataset with the other tensorflow code that will do the training. I think what will happen is we may need to download it in a different way for it to work with tensorflow. I could be wrong. 


# Tensorflow sample code

I added the tensorflow sample code. It might be able to run right out of the box. Once we are able to get it to run, we should be able to literally just replace the dataset URL with the actual code generation dataset that we will be using. 

# Info on AI Agents

This program is implemented using a large language model called Ollama. This is an interesting way to go about impplementing a large language model because everything is local. This is beneficial because it can get very expensive to have a similar architecture with an OpenAI API. Since everything is done locally, we can run this AI Agent program as much as we want without worrying about getting billed every time an AI Agent has something to say. 


Details on Ollama and how to download can be found here: https://ollama.ai/


Basically the way I see the whole AI Agent architecture is by assigning each agent a "role" where you give the agent a role and explain what purpose it has. Then you feed it a prompt. There may need to be additional logic for some AI agents like if else statements. An example would be the critic agent and writing if else statements for if the critic gives it a score of greater than 80.   

# Need to Implement

- Debugging AI Agent
This AI Agent will basically take code that doesn't work and generate a fixed version of the code. It will then pass this code to the code running AI agent. This will get passed back to this AI agent if the code doesn't run, and keep getting passed back until it actually does run. It could be 5 times or 50 times, but eventually it should be able to be run. The fact that we are able to have a free and local large language model run at this point is really revolutionary. Using an OpenAI API that costs money would not make this part possible. Honestly haven't seen anyone do this on github yet.  


- Code Generation AI Agent
This AI Agent basically takes a prompt and generates code based on the prompt. This acts just like The way ChatGPT works, just for code instead of normal text.

- AI Agent that runs the code
This AI Agent will basicaly take the written code from the code generation AI agent and try to run it. I think there are a couple libraries out there that will allow us to do this. If the code runs, we can pass it to the critic agent to review and score. If the code doesnt run, pass to the debugging agent.  

- Code Structure AI Agent
This AI Agent will come up with a basic structure for the program. What files should be named what. What the classes should be. What should be a class and what should be a separate file. That kindof stuff. 

- Critic AI Agent
This AI Agent basically takes in running code as well as what the original request was from the user and ranks the program from 1-10 on how well the program completes the user's request. TShis then get's passed to the code generation agent if it is below a score of 8. This agent will also explain why it gave it the score it did, which can help the code generation agent modify the code accordingly. If the score is 8 or above, we can complete the loop and the user should be presented with the final written program.  

- Package manager agent

There will probably have to be some type of package manager agent that looks to see if all th packages and python modules are properly installed. If something isn't installed, it will have to somehow know what package needs to be installed and what it's called. It will also have to know how to install it, probably through command line command. 


