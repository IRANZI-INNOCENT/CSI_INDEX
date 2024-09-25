# README

## Project: Hunger Coping Strategies Index (CSI) Dashboard

### Overview

This project is a web-based application developed using Python's Dash framework, designed to calculate and display the Hunger Coping Strategies Index (CSI) based on user inputs. The application allows users to input various household strategies for coping with food insecurity, and it computes a weighted CSI score. The app features a clean, interactive user interface styled with Dash Bootstrap Components.

### Features
- User inputs: Location, Household Number, Number of People in the Family
- Raw CSI coping strategies input (12 categories)
- Calculation of a total weighted score based on severity weights for each coping strategy
- Dynamic output display of the total score and user inputs

### Files and Structure
- `app.py`: Main file containing the Dash application, layout, and callback logic.
- No additional files or directories are needed unless you modify the project further.

### Requirements

To run this application locally, the following dependencies are required:

- Python 3.x
- Dash
- Dash Bootstrap Components

You can install the required libraries using `pip`:
```bash
pip install dash dash-bootstrap-components
```

### Running the Application

1. **Clone the Repository:**

   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/hunger-csi-app.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd hunger-csi-app
   ```

3. **Run the Application:**
   Execute the following command in your terminal to run the app:
   ```bash
   python app.py
   ```

4. **Access the App in Your Browser:**
   Once the app is running, open your browser and go to `http://127.0.0.1:8050/` to view and interact with the Hunger CSI dashboard.

### App Structure

- **Layout**: The app consists of a main input form that allows users to enter details like location, household number, number of family members, and frequency of different coping strategies.
  
- **Callback**: The app uses a Dash callback to handle the input values and compute the total weighted score. The result is dynamically updated and displayed on the same page.

### Example Workflow

1. Input your location, household number, and family size.
2. Provide the frequency of different coping strategies (0-7 scale).
3. The app will compute and display the total weighted CSI score in the output container.

### Customization  
- **Styling**: The app uses `Dash Bootstrap Components` for layout and styling. You can easily customize the look and feel by modifying the CSS classes and component styles.

### Deployment

To deploy this application on platforms like Heroku or any cloud provider, ensure that:
- The `server` variable is properly exposed as shown in the code (`server = app.server`).
- Create a `Procfile` and `requirements.txt` for Heroku deployment

**Enjoy exploring the Hunger CSI Dashboard!**
