"""
Employee Performance Dashboard Application

This module provides a Flask-based web application for serving
the Employee Performance dashboard with ML visualizations.
"""
from flask import Flask
from pathlib import Path

app = Flask(__name__)

# Define paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
ASSETS_DIR = PROJECT_ROOT / 'assets'


def get_dashboard_html():
    """Generate the dashboard HTML with all visualizations."""

    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Performance</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 30px;
        }
        h2 {
            color: #555;
            border-bottom: 2px solid #007bff;
            padding-bottom: 10px;
        }
        .visualization-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .viz-card {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 20px;
        }
        .viz-card img {
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto;
        }
        .ml-section {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 20px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Employee Performance Dashboard</h1>

        <h2>Team Performance Overview</h2>
        <div class="visualization-grid">
            <div class="viz-card">
                <h3>Time Series Analysis</h3>
                <p>Cumulative event counts over time</p>
                <!-- Placeholder for bar chart visualization -->
            </div>
            <div class="viz-card">
                <h3>Recruitment Risk</h3>
                <p>Predicted recruitment risk based on performance metrics</p>
                <!-- Placeholder for time series visualization -->
            </div>
        </div>

        <div class="ml-section">
            <h2>ML Performance Analysis</h2>
            <p>KMeans clustering analysis of department performance metrics</p>
            <img src="/static/ml_performance.png" alt="ML Performance Visualization" />
        </div>
    </div>
</body>
</html>
    """
    return html_template


@app.route('/')
def index():
    """Serve the main dashboard page."""
    return get_dashboard_html()


@app.route('/employee/<int:employee_id>')
def employee_view(employee_id):
    """Serve employee-specific dashboard."""
    html = get_dashboard_html().replace(
        '<h1>Employee Performance Dashboard</h1>',
        f'<h1>Employee Performance - Employee {employee_id}</h1>'
    )
    return html


@app.route('/team/<int:team_id>')
def team_view(team_id):
    """Serve team-specific dashboard."""
    html = get_dashboard_html().replace(
        '<h1>Employee Performance Dashboard</h1>',
        f'<h1>Team Performance - Team {team_id}</h1>'
    )
    return html


# Configure static file serving for assets
@app.route('/static/<path:filename>')
def serve_static(filename):
    """Serve static files from assets directory."""
    from flask import send_from_directory
    return send_from_directory(str(ASSETS_DIR), filename)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
