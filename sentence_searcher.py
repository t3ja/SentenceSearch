from typing import List


class SentenceSearcher:
    def __init__(self, corpus):
        self.corpus = corpus
        self.sentences = self.split_sentences()
        
    def split_sentences(self) -> List[str]:
        """

        Returns:
            List[str]: Sentences split from the corpus as a list
        """
        return []
    
    def search(self, query) -> str:
        """

        Returns:
            str: Returns the first sentence containing the query word if exists. Returns an empty string otherwise.
        """
        return ""
