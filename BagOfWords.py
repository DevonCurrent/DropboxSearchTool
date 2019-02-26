from StemmedCountVectorizer import StemmedCountVectorizer
import scipy as sp
import sys

class BagOfWords:

    # finds Euclidean distance of fileWordList to the keywords
    def dist_norm(v1, v2):
        v1Normalized = v1/sp.linalg.norm(v1.toarray())
        v2Normalized = v2/sp.linalg.norm(v2.toarray())
        delta = v1Normalized - v2Normalized
        return sp.linalg.norm(delta.toarray())

    def find_accurate_docs(fileList, fileWordList, keywords):

        """
        An algorithm that vectorizes the fileList into a 2D array containing the number of instances used of each
        keyword in each file. The Euclidean distance can then be measured to return the smallest distance (the most
        accurate file). 

        Parameters
        ----------
        fileList : list
            A list of files found on the Dropbox that are located in the specified companies and year fields.
        fileWordList : list
            A list of strings. Each string is the full content of a file.
        keywords : list
            The keywords that the Slack user requests a file to contain

        Returns
        -------
        bestDocs
            The list of files that are most accurate to the search that the Slack user requested.
        """
        
        RETURN_SIZE = 5

        #StemmedCountVectorizer creates a 2d array of word counts for each file            
        vectorizer = StemmedCountVectorizer(min_df=1) #can add "stop_words='english'" to remove common english words
        trainVectors = vectorizer.fit_transform(fileWordList)
        numSamples, numFeatures = trainVectors.shape

        # the keywords the session leader wants to find in Dropbox
        keywordsVec = vectorizer.transform([keywords])

        distList = []
        for i in range(0, numSamples):
            if fileWordList[i] == keywords:
                continue
            fileWordList_vec = trainVectors.getrow(i)
            d = BagOfWords.dist_norm(fileWordList_vec, keywordsVec)   
            #print("=== fileWordList %i with dist=%.2f: %s"%(i, d, fileWordList[i]))
            distList.append(d)

        bestDocs = []
        #selects only the files that have smallest distance
        #print("TOP " + str(RETURN_SIZE) + " MOST ACCURATE fileWordListS ARE:")
        for i in range(0, RETURN_SIZE):
            doc = distList.index(min(distList))
            #print("=== fileWordList %i with dist=%.2f: %s"%(i, distList[doc], fileWordList[doc]))
            bestDocs.append(fileList[doc])
            distList[doc] = sys.maxsize
        
        return bestDocs