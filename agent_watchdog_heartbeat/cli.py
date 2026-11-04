"""CLI for agent-watchdog-heartbeat."""
import sys
import argparse
from .watchdog import WatchdogSupervisor


def main():
    parser = argparse.ArgumentParser(description="Agent Watchdog Heartbeat")
    parser.add_argument("--demo", action="store_true", help="Run watchdog demo")
    args = parser.parse_args()

    wd = WatchdogSupervisor(timeout_seconds=2.0)
    wd.beat("worker_1")
    healthy, stalled = wd.check_liveness()
    print(f"Healthy workers: {healthy}, Stalled workers: {stalled}")
    sys.exit(0)


if __name__ == "__main__":
    main()
