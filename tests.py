import unittest
from sentence_searcher import SentenceSearcher


class MyTestCase(unittest.TestCase):
    def test_simple_1(self):
        ss = SentenceSearcher("""Mutley, you snickering, floppy eared hound. When courage is needed, 
        you’re never around. Those medals you wear on your moth-eaten chest should be there for bungling at which
         you are best. So, stop that pigeon, stop that pigeon, stop that pigeon, stop that pigeon, stop that pigeon, 
         stop that pigeon, stop that pigeon. Howwww! Nab him, jab him, tab him, grab him, stop that pigeon now.""")
        results = ss.search("floppy")
        expected = "Mutley, you snickering, floppy eared hound."
        self.assertEqual(results, expected)

    def test_case_insensitive(self):
        ss = SentenceSearcher("""I have a cat. I have a mat. Things are going well.""")
        results = ss.search("MAT")
        expected = "I have a mat."
        self.assertEqual(results, expected)

    def test_decimal(self):
        ss = SentenceSearcher("""I have a 5.5 cats. I have 2.3 dogs and 9.4 rats. Things are going swell""")
        results = ss.search("cats")
        expected = "I have a 5.5 cats."
        self.assertEqual(results, expected)

    def test_exact_match(self):
        ss = SentenceSearcher("""I have a 5.5 cats. I have 2.3 dogs and 9.4 rats. Things are going swell""")
        results = ss.search("cat")
        expected = ""
        self.assertEqual(results, expected)

    def test_abbreviations(self):
        ss = SentenceSearcher("""Among the finest Orthopaedic Doctors in the city, Dr. Pradeep Kocheeppan 
        (Apollo Hospital) in Bannerghatta Road, Bangalore is known for offering excellent patient care. The doctor 
        holds an experience of 8 years and has specialization in A.B.C from University of U.S.A.""")
        results = ss.search("years")
        expected = """The doctor 
        holds an experience of 8 years and has specialization in A.B.C from University of U.S.A."""
        self.assertEqual(results, expected)

    def test_exact_match(self):
        ss = SentenceSearcher("""80 days around the world, we’ll find a pot of gold just sitting where the 
        rainbow’s ending. Time — we’ll fight against the time, and we’ll fly on the white wings of the wind. 
        80 days around the world, no we won’t say a word before the ship is really back. 
        Round, round, all around the world. Round, all around the world. Round, all around the world. 
        Round, all around the world.""")
        results = ss.search("round")
        expected = "Round, round, all around the world."
        self.assertEqual(results, expected)

    def test_salutations(self):
        ss = SentenceSearcher("""Barnaby The Bear’s my name, never call me Mr. Jack or Mr. James.
        I will sing my way to fame, Barnaby the Bear’s my name. 
        Birds taught me to sing, when they took me to their king, first I had to fly, in the sky so high so high, 
        so high so high so high, so — if you want to sing this way. Think of what you’d like to say, add a tune and 
        you will see, just how easy it can be. Treacle pudding, fish and chips, fizzy drinks and liquorice, flowers,
         rivers, sand and sea, snowflakes and the stars are free. """)
        results = ss.search("James")
        expected = "Barnaby The Bear’s my name, never call me Mr. Jack or Mr. James."
        self.assertEqual(results, expected)

    def test_salutations_2(self):
        ss = SentenceSearcher("""Among the finest Orthopaedic Doctors in the city, Dr. Pradeep Kocheeppan 
        (Apollo Hospital) in Bannerghatta Road, Bangalore is known for offering excellent patient care. The doctor 
        holds an experience of 8 years and has extensive knowledge in the respective field of medicine. 
        The clinic is located centrally in Bannerghatta Road, a prominent locality in the city.""")
        results = ss.search("Pradeep")
        expected = """Among the finest Orthopaedic Doctors in the city, Dr. Pradeep Kocheeppan 
        (Apollo Hospital) in Bannerghatta Road, Bangalore is known for offering excellent patient care."""
        self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main()
