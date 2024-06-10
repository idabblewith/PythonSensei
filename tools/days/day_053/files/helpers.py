from misc import nls, nli, title, cls, bcolors
from dotenv import load_dotenv
import os, requests
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
)
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

from bs4 import BeautifulSoup
from pprint import pprint
from typing import Dict, List
import time
import os
import concurrent.futures as futures
