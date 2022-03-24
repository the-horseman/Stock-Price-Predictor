from git import Repo
from datetime import datetime
import os

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

Path_of_Repo = os.path.dirname(os.path.realpath(__file__)) + "/.git"
repo = Repo(Path_of_Repo)
repo.git.add(all=True)
repo.index.commit("Data Automation Commit for " + dt_string)
origin = repo.remote(name='origin')
origin.push()