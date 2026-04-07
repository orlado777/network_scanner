import unittest
import warnings
import sys, os

# Ignorar ResourceWarning para salida limpia
warnings.filterwarnings("ignore", category=ResourceWarning)

# Asegurar import de scanner.py desde raíz del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import scanner
from unittest.mock import patch

class TestScanner(unittest.TestCase):

    def test_ping_localhost(self):
        self.assertTrue(scanner.ping("127.0.0.1"))

    def test_scan_port_boolean(self):
        result = scanner.scan_port("127.0.0.1", 80)
        self.assertIn(result, [True, False])

    def test_port_scan_list(self):
        abiertos = scanner.port_scan("127.0.0.1", range(20, 25))
        self.assertIsInstance(abiertos, list)

    @patch("scanner.ping", return_value=True)
    def test_ping_sweep_192(self, mock_ping):
        activos = scanner.ping_sweep("192.168.1")
        self.assertIsInstance(activos, list)

    @patch("scanner.ping", return_value=False)
    def test_ping_sweep_10(self, mock_ping):
        activos = scanner.ping_sweep("10.0.0")
        self.assertIsInstance(activos, list)

    @patch("scanner.ping", return_value=False)
    def test_ping_sweep_172(self, mock_ping):
        activos = scanner.ping_sweep("172.16.0")
        self.assertIsInstance(activos, list)

if __name__ == "__main__":
    unittest.main()
