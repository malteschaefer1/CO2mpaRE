# test_web_scraping.py

import sys
sys.path.append('/Users/malteschafer/Documents/GitHub/CO2mpaRE/src')

from web_scraping import check_api_health, get_expost_latest, get_co2_intensity

def test_check_api_health():
    """Test API health endpoint."""
    assert check_api_health() is True, "API health check failed."

def test_get_expost_latest():
    """Test fetching expost latest data."""
    region = 'DE'
    data = get_expost_latest(region=region)
    assert data is not None, "Failed to fetch expost latest data."
    print("Expost latest data fetched successfully:")
    print(data)

def test_get_co2_intensity():
    """Test fetching CO2 intensity data."""
    start_date = '2024-07-02T00:00:00Z'
    end_date = '2024-07-02T01:00:00Z'
    region = 'DE'
    dataset = 'expost'
    scope = 'LC'
    data = get_co2_intensity(start_date, end_date, dataset=dataset, scope=scope, region=region)
    assert data is not None, "Failed to fetch CO2 intensity data."
    print("CO2 intensity data fetched successfully:")
    print(data)

if __name__ == "__main__":
    # Run tests
    test_check_api_health()
    test_get_expost_latest()
    test_get_co2_intensity()
