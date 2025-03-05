# Activity Recommendation Program / r00t
#### Video Demo:  <URL HERE>

## Overview 
The Activity Recommendation Program is a Python-based application that provides users with personalized activity suggestions based on their available time and preferences. Whether you’re looking 
to be productive, engage in self-care, or simply unwind, this program intelligently recommends activities that fit your schedule. It also prioritizes tasks based on importance and ensures that
users can manage their time efficiently.A unique feature of this program is that it can provide inspirational quotes at the beginning of each session, which equips the user with a positive attitude
to perform their tasks. Considering user-defined constraints such as bedtime and activity type of interest, this program brings value addition to daily planning and helps users make the optimum
utilization of their time.

### Features
* Personalized Activity Suggestions – Activity suggestions are personalized according to user input for relevance and applicability.
* Category-Based Filtering – The user is given the option to choose a particular category of activities (e.g., work, fitness, relaxation) or general suggestions.
* Priority-Based Ranking – More important tasks are prioritized first to promote efficient time management.
* Motivational Quotes – Inspirational quotes at the beginning of each session motivate the user and increase productivity.

### Installation

1. Install Python

Ensure you have Python installed on your system. You can verify this by running the following command in the terminal (Mac/Linux) or command prompt (Windows):

python --version

If Python is not installed, download and install it from the official Python website: python.org.

2. Clone or Download the Repository

To obtain the program files, you can either download the ZIP file manually or use Git:

git clone https://github.com/aggxx/project.git

3. Install Required Dependencies

Some features of this program may require additional Python libraries. Install dependencies using:

pip install -r requirements.txt

This will install all necessary packages automatically.

4. Run the Program

Execute the Python script using:

python project.py

Once started, the program will guide you through the activity recommendation process.

# How It Works
* Start the Program – Run the project.py script in your terminal or command prompt.
* Enter Your Name – The program greets you personally for a friendly experience.
* Provide Your Time Constraints – Enter the current time and your bedtime. The system uses this information to suggest activities that fit your schedule.
* Select an Activity Category (Optional) – You can choose a specific category (e.g., work, health, fun) or request a general recommendation.
* Receive Recommendations – The program suggests activities based on your available time and prioritization rules.
* End the Session – Once you receive your recommendations, you can choose to exit or restart the program.

### At the start of each session, a motivational quote will be displayed to inspire productivity.

# Configuration and Customization
Users can customize various aspects of the program by modifying the Python script:
* Adding New Activities – To introduce new activities, update the predefined database in project.py.
* Changing Motivational Quotes – Modify or expand the list of quotes in quotes.
* Adjusting Priorities – If certain tasks should be prioritized differently, update the ranking in database.


# So how did we write this program?

We created a list to put inspirational quotes. Every time the program runs, it will randomly choose one to greet the user. Because we use this program
when we are not motivated and use our time more efficiently. So, we thought it would be funny to see a message like this when we open the program. 
We created a dictionary (db) that stores the daily activities of the user. (Me) Adora and (My teammate) Aarya. Each user has a unique list of activities
they do, with different time frames and priorities. In the Main function, we call and execute the functions and variables we created. We created a 
welcome() function, which randomly selects a quote from a list of quotes and prints it as a greeting. To select a random quote, we used the random.
choice() function, which is a function of the random library. We created a userin() function. This function first asks the user for their name, current
time, and planned sleep time. We used the datetime.strptime() function to convert the variable whattimeisnow to a datetime object. The format "%H:%M" 
tells the function that the time is in hours and minutes (24-hour format). We stored the result as a datetime object in the startTime variable. We did
the same thing for endTime. Next, we used print to print a list of categories, each corresponding to a number. The user can then select one of these
categories. We used end="" to prevent input() from starting a new line after the categories are printed. Next, we asked the user to enter a number
that corresponds to one of the categories. If the user leaves the input blank, they will get all events, not just a specific category. Next we check if
the user left the input blank. If the selection is an empty string (i.e. the user pressed Enter without typing anything), we set the category variable to
None. Then, we created a dictionary called categorytochoose, which matches category numbers (as strings) with category names. We defined a function called
getactivities. We got the username, startTime, endTime, category variables. Next, we checked if the username is in the database. If the username is
not found, we print an error message. So if the user is not in the database, we stop this function earlier. If the username is found, we retrieved the
list of activities associated with that user from the database and saved it in the activities_db variable. Next, we have created an empty list called
aactivities. This list will hold activities that match the user's time range and optional category filter, for later use. We check if a category filter
is provided. If the category is not None, we check if the "category" of the current activity matches the provided category. If they don't, we skip repeating
the loop using continue. We have used split("-") function to create and format the best time range of activities and divide it by start and end time. 
We converted the start and end times of the event into datetime objects using the datetime.strptime() function from the datetime library. because we wanted
to write the times in 24-hour format (HH:MM). We have created activityreco function, with this function we check if there is any activity in the provided
activity list and if there is activity then it prints a message listing the available activities from a specific category or all activities and displays details
like activity name, category, suggested time range, duration in minutes and priority order; if no activity is found then it informs the user that no activity is
available in the selected category or specified time range.













