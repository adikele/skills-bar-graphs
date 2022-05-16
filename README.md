Last Updated: 16th May 2022

# skills-bar-graphs
Plots bargraphs of a user's language proficiency for user-selected languages.
The project website can be found at: https://skills-bar.lm.r.appspot.com/

An example of a bargraph plot:
![An example of a linegraph plot using the 'Spread of Infections in Countries' link](https://github.com/adikele/covidplots-using-django/blob/master/SweChiIndia.png)

### Structure:
The backend is a RESTful API application built with Django.
The data source for the available languages in the dropdown list is a dictionary listing some of the most common languages in the world.
The bargraphs for plotting a user's levels are drawn using the Plotly library.


### Running this project:
On Linux and Mac: Download this project from Github and run it like any other Django Python project. 

Step 1 : Install Python 3.7+

Step 2 : In a terminal, first cd into the directory you would like to store this project. Then type the following commands one after:
```bash
mkdir skills-project && cd skills-project
python3 -m venv skills-venv
source skills-venv/bin/activate
git clone https://github.com/adikele/skills-bar-graphs
cd skills-bar-graphs
pip install -r requirements.txt
python manage.py runserver
```

### To Do: 
1. Create the option for the user to add languages of his/her choice.
2. Create the option for the user to decide how many languages to display for the bargraphs.
3. Store results using a cloud service.

