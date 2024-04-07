import pickle
import sqlite3

# Create/connect to a SQLite database
splite3_conn = sqlite3.connect('key_value_store.db')
cursor = splite3_conn.cursor()

# Create a table to store key-value pairs
cursor.execute('''CREATE TABLE IF NOT EXISTS key_value_pairs
                  (key TEXT PRIMARY KEY, value BLOB)''')
splite3_conn.commit()


# Function to add objects to a key
def add(key, name, age):
    try:
        key_str = str(key)  # Convert key to string
        data = pickle.dumps({"name": name, "age": age})
        cursor.execute('INSERT OR REPLACE INTO key_value_pairs VALUES (?, ?)', (key_str, data))
        splite3_conn.commit()
    except sqlite3.IntegrityError:
        print(f"Key '{key}' already exists.")
    except Exception as e:
        print("Error adding data:", e)


# Function to remove a key and its associated data
def remove(key):
    try:
        key_str = str(key)  # Convert key to string
        cursor.execute('DELETE FROM key_value_pairs WHERE key=?', (key_str,))
        splite3_conn.commit()
    except Exception as e:
        print("Error removing data:", e)


# Function to update objects associated with a key
def update(key, name=None, age=None):
    try:
        key_str = str(key)  # Convert key to string
        new_dict = get(key_str) or {}
        if name:
            new_dict["name"] = name
        if age:
            new_dict["age"] = age

        data = pickle.dumps(new_dict)
        cursor.execute('INSERT OR REPLACE INTO key_value_pairs VALUES (?, ?)', (key_str, data))
        splite3_conn.commit()
    except Exception as e:
        print("Error updating data:", e)


# Function to get objects associated with a key
def get(key):
    try:
        key_str = str(key)  # Convert key to string
        cursor.execute('SELECT value FROM key_value_pairs WHERE key=?', (key_str,))
        row = cursor.fetchone()
        if row:
            return pickle.loads(row[0])
        else:
            print(f"Key '{key}' not found.")
            return None
    except Exception as e:
        print("Error retrieving data:", e)
        return None


def test_key_value_store():
    # Test adding data
    add("1", "Alice", 30)
    add("2", "Bob", 25)
    add("3", "Charlie", 35)

    # Test getting data
    assert get("1") == {"name": "Alice", "age": 30}
    assert get("2") == {"name": "Bob", "age": 25}
    assert get("3") == {"name": "Charlie", "age": 35}

    # Test updating data
    update("1", age=31)
    assert get("1") == {"name": "Alice", "age": 31}

    # Test removing data
    remove("2")
    assert get("2") is None

    # Test adding existing key
    add("1", "Eve", 28)  # Should print a message that key already exists

    # Test getting non-existent key
    assert get("4") is None  # Should print a message that key is not found


# Run the test
test_key_value_store()
