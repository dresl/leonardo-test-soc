from django.apps import AppConfig

from .widget import *

default_app_config = 'leonardo_test_soc.Config'


LEONARDO_APPS = ['leonardo_test_soc']

LEONARDO_OPTGROUP = "Test widget"

LEONARDO_WIDGETS = [
    'leonardo_test_soc.widget.test_soc.models.TestSocWidget'
]

LEONARDO_CSS_FILES = [
	'css/style.css'
]

class Config(AppConfig):
    name = 'leonardo_test_soc'
    verbose_name = "leonardo_test_soc"
