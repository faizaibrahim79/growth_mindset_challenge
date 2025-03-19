import streamlit as st
import time
from datetime import datetime

# Set up the app's title
st.title("Task Reminder App 🔔")

# Initialize session state for tasks if it doesn't exist
if 'tasks_list' not in st.session_state:
    st.session_state.tasks_list = []

# Set up a text input for the task description
task = st.text_input("Enter your task:")

# Manually set the default time to 4 AM (24-hour format: 04:00:00)
default_time = datetime.strptime("04:00:00", "%H:%M:%S").time()

# Set up the time input for setting a reminder time, using the fixed 4 AM as the default value
reminder_time = st.time_input("Set reminder time:", value=default_time)

# Store the task and reminder in the tasks_list when the button is pressed
if st.button("Set Reminder"):
    if task:
        # Append new task to the session state tasks list
        st.session_state.tasks_list.append({"task": task, "time": reminder_time})
        st.write(f"Task '{task}' set for {reminder_time.strftime('%H:%M:%S')}")
    else:
        st.write("Please enter a task description.")

# Display all tasks and their reminder times
if st.session_state.tasks_list:
    st.write("Your set reminders:")
    for task_entry in st.session_state.tasks_list:
        st.write(f"- Task: {task_entry['task']} at {task_entry['time'].strftime('%H:%M:%S')}")

# Display countdown and reminder for each task
if st.session_state.tasks_list:
    while True:
        current_time = datetime.now().time()  # Get the current time
        for task_entry in st.session_state.tasks_list:
            # Compare the current time with the reminder time
            if current_time.hour == task_entry['time'].hour and current_time.minute == task_entry['time'].minute:
                st.write(f"Reminder: It's time to: {task_entry['task']}")
                # Optionally, remove the task from the list after it gets triggered
                st.session_state.tasks_list.remove(task_entry)
                break  # Exit the loop to avoid skipping tasks
                
        time.sleep(60)  # Check every minute
