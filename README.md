run "python setup.py install"  


edit "djangotest/djangotest/settings/test.py" and add
```
from __future__ import absolute_import

from .base import *

TWITTER_CONSUMER_KEY         = 'xxx'
TWITTER_CONSUMER_SECRET      = 'xxx'
FACEBOOK_APP_ID              = 'xxx'
FACEBOOK_API_SECRET          = 'xxx'
LINKEDIN_CONSUMER_KEY        = ''
LINKEDIN_CONSUMER_SECRET     = ''
GOOGLE_OAUTH2_CLIENT_ID      = 'xxx'
GOOGLE_OAUTH2_CLIENT_SECRET  = 'xxx'

```

run "DJANGO_SETTINGS_MODULE=djangotest.settings.test python manage.py runserver python manage.py runserver"  
 
