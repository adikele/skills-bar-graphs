import pandas as pd
import django
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SkillsSelectForm

from .utilities import *  # not used
import random
from datetime import date
from plotly.offline import plot
import plotly.graph_objects as go


def index(request):
    return render(request, "index.html")


def api_info(request):
    return render(request, "skillsbar/api_info.html")


def valstreetdesign(request):
    return render(request, "skillsbar/valstreetdesign.html")


def show_skills(request):
    form = SkillsSelectForm()
    # years = ['general python skills', 'Django skills', 'cloud programming skills', 'React skills' ]
    # years = ['general python skills']
    if request.method == "POST":
        form = SkillsSelectForm(request.POST)
        # foll does not work:
        # form = SkillsSelectForm(request.POST initial={"prefered_contact": res})
        # form = SkillsSelectForm(request.POST initial={"selected_skill2": Marathi})
        if form.is_valid():
            cd = form.cleaned_data
            plotting_skill1 = cd.get("selected_skill1")
            plotting_level_skill1 = cd.get("selected_level_skill1")
            plotting_skill2 = cd.get("selected_skill2")
            plotting_level_skill2 = cd.get("selected_level_skill2")
            plotting_skill3 = cd.get("selected_skill3")
            plotting_level_skill3 = cd.get("selected_level_skill3")
            plotting_name = cd.get("name")
            skill_names = [plotting_skill1, plotting_skill2, plotting_skill3]  # adding

            fig = go.Figure()
            colour_list = [
                "rgb(26, 118, 255)",
                "rgb(204, 204, 205)",
                "rgb(255, 100, 100)",
                "rgb(100, 255, 100)",
            ]
            today = date.today()
            fig.add_trace(
                go.Bar(
                    x=skill_names,
                    y=[40, 40, 40],
                    name="Beginner level",
                    marker_color="rgb(55, 83, 109)",
                )
            )

            fig.add_trace(
                go.Bar(
                    x=skill_names,
                    y=[
                        plotting_level_skill1,
                        plotting_level_skill2,
                        plotting_level_skill3,
                    ],
                    name=plotting_name + "'s skill level",
                    marker_color=random.choice(colour_list),
                )
            )

            fig.update_layout(
                title=f"Self-evaluation of {plotting_name}'s skills dt:{today}. Chart is done using Python's Plotly library",
                xaxis_tickfont_size=14,
                yaxis=dict(
                    title="Skill level",
                    titlefont_size=16,
                    tickfont_size=14,
                ),
                legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="left",
                    x=0.01,
                    bgcolor="rgba(255, 255, 255, 0)",
                    bordercolor="rgba(255, 255, 255, 0)",
                ),
                barmode="group",
                bargap=0.15,  # gap between bars of adjacent location coordinates.
                bargroupgap=0.1,  # gap between bars of the same location coordinate.
            )

            layout = {
                "title": "Title of the figure",
                "xaxis_title": "X",
                "yaxis_title": "Y",
                "height": 420,
                "width": 560,
            }

            plot_div = plot({"data": fig, "layout": layout}, output_type="div")

            return render(
                request,
                "skillsbar/ref_plotly_graph.html",
                context={"plot_div": plot_div},
            )

    else:
        # this is the case when user sees the form for the first time
        form = SkillsSelectForm()
    return render(request, "skillsbar/skills_form.html", {"form": form})


'''
#woks -- this is the reference from:
#https://albertrtk.github.io/2021/01/24/Graph-on-a-web-page-with-Plotly-and-Django.html
def ref_plotly(request):

    """ 
    View demonstrating how to display a graph object
    on a web page with Plotly. 
    """
    
    # Generating some data for plots.
    x = [i for i in range(-10, 11)]
    y1 = [3*i for i in x]
    y2 = [i**2 for i in x]
    y3 = [10*abs(i) for i in x]

    # List of graph objects for figure.
    # Each object will contain on series of data.
    graphs = []

    # Adding linear plot of y1 vs. x.
    graphs.append(
        go.Scatter(x=x, y=y1, mode='lines', name='Line y1')
    )

    # Adding scatter plot of y2 vs. x. 
    # Size of markers defined by y2 value.
    graphs.append(
        go.Scatter(x=x, y=y2, mode='markers', opacity=0.8, 
                   marker_size=y2, name='Scatter y2')
    )

    # Adding bar plot of y3 vs x.
    graphs.append(
        go.Bar(x=x, y=y3, name='Bar y3')
    )

    # Setting layout of the figure.
    layout = {
        'title': 'Title of the figure',
        'xaxis_title': 'X',
        'yaxis_title': 'Y',
        'height': 420,
        'width': 560,
    }

    # Getting HTML needed to render the plot.
    plot_div = plot({'data': graphs, 'layout': layout}, 
                    output_type='div')

    return render(request, 'skillsbar/ref_plotly_graph.html', 
                  context={'plot_div': plot_div})

#woks!
def show_graph(request):
    years = ['general python skills', 'Django skills', 'cloud programming skills', 'React skills' ]


    fig = go.Figure()
    fig.add_trace(go.Bar(x=years,
                y=[60, 60, 60, 40],
                name='Skill level requirement for junior backend developer',
                marker_color='rgb(55, 83, 109)'
                ))
                
    fig.add_trace(go.Bar(x=years,
                y=[80, 60, 40, 20],
                name="Aditya's skill level",
                marker_color='rgb(26, 118, 255)'
                ))

    fig.update_layout(
        title="Chart for TE Palvelu: Self-evaluation of Aditya Kelekar's skills dt: 25.4.2022. Chart is done using Python's Plotly library",
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Skill level',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)',
            xanchor="right",
        ),
        barmode='group',
        bargap=0.15, # gap between bars of adjacent location coordinates.
        bargroupgap=0.1 # gap between bars of the same location coordinate.
    )

    layout = {
        'title': 'Title of the figure',
        'xaxis_title': 'X',
        'yaxis_title': 'Y',
        'height': 420,
        'width': 560,
    }

    plot_div = plot({'data': fig, 'layout': layout}, 
                    output_type='div')

    return render(request, 'skillsbar/ref_plotly_graph.html', 
                  context={'plot_div': plot_div})


def select_country_form(request):
    #Gathers data from the form 
    #gives data to Plotly to plot
    
    form = CountrySelectForm()
    if request.method == "POST":
        form = CountrySelectForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            country_sel = cd.get("selected_country")
            show_graph() 



            fig = create_figure(x, y)

            response = django.http.HttpResponse(content_type="image/png")
            FigureCanvas(fig).print_png(response)
            return response

    else:
        # this is the case when user sees the form for the first time
        form = CountrySelectForm()
    return render(request, "skillsbar/country_form.html", {"form": form})

'''
