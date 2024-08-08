# SQLAlchemy Database Management

This script demonstrates how to use SQLAlchemy to manage a database with tables for students and subjects, including relationships between them.

## Code Overview

### Imports

The script imports necessary modules and classes from SQLAlchemy:

```python
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
