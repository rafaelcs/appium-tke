## Project Structure

- `conftest.py`: Contains all the Appium configuration settings.
- `tests/`: Directory containing all test cases.
- `screens/`: Directory for screen object classes representing the screens in the app.
- `requirements.txt`: List of dependencies required to run the tests.

### Prerequisites
- Python 3.x
- Appium 2.11
- Android SDK
- Node.js 

### Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Tests

1. Ensure Appium server is running with the --relaxed-security flag (to run ADB commands):
```bash
appium --relaxed-security
```
2. To execute all tests:
```bash
pytest -s tests
```
