#!/bin/bash
# Setup script for Task Tracker API

echo "Setting up Task Tracker API..."

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "Please update .env with your configuration"
fi

echo "Setup complete!"
echo "To activate the virtual environment, run: source venv/bin/activate"
echo "To start the application, run: python main.py"
