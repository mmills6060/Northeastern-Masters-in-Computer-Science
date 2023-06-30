# Midterm Part 1: Analysis of Fibonacci Series

For this part of the midterm, you will generate a report looking at the time analysis 
of various fibonacci series algorithms. While you will be submitting
all code you write, your grade will be based off the report written in markdown. 


## Language Selection and Algorithms  Needed
👉🏽 **Task** : Implement the algorithms in two different languages.

For this report, you will need to pick one language in addition to C. You may 
pick a language from the following options:

* Python
* Java
* C#
* Kotlin
* Rust

While most of you know Python, you are encouraged to explore other languages, but the choice is yours.  In BOTH *C* and
your second language, you will need to implement the following algorithms. 

* Find the Nth value of the Fibonacci Series... 
  * Iteratively 
  * Recursively
  * Using Dynamic Programming

* Be able to print out from 1..N of the Fibonacci Series
  * Print just N
  * Print nothing / execute correctly 

Go back to your [Dynamic Programming Lab] for a similar setup.  The code had the option to print either 
everything, the final result, or nothing. The nothing version helps with running tests scripts. 

For your second language, you will want to use techniques that are more common for that language, and are free to
use their full library support.

The primary goal of this assignment in addition to demonstrating your understanding of Big O and dynamic programming, 
is for you to explore the differences between languages, and ways to make your code more efficient. 

## Report
👉🏽 **Task** : Write your final report in your [README.md]. Make sure to use proper "formatting".

An outline for the report is provided already in your [README.md]. While you are free to modify / adapt
the outline to your writing style, you will need to make sure each topic is addressed. 

Topics need to include:
* Overview - Describe the algorithm, and common approaches to solving it. Address all three (iterative, recursive,
and dynamic programming). **Include the BIG O analysis**. It can be a chart, but also describe how you
got to it. Saying,  "I read about it", doesn't work. 
* Empirical Data & Discussion - Does the empirical data (running the code and getting timings) match with your analysis? 
What are other factors affecting the run time? This is a good place to include charts/images.
* Language Analysis - make sure to include why you picked the second language. What were some of the features you wanted
to test to help with your understanding of that language?
  * Language 1: C - talk about implementing the code in C. What were concerns or issues you had? What did you have
  to focus on the most to make it work 
  * Language 2: (YOUR CHOICE) - talk about implementing the code in the second language. Which features helped you?
  What were some concerns you ran into that you had to account for? Did you end up using specific libraries?
* Comparison and Discussion Between Experiences - Make sure to compare and contrast your experiences with languages
and use this opportunity to better detail any differences that came up in your empirical results. This is also
a great location to talk about things you tried/attempted, but opted not to be part of your full report. 
* Conclusions / Reflection - Mainly a reflection / lessons learned, but ties up your final report with the key takeaway
experiences. 

> We don't have a specific format for references, but if you use references make sure to include them! 

## 📝 Grading Rubric
You will submit your files on gradescope, including both the report, your code, and any (text-based) data files
you generated. This is a **SUMMATIVE** assignment, and as such, will follow a traditional grading pattern meaning
grades will not be calculated until after the late date. 

As per usual, you will have a due date and an available by/late date. We don't charge a penalty for being late, but the 
hard cutoff is a hard cutoff, no exceptions. Why, because you should be submitting by the due date, and use the
extra window in case there are issues. Waiting until the available by date does not warrant any additional time.


### Canvas Rubric
For this assignment, you will *submit* to canvas by providing a link to your github classroom repository (there is no gradescope submission). The grading will be manually graded following the rubric in canvas. The rubric is as follows:

| Category | Missing (0pts) | Learning (1pts) | Approaching (2pts) | Meets (3pts) | Exceeds (4pts) |
| -------- | --------------- | ---------------- | ------------------- | ------------- | --------------- |
| **Code Quality** | No code  | Code exists but is not documented or tested. | Code exists, is documented or tested by including test files for all the code. | Code is both documented and test files included. | Code is written correctly, based on the language norms including memory management and small concise functions. Tests included to show validity. |
| **Writing / Grammar** | No report | Difficult to read. Report uses basic grammar, may have misspelling and obvious grammar mistakes. | Difficult to read due to poor sentence structures and wording choices. | Report uses grammar at a college level. | Report is easy to read, follows proper formatting guidelines, matches correct audience. | 
| **Visuals** (chart, graph, math notation, etc) | No visuals | Student includes visuals, but they are distracting and not informative. | Has a visual but no reference to visual in the paper, and out of place. | Visuals are informative, and help clarify the report. | Visuals are informative, and described properly in the paper writing, adding to the overall report. 
| **BigO** | No mention  | Provides minimal complexity discussion. | Provides BigO run-time for only part of the functions. | Provides Big O for the required functions/algorithms, including both space and time complexity. | Provides Big O, including space & time, also compares and contrasts in discussion using Big O as a means to compare performance. |
| **Empirical Analysis** | No mention | Provides minimal discussion. | Uses visuals to compare and contrast. | Details differences between algorithms based on run times. | Details differences apparent based on analysis, and provides concerns and potential limitations of the analysis. |
| **Language Analysis** | No mention | Provides code snippets, and details a single language's implementation. | Provides code snippets for  both languages. | Compares and contrasts two languages, giving advantages and disadvantages. | Able to identify limitations for both that may affect analysis. Adjusts analysis based on limitations. | 


24 points total

## 📚 Resources
* [Sample Report](sample_midterm) - A sample midterm for comparison/examples. 
* [Github Markdown Tables](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/organizing-information-with-tables)
* [Markdown Latex Math](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)
* [Latex Math](https://en.wikibooks.org/wiki/LaTeX/Mathematics) 
* [Tables Generator](https://www.tablesgenerator.com/markdown_tables)
* [Grammarly How to write a report](https://www.grammarly.com/blog/how-to-write-a-report/) - no need to follow their specific format, but decent guidelines.
* [Indeed Write A Report](https://www.indeed.com/career-advice/career-development/how-to-write-a-report) - same, no need for specific format, but decent guidelines


<!--- Link References -->
[README.md]: ../README.md
[Dynamic Programming Lab]: https://github.com/CS5008-khoury-lionelle/TeamActivities/tree/main/Module07