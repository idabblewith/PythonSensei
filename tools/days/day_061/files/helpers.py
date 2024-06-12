from misc import nls, nli, title, cls, bcolors, os
import requests
from flask import Flask, render_template, request
import smtplib
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
)  # pip install email-validator
from flask_bootstrap import Bootstrap5  # pip install bootstrap-flask
