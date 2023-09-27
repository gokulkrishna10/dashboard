import json

import dbConnection as db
import queries
from flask import Flask, render_template, request, abort

# Create a new Flask app instance
app = Flask(__name__)


# Define the route for the dashboard page
@app.route('/dashboard')
def entryPoint() -> str:
    try:
        # Render the dashboard.html template
        return render_template('dashboard.html')
    except Exception:
        # If an exception occurs, abort with a 404 error and a message
        abort(404, "Invalid path")


@app.route('/plot')
def plot() -> str:
    """Endpoint to fetch data for a plot.

    Returns:
        str: JSON-encoded string of time series data.
    """
    # Get the selected option from the query string
    selectedOption: str = request.args.get('key')

    # Get the corresponding SQL query for the selected option
    queryType: str = queries.QUERY_MAP[selectedOption]

    # Set up a database connection and execute the query
    cur, conn = db.setupConnection()
    cur.execute(queryType)
    rows = cur.fetchall()

    # Close the connection after the fetch operation
    db.closeConnection(cur, conn)

    # Convert the query results into a JSON-serializable format
    json_data = {'times': [d.strftime('%Y-%m-%d %H:%M:%S.%f') for d, _ in rows], 'values': [v for _, v in rows]}

    # Serialize the JSON-serializable data into a JSON string using the json.dumps() function.
    # Set the default argument to the str() function to ensure that all non-serializable values are converted to strings
    res: str = json.dumps(json_data, default=str)
    return res
