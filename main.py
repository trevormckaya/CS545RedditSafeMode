import tkinter as tk
import webbrowser
'''
Future prototypes (3 to N)
- expand subreddit list
- make more visually appealing: think pictures 
- have user go through our deliverable
    - 1 pass to get a feel for the opp
    - 2nd pass with a checklist we create to review the application
        - create the checklist for the user (basically a list to ensure all functions of the GUI work as expected)
- Continue to focus on our E
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

        self.sOne = tk.Button(root, text="r/toys", command=self.testsOne)
        self.sOne.grid(row=3,column=0,pady=20,padx=20)

        self.sTwo = tk.Button(root, text="r/cute", command=self.testsTwo)
        self.sTwo.grid(row=3,column=1,pady=20,padx=20)

        self.sThree = tk.Button(root, text="r/Awwducational", command=self.testsThree)
        self.sThree.grid(row=3,column=2,pady=20,padx=20)

        #list of all subreddits on our platform
        list_label = tk.Label(root, text="List of all subreddits:")
        list_label.grid(row=4,column=0,padx=20,pady=20)
        self.subreddits = ["r/toys", "r/cute", "r/Awwducational", "r/wholesome"]
        self.selected_subreddit = tk.StringVar()
        self.selected_subreddit.set(self.subreddits[0])
        self.listAll = tk.OptionMenu(root, self.selected_subreddit, *self.subreddits)
        self.listAll.grid(row=4,column=1,padx=20,pady=20)
        def goToSub():
            webbrowser.open_new('https://www.reddit.com/' + self.selected_subreddit.get())
        optionGo = tk.Button(root, text="Go", command=goToSub)
        optionGo.grid(row=4,column=2,padx=20,pady=20)

        #suggestion a new subreddit action
        request_label = tk.Label(root, text="Dont see your favorite SubReddit?")
        request_label.grid(row=5,column=0,padx=20,pady=20)

        self.request = tk.Button(root, text="Request Here", command=self.request_page)
        self.request.grid(row=5,column=1,padx=20,pady=20)

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
            print("request submitted: " + text)
            request_window.destroy()
            thankyou_window = tk.Toplevel(self.root)
            thankyou_window.title("Thank You")
            thankyou_label = tk.Label(thankyou_window, text="Your request has been submitted. Thank you!")
            thankyou_label.pack(pady=10)
            def thankyou_close():
                thankyou_window.destroy()
            close_button = tk.Button(thankyou_window, text="Close", command=thankyou_close)
            close_button.pack(pady=10)
        
        request_button = tk.Button(request_window, text="Submit", command=submit_request)
        request_button.pack(pady=10)


    #handles the button interactions 
    def testsOne(self):
        print("sOne clicked")
        webbrowser.open_new('https://www.reddit.com/r/toys/')

    def testsTwo(self):
        print("sTwo clicked")
        webbrowser.open_new('https://www.reddit.com/r/cute/')
    
    def testsThree(self):
        print("sThree clicked")
        webbrowser.open_new('https://www.reddit.com/r/Awwducational/')

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()

    # Create an instance of the application
    app = MyApp(root)

    # Start the Tkinter event loop
    root.mainloop()
