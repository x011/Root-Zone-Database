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
