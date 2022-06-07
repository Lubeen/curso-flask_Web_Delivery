import click

from delivery.ext.auth.models import User
from delivery.ext.auth.controller import create_user
from delivery.ext.db import db


def list_users():
    users = User.query.all()
    click.echo(f"lista de usuarios {users}")


@click.option("--email", "-e")
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    """adiciona novo usuario"""
    create_user(email=email, passwd=passwd, admin=admin)
    #tratar user exists except

    click.echo(f"Usuário {email} criado com sucesso!")
