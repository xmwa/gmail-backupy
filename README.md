# Python Compatibility Update

This repository has been updated to maintain compatibility with modern Python versions. The original code was last updated over 10 years ago, and this update aims to:

1. Ensure the core backup and restore functionality works with current Python releases
2. Support both GUI and command-line operation modes
3. Preserve the original functionality while modernizing the codebase

## Requirements

- Python 3.8+ (tested up to Python 3.12)
- Required packages are listed in requirements.txt

## Running the Application

The most straightforward way to use Gmail Backup is through its graphical interface:

1. Retrieve your Gmail application-specific password from [Google Account Settings](https://myaccount.google.com/apppasswords)
2. Run the application: `python3 gmail-backup-gui.py`
3. Follow the on-screen instructions to log in to your Gmail account and select the desired backup options.

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
