import pytest
import asyncio


@pytest.fixture()
def mock_sum(mocker):
    future = asyncio.Future()
    future.set_result(4)
    mocker.patch('PYTEST_MARCH.function_to_sum_two_values', return_value=future)


@pytest.mark.asyncio
async def test_sum(mock_sum):
    result = await sum(1, 2)
    assert result == 4
