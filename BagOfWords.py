from StemmedCountVectorizer import StemmedCountVectorizer
import scipy as sp
import sys
import pdb
import time

class BagOfWords:
    """
    Class used to represent the file content search
    -----
    Methods
    -----
    dist_norm(v1, v2)
        Finds Euclidean distance of fileWordList to the keywords
    normalize(distList)
        Normalizes the distance list
    find_accurate_docs(fileList, fileWordList, keywords)
        An algorithm that vectorizes the fileList into a 2D array containing the number of instances used of each
        keyword in each file. The Euclidean distance can then be measured to return the smallest distance (the most
        accurate file). 
    """

    
    def dist_norm(v1, v2):
        """
        finds Euclidean distance of fileWordList to the keywords

        Parameters
        ----------
        v1: Vector
            First vector
        v2: Vector
            Second vector

        Returns
        -------
        sp.linalg.norm(delta.toarray())
            the change between normalized distances in an array
            
        """
        v1Normalized = v1/sp.linalg.norm(v1.toarray())
        v2Normalized = v2/sp.linalg.norm(v2.toarray())
        delta = v1Normalized - v2Normalized
        return sp.linalg.norm(delta.toarray())

    def normalize(distList):
        """
        normalizes the distList so that we can choose what accuracy threshold to return to user

        Parameters
        ----------
        distList: List
            the distance list

        Returns
        -------
        distList
            the normalized distlist
            
        """
        if len(distList) == 1:
            if(distList[0] < 0.90):
                return # does not need to normalize if there is only one. Will be on scale of 0-1
            else:
                distList = []
                return

        maxWeight = max(distList)
        i = 0
        for weight in distList:
            distList[i] = (weight * (1/maxWeight))
            i = i + 1


    def find_accurate_docs(fileList, fileWordList, keywords):
        startTime = time.time()

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
        distList
            A list of each file's distance. Each file's distance is the accuracy of the file's content or name to
            that of the Slack search query of the user
        """
        distList = []
        try:
            #StemmedCountVectorizer creates a 2d array of word counts for each file            
            vectorizer = StemmedCountVectorizer(min_df=1) #can add "stop_words='english'" to remove common english words
        
            trainVectors = vectorizer.fit_transform(fileWordList)
            numSamples, numFeatures = trainVectors.shape

            # the keywords the session leader wants to find in Dropbox
            keywordsVec = vectorizer.transform([keywords])
            
            for i in range(0, numSamples):
                if fileWordList[i] == keywords:
                    continue
                fileWordList_vec = trainVectors.getrow(i)
                d = BagOfWords.dist_norm(fileWordList_vec, keywordsVec)   
                distList.append(d)
            
            BagOfWords.normalize(distList) # normalizes the distList so that we can choose what accuracy threshold to return to user

            """
            for i in range(0, numSamples):
                print("=== fileWordList %i with dist=%.2f: %s"%(i, distList[i], fileWordList[i]))
            """

        except Exception as exc:
            print('generated an exception: %s' % exc)

        return distList