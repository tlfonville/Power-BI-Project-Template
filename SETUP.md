# Power BI Project Setup Guide

*This guide will help you quickly establish a project workflow for any Power BI project you are working on. It aims to standardize the team's PBI project workflow, implement quick documentation, and allow for better collaboration.*

> **Pro-tip:** Give an AI assistant a short description of your project (goals, data sources, audience) **plus the example files listed in [Section 4](#4-documentation)** and ask it to draft your documentation. Then review and trim.

---

## 🚀 Quick Start

### 1) Create Project Structure
Create these folders and files in your project directory (e.g., `/SDOPS/FolderYouWant/<your-project-name>` or anywhere in File Explorer):

```
your-project-name/
├── README.md
├── data/                 # Data files (add your CSV/Excel here)
│   ├── archive/          # Old data/backups (dated copies)
│   └── raw/              # Unclean raw exports
├── docs/
│   ├── metrics-dictionary.md
│   ├── dax-library.md
│   └── development-log.md
├── src/                  # Helper scripts (optional; Python/PowerShell)
└── projectname.pbix      # Your Power BI file
```

### 2) Copy Template Files
1. Paste the template contents into each file  
2. Replace `[placeholder text]` with real information  
3. Set dates to today’s date  
4. Add owner name and contact info

---

## 📋 Daily Workflow

### While Working
- Add/adjust measures in **`docs/dax-library.md`** (keep one measure per heading).
- Update KPI definitions in **`docs/metrics-dictionary.md`** as they evolve.
- Note issues, fixes, and decisions in **`docs/development-log.md`** (short bullets are fine).

### End of Day
1. Add a brief “what changed / what’s next” entry to **`docs/development-log.md`**  
2. If data changed:
   - Drop new raw into `data/raw/Raw_<Source>_<YYYY-MM-DD>.csv`
   - Overwrite your cleaned dataset (e.g., `data/ExampleData.csv`)
   - Move the prior cleaned file to `data/archive/ExampleData_<YYYY-MM-DD>.csv`

---

## 🛠️ Setup Details

### 3) Naming & Versioning
- **Dates:** Use ISO format `YYYY-MM-DD` (e.g., `2025-10-24`).
- **Clean dataset:** `data/ExampleData.csv` (the main data your PBIX points to).
- **Raw files:** `data/raw/Raw_<Source>_<YYYY-MM-DD>.csv` (never overwrite raw).
- **Archives:** Before replacing the clean file, copy the old one to `data/archive/ExampleData_<YYYY-MM-DD>.csv`.
- **PBIX backups (optional):** `projectname_YYYY-MM-DD.pbix` stored under `data/archive/` (if you keep dated PBIX copies).

### 4) Documentation
Start with these files (click to open/edit):
- [`README.md`](README.md)
- [`docs/dax-library.md`](docs/dax-library.md)
- [`docs/development-log.md`](docs/development-log.md)
- [`docs/metrics-dictionary.md`](docs/metrics-dictionary.md)

**Format preference:** Markdown is preferred (easy diffing, readable in any editor).  
**Plain text is OK** if that’s easier; consistency matters more than format.

**Convert plain text → Markdown (easy options):**
- **Pandoc (CLI):** `pandoc input.txt -o output.md`
- **Dillinger (web):** Online editor that exports to Markdown
- **VS Code:** Paste your text into a `.md` and use “Markdown All in One” for formatting help

### 5) Power BI Desktop — Quick Workflow
1. Save the report as `projectname.pbix` in the project root.  
2. Point data sources to `data/ExampleData.csv` (use relative paths if possible).  
3. Keep **staging queries** separate from **final model tables**.  
4. On updates, refresh the PBIX and validate key visuals/KPIs before sharing.

### 6) Publish & Refresh (if applicable)
- Publish to the agreed workspace.  
- Configure gateway/credentials if the dataset reads from shared drives.  
- Set and test a refresh schedule as needed.  
- Grant access per team policy.

### 7) Tooling (nice to have)
- **Power BI Desktop** (latest)  
- **VS Code** with:
  - *Markdown All in One* (Markdown productivity)
  - *GitLens* (if you later use Git)
  - *Python* (if you keep prep scripts in `src/`)

---

## 📝 Template Customization

**Replace these placeholders** across files:
- `[Your Name]`, `[Your Email]`, `[Date]`, `[Current Date]`
- In **README.md**: list stakeholders, primary data source(s), refresh approach
- In **metrics-dictionary.md**: confirm definitions, formulas, caveats
- In **dax-library.md**: include the core measures used on your report


---

## 🎯 Success Checklist

- [ ] Folder structure created and populated  
- [ ] `README.md` has owner, overview, and data/refresh notes  
- [ ] `docs/metrics-dictionary.md` started with core KPIs  
- [ ] `docs/dax-library.md` includes the first key measures  
- [ ] `docs/development-log.md` has first entries
- [ ] Stakeholders reviewed KPI definitions  
- [ ] Data model and key visuals validated  
- [ ] Routine for raw/clean/archive established
- [ ] DAX library growing and referenced by team  
- [ ] Docs consulted during changes/reviews  
- [ ] Process improvements identified and captured in the dev log

---

## 📚 Resources
- Power BI docs: https://learn.microsoft.com/power-bi/  
- DAX docs: https://learn.microsoft.com/dax/  
- Markdown basics: https://commonmark.org/help/tutorial/  
- Power BI Community: https://community.powerbi.com/  
- DAX Guide: https://dax.guide/

---

## Optional: Use GitHub for source control & collaboration

GitHub is **one** good way to track changes and collaborate (not required).

### A) GitHub Desktop (no terminal)
1. **GitHub Desktop** → *File* → **Add local repository…** → select your project folder  
2. Initialize when prompted  
3. **Publish repository**  
   - Name: `your-project-name`  
   - Visibility: Private (recommended)  
4. Use **Commit** (top left) and **Push origin** (top right) as you work

### B) Command Line (for devs)
```bash
cd /SDOPS/PowerBI/your-project-name

git init
git add .
git commit -m "feat: initial PBI project setup with documentation templates"

# Create an empty repo on GitHub (via website), then:
git branch -M main
git remote add origin https://github.com/<org-or-user>/<your-project-name>.git
git push -u origin main
```

### Daily Git (optional)
```bash
git add .
git commit -m "docs: update development log for <YYYY-MM-DD>"
git push
```

### Git Config (optional)
```bash
git config commit.template .gitmessage
```

### Suggested `.gitignore`
```
data/raw/
data/archive/
*.pbix.autosave
~$*.*
```

### Git Troubleshooting

- Git docs: https://git-scm.com/doc  
- GitHub docs: https://docs.github.com/
