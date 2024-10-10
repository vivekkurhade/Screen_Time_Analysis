 <h1>Screen Time Analysis</h1>

    <p>Hey there! 👋</p>

    <p>So, this project is all about analyzing screen time data from different apps. You know how we all get a bit curious about how much time we spend on our phones? Well, this code does just that!</p>

    <h2>What’s Inside?</h2>

    <h3>Libraries Used</h3>
    <ul>
        <li><strong>Pandas</strong>: For handling our data in a cool and easy way.</li>
        <li><strong>NumPy</strong>: Just in case we need some mathematical operations.</li>
        <li><strong>Matplotlib</strong>: To create awesome graphs and charts. Gotta visualize that data!</li>
    </ul>

    <h3>Dataset</h3>
    <p>We're using a CSV file named <code>screentime_analysis.csv</code>. Make sure you have this file in the same directory as the script. It has columns for the app names, usage in minutes, and the date.</p>

    <h2>What Does the Code Do?</h2>

    <ol>
        <li><strong>Importing and Preprocessing the Data:</strong>
            <p>It reads the CSV file and converts the date column into a proper datetime format.</p>
        </li>
        <li><strong>Total App Usage:</strong>
            <p>The code groups the data by app and sums up the total usage in minutes. Then, it plots a bar chart showing which apps are used the most.</p>
        </li>
        <li><strong>Daily Usage Trends:</strong>
            <p>It checks how usage changes over time for each app. A line plot is created for each app to show trends.</p>
        </li>
        <li><strong>Average Usage by Day:</strong>
            <p>This section breaks down the average usage for each day of the week. It creates a bar chart showing how our screen time varies from Monday to Sunday.</p>
        </li>
        <li><strong>App-Specific Usage:</strong>
            <p>Finally, it digs deeper into the average daily usage for Instagram, Netflix, and WhatsApp. It shows a grouped bar chart for easy comparison.</p>
        </li>
    </ol>

    <h2>How to Run It</h2>
    <ol>
        <li>Make sure you have Python installed along with the required libraries. If you don't have them, you can install them via pip:
            <pre><code>pip install pandas numpy matplotlib</code></pre>
        </li>
        <li>Place the <code>screentime_analysis.csv</code> file in the same folder as this script.</li>
        <li>Run the script in your terminal or your favorite Python IDE.</li>
    </ol>

    <h2>Final Thoughts</h2>
    <p>This little project is a fun way to see how much time we really spend on our phones. You might find some surprising results! If you want to modify it or add more features, feel free to dive in. Happy coding! 😄</p>
