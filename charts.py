"""Chart creation and configuration."""

import plotly.express as px
from config import CHART_HEIGHT, CHART_MARGINS

def create_chart(data, x_col, y_col, title, y_label, color_scheme=None, range_y=None):
    """Create a plotly chart with consistent styling."""
    fig = px.area(
        data,
        x=x_col,
        y=y_col,
        title=title
    )
    
    fig.update_layout(
        title_x=0.5,
        title_font_size=20,
        xaxis_title="Time",
        yaxis_title=y_label,
        template="plotly_dark",
        height=CHART_HEIGHT,
        margin=CHART_MARGINS,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    
    if range_y:
        fig.update_yaxes(range=range_y)
    
    if color_scheme:
        fig.update_traces(line_color=color_scheme)
    
    return fig