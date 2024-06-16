# Fetch leveldb key-value pair 

A test repo to fetch all the key-values stored on local via Chrome Storage API while running hello World! extension

**Note**: This code works for Linux Only


## Steps to Run the Project

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Devendra116/fetch-leveldb-key-pair.git
cd fetch-leveldb-key-pair
```

### 2. Install Dependencies
Install project dependencies using Poetry:

```bash
poetry install
```

### 3. Publish Your Extension on Chrome
Ensure you have enabled Developer Mode in Chrome:

- Open Chrome and go to `chrome://extensions/`.
- Enable Developer mode (usually a toggle switch at the top-right).
- Click on "Load unpacked" and select the directory `hello-world-extension`.


### 4. Update FetchLevelDBdata.py File
Update the FetchLevelDBdata.py script with your specific Chrome profile details:

- `USERNAME`: Replace with your Linux username.
- `CHROME_PROFILE`: Replace with your Chrome profile 
- `EXTENSION_ID`: Replace with your extension's ID found on chrome://extensions/ after loading it.

### 5. Run the Script
#### install dependencies:
```bash
poetry install 
```

#### Run Script:

```bash
poetry run python FetchLevelDBdata.py
```

## Note
- Make sure Chrome is closed to avoid database locking issues.
- Adjust paths to access Chrome's profile and extension data.