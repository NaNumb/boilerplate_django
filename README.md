# Removing Git from a Project
## Instructions

### 1. Identify the `.git` Directory
Git stores all its data in a hidden folder named `.git` at the root of your project. 

**To see it in your terminal:**
- **Linux/macOS/WSL:** `ls -a`
- **Windows (PowerShell):** `dir -Force`

---

### 2. Remove the Directory

#### For Linux / macOS / WSL (Ubuntu, Arch, Fedora)
Run the following command from the root of your project:

```bash
rm -rf .git
