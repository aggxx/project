import unittest
from datetime import datetime
from project import welcome, userin, getactivities, activityreco

#To understand how to use the assert module and unittest library, help was taken from chatgpt.
#ChatGPT. 2025. Source: https://chatgpt.com/

db = {
    "Adora": [
        {"name": "Stretching", "duration": 10, "best_time": "05:40-05:50", "priority": 2, "category": "Health"},
        {"name": "Meditation", "duration": 20, "best_time": "06:00-06:20", "priority": 3, "category": "Mindfulness"},
    ],
    "Aarya": [
        {"name": "Yoga", "duration": 30, "best_time": "15:00-15:30", "priority": 1, "category": "Exercise"},
        {"name": "Cold Shower", "duration": 10, "best_time": "16:30-16:40", "priority": 3, "category": "Health"},
    ]
}

class testthecode(unittest.TestCase):

    def test_welcome(self):
        with self.assertLogs(level='INFO') as log:
            welcome()
            self.assertTrue(any("Welcome!" in message for message in log.output))

    def test_userin(self):
        from unittest.mock import patch

        with patch('builtins.input', side_effect=["Adora", "05:00", "06:00", "1"]):
            username, startTime, endTime, category = userin()
            self.assertEqual(username, "Adora")
            self.assertEqual(startTime, datetime.strptime("05:00", "%H:%M"))
            self.assertEqual(endTime, datetime.strptime("06:00", "%H:%M"))
            self.assertEqual(category, "Exercise")

        with patch('builtins.input', side_effect=["Aarya", "15:00", "16:00", ""]):
            username, startTime, endTime, category = userin()
            self.assertEqual(username, "Aarya")
            self.assertEqual(startTime, datetime.strptime("15:00", "%H:%M"))
            self.assertEqual(endTime, datetime.strptime("16:00", "%H:%M"))
            self.assertIsNone(category)

    def test_getactivities(self):
        username = "Adora"
        start_time = datetime.strptime("05:00", "%H:%M")
        end_time = datetime.strptime("06:00", "%H:%M")
        category = "Health"
        activities = getactivities(username, start_time, end_time, category)
        self.assertEqual(len(activities), 1)  
        self.assertEqual(activities[0]["name"], "Stretching")
        self.assertEqual(activities[0]["category"], "Health")
        activities_empty = getactivities(username, start_time, end_time, "Leisure")
        self.assertEqual(len(activities_empty), 0)

    def test_activityreco(self):
        activities = [
            {"name": "Yoga", "duration": 30, "best_time": "15:00-15:30", "priority": 1, "category": "Exercise"},
            {"name": "Stretching", "duration": 10, "best_time": "05:40-05:50", "priority": 2, "category": "Health"}
        ]

        with self.assertLogs(level='INFO') as log:
            activityreco(activities)
            self.assertIn("Yoga", log.output[0])  
            self.assertIn("Stretching", log.output[1])  

        with self.assertLogs(level='INFO') as log:
            activityreco([], category="Health")
            self.assertIn("There are no activities available", log.output[0])

if __name__ == '__main__':
    unittest.main()
