# Assignment 1 - Designing Models and Analyzing Data (Template)
(remove: **text between brackets to be removed**)

> * Participant name: Chathura Jayalath
> * Project Title: Subway Tunnel Optimization

# General Introduction

The first part of this assignment explores designing models (and basic Python/Git features). 

We will look at **subway model in a city** system. A **subway system** is an underground, tube, or metro, underground railway system used to transport large numbers of passengers within urban and suburban areas - modern subways use different types of electronic data collection sensors to supply information which is used to manage assets and resources efficiently. 

The second part of the assignment explores data analysis. Data analysis and visualization is key to both the input and output of simulations. This assignment explores different random number generators, distributions, visualizations, and statistics. Additionally, it will look at getting you accustomed to specifying input and output variables to a system. We will also practice working with real data.


# Part 1: Designing a Model - Subway System

(remove: States your motivation clearly: why is it important / interesting to solve this problem?)

(remove: Add real-world examples, if any)

(remove: Put the problem into a historical context, from what does it originate? Are there already some proposed solutions?)


![Image of Subway City System](images/subway_model.png)

## (Part 1.1): Requirements (Experimental Design) **(10%)**

(remove: You should start by specifying a set of requirements. I specified a topic a Subway escalator. What exactly does that mean - practice formulating your own set of requirements and an experiment. Define problems cities face and hypothesize how a subway system could help alleviate these issue. This helps you think about your problem communication and system objectives inputs, functions, and outputs - they should be clearly specified.)

## (Part 1.2) Subway (My Problem) Model **(10%)**

(remove: add a high-level overview of your model, the part below should link to the model directory markdown files)
(remove: Look at the [**Object Diagram**](model/object_diagram.md) for how to structure this part of Part 2 for each diagram. Only the Object diagram has the template, the rest are blank. )

* [**Object Diagram**](model/object_diagram.md) - provides the high level overview of components
* [**Class Diagram**](model/class_diagram.md) - provides details of (what are you providing details of)
* [**Behavior Diagram**](model/behavior_diagram.md) - provides details of (what are you providing details of)
* [**Agent / User case** (if appropriate)](model/agent_usecase_diagram.md) - provides details of (what are you providing details of)

## (Part 1.3) Subway (My Problem) Simulation **(10%)**

(remove: Describe how you would simulate this - including type of simulation, rough details, inputs, outputs, and how it will help you analyze your experimental hypothesis, or nullify your null hypothesis.)


## (Part 1.4) Subway City (My Problem) Model **(10%)**
[**Code template**](code/README.md) - Starting coding framework for the (insert your exact problem here.)
You are expected to create the python files - the code should run without errors, create and object(s) for your system, but not provide function detail.



## (Part 1.5) Specifying the Inputs to a System **(10%)**

(remove the below points once ideas are satisfied)
* Specify the independent and dependent input variables of your subway esclator model
* Specify where the data will come from measured subset of real data (empirical) or synthetic data
* What kind of statistics are important to capture this input data
* How do you plan to analyze the output of your model?
* What ways will you visualize your data - charts, and graphs you will create?
* What clever way will you visualize your output with a useful infographic?



# Part 2: Creating a Model from Code

## (Part 2.1) **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model **(10%)**
Here [**we provide an overview**](code/POTS_system/README.md) of the **P**ortable **O**rganic **T**rouble-free **S**elf-watering System (**POTS**) Model and provide a source code template for the code found in  [**the following folder**](code/POTS_system/). Please create a **class** diagram of this model (replace the placeholder diagram). (you can use paper and pencil or a digital tool).



# Part 3: Data Analysis

## (Part 3.1) - Real Data **(10%)**

Find a datasource that looks at part of this model - subway stations locations / escalator number, heights, widths / volume of passangers - ridership numbers   (*fits* - we are pretty loose here, it can be anything.)

* Write up a paragraph that describes the data and how it fits into your system.
* Load the data into Python
* Calculate a few useful statistic on the data - keep it simple- STD, means, etc..., this is just designed * to get used to working with real data. Explain the insights you derive from these statistics.
* Visualize the raw data - visualize a few critical aspects of the data to better describe what it is, what it is showing, and why its useful to your system.
* Calculate and plot some summary statistics that better describe the data.

(Add your plots and visualization here)
(Put your data into the data directory)


## (Part 3.2) -  Plotting 2D Random Number Generators **(15%)**

This portion of the assignment looks at generating random numbers in Python and understanding how to properly plot them. Plot two different random numbers, pseudo random and quasi random, for five different N values. There should be 10 subplots, all properly formatted 2D plots. Note, each of the N points will have two coordinates, an x and a y, therefore you will need to generate two random numbers for each point. You should replace the image with your results in a simalar format. Discuss how the patterns differ. Feel free to change the N values from the suggested N values in the image to state your case.

![Image of 2d template City](images/randomNumbers.png)

### Discussion

I have used __*Mersenne Twister* random number generator__ (from `random` python library) as the __pseudo-random number generator__ and the __*Sobol* sequence generator__ (from `sobol_seq` python library) as the __quasi-random number generator__. 

The pseudo random generator output seems to have no pattern and looks more organic/natrual when compared to the quasi random generator output.

The quasi-random number generator output shows patterns when the number of datapoints are 500, 1000 and 2000. However, such patterns are not clearly visible when there are 100 datapoints probably due to less detail. When the datapoints are 5000, the pattern is slightly visible but not clear probably due to the high density of datapoints. Moreoever, the pattern observed changes with the number of datapoints. 

The patterns that appear in quasi-random output feels more artificial while the pseudo-random output feels more natural and organic.

## (Part 3.3) -  Plotting 1D Random Distributions **(15%)**

Now, choose three different distributions to plot in 1D, or as a histogram. Choose a pseudo-random generator and generate three different distributions. Example distributions are Uniform (part 8), Normal, Exponential, Poisson, and Chi-Squared, but feel free to use any three distributions of your choice. Again, plot each distribution for five different Ns. This will result in 15 different subplots, formatted similar to the image in Part 8. Include your properly formmated 1D plots below and breifly describe what we are looking at and how things change as N is changed.

![Image of 2d template City](images/randomNumbers2.png)

### Discussion

The figure above shows normalized histograms of Pseudo random samples of Uniform(0,1), Normal(0,1) and Chi-Squared(1) distributions. They were generated using `numpy` and `random` python libraries and plotted with `matplotlib` python library.

The first row shows Uniform distribution sampling. The parameters used for Uniform distribution are: a = 0, b = 1 which defines a uniform distribution between the values of 0 and 1. At low N values, the uniformity is not observed. The instance in which the plots were drawn, the probability density of graph where N = 100 has more irregular shape compared to N = 5000 (when N = 5000 the plot is more similar to the ideal uniform plot. As the number of instances increases the fairness of the random number generator has increased.

The second row shows Normal distribution sampling. The parameters used for Normal distribution are: mean = 0.0 and standard deviation = 1.0 which defines the standard bell curve. At low N values the plot doesn't resemble a bell curve at all. It has both very high spikes and zero values closer to the mean. As N increases, the shape of a bell curve is formed. However, it still is not anywhere close to ideal and there are clearly visible irregularities.

The third row shows Chi-Squared distribution sampling. The parameters used for Chi-Squared distribution is: degrees of freedom = 1.0. At low N values irregularities are observed although they are not so visible as for other distributions due to the inherent ideal shape of chi-squared distribution. The shape quickly converges to a better approximation of the ideal chi-squared curve as the N increases.


**Repeat the above using a quasi-random generator. Discuss the similarities and differences.**

![Image of 2d template City](images/randomNumbers3.png)

### Discussion

The figure above shows normalized histograms of Quasi random samples of Uniform(0,1), Normal(0,1) and Chi-Squared(1) distributions. They were generated using `chaospy` python library and plotted with `matplotlib` python library.

Similar to the three cases discribed in the previous section, irregularities are observed when N values are smaller for all three cases and they decrease (become more similar to ideal shapes) as the N increases.

However, the irregularities are more symmetric in the quasi random generator compared to its psuedo random generator respectively. Moreover it should be noted that there are no zero values in all cases of the N values chosen with quasi random generator while zero values and isolated very high values are observed in the pseudo random generator case. Instead of generating isolated very high values, the quasi random generator has generated a series of high values which have the same high probability. And that high probability is lesser than the very high value generated by pseudo random generator (e.g. in case of N=100 for Uniform distribution, the high vlaue in pseudo random generator is ~2.5 while the respective quasi random generator has a set of peaks which have a value of ~1.5).
Additionally it should be noted that for all three cases of distributions, the randomness observed with the pseudo random generator looks less artifical compared to the quasi random variable.
