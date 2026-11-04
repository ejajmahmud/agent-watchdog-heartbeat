"""Subagent liveness probe and supervisor."""
import time
from typing import Dict, List, Tuple


class WatchdogSupervisor:
    def __init__(self, timeout_seconds: float = 5.0):
        self.timeout = timeout_seconds
        self._workers: Dict[str, float] = {}

    def beat(self, worker_id: str):
        self._workers[worker_id] = time.time()

    def check_liveness(self) -> Tuple[List[str], List[str]]:
        """Returns (healthy_workers, stalled_workers)."""
        now = time.time()
        healthy = []
        stalled = []
        for wid, last_seen in self._workers.items():
            if now - last_seen > self.timeout:
                stalled.append(wid)
            else:
                healthy.append(wid)
        return healthy, stalled
