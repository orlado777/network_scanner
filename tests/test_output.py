import unittest
import io
import sys
import scanner

class TestOutput(unittest.TestCase):

    def setUp(self):
        # Redirigir stdout a un buffer para capturar la salida
        self.captured_output = io.StringIO()
        sys.stdout = self.captured_output

    def tearDown(self):
        # Restaurar stdout
        sys.stdout = sys.__stdout__

    def test_output_ping_sweep(self):
        # Simula ejecución con argumento --network
        sys.argv = ["scanner.py", "--network", "127.0.0"]
        scanner.main()
        output = self.captured_output.getvalue()
        self.assertIn("Escaneando subred 127.0.0.0/24...", output)

    def test_output_port_scan(self):
        # Simula ejecución con argumento --host y --ports
        sys.argv = ["scanner.py", "--host", "127.0.0.1", "--ports", "22-22"]
        scanner.main()
        output = self.captured_output.getvalue()
        self.assertIn("Escaneando puertos en 127.0.0.1...", output)

    def test_output_banner_grab(self):
        # Prueba directa de banner_grab en AWS
        banner = scanner.banner_grab("54.167.171.194", 22)
        self.assertIn("SSH", banner)

if __name__ == "__main__":
    unittest.main()
