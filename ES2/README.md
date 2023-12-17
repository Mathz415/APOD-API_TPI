# NASA Image of the Day

This simple Flask web application allows users to view NASA's Astronomy Picture of the Day (APOD) based on a selected date. The application retrieves data from NASA's APOD API and presents it in both JSON and XML formats.

## Features

- **Date Selection:** Users can select a date using the date picker in the form.
- **Image Display:** The selected image, along with its title, date, and explanation, is displayed on the page.
- **Error Handling:** In case of an error during data retrieval, an error message is displayed to the user.
- **JSON and XML Formats:** The application provides the APOD data in both JSON and XML formats. XML conversion is handled using the xmltodict library.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Make sure you have Python and pip installed on your machine.
&nbsp;
### `virtualenv` environment <a name="virtualenv"></a>

1. `cd` into the new directory
```bash
cd APOD-API_TPI/ES2
```
2. Create a new virtual environment `env` in the directory
```bash
python -m venv venv
```
3. Activate the new environment
```bash
.\venv\Scripts\Activate
```
4. Install flask and the other functions in new environment
```bash
pip install Flask requests xmltodict
```
1. Run the Flask application
```bash
python XMLWiew.py
```
Open your web browser and navigate to http://127.0.0.1:5000/. You should see the NASA Image of the Day in XML format for the current date.

## Styling

The application uses simple styling to enhance the user interface. The background color is set to antiquewhite, and there are specific styles applied to different elements:

- **Image Title:** Aligned to the left.
- **Image Container:** Centered, with a maximum width for the image and a box shadow.
- **Image Details:** Each paragraph has a margin-bottom and a box shadow for better readability.

## Form

The form allows users to select a date, and on submission, the application fetches and displays the corresponding NASA Image of the Day.

## Technologies Used

- HTML
- CSS
- Python
- [NASA API](https://api.nasa.gov/) for fetching the Image of the Day.

### Dependencies
- Flask
- Requests
- xmltodict

## Author
Mattia Montagner

## Attribution

The application includes a link to NASA's official website and features the NASA logo aligned to the right of the page.

For more information about NASA, visit [NASA](https://www.nasa.gov).

![NASA Logo](https://www.nasa.gov/wp-content/themes/nasa/assets/images/nasa-logo.svg)