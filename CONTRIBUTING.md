# Contributing to Task Tracker API

Thank you for your interest in contributing to the Task Tracker API! This document provides guidelines and instructions for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/Task_Tracker_API.git`
3. Create a new branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Run tests to ensure everything works
6. Commit your changes: `git commit -m "Add your commit message"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a Pull Request

## Development Setup

1. Follow the installation instructions in the README.md
2. Install development dependencies: `pip install -r requirements.txt`
3. Set up pre-commit hooks (optional but recommended)

## Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Write docstrings for all functions, classes, and modules
- Format code with `black`: `black .`
- Lint with `flake8`: `flake8 src/`
- Type check with `mypy`: `mypy src/`

## Testing

- Write tests for new features
- Ensure all tests pass before submitting PR: `pytest`
- Aim for high test coverage
- Follow existing test patterns

## Commit Messages

- Use clear and descriptive commit messages
- Start with a verb in present tense (Add, Update, Fix, Remove, etc.)
- Keep the first line under 50 characters
- Add detailed description if needed

Example:
```
Add user profile endpoint

- Created new route for user profile
- Added profile schema
- Included tests for profile operations
```

## Pull Request Process

1. Update documentation if needed
2. Add tests for new features
3. Ensure all tests pass
4. Update CHANGELOG.md if applicable
5. Request review from maintainers

## Reporting Bugs

- Use GitHub Issues
- Provide detailed description
- Include steps to reproduce
- Specify your environment (OS, Python version, etc.)
- Include error messages and logs

## Feature Requests

- Use GitHub Issues
- Clearly describe the feature
- Explain the use case
- Discuss potential implementation

## Questions?

Feel free to open an issue for any questions or clarifications.

Thank you for contributing!
