import tkinter as tk
from tkinter import Entry, Label, Button

# Import the rest of your code here

class WebCrawlerGUI:
    def _init_(self, root):
        self.root = root
        self.root.title("Web Crawler")
        
        self.base_url_label = Label(root, text="Enter Website to Crawl:")
        self.base_url_label.pack()
        
        self.base_url_entry = Entry(root)
        self.base_url_entry.pack()
        
        self.num_threads_label = Label(root, text="Enter number of Threads:")
        self.num_threads_label.pack()
        
        self.num_threads_entry = Entry(root)
        self.num_threads_entry.pack()
        
        self.start_button = Button(root, text="Start Crawling", command=self.start_crawling)
        self.start_button.pack()
        
        self.output_label = Label(root, text="")
        self.output_label.pack()

    def start_crawling(self):
        base_url = self.base_url_entry.get()
        num_threads = self.num_threads_entry.get()
        
        # Call your web crawling code with base_url and num_threads
        # ...

        # Replace the following lines with the actual values from your web crawling code
        have_visited = []  # Add the actual list of visited pages
        error_links = []   # Add the actual list of erroneous links

        result = f"Total Number of pages visited are {len(have_visited)}\nTotal Number of Erroneous links: {len(error_links)}"
        self.output_label.config(text=result)

if __name__ == "_main_":
    root = tk.Tk()
    app = WebCrawlerGUI(root)
    root.mainloop()