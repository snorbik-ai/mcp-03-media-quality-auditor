import sys
from pathlib import Path

_TEST_DIR = Path(__file__).resolve().parent
_TOOL_ROOT = _TEST_DIR.parent
if str(_TOOL_ROOT) not in sys.path:
    sys.path.insert(0, str(_TOOL_ROOT))
if str(_TEST_DIR) not in sys.path:
    sys.path.insert(0, str(_TEST_DIR))

from run_all_suites import (
    run_unit_tests,
    run_integration_tests,
    run_validation_and_perf_tests,
    run_smoke_tests,
)

def test_mcp_03_all_suites():
    for fn in [run_unit_tests, run_integration_tests, run_validation_and_perf_tests, run_smoke_tests]:
        res = fn()
        assert res["failed"] == 0, f"Échec dans {res['suite']}"
        assert res["passed"] > 0
