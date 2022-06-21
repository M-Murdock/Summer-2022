# !pip install typing-extensions --upgrade
# !pip install gradio
# !pip install greek-accentuation==1.2.0
# !pip install greek-normalisation
import pandas as pd
import re
import string
import gradio as gr
from greek_accentuation.syllabify import *
from greek_normalisation.utils import *