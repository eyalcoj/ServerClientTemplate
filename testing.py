import pickle
import sqlite3

# Create/connect to a SQLite database
conn = sqlite3.connect('key_value_store.db')
cursor = conn.cursor()

# Create a table to store key-value pairs
cursor.execute('''CREATE TABLE IF NOT EXISTS key_value_pairs
                  (key TEXT PRIMARY KEY, value BLOB)''')
conn.commit()


# Function to add objects to a key
def add(key, name, age):
    try:
        key_str = str(key)  # Convert key to string
        data = pickle.dumps({"name": name, "age": age})
        cursor.execute('INSERT OR REPLACE INTO key_value_pairs VALUES (?, ?)', (key_str, data))
        conn.commit()
    except Exception as e:
        print("Error adding data:", e)


# Function to remove a key and its associated data
def remove(key):
    try:
        key_str = str(key)  # Convert key to string
        cursor.execute('DELETE FROM key_value_pairs WHERE key=?', (key_str,))
        conn.commit()
    except Exception as e:
        print("Error removing data:", e)


# Function to update objects associated with a key
def update(key, name=None, age=None):
    try:
        key_str = str(key)  # Convert key to string
        new_dict = get(key_str)
        if name:
            new_dict["name"] = name
        if age:
            new_dict["age"] = age

        data = pickle.dumps(new_dict)
        cursor.execute('INSERT OR REPLACE INTO key_value_pairs VALUES (?, ?)', (key_str, data))
        conn.commit()
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
            return None
    except Exception as e:
        print("Error retrieving data:", e)
        return None


obj1 = ExampleObject("John", 30)
obj2 = ExampleObject("Alice", 25)

add(123, "shalom", 25)  # Integer key

retrieved_objects = get(123)
print(retrieved_objects["name"])
print(retrieved_objects["age"])

remove(123)

conn.close()
