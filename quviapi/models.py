from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    credit = models.IntegerField(default=200)
    t1 = models.TextField(null=True)
    c1 = models.JSONField(null=True)
    ci1 = models.TextField(null=True, default="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAACmUlEQVR4nO3cO2sUcRSG8WdWg7dEMY2VhUXAWkQQsRO/iFhZ2VlrbWFnpR/ESi28EBElIFgKViJeEoxESSzWgMTNbAKZs5N9n18Twg6cE/bZJbswf5AkSZIkSZIkSZIkSZIkSZIkSdK+1FQM2djYqBizGwvAXeAyMACeA7eA15Ncaqum6f7pSQxgAXgLHB7x2HngVe0626sIYND5hP65x+gnH+B+5SJ9kPYOMAN8Ak60XDMPfKlZp53vAHvvKNu/+jfNVyzSF2kBrANrY675XbFIX6QFoC0MIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhEsLYBkYd6tyL+4MrnJwAjMHwLEJzAWYY3z0p4EPBbuMskrxzamV5wOcBW4DF2m/P79rs7T/3SuMf5foyjKwCNwBFqfpiJgzwDvgUMW8KXGuaZrOzyyq+h/gAT75u/WwYkjVO0BvzojZR9abpjnQ9ZC0TwH7ScmLsyqAl0Vzpsn7iiFVAVwrmjNNrlcMqQpgieHHv0cMP2ZptB/AU+Dq35+dm8Q5gSeB4xVzR5gFXtD+RdQl4GPNOv9ZAT5v/jJN3wNUjNmpb7QHeAT4WbRLKw+K3HtzjI/+VMUifZEWgLYwgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEC4tgAEwM+aaSRydNzFpAawCv8Zc87Vikb5IC2CN4Tl821nin/vzE6QFAHCz5bEbZVv0RGIAb4ALwGOGh0V8B54BV4AnE9xLkiRJkiRJkiRJkiRJkiRJkiRJ2rk/W9VP62vgsq8AAAAASUVORK5CYII=")
    t2 = models.TextField(null=True)
    c2 = models.JSONField(null=True)
    ci2 = models.TextField(null=True, default="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAACmUlEQVR4nO3cO2sUcRSG8WdWg7dEMY2VhUXAWkQQsRO/iFhZ2VlrbWFnpR/ESi28EBElIFgKViJeEoxESSzWgMTNbAKZs5N9n18Twg6cE/bZJbswf5AkSZIkSZIkSZIkSZIkSZIkSdK+1FQM2djYqBizGwvAXeAyMACeA7eA15Ncaqum6f7pSQxgAXgLHB7x2HngVe0626sIYND5hP65x+gnH+B+5SJ9kPYOMAN8Ak60XDMPfKlZp53vAHvvKNu/+jfNVyzSF2kBrANrY675XbFIX6QFoC0MIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhEsLYBkYd6tyL+4MrnJwAjMHwLEJzAWYY3z0p4EPBbuMskrxzamV5wOcBW4DF2m/P79rs7T/3SuMf5foyjKwCNwBFqfpiJgzwDvgUMW8KXGuaZrOzyyq+h/gAT75u/WwYkjVO0BvzojZR9abpjnQ9ZC0TwH7ScmLsyqAl0Vzpsn7iiFVAVwrmjNNrlcMqQpgieHHv0cMP2ZptB/AU+Dq35+dm8Q5gSeB4xVzR5gFXtD+RdQl4GPNOv9ZAT5v/jJN3wNUjNmpb7QHeAT4WbRLKw+K3HtzjI/+VMUifZEWgLYwgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEC4tgAEwM+aaSRydNzFpAawCv8Zc87Vikb5IC2CN4Tl821nin/vzE6QFAHCz5bEbZVv0RGIAb4ALwGOGh0V8B54BV4AnE9xLkiRJkiRJkiRJkiRJkiRJkiRJ2rk/W9VP62vgsq8AAAAASUVORK5CYII=")
    t3 = models.TextField(null=True)
    c3 = models.JSONField(null=True)
    ci3 = models.TextField(null=True, default="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAACmUlEQVR4nO3cO2sUcRSG8WdWg7dEMY2VhUXAWkQQsRO/iFhZ2VlrbWFnpR/ESi28EBElIFgKViJeEoxESSzWgMTNbAKZs5N9n18Twg6cE/bZJbswf5AkSZIkSZIkSZIkSZIkSZIkSdK+1FQM2djYqBizGwvAXeAyMACeA7eA15Ncaqum6f7pSQxgAXgLHB7x2HngVe0626sIYND5hP65x+gnH+B+5SJ9kPYOMAN8Ak60XDMPfKlZp53vAHvvKNu/+jfNVyzSF2kBrANrY675XbFIX6QFoC0MIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhEsLYBkYd6tyL+4MrnJwAjMHwLEJzAWYY3z0p4EPBbuMskrxzamV5wOcBW4DF2m/P79rs7T/3SuMf5foyjKwCNwBFqfpiJgzwDvgUMW8KXGuaZrOzyyq+h/gAT75u/WwYkjVO0BvzojZR9abpjnQ9ZC0TwH7ScmLsyqAl0Vzpsn7iiFVAVwrmjNNrlcMqQpgieHHv0cMP2ZptB/AU+Dq35+dm8Q5gSeB4xVzR5gFXtD+RdQl4GPNOv9ZAT5v/jJN3wNUjNmpb7QHeAT4WbRLKw+K3HtzjI/+VMUifZEWgLYwgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEC4tgAEwM+aaSRydNzFpAawCv8Zc87Vikb5IC2CN4Tl821nin/vzE6QFAHCz5bEbZVv0RGIAb4ALwGOGh0V8B54BV4AnE9xLkiRJkiRJkiRJkiRJkiRJkiRJ2rk/W9VP62vgsq8AAAAASUVORK5CYII=")
    t4 = models.TextField(null=True)
    c4 = models.JSONField(null=True)
    ci4 = models.TextField(null=True, default="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAACmUlEQVR4nO3cO2sUcRSG8WdWg7dEMY2VhUXAWkQQsRO/iFhZ2VlrbWFnpR/ESi28EBElIFgKViJeEoxESSzWgMTNbAKZs5N9n18Twg6cE/bZJbswf5AkSZIkSZIkSZIkSZIkSZIkSdK+1FQM2djYqBizGwvAXeAyMACeA7eA15Ncaqum6f7pSQxgAXgLHB7x2HngVe0626sIYND5hP65x+gnH+B+5SJ9kPYOMAN8Ak60XDMPfKlZp53vAHvvKNu/+jfNVyzSF2kBrANrY675XbFIX6QFoC0MIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhEsLYBkYd6tyL+4MrnJwAjMHwLEJzAWYY3z0p4EPBbuMskrxzamV5wOcBW4DF2m/P79rs7T/3SuMf5foyjKwCNwBFqfpiJgzwDvgUMW8KXGuaZrOzyyq+h/gAT75u/WwYkjVO0BvzojZR9abpjnQ9ZC0TwH7ScmLsyqAl0Vzpsn7iiFVAVwrmjNNrlcMqQpgieHHv0cMP2ZptB/AU+Dq35+dm8Q5gSeB4xVzR5gFXtD+RdQl4GPNOv9ZAT5v/jJN3wNUjNmpb7QHeAT4WbRLKw+K3HtzjI/+VMUifZEWgLYwgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEC4tgAEwM+aaSRydNzFpAawCv8Zc87Vikb5IC2CN4Tl821nin/vzE6QFAHCz5bEbZVv0RGIAb4ALwGOGh0V8B54BV4AnE9xLkiRJkiRJkiRJkiRJkiRJkiRJ2rk/W9VP62vgsq8AAAAASUVORK5CYII=")
    t5 = models.TextField(null=True)
    c5 = models.JSONField(null=True)
    ci5 = models.TextField(null=True, default="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAACmUlEQVR4nO3cO2sUcRSG8WdWg7dEMY2VhUXAWkQQsRO/iFhZ2VlrbWFnpR/ESi28EBElIFgKViJeEoxESSzWgMTNbAKZs5N9n18Twg6cE/bZJbswf5AkSZIkSZIkSZIkSZIkSZIkSdK+1FQM2djYqBizGwvAXeAyMACeA7eA15Ncaqum6f7pSQxgAXgLHB7x2HngVe0626sIYND5hP65x+gnH+B+5SJ9kPYOMAN8Ak60XDMPfKlZp53vAHvvKNu/+jfNVyzSF2kBrANrY675XbFIX6QFoC0MIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhDOAcAYQzgDCGUA4AwhnAOEMIJwBhEsLYBkYd6tyL+4MrnJwAjMHwLEJzAWYY3z0p4EPBbuMskrxzamV5wOcBW4DF2m/P79rs7T/3SuMf5foyjKwCNwBFqfpiJgzwDvgUMW8KXGuaZrOzyyq+h/gAT75u/WwYkjVO0BvzojZR9abpjnQ9ZC0TwH7ScmLsyqAl0Vzpsn7iiFVAVwrmjNNrlcMqQpgieHHv0cMP2ZptB/AU+Dq35+dm8Q5gSeB4xVzR5gFXtD+RdQl4GPNOv9ZAT5v/jJN3wNUjNmpb7QHeAT4WbRLKw+K3HtzjI/+VMUifZEWgLYwgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEM4AwhlAOAMIZwDhDCCcAYQzgHAGEC4tgAEwM+aaSRydNzFpAawCv8Zc87Vikb5IC2CN4Tl821nin/vzE6QFAHCz5bEbZVv0RGIAb4ALwGOGh0V8B54BV4AnE9xLkiRJkiRJkiRJkiRJkiRJkiRJ2rk/W9VP62vgsq8AAAAASUVORK5CYII=")
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='custom_user_groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_permissions'
    )