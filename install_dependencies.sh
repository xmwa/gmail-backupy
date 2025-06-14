#!/bin/bash
# Gmail Backup Dependencies Installation Script
# Supports both Python 2.7 and Python 3.x

echo "Gmail Backup - Dependencies Installation"
echo "========================================"

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to install wxPython for a specific Python version
install_wxpython() {
    local python_cmd="$1"
    local python_name="$2"
    
    echo ""
    echo "Installing wxPython for $python_name..."
    echo "Command: $python_cmd -m pip install wxPython"
    
    # Try normal installation first
    if $python_cmd -m pip install wxPython; then
        echo "✓ wxPython installed successfully for $python_name"
        return 0
    else
        echo "⚠ Normal installation failed, trying alternative methods..."
        
        # Try with --break-system-packages for Python 3 if needed
        if [[ "$python_cmd" == python3* ]]; then
            echo "Trying: $python_cmd -m pip install --break-system-packages wxPython"
            if $python_cmd -m pip install --break-system-packages wxPython; then
                echo "✓ wxPython installed successfully for $python_name (with --break-system-packages)"
                return 0
            fi
        fi
        
        # Try with proxy bypass if still failing
        echo "Trying with proxy bypass..."
        if NO_PROXY="*" HTTP_PROXY="" HTTPS_PROXY="" $python_cmd -m pip install wxPython; then
            echo "✓ wxPython installed successfully for $python_name (with proxy bypass)"
            return 0
        elif [[ "$python_cmd" == python3* ]]; then
            if NO_PROXY="*" HTTP_PROXY="" HTTPS_PROXY="" $python_cmd -m pip install --break-system-packages wxPython; then
                echo "✓ wxPython installed successfully for $python_name (with proxy bypass and --break-system-packages)"
                return 0
            fi
        fi
        
        echo "✗ Failed to install wxPython for $python_name"
        return 1
    fi
}

# Function to test if wxPython works
test_wxpython() {
    local python_cmd="$1"
    local python_name="$2"
    
    if $python_cmd -c "import wx; print('wxPython test successful for $python_name')" 2>/dev/null; then
        echo "✓ wxPython is working for $python_name"
        return 0
    else
        echo "✗ wxPython test failed for $python_name"
        return 1
    fi
}

# Check available Python versions
echo ""
echo "Checking available Python versions..."

PYTHON2_CMD=""
PYTHON3_CMD=""

if command_exists python2.7; then
    PYTHON2_CMD="python2.7"
elif command_exists python2; then
    PYTHON2_CMD="python2"
elif command_exists python; then
    # Check if it's Python 2
    if python -c "import sys; exit(0 if sys.version_info[0] == 2 else 1)" 2>/dev/null; then
        PYTHON2_CMD="python"
    fi
fi

if command_exists python3.12; then
    PYTHON3_CMD="python3.12"
elif command_exists python3; then
    PYTHON3_CMD="python3"
fi

echo ""
echo "Python versions found:"
[[ -n "$PYTHON2_CMD" ]] && echo "  Python 2: $PYTHON2_CMD ($($PYTHON2_CMD --version 2>&1))" || echo "  Python 2: Not found"
[[ -n "$PYTHON3_CMD" ]] && echo "  Python 3: $PYTHON3_CMD ($($PYTHON3_CMD --version 2>&1))" || echo "  Python 3: Not found"

if [[ -z "$PYTHON2_CMD" && -z "$PYTHON3_CMD" ]]; then
    echo "ERROR: No Python installation found!"
    exit 1
fi

# Install wxPython for available Python versions
INSTALL_SUCCESS=0

if [[ -n "$PYTHON2_CMD" ]]; then
    echo ""
    echo "=== Installing for Python 2 ==="
    if ! test_wxpython "$PYTHON2_CMD" "Python 2"; then
        if install_wxpython "$PYTHON2_CMD" "Python 2"; then
            INSTALL_SUCCESS=1
        fi
    else
        echo "✓ wxPython already working for Python 2"
        INSTALL_SUCCESS=1
    fi
fi

if [[ -n "$PYTHON3_CMD" ]]; then
    echo ""
    echo "=== Installing for Python 3 ==="
    if ! test_wxpython "$PYTHON3_CMD" "Python 3"; then
        if install_wxpython "$PYTHON3_CMD" "Python 3"; then
            INSTALL_SUCCESS=1
        fi
    else
        echo "✓ wxPython already working for Python 3"
        INSTALL_SUCCESS=1
    fi
fi

# Final test
echo ""
echo "=== Final Verification ==="

if [[ -n "$PYTHON2_CMD" ]]; then
    test_wxpython "$PYTHON2_CMD" "Python 2"
fi

if [[ -n "$PYTHON3_CMD" ]]; then
    test_wxpython "$PYTHON3_CMD" "Python 3"
fi

echo ""
echo "=== Installation Complete ==="

if [[ $INSTALL_SUCCESS -eq 1 ]]; then
    echo "✓ Dependencies installed! You can now run Gmail Backup:"
    echo ""
    [[ -n "$PYTHON2_CMD" ]] && echo "  $PYTHON2_CMD gmail-backup-gui.py  # GUI mode"
    [[ -n "$PYTHON2_CMD" ]] && echo "  $PYTHON2_CMD gmail-backup.py --help     # CLI mode"
    [[ -n "$PYTHON3_CMD" ]] && echo "  $PYTHON3_CMD gmail-backup-gui.py  # GUI mode"
    [[ -n "$PYTHON3_CMD" ]] && echo "  $PYTHON3_CMD gmail-backup.py --help     # CLI mode"
else
    echo "⚠ Some installations may have failed. Try running the GUI script to see specific error messages."
fi