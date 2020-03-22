import tkinter
from tkinter import StringVar, END
from search import search as web_search
import timeit

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry('1000x600')
        self.master.resizable(0, 0)
        self.master.wm_title("Search Engine")
        self.master.grid_columnconfigure(0, weight=1) ####
        self.master.grid_rowconfigure(1, weight=1) ####

        # create the containers
        self.searchContainer = tkinter.Frame(self.master)
        self.resultsContainer = tkinter.Frame(self.master)

        # position the containers
        self.searchContainer.grid(row=0, column=0, sticky='w', padx=10, pady=10)
        self.resultsContainer.grid(row=1, column=0, sticky='news')
        self.resultsContainer.grid_columnconfigure(0, weight=1) ####

        # create input and button fields
        self.searchText = StringVar()
        self.searchInput = tkinter.Entry(self.searchContainer, textvariable=self.searchText, width=90)
        self.searchButton = tkinter.Button(self.searchContainer, text='Search', width=20, command=self.search)

        # position the input and button
        self.searchInput.grid(row=0, column=0)
        self.searchButton.grid(row=0, column=1, padx=10)

        # results
        self.results = tkinter.Listbox(self.resultsContainer, height=2)
        self.resultsList = tkinter.Listbox(self.resultsContainer, height=24, width=150)

        # scrollbar
        self.scrollBar = tkinter.Scrollbar(self.resultsContainer)

        self.results.grid(row=0, column=0, sticky='ew', rowspan=1, padx=(9, 9))
        self.resultsList.grid(row=1, column=0, sticky='w', padx=(9, 9), pady=10, ipadx=40, ipady=30)

        self.scrollBar.grid(row=1, column=1, sticky='nse')

        self.resultsList.configure(yscrollcommand=self.scrollBar.set)
        self.scrollBar.configure(command=self.resultsList.yview)

    def search(self):
        result = 69
        sec = 69


        self.results.delete(0, END)
        self.resultsList.delete(0, END)

        start = timeit.timeit()
        try:
            search_results = web_search(self.searchText.get())
        except:
            search_results = []
        end = timeit.timeit()


        # a = [_ for _ in range(0, 50)]
        # a.append("hello")

        self.results.insert(END, "Found %d results in %f seconds" % (len(search_results), abs(end-start)))

        for b in search_results:
            self.resultsList.insert(END, b)

master = tkinter.Tk()

GUI(master)
master.mainloop()
