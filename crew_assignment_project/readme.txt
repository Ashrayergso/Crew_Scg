# Crew Assignment Project

This Django-based web application automates the assignment of crew members to ships. It considers various factors such as crew position, contract duration, and vacation time for optimal assignment, promoting efficiency and reducing errors in crew scheduling.

## Tech Stack

- Django framework for building the application
- PostgreSQL for the database
- Python, Django, and Conda for Python environment isolation

## Project Focus

The primary focus of the project is to automate crew scheduling, thereby increasing efficiency and reducing errors.

## Core Feature

The core feature of the application is the `assignCrewToShips` function, which automates the assignment of crew to ships.

## Data Models

The Django models included are:

- CrewMember
- Cert
- Qualification
- Ship
- Positions
- Assignment
- ShipCrewAllowance

## UI Components

UI components include Django templates for each view, with CSS and JavaScript files in the static directory for styling and interactivity.

## Backend

The backend is built using Django. It contains models, views for each model, and URL patterns for each view. Django REST framework can be used if API endpoints are needed.

## Frontend

The frontend is built using Django's template system, complemented with CSS for styling and JavaScript for interactivity.

## URL Configuration

The URL configuration defines the views and maps URLs to them.

## UI Design

The user interface is clean and intuitive, with a main navigation bar for accessing different views. Each data model has its own list/detail view, presented in a table format for easy readability. The overall design is modern and professional, with a consistent color scheme and typography.

## Requirements

- Develop the `assignCrewToShips` function for automatic crew-to-ship assignment.
- Create list/detail views for each data model.
- Create views to create/edit assignments.
- Create views to filter/sort ship and crew lists.

## Messages

The application uses Django's messaging framework to display messages like:

- "CREW_FETCH_SUCCESS": Displayed when the crew members are successfully fetched from the database.
- "SHIP_FETCH_SUCCESS": Displayed when the ships are successfully fetched from the database.
- "ASSIGNMENT_SUCCESS": Displayed when a new assignment is successfully created.
- "ASSIGNMENT_FAILURE": Displayed when there is an error creating a new assignment.

## Setup and Installation

Please refer to `instructions.txt` for setup and installation instructions.

## Dependencies

Please refer to `requirements.txt` for a list of dependencies required for this project.

## Important Notes

- Review code and ensure the `settings.py`, `urls.py` for both project and app are set up correctly.
- Ensure that `instructions.txt`, `requirements.txt`, `readme.txt` are created.
- Ensure that forms are created and referenced properly.