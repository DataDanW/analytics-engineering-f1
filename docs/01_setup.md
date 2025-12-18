# 📕Chapter 1 - Setup: Project, Git and Python virtual enviroment

In a real-world scenario it's highlight likely that your core data infrastructure is already setup for you. Plug and play if you will. 

However, for the first chapter of this project, the initial focus is on setting up a lightweight but realistic development environment to mirror how work is typically done in practice.

---

### GitHub
GitHub is used to version control code, document learning, and share project progress. It also acts as the public home for this project, including the README and longer-form write-ups via GitHub Pages.

### VS Code
VS Code is used as the primary development environment. It is free, open source, and widely adopted across data, analytics, and engineering teams. It supports Python development, Git integration, and terminal access in a single interface, making it well suited for end-to-end data projects.

---

#### Step 1: Project and Git setup

**What I did?**
- Created a dedicated Github repository for the project. This keeps the project self-contained and easily shareable.
- Cloned the repository locally using VS Code. This allows version control while building, enables branching and pull requests later on
- Setup a clear project structure and folder system to seperate source code, documentation and data.
- Added a .gitignore file to avoid commiting raw data files, the python virtual enviroment, secretes and temporary files. 

---
  
#### Step 2: Python environment setup
This setup is reproducable and can be recreated on any machine. At the time of writing this was setup on a work laptop but I will likely use other devices in the future, meaning I can move it to another machine later. This setup will align with real engineering workflows for familiarity and support automation.

**What I did?**
- Created a Python specific environment (.venv)
- Activated the environment for local development
- Installed required Python packages like Kaggle and 
- Made a requirements.txt file to lock in depandancies
- Ensured the virtual environment was ignored by Git 

  ---


## Some key terms and definitions

#### **Branching**
// 
Branching means you diverge from the main line of development and continue to do work without messing with that main line.

#### **Pull Request**
A pull request is a proposal to merge a set of changes from one branch into another.

#### **Cloning a repo locally**
We do this because the code has to run somewhere. We clone repositories locally so we can run, test, and version-control code efficiently; the disk footprint stays small because data and environments are deliberately excluded.

#### **Python virtual environment PENV**
A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.

#### **Commit**
A commit is like a save point in your project. It records a snapshot of your files at a certain time, with a message describing what was changed.

#### **Secrets**
GitHub secrets are used to securely store sensitive information like API keys, tokens, and passwords in repositories
