from misc import nls, nli, title, cls, bcolors, os
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
