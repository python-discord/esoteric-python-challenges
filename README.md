> ! Important: As of October 2, 2018, this repository and all its contents are now under the GNU General Public License Version 3 (GPLv3) See the LICENSE file for more information

# Esoteric Python Challenges

Esoteric programming challenges for the Python programming language.

These challenges are maintained by the Python Discord server. [Come check us out!](https://pythondiscord.com/)

# Challenge Information

Every week or so, we will be posting a new challenge to solve.
Generally, challenges will involve a problem to solve (e.g. implement a specific algorithm), a goal (e.g. code golf (shortest number of characters in source code)) and sometimes even some
restrictions (e.g. no use of imports)

Please note that while these challenges have these rules and restrictions, you are free to submit solutions that do *not* take them into consideration. If you do, please simply make note
of the limitations of your solutions in a comment in the source code! The ultimate goal is to have **fun**, be creative and show off your esoteric coding chops! There are no prizes or true
winners. You win if you had fun trying to solve some challenges or learn a thing or two from other peoples' solutions :) Feel free to golf your solutions to non-golf challenges or to add further 
restrictions for your own challenge.

# Submission Guidelines

At the top of the file, add a comment block with your name, and any notes regarding your solution (e.g. restrictions not followed, instructions on how to use the code, etc.)

> Tip: If your submission is a codegolf, it'd be helpful to fellow coders if you also appended to your code a less-condensed version of the golf annotated with comments on how it works

You may submit more than one solution for a challenge! Just append subsequent solutions to the same file.

## Adding your solution to the repository:

To contribute solutions, you will need a [GitLab](http://gitlab.com/) account and [Git](https://git-scm.com/) installed on your computer. The instructions assume you are using the command line. See the documentation specific to your software if you are using a graphical Git client.

Step 1: Fork and clone the repository

Head to https://gitlab.com/python-discord/esoteric-python-challenges and click the `Fork` button. This will copy this repository to your account. Then, clone your version of the repository locally:

Open a terminal and type
> `git clone https://gitlab.com/python-discord/esoteric-python-challenges.git` 


Step 2: Adding your solution

In the appropriate directory for the challenge, under the `solutions` folder, add either
* A) A single `.py` file with the name `your_name_or_handle.py`
* B) If your solution spans multiple files, *add a directory* named `your_name_or_handle` and place the files inside this new directory
> Important: Try not modifying any other files, as it complicates the merging process

Step 3: Add and commit your changes

Run the following commands on your local repository:
* `git add .` This adds all modified files to the staging area
* `git commit -m "message"` This commits the changes. Replace "message" with a short description such as `-m "add bob's solution"
* `git push` This will apply the changes to (your) *remote* repository (i.e. the version you can see on GitLab)

Step 4: Submit a merge request

Head over to the [New Merge Request](https://gitlab.com/python-discord/esoteric-python-challenges/merge_requests/new) page and use the graphical interface to chose your personal copy of the repository and proceed by clicking `Compare branches and continue` and confirm your request

Step 5: Wait

A repository maintainer will get to your merge request in the briefest of delays and (hopefully) merge it! Don't hesitate to ping Zhawn if your merge request hasn't been accepted within a couple of days!

## Licensing Information

By contributing to this repository, you understand and agree that all code in this repository is licensed under the [GNU General Public License, Version 3 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.html). 