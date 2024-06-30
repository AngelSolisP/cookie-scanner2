https://cookie-scanner2.vercel.app/


---

# Cookie Scanner

Cookie Scanner is a web application that allows users to enter a URL and view the cookies that the specified site collects. This tool is useful for web developers, privacy enthusiasts, and anyone interested in understanding the cookies used by different websites.

## Features

- **URL Input**: Enter any URL to scan for cookies.
- **Cookie Display**: View detailed information about each cookie collected by the site.
- **Privacy Insights**: Understand what kind of data is being collected and how it might be used.
- **User-Friendly Interface**: Easy-to-use interface for quick and efficient scanning.

## Installation

To run Cookie Scanner locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   https://github.com/AngelSolisP/cookie-scanner2.git
   cd cookie-scanner2
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

## Usage

1. Open your web browser and navigate to `http://localhost:5000`.
2. Enter the URL of the site you want to scan in the input field.
3. Click the "Scan" button to initiate the scan.
4. View the cookies collected by the site along with detailed information such as name, value, domain, path, expiry, and secure flag.

## Example

Here's an example of how the Cookie Scanner works:

1. Enter the URL (e.g., `https://example.com`).
2. Click "Scan".
3. The app displays the list of cookies with details:
   - **Name**: SessionID
   - **Value**: abc123xyz
   - **Domain**: example.com
   - **Path**: /
   - **Expiry**: Session
   - **Secure**: True



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or feedback, please feel free to reach out:

- **Email**: angel.solis.p@gmail.com
- **GitHub**: https://github.com/AngelSolisP/

---

Feel free to customize this README to better fit your specific application and needs.
