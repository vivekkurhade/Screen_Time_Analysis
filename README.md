# Screen Time Analysis

Hey there! 👋 

So, this project is all about analyzing screen time data from different apps. You know how we all get a bit curious about how much time we spend on our phones? Well, this code does just that! 

## What’s Inside?

### Libraries Used
- **Pandas**: For handling our data in a cool and easy way.
- **NumPy**: Just in case we need some mathematical operations.
- **Matplotlib**: To create awesome graphs and charts. Gotta visualize that data!

### Dataset
We're using a CSV file named `screentime_analysis.csv`. Make sure you have this file in the same directory as the script. It has columns for the app names, usage in minutes, and the date.

## What Does the Code Do?

1. **Importing and Preprocessing the Data**:
   It reads the CSV file and converts the date column into a proper datetime format.

2. **Total App Usage**:
   The code groups the data by app and sums up the total usage in minutes. Then, it plots a bar chart showing which apps are used the most.

3. **Daily Usage Trends**:
   It checks how usage changes over time for each app. A line plot is created for each app to show trends.

4. **Average Usage by Day**:
   This section breaks down the average usage for each day of the week. It creates a bar chart showing how our screen time varies from Monday to Sunday.

5. **App-Specific Usage**:
   Finally, it digs deeper into the average daily usage for Instagram, Netflix, and WhatsApp. It shows a grouped bar chart for easy comparison.

## How to Run It

1. Make sure you have Python installed along with the required libraries. If you don't have them, you can install them via pip:

2. Place the `screentime_analysis.csv` file in the same folder as this script.

3. Run the script in your terminal or your favorite Python IDE.

## Final Thoughts

This little project is a fun way to see how much time we really spend on our phones. You might find some surprising results! If you want to modify it or add more features, feel free to dive in. Happy coding! 😄

