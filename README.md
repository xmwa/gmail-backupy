# Gmail Backup - Python 2.7 & 3.12 Compatible

This repository has been updated to maintain full compatibility with both Python 2.7 and Python 3.12. The original code was last updated over 10 years ago, and this update aims to:

1. **Full Python 2.7 & 3.12 compatibility** - Both GUI and CLI work seamlessly
2. **Preserve original functionality** - All backup, restore, and migration features maintained
3. **Modern interface improvements** - Better error messages and installation guidance
4. **Enhanced dependency management** - Automated installation scripts included

## Requirements

### Python Versions
- **Python 2.7** (fully supported)
- **Python 3.8+** (tested up to Python 3.12)

### Dependencies
- **wxPython** (for GUI mode) - automatically prompted for installation
- **Standard library modules** (imaplib, email, etc.) - included with Python

## Quick Start

### 1. Install Dependencies (if needed)
```bash
# Automated installation (recommended)
./install_dependencies.sh

# Manual installation
python -m pip install wxPython      # For Python 2.7
python3 -m pip install wxPython     # For Python 3.x
```

### 2. Running the Application

#### GUI Mode (Recommended)
```bash
# Python 2.7
python gmail-backup-gui.py

# Python 3.12
python3 gmail-backup-gui.py
```

#### Command Line Mode
```bash
# Backup
python gmail-backup.py backup /path/to/backup user@gmail.com password

# Restore
python gmail-backup.py restore /path/to/backup user@gmail.com password

# List mailboxes
python gmail-backup.py list user@gmail.com password

# Get help
python gmail-backup.py --help
```

### 3. Gmail Setup
1. Enable 2-factor authentication in your Google Account
2. Generate an app-specific password at [Google Account Settings](https://myaccount.google.com/apppasswords)
3. Use the app-specific password (not your regular password) in Gmail Backup

## Compatibility Features

- **Python 2/3 print statements** - Uses `from __future__ import print_function`
- **Unicode handling** - Automatic Python 2/3 unicode compatibility
- **wxPython versions** - Works with both old and new wxPython APIs
- **Threading compatibility** - Handles `is_alive()` vs `isAlive()` differences
- **Installation guidance** - Clear, specific installation instructions with multiple options

## Files

- **`gmail-backup-gui.py`** - Graphical user interface (Python 2.7 & 3.12 compatible)
- **`gmail-backup.py`** - Command-line interface (Python 2.7 & 3.12 compatible) 
- **`install_dependencies.sh`** - Automated dependency installation script
- **`gmail-backup-original.py`** - Original complex framework (Python 2 only)
- **`gmb.py`** - Core Gmail backup functionality library

# Original README

About:
======
Gmail Backup allows to backup and restore the content of your Gmail account. It
uses the IMAP protocol to fetch and store your messages. It can also be used to
migrate your messages between two accounts, for example between your private
inbox and the Google Apps acount.

This project contains the open sourced code of Gmail Backup
(hosted at www.gmail-backup.com).


Authors:
========
Jan Svec        <honza.svec@gmail.com>
Filip Jurčíček  <filip.jurcicek@gmail.com> 


Homepage:
=========

You can always get the newest version of Gmail Backup from our website hosted
at Google Code:

http://code.google.com/p/gmail-backup-com/


License:
========

Copyright © 2008, 2009, 2010 Jan Svec <honza.svec@gmail.com> and Filip Jurcicek <filip.jurcicek@gmail.com>

Gmail Backup is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

Gmail Backup is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
Gmail Backup.  If not, see <http://www.gnu.org/licenses/

See LICENSE file for license details
