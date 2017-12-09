# -*- coding: utf-8 -*-
"""A source fetching prices from Cryptocompare.
"""

import datetime

from beancount.core.number import D
from beancount.prices import source

import cryptocompare

__copyright__ = "Copyright (C) 2017  Albert De La Fuente Vigliotti"
__license__ = "GNU GPLv3"


class Source(source.Source):
    "Cryptocompare price source extractor."

    def _query_price(self, ticker, timestamp=None):
        if ':' in ticker:
            exchange, symbol = ticker.split(':')
        else:
            exchange = None
            symbol = ticker

        base_currency = 'USD'

        if exchange:
            result = cryptocompare.get_price(symbol, base_currency, exchange)
        else:
            result = cryptocompare.get_price(symbol, base_currency)

        if result is None:
            raise Exception('Symbol not found')

        time = datetime.datetime.now()
        try:
            price = D(result[symbol][base_currency])
        except KeyError:
            raise Exception('Symbol not found on exchange')

        return price, time, base_currency

    def get_latest_price(self, ticker):
        """See contract in beancount.prices.source.Source."""

        price, time, base_currency = self._query_price(ticker)
        return source.SourcePrice(price, time, base_currency)

    def get_historical_price(self, ticker, date):
        """See contract in beancount.prices.source.Source."""

        raise Exception('Historical prices not yet supported')
        # return source.SourcePrice(close_price, date, None)

if __package__ is None:
    print(__package__)
    import sys
    from os import path
    sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
    #from packages.files import fileChecker
else:
    print(__package__)
    #import ipdb; ipdb.set_trace() # BREAKPOINT
    #from packages.files import fileChecker
