import unittest
import scanner

class TestArguments(unittest.TestCase):

    def test_network_argument_192(self):
        args = scanner.parse_args(["--network", "192.168.1"])
        self.assertEqual(args.network, "192.168.1")

    def test_network_argument_10(self):
        args = scanner.parse_args(["--network", "10.0.0"])
        self.assertEqual(args.network, "10.0.0")

    def test_network_argument_172(self):
        args = scanner.parse_args(["--network", "172.16.0"])
        self.assertEqual(args.network, "172.16.0")

    def test_host_ports_arguments(self):
        args = scanner.parse_args(["--host", "127.0.0.1", "--ports", "20-80"])
        self.assertEqual(args.host, "127.0.0.1")
        self.assertEqual(args.ports, "20-80")

    def test_help_argument(self):
        # argparse con --help debe terminar el programa con SystemExit
        with self.assertRaises(SystemExit):
            scanner.parse_args(["--help"])

if __name__ == "__main__":
    unittest.main()
