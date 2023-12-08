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

#Global font that can be changed from the Accessibility Menu, make sure to use a font that is dyslexia friendly if you change it! (Helvetica, Courier, Arial, Verdana, etc, to find more look on Google)
cFont = ("Arial", 12)

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reddit Safe Mode")

        #selfpage Title
        self.self_title = tk.Label(root, font = cFont, text="Reddit Safe Mode")
        self.self_title.grid(row=1,column=1,pady=20,padx=20)

        # Suggested/popular safe subreddits for users to quickly access
        self.suggest_label = tk.Label(root, font = cFont, text="Popular Subreddits:")
        self.suggest_label.grid(row=2,column=1,padx=20,pady=20)

        self.sOne = tk.Button(root, font = cFont, text="r/toys", command=self.testsOne)
        self.sOne.grid(row=3,column=0,pady=20,padx=20)

        self.sTwo = tk.Button(root, font = cFont, text="r/cute", command=self.testsTwo)
        self.sTwo.grid(row=3,column=1,pady=20,padx=20)

        self.sThree = tk.Button(root, font = cFont, text="r/Awwducational", command=self.testsThree)
        self.sThree.grid(row=3,column=2,pady=20,padx=20)

        #list of all subreddits on our platform
        self.list_label = tk.Label(root, font = cFont, text="List of all subreddits:")
        self.list_label.grid(row=4,column=0,padx=20,pady=20)
        self.subreddits = ["r/toys", "r/cute", "r/Awwducational", "r/wholesome", "r/aww", "r/cats", "r/PuppySmiles", "r/CatsWithDogs", "r/lego", "r/Outdoors"]
        self.selected_subreddit = tk.StringVar()
        self.selected_subreddit.set(self.subreddits[0])
        self.listAll = tk.OptionMenu(root, self.selected_subreddit, *self.subreddits)
        self.listAll.config(font=cFont)
        self.listAll['menu'].configure(font=cFont)
        self.listAll.grid(row=4,column=1,padx=20,pady=20)
        def goToSub():
            webbrowser.open_new('https://www.reddit.com/' + self.selected_subreddit.get())
        self.optionGo = tk.Button(root, font = cFont, text="Go", command=goToSub)
        self.optionGo.grid(row=4,column=2,padx=20,pady=20)

        #suggestion a new subreddit action
        self.request_label = tk.Label(root, font = cFont, text="Dont see your favorite SubReddit?")
        self.request_label.grid(row=5,column=0,padx=20,pady=20)

        self.request = tk.Button(root, font = cFont, text="Request Here", command=self.request_page)
        self.request.grid(row=5,column=1,padx=20,pady=20)

        #Accessibility Menu
        self.access_menu = tk.Menu(root, tearoff=0)

        #sub menu for text size
        text_size_menu = tk.Menu(self.access_menu, tearoff=0)
        self.access_menu.add_cascade(label="Text Size", font = ("Arial", 20), menu=text_size_menu)
        text_size_menu.add_radiobutton(label="Normal", font=("Arial", 12), command=lambda: self.set_text_size("normal"))
        text_size_menu.add_radiobutton(label="Large", font=("Arial", 24), command=lambda: self.set_text_size("large"))


        #accessibility menu button
        access_button = tk.Button(root, text="Accessibility",font=("Arial, 20"), command=self.show_accessibility_menu)
        access_button.grid(row=1, column=0, padx=10, pady=10)

    def show_accessibility_menu(self):
        x, y, _, _ = self.root.bbox("current")
        self.root.geometry("+%d+%d" % (x, y))
        self.access_menu.post(x, y)

    def set_text_size(self, size):
        global cFont
        #This should be the same value as the global font at the top of the file
        cFont = ("Arial", 12)
        if size == "large":
            #This is the font and size of the text when changed to Large in accessibility. The font should match what the default font is but size should be bigger (I recommend leaving size alone, in any case, the text size is good as it is, unless it conflicts with design choices)
            cFont = ("Arial", 24) 
        self.self_title.config(font=cFont)
        self.suggest_label.config(font=cFont)
        self.list_label.config(font=cFont)
        self.request_label.config(font=cFont)
        self.sOne.config(font=cFont)
        self.sTwo.config(font=cFont)
        self.sThree.config(font=cFont)
        self.optionGo.config(font=cFont)
        self.request.config(font=cFont)
        self.listAll.config(font=cFont)
        self.listAll['menu'].configure(font=cFont)



    #request a subreddit page
    def request_page(self):
        request_window = tk.Toplevel(self.root)
        request_window.title("Request Page")

        request_label = tk.Label(request_window, font = cFont, text="Here you can request a subreddit! Be sure to follow some basic rules:")
        request_label.pack(pady=10)

        request_label = tk.Label(request_window, font = cFont, text="1. Your requested subreddit must be Safe For Work")
        request_label.pack(pady=10)

        request_label = tk.Label(request_window, font = cFont, text="2. Your requested subreddit's content must be appropriate for younger audiences")
        request_label.pack(pady=10)

        request_label = tk.Label(request_window, font = cFont, text="3. The subreddit's rules must also be appropriate to be considered a safe space")
        request_label.pack(pady=10)

        request_label = tk.Label(request_window, font = cFont, text="After manual review we will decide whether or not this is an appropriate subreddit to add to Reddit Safe Mode")
        request_label.pack(pady=10)

        request_label = tk.Label(request_window, font = cFont, text="Enter the subreddit name below:")
        request_label.pack(pady=10)

        request_text = tk.Entry(request_window, font = cFont)
        request_text.pack(pady=10)
    
        def submit_request():
            text = request_text.get()
            print("request submitted: " + text)
            request_window.destroy()
            thankyou_window = tk.Toplevel(self.root)
            thankyou_window.title("Thank You")
            thankyou_label = tk.Label(thankyou_window, font = cFont, text="Your request has been submitted. Thank you!")
            thankyou_label.pack(pady=10)
            def thankyou_close():
                thankyou_window.destroy()
            close_button = tk.Button(thankyou_window, font = cFont, text="Close", command=thankyou_close)
            close_button.pack(pady=10)
        
        self.request_button = tk.Button(request_window, font = cFont, text="Submit", command=submit_request)
        self.request_button.pack(pady=10)


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
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
