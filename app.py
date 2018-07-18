from string import lower

from flask import Flask, render_template, request, redirect, url_for, session
from sqlalchemy import String, and_
from sqlalchemy_wrapper import SQLAlchemy
from Slambook.models import Parent,Child
from Slambook import routes



if __name__ == '__main__':
    app.run(debug=True)
