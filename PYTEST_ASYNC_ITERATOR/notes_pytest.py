# testing the class
class RepositoryX:

    @classmethod
    async def get_highlights(
        cls, entity_specification, region, entity_type
    ) -> List[dict]:
        highlights = list()
        try:
            query = {
                "entity_type": entity_type,
                "quote_specification": entity_specification,
                "region": region,
            }
            if not entity_specification:
                del query["quote_specification"]
            highlights_entities_interator = await cls.find_all(query, select_fields_dict={"_id": False})
            if highlights_entities_interator:
                highlights = [entity async for entity in highlights_entities_interator]
        except Exception as e:
            raise Exception
        return highlights


# async iter
class AsyncIter:

    def __init__(self, items):
        self.items = items

    async def __aiter__(self):
        for item in self.items:
            yield item

# stub
high_lights = {"name": "Ambev SA", "symbol": "ABEV3", "parent_symbol": "ABEV3"}

# testing the repository
@pytest.mark.asyncio
@patch.object(HighlightsRepository, 'find_all', return_value=AsyncIter(high_lights))
async def test_when_sending_right_params_search_get_highlights_then_return_expected_response(mock_find_all):
    response = await HighlightsRepository.get_highlights(
        region="BR",
        entity_specification="local",
        entity_type="stock",
    )
    assert response == [{"name": "Ambev SA", "symbol": "ABEV3", "parent_symbol": "ABEV3"}]


# ------------ mocking an async function with an attribute to_list

# return_value_stub
stub_return_value = {"entities": [{
                    "name": "Petroleo Brasileiro SA Petrobras",
                    "symbol": "PETR4",
                    "parent_symbol": "PETR4"}]}


# mocking the function find_all with to_list attribute
to_list_stub = AsyncMock(return_value=stub_find_one)
stub_find_all = AsyncMock(to_list=to_list_stub)

# test of the service function
@pytest.mark.asyncio
@patch.object(MongoBaseRepository, 'find_all', return_value=stub_find_all)
async def test_when_sending_right_params_search_symbols_basic_information_then_return_expected_response(mock_find_all):
    response = await BasicInformationRepository.search_symbols_basic_information(symbols="PETR4",
    select_fields_dict={})
    assert response == stub_find_one
    assert isinstance(stub_find_one, list)