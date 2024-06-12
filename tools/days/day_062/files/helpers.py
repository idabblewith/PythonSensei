from misc import nls, nli, title, cls, bcolors, os
from flask import Flask, render_template, request, redirect, url_for
import csv
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import (
    DataRequired,
    URL,
    Email,
    Length,
)  # pip install email-validator
from flask_bootstrap import Bootstrap5  # pip install bootstrap-flask
