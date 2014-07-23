from datetime import datetime, timedelta
from pytz import timezone
import pytz

utc = pytz.utc

eastern = timezone('US/Eastern')
print eastern.zone
