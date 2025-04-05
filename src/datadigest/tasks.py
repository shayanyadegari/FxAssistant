from celery import shared_task
from datetime import timedelta,datetime

from django.apps import apps 
from django.utils import timezone
from helper.prepare_data import TwelveDataAPI
from decimal import Decimal

'''
each sync works with different time frames
and in each sync we only update 1 row of data.
with this method we are sure our data is updated every 15 minutes
'''

@shared_task
def sync_pair_quotes_1day(pair_name):
    
    pair_1d = apps.get_model("datadigest", "pair_1d")

    pair_1d_ = TwelveDataAPI(pair_name='EUR/USD',interval='1day')
    record = pair_1d_.fetch_data()[0]

    dt = datetime.strptime(record['datetime'], '%Y-%m-%d')
    
    obj = pair_1d.objects.create(
        datetime=dt,
        pair_name = 'EUR/USD',
        open_price=Decimal(record['open']),
        high_price=Decimal(record['high']),
        low_price=Decimal(record['low']),
        close_price=Decimal(record['close'])
    )

