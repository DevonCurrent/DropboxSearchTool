from Message import Message

class Search:

    def __init__(self, m):
        self.response = ""
        self.keywords = []
        self.companies = []
        self.years = []
        self.fileContentSearch = False
        self.message = None
        self.message = m     

    def addKeyword(self, value):
        self.SplitSearchTerms(value, 'k')

    def addCompanies(self, value):
        self.SplitSearchTerms(value, 'c')

    def addYears(self, value):
        self.SplitSearchTerms(value, 'y')

    def createCorrectSearchResponse(self):
        self.response = "Ok! I will search for " + str(self.keywords).strip('[]') + " \nfrom " + str(self.companies).strip('[]') + " \nfrom the year(s) " + str(self.years).strip('[]')

    def SplitSearchTerms(self, value, letter):
        splitSearchTerms = value.split(" ")
        splitSearchTerms = [term.lower() for term in splitSearchTerms]
        for i in range(1, len(splitSearchTerms)):
            if letter is 'k':
                self.keywords.append(splitSearchTerms[i])
            elif letter is 'c':
                self.companies.append(splitSearchTerms[i])
            elif letter is 'y':
                self.years.append(splitSearchTerms[i])

        if letter is 'k':
                if '' in self.keywords:  # removes blank space at the end of a search
                    self.keywords.remove('')
        elif letter is 'c':
                if '' in self.companies:  # removes blank space at the end of a search
                    self.companies.remove('')
        elif letter is 'y':
                if '' in self.years:  # removes blank space at the end of a search
                    self.years.remove('')

