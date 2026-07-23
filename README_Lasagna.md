# 🍕 Guido's Gorgeous Lasagna

> **Exercism Python Track** | *Basics & Functions*

## 📌 Problem Overview
This exercise covers the foundational concepts of Python programming: defining functions, accepting arguments, returning values, using module-level constants to avoid magic numbers, and documenting code using standard Python `"""docstrings"""`.

The objective is to write helper functions to calculate cooking times for baking a lasagna based on the number of layers and elapsed bake time.

---

## 🛠️ Concepts & Skills Practiced

* **Functions (`def`):** Defining reusable blocks of code with single or multiple parameters.
* **Return Statements (`return`):** Returning calculated numerical results back to the caller.
* **Constants:** Defining `EXPECTED_BAKE_TIME` and `PREPARATION_TIME` at the top level to avoid hardcoded "magic numbers".
* **Function Composition:** Calling one function (`preparation_time_in_minutes`) inside another (`elapsed_time_in_minutes`) to keep code modular and readable.
* **Docstrings:** Writing standard PEP 257-compliant docstrings detailing function parameters, return types, and operational behavior.

---

## 💻 Functions Implemented

| Function | Parameters | Description |
| :--- | :--- | :--- |
| `bake_time_remaining()` | `elapsed_bake_time` (int) | Calculates remaining bake time by subtracting elapsed time from `EXPECTED_BAKE_TIME` (40 mins). |
| `preparation_time_in_minutes()` | `number_of_layers` (int) | Calculates prep time by multiplying layers by `PREPARATION_TIME` (2 mins/layer). |
| `elapsed_time_in_minutes()` | `number_of_layers` (int), `elapsed_bake_time` (int) | Calculates total elapsed cooking time by combining total prep time and elapsed bake time. |

---

## 📁 File Structure

```text
lasagna/
├── README.md      # Problem statement, concepts, and implementation details
└── lasagna.py     # Completed Python solution
