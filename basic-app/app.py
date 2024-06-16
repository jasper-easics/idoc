import plotly.graph_objects as go
from shiny import App, render, ui
from shinywidgets import output_widget, render_widget

data = dict(
    labels=["TOP", "CUTOP", "DUTOP", "RAM", "data_fsm", "CKTOP", "REGTOP", "regs", "I2C"],
    parents=["", "TOP", "TOP", "DUTOP", "DUTOP", "TOP", "TOP", "REGTOP", "TOP" ],
    values=[0, 14, 2, 10, 2, 6, 2, 4, 2])

app_ui = ui.page_fluid(
    ui.page_navbar(
        ui.nav_panel(
            "Ordinateur",
            ui.layout_sidebar(
                ui.sidebar(open="always"),
                ui.input_switch("enhance", "Enhance", False),
            ),
            ui.div(
                {"style": "font-size:100px; font-weight:bold; padding: 180px 0; text-align:center;"},
                ui.output_text("ordinateur_txt"),
            ),
        ),
        ui.nav_panel(
            "Plot",
            ui.row(
                output_widget("plot"),
                align="center"
            )
        ),
        ui.nav_panel(
            "Frameworks",
            ui.row(
                ui.output_image("frameworks_img"),
                align="center"
            )
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
        title="Interactive Documentation",
    ),
)


def server(input, output, session):
    @render.text
    def ordinateur_txt():
        return "Computer" if input.enhance() else "Ordinateur"

    @render_widget
    def plot():
        fig = go.Figure(go.Sunburst(**data))
        fig.update_layout(
                width=800,
                height=800,
                font=dict(
                    family="Courier New, monospace",
                    size=24
                    )
        )
        return fig

    @render.image
    def frameworks_img():
        from pathlib import Path

        img_dir = Path(__file__).resolve().parent / "img"
        img: ImgData = {"src": str(img_dir / "github_star_history.png"), "width": "1200px"}
        return img


app = App(app_ui, server)
