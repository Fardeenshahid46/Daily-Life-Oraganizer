import datetime
import random
import tkinter as tk
from tkinter import messagebox,simpledialog

#Class to manage tasks
class TaskManager:
    def __init__(self):
        self.tasks=[] #List to store tasks and their priorities
    
    def add_task(self,task,priority):
        self.tasks.append((task,priority)) #Adding task and priority as tuple
    
    def delete_task(self,task):
        self.tasks=[a for a in self.tasks if a[0]!=task] #Deleting task if it exists
    
    def list_tasks(self):
        return self.tasks            

#Class to track mood 
class MoodTracker:
        def __init__(self):
            self.mood_log=[] #List to store mood logs
         
        def log_mood(self,mood):
            timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.mood_log.append("mood:",mood,"time:",timestamp) #Adding mood and time as tuple
        
        def show_mood_chart(self):
            return self.mood_log        

#Class to manage motivational quotes
class QuoteManager:
    def __init__(self): #List to store quotes
        self.quotes=list(set([
           "You are capable of amazing things.",
            "Stay positive, work hard, make it happen.",
            "Believe you can and you're halfway there.",
            "Don't watch the clock; do what it does. Keep going.",
            "Start where you are. Use what you have. Do what you can."   
        ]))
    def show_quote(self):
        return random.choice(self.quotes)      
    
#Class to organize notes    
class NoteOrganizer:
    
    def __init__(self):
        self.notes={} #Dictionary to store notes with title as key and content as value
        
    def add_note(self,title,content):
        self.notes[title]=content    #Adding note with title and content as key-value pair
    
    def search_notes(self,keyword):
        return{title: content for title,content in self.notes.items() if keyword in title or keyword in content} #Searching notes with keyword in title or content
 
#Main class to create the GUI and integrate all components    
class DailyLifeOrganizerApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Daily Life Organizer")  #Setting title of the window             
       
       #Creating instances of all classes 
        self.task_manager=TaskManager()
        self.mood_tracker=MoodTracker()
        self.quote_manager=QuoteManager()
        self.note_organizer=NoteOrganizer()
        
        self.create_widgets()
   
   #Creating the GUI widgets 
    def create_widgets(self):
        tk.Button(self.root,text="Add Task",command=self.add_task).pack(pady=5)
        tk.Button(self.root,text="Show Tasks",command=self.show_task).pack(pady=5)
        tk.Button(self.root,text="Delete Tasks",command=self.delete_task).pack(pady=5)
        tk.Button(self.root,text="Log Mood",command=self.log_mood).pack(pady=5)
        tk.Button(self.root, text="Show Mood Log", command=self.show_mood_log).pack(pady=5)
        tk.Button(self.root, text="Show Motivation", command=self.show_motivation).pack(pady=5)
        tk.Button(self.root, text="Add Note", command=self.add_note).pack(pady=5)
        tk.Button(self.root, text="Search Notes", command=self.search_notes).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=5)
   
   #Adding functionality to buttons        
    def add_task(self):
        task=simpledialog.askstring("Task","Enter task:")
        priority=simpledialog.askstring("Priority","Enter priority:(Low/Medium/High):")
        if task and priority:
            self.task_manager.add_task(task,priority)
            messagebox.showinfo("Success","Task added successfully!")
     
    #Function to show all tasks        
    def show_task(self):
        tasks=self.task_manager.list_tasks()
        if not tasks:
            messagebox.showinfo("Tasks","No tasks available.")  
        else:
             task_str="\n".join([f"{i+1}. {t[0]} [Priority: {t[1]}]" for i, t in enumerate(tasks)])
             messagebox.showinfo("Tasks",task_str) 
    
    #Function to delete task
    def delete_task(self):
         task=simpledialog.askstring("Delete Task","Enter task to delete:")
         if task:
             self.task_manager.delete_task(task)
             messagebox.showinfo("Success","Task deleted (if it existed)")          
     
    
    #Function to log mood
    def log_mood(self):
        mood=simpledialog.askstring("Mood","How are you feeling today?")
        if mood:
            self.mood_tracker.log_mood(mood)
            messagebox.showinfo("Logged","Mood logged successfully!") 
    
    #Function to show mood log
    def show_mood_log(self):
        logs=self.mood_tracker.show_mood_chart()
        if not logs:
            messagebox.showinfo("Mood Log","No mood entries yet.")
        else:
            log_str = "\n".join([f"[{entry['time']}] Mood: {entry['mood']}" for entry in logs])
            messagebox.showinfo("Mood Log", log_str)
    
    #Function to show motivational quotes
    def show_motivation(self):
        quote=self.quote_manager.show_quote()
        messagebox.showinfo("Motivation",quote) 
    
    #Function to add notes 
    def add_note(self):                 
        title=simpledialog.askstring("Note Title","Enter note title:")
        content=simpledialog.askstring("Note Content","Enter note content:")
        if title and content:
            self.note_organizer.add_note(title,content)
            messagebox.showinfo("Success","Note added successfully!")  
   
   #Function to search notes 
    def search_notes(self):
        keyword=simpledialog.askstring("Search Notes","Enter keyword to search:") 
        if keyword:
            results=self.note_organizer.search_notes(keyword)
            if results:
                result_str="\n".join([f"{title}: {content}" for title, content in results.items()])
                messagebox.showinfo("Search Results",result_str) 
            else:
                messagebox.showinfo("Search Results","No notes found with that keyword.")          

#Main function to run the application   
if __name__=="__main__": #Creating the main window
    root=tk.Tk() #Creating an instance of Tk
    app=DailyLifeOrganizerApp(root) #Creating an instance of DailyLifeOrganizerApp
    root.geometry("300x400") #Setting the size of the window
    root.mainloop() #Running the main loop                