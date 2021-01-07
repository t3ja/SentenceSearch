import re
import string
from typing import List


class SentenceSearcher:
    def __init__(self, corpus):
        self.corpus = corpus
        self.digits = "([0-9])"
        self.alphabets = "([A-Za-z])"
        self.prefixes = "(Jr|Sr|Mr|St|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|Mt)[.]"
        self.websites = "[.](com|net|org|io|gov|ai|edu|co.uk|ru|info|biz|online)"
        self.sentences = self.split_sentences()

    def split_sentences(self) -> List[str]:
        """
        Converts the input string, passed in as corpus in the constructor into a list of sentences,
        following a set of rules.
        - Handles decimal point numbers like 5.5
        - Salutations like Mr.
        - website addresses like .com
        - abbreviations like U.S.A
        Returns:
            List[str]: Sentences split from the corpus as a list
        """
        text = self.corpus
        text = " " + text + "  "  # append spaces at the beginning and end to handle edge sentences
        text = re.sub(self.digits + "[.]" + self.digits, "\\1<period>\\2", text)  # Replace all decimal dots with <period>
        text = re.sub(self.prefixes, "\\1<period>", text)  # Replace all prefix dots with <period>
        text = re.sub(self.websites, "<period>\\1", text)  # Replace all dots in website domains with <period>
        text = re.sub(self.alphabets + "[.]" + self.alphabets + "[.]" + self.alphabets + "[.]",
                      "\\1<period>\\2<period>\\3<period>", text)  # Replace all dots between alphabets like U.S.A
        text = re.sub(self.alphabets + "[.]" + self.alphabets + "[.]", "\\1<period>\\2<period>",
                      text)  # Replace all dots between alphabets like U.S
        text = text.replace(".", ".<stop>")  # Replace all remaining sentence endings with <stop>
        text = text.replace("?", "?<stop>")
        text = text.replace("!", "!<stop>")
        text = text.replace("<period>", ".")  # Replace period tags
        sentences = text.split("<stop>")  # split by <stop> tag
        sentences = sentences[:-1] if not sentences[:-1] else sentences  # ignore last empty sentence
        sentences = [s.strip() for s in sentences]
        return sentences

    def search(self, query) -> str:
        """

        Returns:
            str: Returns the first sentence containing the query word if exists. Returns an empty string otherwise.
        """
        for sentence in self.sentences:
            for word in sentence.split():
                if query.strip(string.punctuation).lower() == word.strip(string.punctuation).lower():
                    return sentence
        return ""
