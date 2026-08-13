import unittest

from thought_to_x.scorer import QualityScore


class ScorerTests(unittest.TestCase):
    def test_passing_score(self) -> None:
        score = QualityScore(18, 12, 12, 18, 8, 8, 8)
        self.assertEqual(score.total, 84)
        self.assertTrue(score.passed)

    def test_hard_gate_fails_even_with_high_total(self) -> None:
        score = QualityScore(14, 15, 15, 20, 10, 10, 10)
        self.assertEqual(score.total, 94)
        self.assertFalse(score.passed)
        self.assertIn("idea_preservation_below_15", score.failures)

    def test_fabrication_fails(self) -> None:
        score = QualityScore(20, 15, 15, 20, 10, 10, 10, fabricated_experience=True)
        self.assertFalse(score.passed)

    def test_out_of_range_score_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            QualityScore(21, 15, 15, 20, 10, 10, 10)
