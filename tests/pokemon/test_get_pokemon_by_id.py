import pytest

from src.pokemon.get_pokemon_by_id import get_pokemon


@pytest.mark.parametrize("poke_id, expected_status", [
    (1, 200),
    (6, 200),
    (20, 200)
])
def test_when_id_exists_returns_200(poke_id, expected_status):
    response = get_pokemon(poke_id)
    assert response.status_code == expected_status


@pytest.mark.parametrize("poke_id, expected_status", [
    (2000, 404),
    (1000, 404),
    (950, 404),
])
def test_when_id_does_not_exist_returns_404(poke_id, expected_status):
    response = get_pokemon(poke_id)
    assert response.status_code == expected_status
