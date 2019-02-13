from StemmedCountVectorizer import StemmedCountVectorizer
import scipy as sp
import sys
import pdb

class BagOfWords:

    def __init__(self, fileList, keywords):
        self.RETURN_SIZE = 5
        self.fileList = fileList
        self.keywords = keywords

    def find_accurate_docs(self):

        fileNameList = []
        for entry in self.fileList:
            fileNameList.append(entry.name)

        #StemmedCountVectorizer creates a 2d array of word counts for each file            
        vectorizer = StemmedCountVectorizer(min_df=1, stop_words='english') #can add "stop_words='english'" to remove common english words
        trainVectors = vectorizer.fit_transform(fileNameList)
        numSamples, numFeatures = trainVectors.shape

        # the keywords the session leader wants to find in Dropbox
        keywords_vec = vectorizer.transform([self.keywords])

        distList = []
        for i in range(0, numSamples):
            if fileNameList[i] == self.keywords:
                continue
            fileNameList_vec = trainVectors.getrow(i)
            d = self.dist_norm(fileNameList_vec, keywords_vec)   
            print("=== fileNameList %i with dist=%.2f: %s"%(i, d, fileNameList[i]))
            distList.append(d)

        bestDocs = []
        #selects only the files that have smallest distance
        print("TOP " + str(self.RETURN_SIZE) + " MOST ACCURATE fileNameListS ARE:")
        for i in range(0, self.RETURN_SIZE):
            doc = distList.index(min(distList))
            print("=== fileNameList %i with dist=%.2f: %s"%(i, distList[doc], fileNameList[doc]))
            bestDocs.append(self.fileList[doc])
            distList[doc] = sys.maxsize
        
        return bestDocs
    
    # finds Euclidean distance of fileNameList to the keywords
    def dist_norm(self, v1, v2):
        v1Normalized = v1/sp.linalg.norm(v1.toarray())
        v2Normalized = v2/sp.linalg.norm(v2.toarray())
        delta = v1Normalized - v2Normalized
        return sp.linalg.norm(delta.toarray())