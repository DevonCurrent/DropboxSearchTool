from Message import Message

class Search:
    response = ""
    keywords = []
    companies = []
    years = []
    fileContentSearch = False

    def __init__(self, m):
        self.message = m

    def addKeyword(self, value):
        splitSearchTerms = value.split(" ")
        splitSearchTerms = [term.lower() for term in splitSearchTerms]
        for i in range(1, len(splitSearchTerms)):
            self.keywords.append(splitSearchTerms[i])
        if '' in self.keywords:  # removes blank space at the end of a search
            self.keywords.remove('')

    def addCompanies(self, value):
        splitSearchTerms = value.split(" ")
        splitSearchTerms = [term.lower() for term in splitSearchTerms]
        for i in range(1, len(splitSearchTerms)):
            self.companies.append(splitSearchTerms[i])
        if '' in self.companies:  # removes blank space at the end of a search
            self.companies.remove('')

    def addYears(self, value):
        splitSearchTerms = value.split(" ")
        splitSearchTerms = [term.lower() for term in splitSearchTerms]
        for i in range(1, len(splitSearchTerms)):
            self.years.append(splitSearchTerms[i])
        if '' in self.years:  # removes blank space at the end of a search
            self.years.remove('')

    def createCorrectSearchResponse(self):
        self.response = "Ok! I will search for " + str(self.keywords).strip('[]') + " \nfrom " + str(self.companies).strip('[]') + " \nfrom the year(s) " + str(self.years).strip('[]')