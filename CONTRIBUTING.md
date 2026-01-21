# Contributing to Python Web Crawler

Thank you for your interest in contributing to Python Web Crawler! This document provides guidelines for contributors.

## 🤝 How to Contribute

### Reporting Bugs

- Use [issue tracker](https://github.com/Shubhamji038/websit-crawler/issues) to report bugs
- Provide detailed information about the bug
- Include steps to reproduce the issue
- Add relevant error messages and screenshots if applicable

### Suggesting Features

- Open an issue with the "enhancement" label
- Describe the feature in detail
- Explain why it would be useful
- Consider if it fits the project's scope

### Code Contributions

1. **Fork** repository
   ```bash
   git clone https://github.com/Shubhamji038/websit-crawler.git
   cd websit-crawler
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation if needed

4. **Run tests**
   ```bash
   make test
   make lint
   ```

5. **Commit your changes**
   ```bash
   git commit -m "feat: add your feature description"
   ```

6. **Push and create a pull request**
   ```bash
   git push origin feature/your-feature-name
   ```

## 📝 Code Style

- Follow PEP 8 guidelines
- Use descriptive variable and function names
- Add docstrings to new functions and classes
- Keep lines under 88 characters (Black formatter)

## 🧪 Testing

- Write unit tests for new functionality
- Ensure all tests pass before submitting
- Add integration tests if applicable
- Test edge cases and error conditions

## 📚 Documentation

- Update README.md for user-facing changes
- Add inline comments for complex logic
- Update docstrings for API changes
- Consider adding examples for new features

## 🏷️ Commit Message Format

Use conventional commit messages:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `style:` for code style changes
- `refactor:` for code refactoring
- `test:` for test-related changes
- `chore:` for maintenance tasks

Example:
```
feat: add proxy support for HTTP requests
```

## 🚀 Development Setup

1. Clone your fork
2. Install dependencies:
   ```bash
   make install-dev
   ```
3. Set up pre-commit hooks (optional)
4. Run tests to verify setup:
   ```bash
   make test
   ```

## 📋 Pull Request Process

1. Ensure your PR description clearly describes the changes
2. Link any relevant issues
3. Include screenshots for UI changes
4. Wait for code review
5. Address feedback promptly
6. Maintain clean commit history

## 🎯 Project Goals

- Provide a user-friendly web crawling solution
- Maintain clean, well-documented code
- Support both beginners and advanced users
- Ensure cross-platform compatibility

## ❓ Questions?

- Check existing issues and discussions
- Create a new issue with the "question" label
- Join discussions in existing issues

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to Python Web Crawler! 🎉
