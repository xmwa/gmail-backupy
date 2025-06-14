#!/usr/bin/env python
# -*-  coding: utf-8 -*-

# Python 2/3 compatibility
from __future__ import print_function, unicode_literals
import sys
if sys.version_info[0] >= 3:
    unicode = str
    raw_input = input

#
#   Gmail Backup CLI - Simple Version
#   
#   Copyright © 2008, 2009, 2010 Jan Svec <honza.svec@gmail.com> and Filip Jurcicek <filip.jurcicek@gmail.com>
#   
#   This file is part of Gmail Backup.
#
#   Gmail Backup is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the Free
#   Software Foundation, either version 3 of the License, or (at your option)
#   any later version.
#
#   Gmail Backup is distributed in the hope that it will be useful, but WITHOUT
#   ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#   FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#   more details.
#
#   You should have received a copy of the GNU General Public License along
#   with Gmail Backup.  If not, see <http://www.gnu.org/licenses/
#
#   See LICENSE file for license details

import argparse
import os
from gmb import ConsoleNotifier, _convertTime, GMailBackup, GMB_REVISION, GMB_DATE, imap_decode, imap_encode

try:
    from hashlib import md5
except ImportError:
    from md5 import md5

GMB_CMD_REVISION = u'-Revision: 12348 -'
GMB_CMD_DATE = u'-Date: 2025-06-14 -'

GMB_CMD_REVISION = GMB_CMD_REVISION[11:-2]
GMB_CMD_DATE = GMB_CMD_DATE[7:-2].split()[0]
 
MAX_REVISION = str(max(int(GMB_CMD_REVISION), int(GMB_REVISION)))
MAX_DATE = max(GMB_CMD_DATE, GMB_DATE)

USAGE_TEXT = '''
Gmail Backup - Command Line Interface

DESCRIPTION:
Program for backup and restore of your GMail mailbox. You will need to activate
the IMAP access to your mailbox, to do so, please open your GMail settings and
under POP/IMAP tab activate this option.

EXAMPLES:
To perform full backup of your GMail account into directory dir, use:
  %(prog)s backup dir user@gmail.com password

To specify time interval, you can add additional date specification:
  %(prog)s backup dir user@gmail.com password --since 20070621 --before 20080101

To restore your backup use the restore command:
  %(prog)s restore dir user@gmail.com password

To use timestamp feature (stores date of last backup):
  %(prog)s backup dir user@gmail.com password --stamp

To clear mailbox (remove all messages):
  %(prog)s clear user@gmail.com password

To list mailbox information:
  %(prog)s list user@gmail.com password
'''

def backup_command(args):
    """Performs backup of your GMail mailbox"""
    notifier = ConsoleNotifier()
    
    where = ['ALL']
    if args.since:
        since = _convertTime(args.since)
        where.append('SINCE')
        where.append(since)
    if args.before:
        before = _convertTime(args.before)
        where.append('BEFORE')
        where.append(before)
    
    b = GMailBackup(args.username, args.password, notifier)
    b.backup(args.dirname, where, stamp=args.stamp)

def restore_command(args):
    """Performs restore of your previously backed up GMail mailbox"""
    notifier = ConsoleNotifier()
    b = GMailBackup(args.username, args.password, notifier)
    b.restore(args.dirname, args.since, args.before)

def clear_command(args):
    """Clear this GMail mailbox (remove all messages and labels)"""
    mailbox = raw_input("Do you want to delete all messages from your mailbox (%s)?\nPlease, repeat the name of your mailbox: " % args.username)
    if mailbox != args.username:
        print("Mailbox names doesn't match")
        return
    notifier = ConsoleNotifier()
    b = GMailBackup(args.username, args.password, notifier)
    b.clear()

def list_command(args):
    """List the names and number of messages of GMail IMAP mailboxes"""
    notifier = ConsoleNotifier()
    b = GMailBackup(args.username, args.password, notifier)
    for item, n_messages in b.list():
        print(item, imap_decode(item).encode('utf-8'), n_messages, ' '*8)

def version_command(args):
    """Show version information"""
    notifier = ConsoleNotifier()
    b = GMailBackup(None, None, notifier)
    b.reportNewVersion()

def main():
    parser = argparse.ArgumentParser(
        description='Gmail Backup - backup and restore Gmail mailboxes',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=USAGE_TEXT
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Backup command
    backup_parser = subparsers.add_parser('backup', help='Backup Gmail mailbox')
    backup_parser.add_argument('dirname', help='Directory to store backup')
    backup_parser.add_argument('username', help='Gmail username (user@gmail.com)')
    backup_parser.add_argument('password', help='Gmail password')
    backup_parser.add_argument('--since', help='Only emails since this date (YYYYMMDD)')
    backup_parser.add_argument('--before', help='Only emails before this date (YYYYMMDD)')
    backup_parser.add_argument('--stamp', action='store_true', help='Use timestamp feature')
    backup_parser.set_defaults(func=backup_command)
    
    # Restore command
    restore_parser = subparsers.add_parser('restore', help='Restore Gmail mailbox from backup')
    restore_parser.add_argument('dirname', help='Directory containing backup')
    restore_parser.add_argument('username', help='Gmail username (user@gmail.com)')
    restore_parser.add_argument('password', help='Gmail password')
    restore_parser.add_argument('--since', help='Only emails since this date (YYYYMMDD)')
    restore_parser.add_argument('--before', help='Only emails before this date (YYYYMMDD)')
    restore_parser.set_defaults(func=restore_command)
    
    # Clear command
    clear_parser = subparsers.add_parser('clear', help='Clear Gmail mailbox (delete all messages)')
    clear_parser.add_argument('username', help='Gmail username (user@gmail.com)')
    clear_parser.add_argument('password', help='Gmail password')
    clear_parser.set_defaults(func=clear_command)
    
    # List command
    list_parser = subparsers.add_parser('list', help='List Gmail mailbox information')
    list_parser.add_argument('username', help='Gmail username (user@gmail.com)')
    list_parser.add_argument('password', help='Gmail password')
    list_parser.set_defaults(func=list_command)
    
    # Version command
    version_parser = subparsers.add_parser('version', help='Show version information')
    version_parser.set_defaults(func=version_command)
    
    if len(sys.argv) == 1:
        parser.print_help()
        return
    
    args = parser.parse_args()
    
    try:
        args.func(args)
    except Exception as e:
        print("Error:", str(e))
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()