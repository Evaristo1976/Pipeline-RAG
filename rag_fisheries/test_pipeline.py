import unittest
from pipeline import chunk_text, retrieve, validate

class EvidenceTests(unittest.TestCase):
    def test_chunk_overlap_retains_boundary(self):
        self.assertEqual(list(chunk_text('a b c d e', 3, 1)), ['a b c', 'c d e'])

    def test_filter_and_no_match(self):
        chunks = [{'chunk_id':'A:1','paper_id':'A','text':'fisheries Timor'},
                  {'chunk_id':'B:1','paper_id':'B','text':'aquaculture'}]
        self.assertEqual(retrieve(chunks, 'aquaculture', paper_id='A'), [])
        self.assertEqual(retrieve(chunks, 'fisheries')[0]['paper_id'], 'A')

    def test_reject_invented_evidence(self):
        row = dict(paper_id='A', method='', findings='', reported_limitations='',
                   inferred_gap='', proposed_contribution='',
                   evidence=[{'chunk_id':'A:1','supporting_text':'invented'}])
        context = [{'chunk_id':'A:1','text':'actual passage'}]
        with self.assertRaises(ValueError):
            validate(row, 'A', context)
        row['evidence'][0]['supporting_text'] = 'actual passage'
        self.assertEqual(validate(row, 'A', context), row)

if __name__ == '__main__':
    unittest.main()
