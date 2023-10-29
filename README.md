![CS50 Picture](https://goo.gl/mJwNUC)

# Harvard University - CS50’s Introduction to Artificial Intelligence with Python
This repository contains my solutions to the CS50AI's, as taught by Brian Yu. The nominally 7 week course included 12 practical assignments covering main approaches both in traditional deterministic AI and in more modern approaches such as deep neural networks and natural language processing.

Warning : before visiting this repo files, please read about [CS50's Academic Honesty rules](https://cs50.harvard.edu/ai/2023/honesty/).

## Links to the course:
[CS50AI on Harvard's website](https://cs50.harvard.edu/ai/2023/) and 
[CS50AI on edX](https://cs50.edx.org/ai)

![CS50AI](https://github.com/KhizarAI/CS50AI-projects/assets/105581015/aa7f521c-a3ef-4715-9713-e209d0d53f34)

### Week 0 - Search
The initial module covered traditional algorithms aimed at finding preferrably optimal or near-optimal ways of completing a task that can be converted to a problem of "finding a path between two points pertaining minimal cost incurred".

Algorithms covered:
- Depth-First Search
- Breadth-First Search
- Greedy best-first search
- A * search
- MiniMax
- Alpha-Beta Pruning
- Depth-Limited Minimax

#### Project 0a: Degrees
The first project utilizes the breadth-first search algorithm to find the so-called "degrees of separation" between two actors, also known as the "Six degrees of Kevin Bacon".

[Full Assignment on Harvard's website](https://cs50.harvard.edu/ai/2023/projects/0/degrees)


#### Project 0b: Tic-Tac-Toe
A project showcasing a simple game of Tic-Tac-Toe with an AI opponent utilizing the minimax algorithm to have an optimal strategy.

[Full Assignment on Harvard's website](https://cs50.harvard.edu/ai/2023/projects/0/tictactoe)



### Week 1 - Knowledge
This module deals with knowledge representation and logical reasoning in a way a machine can understand, solving logically deductive problems algorithmically.

Algorithms and concepts covered:
- Inference algorithms
- Truth table
- Model Checking
- Knowledge Engineering
- Inference rules
- De Morgan’s Law
- Conjunctive normal form
- Inference by resolution
- First-Order Logic

#### Project 1a: Knights
This project's task is to create an AI that can logically deduce solutions to various classic "Knights and knaves" problems using inference.

[Full Assignment on Harvard's website](https://cs50.harvard.edu/ai/2023/projects/1/knights)


#### Project 1b: Minesweeper
This project implements an AI to the classic Windows game, Minesweeper. It works by making safe moves based on the knowledge of the field, and if no safe move may be made, making a random one.

[Full Assignment on Harvard's website](https://cs50.harvard.edu/ai/2023/projects/1/minesweeper)



### Week 2 - Uncertainty
This module tackles the idea that the AI, like us, might not always know all the information available within the problem at any given time, due to various constraints. Therefore, the problems focus on designing AI to work with reasoning based on probabilities.

Algorithms and concepts covered:
- Unconditional probability 
- Conditional probability 
- Joint probability
- Bayes’ Rule
- Bayesian Kings 
- Inference by enumeration
- Inference by approximation
- Sampling
- Uncertainty over time

#### Project 2a: Pagerank
This assignment simulates Google's algorithm of ranking different webpages by relevancy.

[Full Assignment on Harvard's website](https://cs50.harvard.edu/ai/2023/projects/2/pagerank)


#### Project 2b: Heredity
This assignment implements a genetic-like algorithm estimating a hidden trait of having a faulty gene based on a visible disability, hearing loss in this case.

[Full Assignment on Harvard's website](https://cs50.harvard.edu/ai/2023/projects/2/heredity)



### Week 3 - Optimization
This module presents problems that can be solved by an AI finding an optimal solution within a scope of permissible solutions.

Algorithms and concepts covered:
- Local Search Algorithms
- Linear Programming 
- Arc Consistency

#### Project 3: Crossword
This project implements an AI generating crosswords given a template and a dictionary of words.

[Full Assignment on Harvard's website](https://cs50.harvard.edu/ai/2023/projects/3/crossword)



### Week 4 - Learning
This module begins the chapters on machine learning, ie. designing AI which can reach conclusions without direct human intervention.

Algorithms and concepts covered:
- Nearest-neighbor classification
- K-nearest-neighbor classification
- K-means clustering
- Supervised learning
- Unsupervised learning
- Reinforcement learning

#### Project 4a: Shopping
This project features an AI to predict whether a customer is likely to complete a purchase.

[Full Assignment on Harvard's website](https://cs50.harvard.edu/ai/2023/projects/4/shopping)


#### Project 4b: Nim
This project implements an AI which learns to play the game of NIM, ie. two players take away rings from several towers, last one to take away a ring loses.

[Full Assignment on Harvard's website](https://cs50.harvard.edu/ai/2023/projects/4/nim)



### Week 5 - Neural Networks
This module covers the currently extremely popular concept of neural networks, which is a concept created already in the 1970s.

Algorithms and concepts covered:
- Gradient Descent
- Backpropagation
- Neural network architectures (Convolutional, Recurrent, GAN)

#### Project 5: Traffic
This project implements a simple computer vision neural network that classifies road signs for automated driving.

[Full Assignment on Harvard's website](https://cs50.harvard.edu/ai/2023/projects/5/traffic)



### Week 6 - Language
The last module covers Natural Language Processing (NLP), algorithmical design through which AI can start understanding and working with human language.

Algorithms and concepts covered:
- n-gram Tokenization
- Text Categorization
- Naive Bayes
- TF-IDF
- One-Hot Representation

#### Project 6a: Parser
This project uses the nlk library to parse sentences into its basic noun phrase components

[Full Assignment on Harvard's website](https://cs50.harvard.edu/ai/2023/projects/6/parser)


#### Project 6b: Questions
This assignment parses datasets / corpuses of data by n-grams to understand the word frequencies and meanings. Then, it answers questions with likely answer-sentences from the source dataset.

[Full Assignment on Harvard's website](https://cs50.harvard.edu/ai/2023/projects/6/questions)
