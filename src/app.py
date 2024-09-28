from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def multiplication_table():
    if request.method == 'POST':
        # Get user inputs from the form
        number = int(request.form.get('number', 1))
        up_to = int(request.form.get('up_to', 10))

        # List of colors to be used for rows
        colors = [
                    "#f2f2f2", "#ffffff", "#ffcccc", "#ccffcc", "#ccccff", "#ffcc99", "#ffffcc", "#ccffff",
                    "#ffe6e6", "#e6ffe6", "#e6e6ff", "#ffd9b3", "#d9ffb3", "#b3d9ff", "#ffb3b3", "#b3ffb3",
                    "#b3b3ff", "#ffd1dc", "#c1ffc1", "#c1d4ff", "#ffecb3", "#ecffb3", "#b3ffec", "#ffb3ec",
                    "#ecb3ff", "#ffb3d9", "#d9b3ff", "#e6b3ff", "#ffb3c6", "#c6ffb3", "#b3ffe6", "#e6b3b3",
                    "#b3e6b3", "#e6b3e6", "#c6b3ff", "#b3c6ff", "#ffc6b3", "#b3ffc6", "#c6ffb3", "#ffb3b3"
]


        # Generate the multiplication table as an HTML string
        table_html = """
        <table style="margin: 20px auto; border-collapse: collapse; width: 50%; font-family: Arial, sans-serif;">
            <tr style="background-color: #3498db; color: white; justify-content: center">
                <th style="padding: 10px; border: 1px solid #dddddd;">Multiplier</th>
                <th style="padding: 10px; border: 1px solid #dddddd;">Result</th>
            </tr>
        """

        # Create table rows dynamically based on user input
        for i in range(1, up_to + 1):
            row_color = colors[(i - 2) % len(colors)]
            table_html += f"""
            <tr style="background-color: {row_color};">
                <td style="padding: 10px; border: 1px solid #dddddd;">{number} x {i}</td>
                <td style="padding: 10px; border: 1px solid #dddddd;">{number * i}</td>
            </tr>
            """

        # Close the table tag
        table_html += "</table>"

        # Return the table with a heading
        return render_template_string(f"""
        <div style="text-align: center;">
            <h1 style="color: #3498db;">Multiplication Table for {number}</h1>
            {table_html}
            <br><a href="/">Go Back</a>
        </div>
        """)

    # Display the input form
    return render_template_string("""
    <div style="display: flex; height: 100vh; justify-content: center; align-items: center; background-color: #f0f0f0;">
        <div style="text-align: center;">
            <h1 style="color: #3498db;">Enter Multiplication Table Details</h1>
            <form method="POST">
                <label for="number" style="font-size: 1.2em;">Enter a Number:</label><br>
                <input type="number" id="number" name="number" min="1" required><br><br>
                <label for="up_to" style="font-size: 1.2em;">Upto how many times?</label><br>
                <input type="number" id="up_to" name="up_to" min="1" required><br><br>
                <button type="submit" style="padding: 10px 20px; background-color: #3498db; color: white; border: none; cursor: pointer;">Generate Table</button>
            </form>
        </div>
    </div>
    """)

if __name__ == '__main__':
    app.run(debug=True)
