
# NASA APOD Web Application

This web application is designed to display the Astronomy Picture of the Day (APOD) provided by NASA. Users can select a specific date or a range of dates to view the corresponding images.

## Styling

The application features a simple and visually appealing design. The key style elements are as follows:

### Body Background

The background color of the body is set to `antiquewhite`, providing a pleasant and neutral background for the content.

### Image Title

The title of the image is left-aligned for a clean and easy-to-read presentation.

### Image Container

The container for displaying the image is centered on the page. The image itself is styled to ensure a maximum width of 100%, a maximum height of 500px, and a subtle box shadow for a visual effect.

### Image Details

The details section of the image includes a box shadow for each paragraph, providing a sense of separation and focus on the content.

## User Interaction

The user can interact with the application through two forms:

### Single Date Selection

- Users can select a specific date using the first form.
- The selected date is displayed in the input field with the name `data_selezionata`.
- Clicking the "Visualizza Immagine" button will display the corresponding image.

### Date Range Selection

- Users can specify a date range using the second form.
- Input fields `data-iniziale` and `data-finale` represent the start and end dates, respectively.
- Both fields are required for submission.
- Clicking the "Visualizza Immagini" button will display images for the specified date range.

## Display of NASA APOD Data

If data from NASA APOD is successfully retrieved, it is displayed in a structured manner:

- The image title and date are presented prominently.
- The image itself is displayed along with relevant details.
- In case of an error during data retrieval, a message indicating the issue is displayed.




# NASA Image Viewer

This Flask application allows users to view NASA's Astronomy Picture of the Day (APOD) for a specific date.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Make sure you have Python and pip installed on your machine.

&nbsp;
### `virtualenv` environment <a name="virtualenv"></a>

1. `cd` into the new directory
```bash
cd APOD-API_TPI
```
2. Create a new virtual environment `env` in the directory
```bash
python -m venv venv
```
3. Activate the new environment
```bash
.\venv\Scripts\Activate
```
4. Install flask in new environment
```bash
pip install Flask
```
4. Install dependencies in new environment
```bash
pip install requests
```
5. Run the Flask application
```bash
python app.py
```
Open your web browser and go to http://localhost:5000 to view the NASA image for the current date.

## Usage
- By default, the application shows the NASA image for the current date.
- To view images for a specific date, append ?data=YYYY-MM-DD to the URL, replacing YYYY-MM-DD with the desired date, or use the selection in the application by click the "Visualizza Immagine" button .
```bash
Example: http://localhost:5000?data=2023-01-01
```
- Selecting multiple dates is still in the works.

## Built With
- Flask - Web framework for Python
- NASA Open API - APOD API for fetching images: https://api.nasa.gov/

## Author
Mattia Montagner

## Attribution

The application includes a link to NASA's official website and features the NASA logo aligned to the right of the page.

For more information about NASA, visit [NASA](https://www.nasa.gov).

![NASA Logo](https://www.nasa.gov/wp-content/themes/nasa/assets/images/nasa-logo.svg)