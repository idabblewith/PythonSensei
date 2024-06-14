from misc import nls, nli, title, cls, bcolors, os
from dotenv import load_dotenv
from datetime import date
from .forms import CreatePostForm, RegisterForm, LoginForm, CommentForm

# from flask_gravatar import Gravatar
from hashlib import md5

from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user

from flask_ckeditor import CKEditor, CKEditorField
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
