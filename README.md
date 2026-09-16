
* **Overview:** 
  * Call a openai model from a simple python code.
* **Prerequisites:**
  * Ensure you have `Python 3 or Python 3.11` installed on your machine.
  * Pre-req mentioned in the requirement.txt
* **Installation & Setup:**
  * Clone the repository: `git clone https://github.com/your-username/your-repo.git`
  * Navigate to the project directory: `cd your-repo-name`
  * Install required dependencies: `[e.g., pip install -r requirements.txt OR npm install]`
* **Environment Configuration:**
  * Create a `.env` file in the root directory.
  * Add the required environment variables:
    * `API_KEY=your_api_key_here`
    * `DATABASE_URL=your_database_url_here`
* **1.- How to Execute the Code:**
  * Run the main script using the following command: 
  	> python3.11 main.py "hi" ## Here "hi" is your argument
  * NOTE: Pass your input in the first argument
* **2.- How to Execute the Code:**
  * Run the main script using the following command: 
  	> python3.11 main.py "Answer the question using only the document below.

> Document: The local train starts at 3AM everyday, it reach the destination by 9AM on the same day.
> This is the daily routine and no gaps.

> Question: What time the train starts? and travel duration?"

  * NOTE: Passing a document in the input and asking question from it
* **Expected Output from the 2nd exeuction:**
	Based on the document provided:
	* **Start time:** 3AM
	* **Travel duration:** 6 hours (from 3AM to 9AM)


***


# About the code structure
##### 1. Folder structure
my-ai-project/
│
├── .env
├── .gitignore
├── requirements.txt
│
└── src/
    ├── __init__.py
    └── main.py

##### 2. .env
MY_API_KEY=your_groq_api_key_here
MY_BASE_URL=your_base_url

##### 3. .gitignore
.env
.venv/
__pycache__/
*.pyc

##### 4. requirements.txt
openai
python-dotenv

##### 5 __init__.py
from . import agent

# To start
##### 1. Create virtual env
cd path/to/your/project_folder 
python3.11 -m venv .venv

##### 2. source .venv/bin/activate

##### 3. To Install the packages    
	pip install -r requirements.txt

##### 4. To execute (pass input as the first parameter)
cd path/to/your/project_folder/src -->  
python3.11 main.py "hi"*

# How it works
.env
 │
 │ GROQ_API_KEY
 │ GROQ_BASE_URL
 ↓
main.py
 │
 │ load_dotenv()
 ↓
os.environ
 │
 ↓
OpenAI Python SDK
 │
 │ base_url = Groq
 ↓
Groq API



=======
>>>>>>> 2ae6b822d8a81728115d64c37ba4357f3da046bc
