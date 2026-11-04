"""Tests for agent-watchdog-heartbeat."""
import time
import unittest
from agent_watchdog_heartbeat.watchdog import WatchdogSupervisor


class TestWatchdogSupervisor(unittest.TestCase):
    def setUp(self):
        self.wd = WatchdogSupervisor(timeout_seconds=0.1)

    def test_healthy_and_stalled(self):
        self.wd.beat("w1")
        self.wd.beat("w2")
        h, s = self.wd.check_liveness()
        self.assertEqual(len(h), 2)
        self.assertEqual(len(s), 0)

        time.sleep(0.15)
        self.wd.beat("w1")  # w1 refreshed, w2 not
        h2, s2 = self.wd.check_liveness()
        self.assertIn("w1", h2)
        self.assertIn("w2", s2)


if __name__ == "__main__":
    unittest.main()
