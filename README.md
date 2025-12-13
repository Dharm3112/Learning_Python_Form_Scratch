# Learning Python From Scratch

This repository documents my journey of learning Python from the ground up. It contains a collection of practice scripts, exercises, and mini-projects organized by topic, ranging from basic control flow to working with databases and APIs.

## 📂 Repository Structure

The projects are structured sequentially to reflect the learning path:

### 1\. Basics & Control Flow

  * **01\_Practice If Else Projects**: Scenarios involving conditional logic (e.g., Age Categorization, Ticket Pricing, Grading System).
  * **02\_Practice Loop Projects**: Exercises on iteration (e.g., Multiplication Tables, Factorial Calculator, String Reversal).

### 2\. Functions & Scope

  * **03\_Practice Function Problems**: Covers function syntax, parameters (args/kwargs), lambda functions, generators, and recursion.
  * **04\_Scopes**: Examples demonstrating local vs. global variable scope and closures.

### 3\. Object-Oriented Programming (OOP)

  * **05\_Object Oriented Programming**: Comprehensive examples of OOP principles:
      * Classes & Objects
      * Inheritance & Multiple Inheritance
      * Encapsulation (Private/Protected members)
      * Polymorphism
      * Static Methods & Class Variables

### 4\. Advanced Concepts

  * **06\_Decorators**: Practical implementation of decorators for timing functions, debugging calls, and caching return values.
  * **07\_Error\_Handling**: File I/O operations and exception handling.

### 5\. Real-World Applications & Data Persistence

This section features the **YouTube Manager App**, built in three different versions to demonstrate data persistence evolution:

1.  **File-based** (`07_Error_Handling/`): Stores video data in a simple `.txt` file.
2.  **SQLite** (`08_Database_sqlite3/`): Implements a relational database using Python's built-in `sqlite3` module.
3.  **MongoDB** (`10_Python_mongoDB/`): Connects to a MongoDB cluster using `pymongo` for NoSQL data storage.

### 6\. APIs

  * **09\_Handling\_Api's**: A script demonstrating how to fetch and process data from public APIs (e.g., random user generation) using the `requests` library.

## 🚀 Key Projects

### YouTube Manager App

A CLI-based application to manage a list of favorite YouTube videos (Add, Update, Delete, List).

  * **Version 1:** Uses standard File I/O (JSON format).
  * **Version 2:** Uses SQLite for local SQL storage.
  * **Version 3:** Uses MongoDB for cloud/NoSQL storage.

### Utility Scripts

  * **Password Strength Checker**: Evaluates password complexity.
  * **Exponential Backoff**: Simulates retry logic for network requests.
  * **FreeAPI Username Fetcher**: Fetches random user data from an external API.

## 🛠️ Getting Started

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Dharm3112/Learning_Python_Form_Scratch.git
    ```

2.  **Run a script:**
    Navigate to any folder and run the Python files. For example:

    ```bash
    cd "01_Practice If Else Projects"
    python 01_age_group_categourization.py
    ```

3.  **Dependencies:**
    Most scripts run on standard Python libraries. For the MongoDB and API projects, you may need to install external packages:

    ```bash
    pip install pymongo requests
    ```

*Created by [Dharm Patel](https://github.com/Dharm3112)*
