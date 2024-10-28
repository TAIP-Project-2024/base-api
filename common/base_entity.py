import datetime
import uuid

"""
 Base class for all entities.
 Contains fields useful for audit.
"""
class Entity:
    created_at: datetime
    last_modified_at: datetime
    created_by: uuid
    last_modified_by: uuid