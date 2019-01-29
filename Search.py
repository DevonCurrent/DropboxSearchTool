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

    def add_keywords(self, value):
        self.split_search_terms(value, 'k')

    def add_companies(self, value):
        self.split_search_terms(value, 'c')

    def add_years(self, value):
        self.split_search_terms(value, 'y')

    def create_correct_search_response(self):
        self.response = "Ok! I will search for " + str(self.keywords).strip('[]') + " from " + str(self.companies).strip('[]') + " from the year(s) " + str(self.years).strip('[]')

    def split_search_terms(self, value, letter):
        separated_keywords = value.split(" ")
        separated_keywords = [term.lower() for term in separated_keywords]
        for i in range(1, len(separated_keywords)):
            if letter is 'k':
                self.keywords.append(separated_keywords[i])
            elif letter is 'c':
                self.companies.append(separated_keywords[i])
            elif letter is 'y':
                self.years.append(separated_keywords[i])

        if letter is 'k':
                if '' in self.keywords:  # removes blank space at the end of a search
                    self.keywords.remove('')
        elif letter is 'c':
                if '' in self.companies:  # removes blank space at the end of a search
                    self.companies.remove('')
        elif letter is 'y':
                if '' in self.years:  # removes blank space at the end of a search
                    self.years.remove('')

