import os
from invoke import task

@task
def init(c):
    """
    Inicializa el proyecto Flask.
    """
    is_windows = os.name == 'nt'

    if is_windows:
        c.run(r'venv\Scripts\activate')
        c.run('set FLASK_APP=index.py') 
    else:
        c.run('source venv/bin/activate')
        c.run('export FLASK_APP=index.py') 

       

    c.run('pip install -r requirements.txt')

    c.run('flask --app app run')