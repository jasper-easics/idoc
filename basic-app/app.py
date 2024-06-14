import plotly.express as px
from shiny import App, render, ui
from shinywidgets import output_widget, render_widget

data = dict(
    character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    value=[14, 14, 12, 10, 2, 6, 6, 4, 4])

app_ui = ui.page_fluid(
    ui.panel_title("Interactive Documentation"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),

    ui.navset_tab(
        ui.nav_panel(
            "Ordinateur",
            ui.div(
                {"style": "font-size:100px; font-weight:bold; padding: 180px 0; text-align:center;"},
                "Ordinateur"
            ),
        ),
        ui.nav_panel(
            "Plot",
            output_widget("plot", width=1000, height=600)
        ),
        ui.nav_panel(
            "Commandments",
            {"style": "font-size:40px; padding: 180px 0;"},
            ui.markdown(
            """
            ```bash
            python -m pip install shiny
            shiny create
            shiny run
            ```
            """),
        ),
        id="tab",
    )
)


def server(input, output, session):
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"

    @render_widget
    def plot():
        sunburst = px.sunburst(
                data,
                names='character',
                parents='parent',
                values='value',
                branchvalues="remainder"
                )
        return sunburst

app = App(app_ui, server)
