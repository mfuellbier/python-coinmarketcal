# python-coinmarketcal
Coinmarketcal.com REST API python implementation

API (1.0.0): https://api.coinmarketcal.com/

## Usage
```python
import coinmarketcal
# Get Token
coinmarketcal.getToken(Client ID, Client Secret)
# Get coins list
coinmarketcal.getCoins(token)
# Get categories list
coinmarketcal.getCategories(token)
# Get default events
coinmarketcal.getEvents(token)
```
