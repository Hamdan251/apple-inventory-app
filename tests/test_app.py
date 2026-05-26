import csv
import os
import tempfile
import unittest

import app


class ExportSpecComplianceTests(unittest.TestCase):
    def test_export_spec_compliant_csv_writes_expected_rows(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            original_cwd = os.getcwd()
            try:
                os.chdir(tmpdir)
                app.export_spec_compliant_csv()

                with open(app.EXPORT_FILE, newline="", encoding="utf-8") as file:
                    rows = list(csv.reader(file))
            finally:
                os.chdir(original_cwd)

        self.assertEqual(rows[0], ["Apple Variety", "Quantity"])
        self.assertEqual(rows[1], ["Honeycrisp", "50"])
        self.assertEqual(rows[2], ["Gala", "32"])
        self.assertEqual(rows[3], ["Granny Smith [OUT OF STOCK]", "0"])

    def test_export_rows_only_include_active_inventory_items(self):
        rows = app.build_export_rows()

        self.assertEqual(len(rows), len(app.inventory))
        self.assertIn(("Honeycrisp", 50), rows)
        self.assertIn(("Gala", 32), rows)
        self.assertIn(("Granny Smith [OUT OF STOCK]", 0), rows)


if __name__ == "__main__":
    unittest.main()
