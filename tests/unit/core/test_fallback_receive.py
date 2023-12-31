from pathlib import Path

from solscan import Solscan
from solscan.core.declarations.function import FunctionType

TEST_DATA_DIR = Path(__file__).resolve().parent / "test_data"


def test_fallback_receive(solc_binary_path):
    solc_path = solc_binary_path("0.6.12")
    file = Path(TEST_DATA_DIR, "fallback.sol").as_posix()
    solscan = Solscan(file, solc=solc_path)
    fake_fallback = solscan.get_contract_from_name("FakeFallback")[0]
    real_fallback = solscan.get_contract_from_name("Fallback")[0]

    assert fake_fallback.fallback_function is None
    assert fake_fallback.receive_function is None
    assert real_fallback.fallback_function.function_type == FunctionType.FALLBACK
    assert real_fallback.receive_function.function_type == FunctionType.RECEIVE
