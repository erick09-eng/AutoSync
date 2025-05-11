from logging.config import fileConfig
import os
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# Import your model's MetaData object here
# for 'autogenerate' support
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.database import Base  # Import your Base
from models.Audit_log import AuditLog
from models.Category import Category
from models.Customers import Customers
from models.DocumentType import DocumentType
from models.inventory_movements import Inventory_movements
from models.Payment_methods import PaymentMethod
from models.Payments import Payments
from models.product_promotions import Product_Promotions
from models.Product import Product
from models.promotions import Promotions
from models.Roles import Roles
from models.sale_details import Sale_details
from models.Sales import Sale
from models.Users import User


target_metadata = Base.metadata



def get_url():
        # Use environment variables or config file to get the database URL
    MYSQL_USER = os.getenv("MYSQL_USER", "user_full_1")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "userPassB1")
    MYSQL_HOST = os.getenv("MYSQL_HOST", "db")  # Docker Compose service name
    MYSQL_DB = os.getenv("MYSQL_DATABASE", "db_autosync")
    return f"mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        url=get_url()
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()