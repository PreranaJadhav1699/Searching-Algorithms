1. Overview

This project compares four different search algorithms:

Linear Search

Binary Search (on a sorted array)

Binary Search Tree (BST) search

Red-Black Tree search

The program is built in Python using Flask and a small HTML page.
The user can enter an array, choose a target value, pick an algorithm, and see:

whether the target was found

how long the search took
a table comparing all four algorithms
a line chart that shows running time vs. input size

The main idea is to observe how the running time changes when the input size grows and how the algorithms behave differently.

2. Requirements

Python 3

Flask library

3. How to Run the Project

Download the project ZIP archive.

Extract the folder to a location on your system.

Open a terminal / command prompt in the extracted project directory (the one with main.py).

Install Flask (only needed once):

pip install flask

Start the program:

python main.py

4. Files in the Project

main.py

Contains all four search algorithms.

Implements the Binary Search Tree and Red-Black Tree structures.

Handles timing for each algorithm.

Defines the Flask route that connects the backend to the HTML page.

templates/home.html

Front-end page for the project.

Has the form for entering the array, target, and algorithm choice.

Includes a random array generator (JavaScript).

Shows the result message, comparison table, and performance chart (using Chart.js).

5. How the Interface Works

On the web page, the user can:

Enter an array as comma-separated numbers (for example: 3,7,1,56,34).

Optionally, generate a random test array by providing:

minimum value (From),

maximum value (To),

number of elements (Count).

Enter the target value to search for.

Select one of the four algorithms from the dropdown list.

Click “Run Search” to send the data to the backend.

After running:

A short message shows if the target was found or not (and indices for linear search).

A table lists all four algorithms with:

whether they found the target,

and their running time in seconds.

A line chart displays input sizes on the x-axis and time on the y-axis for all algorithms.

