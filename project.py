from datetime import datetime
import random

#Help was received from chatgpt while creating the databases.
#ChatGPT. 2025. Source: https://chatgpt.com/

quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "It does not matter how slowly you go as long as you do not stop. – Confucius"
]

db = {
    "Adora": 
      [
    {"name": "Stretching", "duration": 10, "best_time": "05:40-05:50", "priority": 2, "category": "Health"},
    {"name": "Meditation", "duration": 20, "best_time": "06:00-06:20", "priority": 3, "category": "Mindfulness"},
    {"name": "Morning Walk/Jog", "duration": 30, "best_time": "06:00-06:30", "priority": 1, "category": "Exercise"},
    {"name": "Yoga", "duration": 30, "best_time": "06:30-07:00", "priority": 2, "category": "Exercise"},
    {"name": "Cold Shower", "duration": 10, "best_time": "07:00-07:10", "priority": 3, "category": "Health"},
    {"name": "Healthy Breakfast", "duration": 30, "best_time": "07:10-07:40", "priority": 1, "category": "Nutrition"},
    {"name": "Prepare Lunch for the Day", "duration": 20, "best_time": "07:40-08:00", "priority": 2, "category": "Nutrition"},
    {"name": "Plan Daily Goals", "duration": 15, "best_time": "08:00-08:15", "priority": 1, "category": "Productivity"},
    {"name": "Journal/Gratitude Practice", "duration": 15, "best_time": "08:15-08:30", "priority": 2, "category": "Mindfulness"},
    {"name": "Review Calendar & To-Do List", "duration": 15, "best_time": "08:30-08:45", "priority": 1, "category": "Productivity"},
    {"name": "Deep Work/Focused Tasks", "duration": 60, "best_time": "09:00-10:00", "priority": 1, "category": "Work"},
    {"name": "Check Emails", "duration": 15, "best_time": "10:00-10:15", "priority": 3, "category": "Work"},
    {"name": "Organize Workspace", "duration": 15, "best_time": "10:15-10:30", "priority": 2, "category": "Productivity"},
    {"name": "Brainstorm Ideas", "duration": 30, "best_time": "10:30-11:00", "priority": 3, "category": "Creativity"},
    {"name": "Attend Virtual Meeting", "duration": 45, "best_time": "11:00-11:45", "priority": 2, "category": "Work"},
    {"name": "Quick Break/Stretch", "duration": 10, "best_time": "11:45-11:55", "priority": 2, "category": "Health"},
    {"name": "Continue Deep Work/Project", "duration": 45, "best_time": "11:55-12:40", "priority": 1, "category": "Work"},
    {"name": "Lunch", "duration": 45, "best_time": "12:00-12:45", "priority": 1, "category": "Nutrition"},
    {"name": "Go for a Walk", "duration": 15, "best_time": "12:45-13:00", "priority": 2, "category": "Health"},
    {"name": "Read or Listen to a Podcast", "duration": 30, "best_time": "13:00-13:30", "priority": 3, "category": "Leisure"},
    {"name": "Take a Power Nap", "duration": 20, "best_time": "13:30-13:50", "priority": 3, "category": "Health"},
    {"name": "Do Quick Household Chore", "duration": 15, "best_time": "13:50-14:05", "priority": 2, "category": "Housework"},
    {"name": "Stretching or Yoga", "duration": 20, "best_time": "14:05-14:25", "priority": 2, "category": "Exercise"},
    {"name": "Creative Work (Art, Writing, Music)", "duration": 60, "best_time": "14:30-15:30", "priority": 1, "category": "Creativity"},
    {"name": "Work on a Side Project", "duration": 45, "best_time": "15:30-16:15", "priority": 2, "category": "Productivity"},
    {"name": "Check Financials or Budget", "duration": 20, "best_time": "16:15-16:35", "priority": 3, "category": "Finance"},
    {"name": "Attend In-Person Meeting", "duration": 45, "best_time": "16:30-17:15", "priority": 2, "category": "Work"},
    {"name": "Organize Files/Inbox", "duration": 15, "best_time": "17:15-17:30", "priority": 2, "category": "Productivity"},
    {"name": "Read a Book or Article", "duration": 30, "best_time": "17:30-18:00", "priority": 2, "category": "Leisure"},
    {"name": "Quick Break/Walk Outside", "duration": 15, "best_time": "18:00-18:15", "priority": 2, "category": "Health"},
    {"name": "Finish Up Work Tasks", "duration": 30, "best_time": "18:15-18:45", "priority": 1, "category": "Work"},
    {"name": "Call a Friend or Family Member", "duration": 15, "best_time": "18:45-19:00", "priority": 2, "category": "Social"},
    {"name": "Prepare Dinner", "duration": 30, "best_time": "19:00-19:30", "priority": 1, "category": "Nutrition"},
    {"name": "Exercise or Strength Training", "duration": 45, "best_time": "19:30-20:15", "priority": 2, "category": "Exercise"},
    {"name": "Clean Up Workspace/Area", "duration": 15, "best_time": "20:15-20:30", "priority": 3, "category": "Housework"},
    {"name": "Eat Dinner", "duration": 45, "best_time": "20:30-21:15", "priority": 1, "category": "Nutrition"},
    {"name": "Relax with TV Show or Movie", "duration": 60, "best_time": "21:00-22:00", "priority": 3, "category": "Leisure"},
    {"name": "Spend Time with Family/Friends", "duration": 45, "best_time": "21:00-21:45", "priority": 1, "category": "Social"},
    {"name": "Do a Relaxing Activity (Puzzles, Crafts)", "duration": 30, "best_time": "21:45-22:15", "priority": 3, "category": "Leisure"},
    {"name": "Play a Game (Board, Video, etc.)", "duration": 30, "best_time": "22:15-22:45", "priority": 2, "category": "Leisure"},
    {"name": "Take a Leisurely Walk Outside", "duration": 15, "best_time": "22:45-23:00", "priority": 3, "category": "Health"},
    {"name": "Reflect on the Day", "duration": 15, "best_time": "23:00-23:15", "priority": 2, "category": "Mindfulness"},
    {"name": "Organize Tomorrow’s Tasks", "duration": 15, "best_time": "23:15-23:30", "priority": 1, "category": "Productivity"},
    {"name": "Write in Your Journal", "duration": 15, "best_time": "23:30-23:45", "priority": 3, "category": "Mindfulness"},
    {"name": "Gratitude Practice", "duration": 15, "best_time": "23:45-00:00", "priority": 2, "category": "Mindfulness"},
    {"name": "Prepare for Bed (Skin Care, Hygiene)", "duration": 20, "best_time": "00:00-00:20", "priority": 1, "category": "Health"},
    {"name": "Read Before Bed", "duration": 20, "best_time": "00:20-00:40", "priority": 3, "category": "Leisure"}

    ],
    "Aarya": 
     [
    {"name": "Stretching", "duration": 10, "best_time": "15:10-15:20", "priority": 2, "category": "Health"},
    {"name": "Meditation", "duration": 20, "best_time": "15:30-15:50", "priority": 3, "category": "Mindfulness"},
    {"name": "Morning Walk/Jog", "duration": 30, "best_time": "15:30-16:00", "priority": 1, "category": "Exercise"},
    {"name": "Yoga", "duration": 30, "best_time": "16:00-16:30", "priority": 2, "category": "Exercise"},
    {"name": "Cold Shower", "duration": 10, "best_time": "16:30-16:40", "priority": 3, "category": "Health"},
    {"name": "Healthy Breakfast", "duration": 30, "best_time": "16:40-17:10", "priority": 1, "category": "Nutrition"},
    {"name": "Prepare Lunch for the Day", "duration": 20, "best_time": "17:10-17:30", "priority": 2, "category": "Nutrition"},
    {"name": "Plan Daily Goals", "duration": 15, "best_time": "17:30-17:45", "priority": 1, "category": "Productivity"},
    {"name": "Journal/Gratitude Practice", "duration": 15, "best_time": "17:45-18:00", "priority": 2, "category": "Mindfulness"},
    {"name": "Review Calendar & To-Do List", "duration": 15, "best_time": "18:00-18:15", "priority": 1, "category": "Productivity"},
    {"name": "Deep Work/Focused Tasks", "duration": 60, "best_time": "18:30-19:30", "priority": 1, "category": "Work"},
    {"name": "Check Emails", "duration": 15, "best_time": "19:30-19:45", "priority": 3, "category": "Work"},
    {"name": "Organize Workspace", "duration": 15, "best_time": "19:45-20:00", "priority": 2, "category": "Productivity"},
    {"name": "Brainstorm Ideas", "duration": 30, "best_time": "20:00-20:30", "priority": 3, "category": "Creativity"},
    {"name": "Attend Virtual Meeting", "duration": 45, "best_time": "20:30-21:15", "priority": 2, "category": "Work"},
    {"name": "Quick Break/Stretch", "duration": 10, "best_time": "21:15-21:25", "priority": 2, "category": "Health"},
    {"name": "Continue Deep Work/Project", "duration": 45, "best_time": "21:25-22:10", "priority": 1, "category": "Work"},
    {"name": "Lunch", "duration": 45, "best_time": "22:00-22:45", "priority": 1, "category": "Nutrition"},
    {"name": "Go for a Walk", "duration": 15, "best_time": "22:45-23:00", "priority": 2, "category": "Health"},
    {"name": "Read or Listen to a Podcast", "duration": 30, "best_time": "23:00-23:30", "priority": 3, "category": "Leisure"},
    {"name": "Take a Power Nap", "duration": 20, "best_time": "23:30-23:50", "priority": 3, "category": "Health"},
    {"name": "Do Quick Household Chore", "duration": 15, "best_time": "23:50-00:05", "priority": 2, "category": "Housework"},
    {"name": "Stretching or Yoga", "duration": 20, "best_time": "00:05-00:25", "priority": 2, "category": "Exercise"},
    {"name": "Creative Work (Art, Writing, Music)", "duration": 60, "best_time": "00:30-01:30", "priority": 1, "category": "Creativity"},
    {"name": "Work on a Side Project", "duration": 45, "best_time": "01:30-02:15", "priority": 2, "category": "Productivity"},
    {"name": "Check Financials or Budget", "duration": 20, "best_time": "02:15-02:35", "priority": 3, "category": "Finance"},
    {"name": "Attend In-Person Meeting", "duration": 45, "best_time": "02:30-03:15", "priority": 2, "category": "Work"},
    {"name": "Organize Files/Inbox", "duration": 15, "best_time": "03:15-03:30", "priority": 2, "category": "Productivity"},
    {"name": "Read a Book or Article", "duration": 30, "best_time": "03:30-04:00", "priority": 2, "category": "Leisure"},
    {"name": "Quick Break/Walk Outside", "duration": 15, "best_time": "04:00-04:15", "priority": 2, "category": "Health"},
    {"name": "Finish Up Work Tasks", "duration": 30, "best_time": "04:15-04:45", "priority": 1, "category": "Work"},
    {"name": "Call a Friend or Family Member", "duration": 15, "best_time": "04:45-05:00", "priority": 2, "category": "Social"},
    {"name": "Prepare Dinner", "duration": 30, "best_time": "05:00-05:30", "priority": 1, "category": "Nutrition"},
    {"name": "Exercise or Strength Training", "duration": 45, "best_time": "05:30-06:15", "priority": 2, "category": "Exercise"},
    {"name": "Clean Up Workspace/Area", "duration": 15, "best_time": "06:15-06:30", "priority": 3, "category": "Housework"},
    {"name": "Eat Dinner", "duration": 45, "best_time": "06:30-07:15", "priority": 1, "category": "Nutrition"},
    {"name": "Relax with TV Show or Movie", "duration": 60, "best_time": "07:00-08:00", "priority": 3, "category": "Leisure"},
    {"name": "Spend Time with Family/Friends", "duration": 45, "best_time": "07:00-07:45", "priority": 1, "category": "Social"},
    {"name": "Do a Relaxing Activity (Puzzles, Crafts)", "duration": 30, "best_time": "07:45-08:15", "priority": 3, "category": "Leisure"},
    {"name": "Play a Game (Board, Video, etc.)", "duration": 30, "best_time": "08:15-08:45", "priority": 2, "category": "Leisure"},
    {"name": "Take a Leisurely Walk Outside", "duration": 15, "best_time": "08:45-09:00", "priority": 3, "category": "Health"},
    {"name": "Reflect on the Day", "duration": 15, "best_time": "09:00-09:15", "priority": 2, "category": "Mindfulness"},
    {"name": "Organize Tomorrow’s Tasks", "duration": 15, "best_time": "09:15-09:30", "priority": 1, "category": "Productivity"},
    {"name": "Write in Your Journal", "duration": 15, "best_time": "09:30-09:45", "priority": 3, "category": "Mindfulness"},
    {"name": "Gratitude Practice", "duration": 15, "best_time": "09:45-10:00", "priority": 2, "category": "Mindfulness"}
]

}

def main():
    welcome()  
    username, startTime, endTime, category = userin()
    aactivities = getactivities(username, startTime, endTime, category)
    activityreco(aactivities, category)


def welcome():
    aquote = random.choice(quotes)
    print(f"\nWelcome!:\n\"{aquote}\"\n")

def userin():
    username = input("What is your name, if you don't mind me asking?: ")
    whattimeisnow = input("Could you please let me know what time it is? (HH:MM): ")
    whensleep = input("May I ask what time you plan to go to sleep? (HH:MM): ")
    startTime = datetime.strptime(whattimeisnow, "%H:%M")
    endTime = datetime.strptime(whensleep, "%H:%M")
    
    print("\nCategories:")
    print("\n 1. Exercise\n 2. Mindfulness\n 3. Creativity\n 4. Work\n 5. Health\n 6. Nutrition\n 7. Productivity\n 8. Housework\n 9. Leisure\n 10. Social\n 11. Finance\n", end="")    
    
    yourchoice = input("Pick a category number if you want to see specific activities! If you leave it blank, you’ll get everything.: ")

    if yourchoice == "":
        category = None
    else:
        categorytochoose = {"1": "Exercise", "2": "Mindfulness", "3": "Creativity", "4": "Work", "5": "Health", "6": "Nutrition", "7": "Productivity", "8": "Housework", "9": "Leisure", "10": "Social", "11": "Finance"}
        category = categorytochoose.get(yourchoice, None)
    return username, startTime, endTime, category

def getactivities(username, startTime, endTime, category=None):
    if username not in db:
        print(f"Oops! We couldn’t find that user: {username}")
        return []

    activities_db = db[username]
    aactivities = []

    for activity in activities_db:
        if category and activity["category"] != category:
            continue
        
        best_time_range = activity["best_time"].split("-")
        best_start_time = datetime.strptime(best_time_range[0], "%H:%M")
        best_end_time = datetime.strptime(best_time_range[1], "%H:%M")
        
        if best_start_time < endTime and best_end_time > startTime: 
            aactivities.append(activity)

    aactivities.sort(key=lambda x: x["priority"])
    return aactivities

def activityreco(aactivities, category=None):
    if aactivities:
        if category:
            print(f"\nActivities you can do today in the {category} category:")
        else:
            print("\nHere are all the activities you can do today:")
        for activity in aactivities:
            print(f"- {activity['name']} (Category: {activity['category']}, Recommended Time: {activity['best_time']}, Time: {activity['duration']} minute, Priority Order: {activity['priority']})")
    else:
        if category:
            print(f"There are no activities available in the {category} category.")
        else:
            print("There are no activities available in this time slot.")


if __name__ == "__main__":
    main()



