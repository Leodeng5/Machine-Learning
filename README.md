# Machine Learning Projects
Repository consists of various implementations of testing different kinds of Machine Learning Algorithms in different context (Forest Fire Prediction, Analysis of the specificity of HIV-1 Protease, etc.).

The **ML-Theory-Experimental** folder tests a novel Machine Learning method that attempts to combine Decision Trees with other algorithms (Combining Classical Occam's Razor Learning with Vapnik's Modern Statistical Theory).

All python implementations utilize the Orange Machine Learning Software.
A preliminary implementation was done using MATLAB. Code dates back to 2014.

**General Test of All ML Methods included in root of repository**
- Meant to provide an easily modifiable template for testing the efficiency/accuracy of different Machine Learning Algorithms on different types/sizes of databases. A similar script is used within each specific application seen in repositories folders.

1. Forest Fire Prediction Tool (2013-2018)
	 - Includes script to process data from a local Fire Weather Database provided by the Northwest Interagency Coordination Center (located in Portland, OR).
	 - Includes script to easily train machines on a random subset of a given database (percentage of total database is modifiable) and test on the unlearned data for accuracy.
	 - PDF of published paper provided.

2. HIV-1 Analysis
	 - Deals with data on HIV-1 Protease's chemical specificity with goal to create machine that can derive rules that may assist drug developers in procuring an inhibitory vaccine.