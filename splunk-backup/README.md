# See the Usage Section in each .py file to see what the code does

# 1. Create virtual python env
```bash
python -m venv venv && source venv/bin/activate #Linux
python -m venv venv && \venv\Scripts\activate #Windows
```

### Creates virtual python environment 
```bash
python -m venv venv 
```

### Steps into virtual environment 
```bash
source .venv/bin/activate
```

### See the terminal now has the name of your virtual environment
```bash
(venv) drew@Andrews-MacBook-Pro% 
```

### To Step out of the virtual environment 
```bash
deactivate
```

# 2. Install dependencies (Inside of Virtual environment)
```bash
pip install -r requirements.txt --use-pep517
```

# 3 Run the Code
```bash
python <file_name.py>
```

# TROUBLESHOOTING
```bash
pip list
python --version 
pip --version
This Script has been tested on mac using Python 3.10.10 
```

```plain text
If trying to do this with VS CODE ensure you have your files open on the left side aka the workspace 

Command+shift+p select interpreter and chose .venv/bin python
```

## Documentation 
Docs about backup
 - Indexed data (bcukets) http://docs.splunk.com/Documentation/Splunk/6.5.0/Indexer/Backupindexeddata
 - Configuration (etc) http://docs.splunk.com/Documentation/Splunk/6.5.0/Admin/Backupconfigurations