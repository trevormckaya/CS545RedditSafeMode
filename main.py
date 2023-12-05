import tkinter as tk
import webbrowser
'''
Prototype 2 TODO:
- update suggestions to actual reddit pages
- update suggestion names to subreddit names
- fully implement request window
    - store requests
    - print thank you message
    - auto close request window upon submition
- remove unneeded code
    - page displays (changed approach to the design)
- implement ability to click on drop down menu options and access sub reddits
Future prototypes (3 to N)
- expand subreddit list
- make more visually appealing: think pictures 
'''
class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reddit Safe Mode")

        #selfpage Title
        #notes: future prototypes update font and font size
        self_title = tk.Label(root, text="Reddit Safe Mode")
        self_title.grid(row=1,column=1,pady=20,padx=20)

        # Suggested/popular safe subreddits for users to quickly access
        suggest_label = tk.Label(root, text="Popular Subreddits:")
        suggest_label.grid(row=2,column=1,padx=20,pady=20)

        self.sOne = tk.Button(root, text="Suggestion 1", command=self.testsOne)
        self.sOne.grid(row=3,column=0,pady=20,padx=20)

        self.sTwo = tk.Button(root, text="Suggestion 2", command=self.testsTwo)
        self.sTwo.grid(row=3,column=1,pady=20,padx=20)

        self.sThree = tk.Button(root, text="Suggestion 3", command=self.testsThree)
        self.sThree.grid(row=3,column=2,pady=20,padx=20)

        #list of all subreddits on our platform
        list_label = tk.Label(root, text="List of all subreddits:")
        list_label.grid(row=4,column=0,padx=20,pady=20)
        self.subreddits = ["Subreddit 1", "Subreddit 2", "Subreddit 3", "Subreddit 4", "Subreddit 5"]
        self.selected_subreddit = tk.StringVar()
        self.selected_subreddit.set(self.subreddits[0])
        self.listAll = tk.OptionMenu(root, self.selected_subreddit, *self.subreddits)
        self.listAll.grid(row=4,column=2,padx=20,pady=20)

        #suggestion a new subreddit action
        request_label = tk.Label(root, text="Dont see your favorite SubReddit?")
        request_label.grid(row=5,column=0,padx=20,pady=20)

        self.request = tk.Button(root, text="Request Here", command=self.request_page)
        self.request.grid(row=5,column=1,padx=20,pady=20)

        #page frame setups
        self.request_frame = tk.Frame(root) #to remove
        self.listAll_frame = tk.Frame(root)

        #ensure home page is first page:
        self.show_home() #to remove - shouldnt need after I'm done with windows

    #Homepage
    def show_home(self):#to remove
        #forget all page grids
        self.request_frame.grid_forget()
        self.listAll_frame.grid_forget()
    #request a subreddit page
    def request_page(self):
        print("request page clicked")
        request_window = tk.Toplevel(self.root)
        request_window.title("Request Page")

        request_label = tk.Label(request_window, text="Enter the subreddit name below")
        request_label.pack(pady=10)

        request_text = tk.Entry(request_window)
        request_text.pack(pady=10)

        def submit_request():
            text = request_text.get()
            print(text)
            request_result.config(text)
        
        request_button = tk.Button(request_window, text="submit", command=submit_request)
        request_button.pack(pady=10)

        request_result = tk.Label(request_window, text="")
        request_result.pack(pady=10)
    

    def listAll_page(self):
        print("listAll page clicked")

    #handles the button interactions 
    def testsOne(self):
        print("sOne clicked")
        webbrowser.open_new('https://www.google.com/')

    def testsTwo(self):
        print("sTwo clicked")
        webbrowser.open_new('https://www.google.com/')
    
    def testsThree(self):
        print("sThree clicked")
        webbrowser.open_new('https://www.google.com/')




if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()

    # Create an instance of the application
    app = MyApp(root)

    # Start the Tkinter event loop
    root.mainloop()
