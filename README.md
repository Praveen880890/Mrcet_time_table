# Malla Reddy College of Engineering and Technology Timetable Display

This Python application is designed to display the timetable for Malla Reddy College of Engineering and Technology's Department of Emerging Technologies. It reads data from an Excel file (`tables.xlsx`) and dynamically updates the current period and subject information for different years and sections.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Application Features](#application-features)
- [Code Structure](#code-structure)
- [Output](#output)

## Introduction

This application provides a real-time representation of the college timetable for different years (2nd, 3rd, and 4th) and sections. It updates the current period, subject, and teacher information based on the current time and day of the week. The timetable data is stored in the `tables.xlsx` Excel file and is read dynamically by the application.

## Requirements

Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- Pandas library (`pip install pandas`)
- PySimpleGUI library (`pip install PySimpleGUI`)

## Usage

To run the application, execute the `app.py` script:

```bash
python app.py
```

This will launch the timetable display window, showing the current period, subject, and teacher for the specified year and section.

## Application Features

- **Dynamic Timetable Display**: The application reads timetable data from the `tables.xlsx` file and displays the current period, subject, and teacher information for different years and sections.

- **Theme Customization**: Users can switch between different themes (color schemes) by right-clicking on the title bar and selecting a theme from the menu.

- **Real-Time Updates**: The application updates the displayed information based on the current time and day of the week. It also indicates the current day (e.g., MON, TUES) at the top.

## Code Structure

The code is organized into multiple files for better modularity:

- `app.py`: The main script that creates the PySimpleGUI window, handles events, and updates the timetable based on the current time.

- `excel_test.py`: A module for reading timetable data from the `tables.xlsx` file and organizing it into data frames for different years and sections.

- `sdef.py`: A module containing functions to play sound or text-to-speech notifications for each period (currently commented out).

## Output
