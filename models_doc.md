# Models Documentation

> Auto-generated from `demo/models.py`. Do not edit manually.

### Item

A basic item with a name, optional description, and automatic timestamps for creation and updates.

| Field Name | Field Type | Options | Description |
|------------|------------|---------|-------------|
| name | CharField | max_length=200 | The name of the item |
| description | TextField | blank=True | Optional text description |
| created_at | DateTimeField | auto_now_add=True | Timestamp set automatically when the item is created |
| updated_at | DateTimeField | auto_now=True | Timestamp updated automatically on every save |

**Methods:**

- `__str__()`: Returns the item's name.

---

### Category

Represents a category used to group or classify items. Ordered alphabetically by name.

| Field Name | Field Type | Options | Description |
|------------|------------|---------|-------------|
| name | CharField | max_length=100, unique=True | Unique display name of the category |
| slug | SlugField | max_length=100, unique=True | URL-friendly unique identifier |
| description | TextField | blank=True | Optional text description |
| is_active | BooleanField | default=True | Whether the category is currently active |
| created_at | DateTimeField | auto_now_add=True | Timestamp set automatically when the category is created |

**Meta:**

- `verbose_name_plural`: `"categories"`
- `ordering`: `["name"]`

**Methods:**

- `__str__()`: Returns the category's name.

---

### Tag

A label that can be applied to items, with an optional color and genre.

| Field Name | Field Type | Options | Description |
|------------|------------|---------|-------------|
| name | CharField | max_length=50, unique=True | Unique name of the tag |
| color | CharField | max_length=7, default="#000000" | Hex color code for the tag (e.g. `#ff0000`) |
| genre | CharField | max_length=50, blank=True | Optional genre classification for the tag |

**Methods:**

- `__str__()`: Returns the tag's name.
