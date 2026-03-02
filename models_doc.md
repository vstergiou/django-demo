# Models Documentation

> Auto-generated from `demo/models.py`. Do not edit manually.

### Item

A basic item with a name, description, and creation timestamp.

| Field Name | Field Type | Options | Description |
|------------|-----------|---------|-------------|
| name | CharField | max_length=200 | The name of the item |
| description | TextField | blank=True | Optional text description |
| created_at | DateTimeField | auto_now_add=True | Timestamp set automatically when the item is created |

**Methods:**

- `__str__()`: Returns the item's name.
