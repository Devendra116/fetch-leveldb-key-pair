import plyvel

username='USERNAME' # add your local username
chrome_profile = 'CHROME_PROFILE' # add your chrome profile
extension_id = 'EXTENSION_ID'  # add your extension ID 

leveldb_path = f'/home/{username}/.config/google-chrome/{chrome_profile}/Local Extension Settings/{extension_id}'


def fetch_all_values_from_leveldb():
    try:
        db = plyvel.DB(leveldb_path, create_if_missing=False)
        values = {}
        with db.iterator() as it:
            for key, value in it:
                values[key.decode('utf-8')] = value.decode('utf-8')
        db.close()
        return values
    except Exception as e:
        print(f"Error fetching values from LevelDB: {e}")
        return None

def main():
    all_values = fetch_all_values_from_leveldb()
    if all_values:
        print("Successfully fetched all key-value pairs from LevelDB:")
        for key, value in all_values.items():
            print(f"{key}: {value}")
    else:
        print("Failed to fetch values from LevelDB.")

if __name__ == "__main__":
    main()