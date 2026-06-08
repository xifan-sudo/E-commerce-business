import unittest

from data_processing import process_data


class ProcessDataTests(unittest.TestCase):
    def test_process_data_summarizes_numeric_values(self):
        result = process_data([1, 2.5, None, 3])
        self.assertEqual(result["count"], 3)
        self.assertEqual(result["sum"], 6.5)
        self.assertAlmostEqual(result["average"], 6.5 / 3)

    def test_process_data_returns_zero_summary_for_empty_data(self):
        self.assertEqual(
            process_data([None, None]),
            {"count": 0, "sum": 0.0, "average": 0.0},
        )

    def test_process_data_rejects_unsupported_types(self):
        with self.assertRaises(TypeError):
            process_data([1, "2"])


if __name__ == "__main__":
    unittest.main()
