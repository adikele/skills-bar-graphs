import plotly.graph_objects as go



def show_graph():
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
    return fig.show()

    # show_graph() in main program