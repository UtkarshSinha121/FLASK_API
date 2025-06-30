# 🚀 Flask Project Setup Guide (with `venv` and GitHub)

This guide explains how to set up a Flask project using a virtual environment (`venv`), manage dependencies, and push your project to GitHub.

---

## 📦 Why Use `venv`?

- Isolates dependencies for each project.
- Prevents conflicts between package versions.
- Keeps system Python clean.
- Makes it easy to share dependencies using `requirements.txt`.

---

## ⚙️ Setting Up `venv` in Flask Project

### ✅ Create Virtual Environment
```bash
python -m venv venv
```

### ✅ Activate the Environment

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### ✅ Install Flask
```bash
pip install flask
```

### ✅ Save Dependencies
```bash
pip freeze > requirements.txt
```

### ✅ Deactivate When Done
```bash
deactivate
```

---

## ❗ What If You Don't Use `venv`?

- Shared global packages → version conflicts.
- One project's packages may break another.
- Harder to reproduce environment for teammates or deployment.

---

## 💻 Using `venv` in VS Code

1. Open your project folder in VS Code.
2. Open Terminal (`Ctrl + \``).
3. Run:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment (see above).
5. Open Command Palette → `Python: Select Interpreter` → choose the `venv` one.

---

## ➡️ Note About Redirection (`>`)

- This is **not** a right arrow `→` — it's a shell operator.
- Used like this:
  ```bash
  pip freeze > requirements.txt
  ```
  It writes the output to a file.

---

## 🗃️ Pushing Project to GitHub

### 1. Initialize Git
```bash
git init
```

### 2. Add a `.gitignore` File (in project root)
```gitignore
venv/
__pycache__/
*.pyc
.env
```

### 3. Commit Your Code
```bash
git add .
git commit -m "Initial commit"
```

### 4. Create GitHub Repo

1. Go to [https://github.com](https://github.com)
2. Click **New repository**
3. Name your repo
4. ❌ Don’t initialize with README (you already have files)
5. Click **Create**

### 5. Link to Remote Repo
```bash
git remote add origin https://github.com/your-username/your-repo.git
git branch -M main
git push -u origin main
```

### 6. Verify Connection
```bash
git remote -v
```

---

## ✅ Summary

| Task                     | Use `venv`? | Global? | Notes                                  |
|--------------------------|-------------|---------|----------------------------------------|
| Python packages (Flask)  | ✅ Yes       | ❌ No   | Install inside `venv`                  |
| Git installation         | ❌ No        | ✅ Yes  | Git is system-level, not Python-based  |
| `.gitignore` file        | ✅ Yes       |         | Place in project root, not in `venv`   |
| Git commands             | ✅ Yes       |         | Can run with or without `venv` active  |

---

Happy Coding! ✨
