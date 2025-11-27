# 💰 Personal Expense Tracker

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📌 Project Overview
The **Personal Expense Tracker** is a command-line interface (CLI) application built in Python. It is designed to help users manage their finances efficiently by logging daily expenses, categorization, and viewing spending summaries.

This project focuses on the practical application of **data structures (dictionaries/lists)**, **file handling (JSON)**, and **modular programming**.

## 🚀 Features
* **Add Expenses:** Log new expenses with an amount, category, and automatic date stamping.
* **View Summaries:**
    * View total spending across all categories.
    * View a breakdown of spending by specific categories (e.g., Food, Transport).
    * View a chronological history of all transactions.
* **Data Persistence:** All data is saved to `expenses.json`, ensuring records are not lost when the program is closed.
* **User-Friendly Interface:** A clean, interactive menu for easy navigation.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Modules Used:**
    * `json` (Data storage and retrieval)
    * `os` (File existence checks)
    * `datetime` (Date handling)

## ⚙️ How to Run
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/personal-expense-tracker.git](https://github.com/your-username/personal-expense-tracker.git)
    ```
2.  **Navigate to the directory:**
    ```bash
    cd personal-expense-tracker
    ```
3.  **Run the application:**
    ```bash
    python expense_tracker.py
    ```

## 🖥️ Usage Example
```text
--- MAIN MENU ---
1. Add an Expense
2. View Summaries
3. Save & Exit
Select an option (1-3): 1

--- Add New Expense ---
Enter amount: $ 50
Enter category: Food
Expense of $50.0 added for Food on 2024-11-27.
