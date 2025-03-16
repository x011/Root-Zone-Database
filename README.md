# Root Zone Database Updater

This project automatically retrieves and parses the IANA Root Zone Database webpage and updates a JSON file in the repository with the current top-level domain (TLD) data. The JSON file maps each TLD (with its leading dot) to its associated type and TLD manager information.

## Features

- **Automated Updates:**  
  Uses a Python script to fetch the [IANA Root Zone Database](https://www.iana.org/domains/root/db) page and extract the TLD information.
  
- **JSON Output:**  
  The extracted data is stored in a JSON file (`tld_data.json`) with the following structure:
  
  ```json
  {
      ".aaa": {
          "tld type": "generic",
          "tld manager": "American Automobile Association, Inc."
      },
      ".aarp": {
          "tld type": "generic",
          "tld manager": "AARP"
      }
      // More entries...
  }

Below is an example project description and README file you can include in your repository. You can adjust the content as needed.

---

**README.md**

```markdown
# Root Zone Database Updater

This project automatically retrieves and parses the IANA Root Zone Database webpage and updates a JSON file in the repository with the current top-level domain (TLD) data. The JSON file maps each TLD (with its leading dot) to its associated type and TLD manager information.

## Features

- **Automated Updates:**  
  Uses a Python script to fetch the [IANA Root Zone Database](https://www.iana.org/domains/root/db) page and extract the TLD information.
  
- **JSON Output:**  
  The extracted data is stored in a JSON file (`tld_data.json`) with the following structure:
  
  ```json
  {
      ".aaa": {
          "tld type": "generic",
          "tld manager": "American Automobile Association, Inc."
      },
      ".aarp": {
          "tld type": "generic",
          "tld manager": "AARP"
      }
      // More entries...
  }
  ```

- **GitHub Actions Integration:**  
  The project includes a GitHub Actions workflow that:
  - Runs on every push to the `main` (or `master`) branch.
  - Is scheduled to run periodically (every hour in the provided example).
  - (Optionally) Sends notifications via Slack if the workflow fails.

## File Structure

```
.
├── .github
│   └── workflows
│       └── update_tld.yml       # GitHub Actions workflow file
├── scripts
│   └── update_content.py        # Python script to fetch, parse, and update the JSON file
├── requirements.txt             # Python dependencies
├── tld_data.json                # Output JSON file with TLD information (auto-generated)
└── README.md                    # This file
```

## Setup and Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Root-Zone-Database.git
   cd Root-Zone-Database
   ```

2. **Install Dependencies:**

   The project requires Python (3.x) along with the `requests` and `beautifulsoup4` libraries. You can install them using pip:

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt` yet, create one with the following content:

   ```
   requests
   beautifulsoup4
   ```

## Running the Script Locally

You can test the script locally by running:

```bash
python scripts/update_content.py
```

This command fetches the latest TLD data from IANA, processes the webpage, and updates the `tld_data.json` file in the repository.

## GitHub Actions Workflow

The project includes a GitHub Actions workflow defined in `.github/workflows/update_tld.yml`. This workflow:

- **Triggers on:**
  - Every push to the repository's default branch.
  - A scheduled cron job (e.g., every hour).
  
- **Steps:**
  1. **Checkout Repository:** Retrieves the latest code.
  2. **Set Up Python:** Installs the desired Python version.
  3. **Install Dependencies:** Installs required libraries using `requirements.txt`.
  4. **Run Update Script:** Executes `scripts/update_content.py` to update the TLD data.
  5. **Optional Notification:** If configured, sends notifications (e.g., via Slack) when the workflow fails.

### Example Workflow Snippet

```yaml
name: Update TLD Data

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 * * * *'  # Adjust the schedule as needed

jobs:
  update-tld:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run TLD Update Script
        run: python scripts/update_content.py

  # Optional: Notify on failure using Slack
  notify-on-failure:
    needs: update-tld
    if: failure()
    runs-on: ubuntu-latest
    steps:
      - name: Send Slack notification on failure
        uses: slackapi/slack-github-action@v1.23.0
        with:
          payload: |
            {
              "text": "The TLD update workflow for repository `${{ github.repository }}` has failed. Please check the logs."
            }
        env:
          SLACK_BOT_TOKEN: ${{ secrets.SLACK_BOT_TOKEN }}
```

## Authentication Note

- **Personal Access Token (PAT):**  
  When pushing changes that include workflow files, GitHub requires that your PAT includes the `workflow` scope. If you encounter authentication issues, please generate a new PAT with the appropriate scopes and update your Git credentials.

- **SSH Alternative:**  
  Alternatively, you can set up SSH authentication to avoid HTTPS PAT issues.

## Troubleshooting

- **Workflow Failures:**  
  Check the **Actions** tab in your GitHub repository for detailed logs.
- **Authentication Issues:**  
  Ensure your PAT has the required scopes or consider switching to SSH.

## License

This project is licensed under the (GNU General Public License v3 (GPLv3))[https://www.gnu.org/licenses/gpl-3.0.en.html].

