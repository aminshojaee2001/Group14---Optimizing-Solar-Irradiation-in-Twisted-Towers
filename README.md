# Group14---Optimizing-Solar-Irradiation-in-Twisted-Towers

Project: Turning Torso
This README file is provided to assist the user in understanding and working with the files included in this project package:

1. Rhino Turning Torso.3dm
This is the Rhino file created to provide an environment for running the corresponding Grasshopper file described below.
Important Note: The Rhino file itself appears empty because all modeling has been carried out entirely within the Grasshopper environment. Therefore, do not be surprised if the Rhino file seems blank upon opening.

2. Grasshopper Turning Torso.gh
This is the main modeling file of the building, developed in Grasshopper. It contains three grouped sections to help users understand the step-by-step modeling process:
  1.Base Surface Modeling
  2.Climate and Sky Modeling
  3.Rotation and Irradiation Analysis

Each group is clearly labeled for easier navigation and understanding of the modeling procedure.

3. dataset.xlsx
This Excel file includes the original irradiation result values obtained from the Grasshopper model, along with their corresponding edge lengths and rotation angles of the building.
The dataset contains 92 entries, which are used as the input for the optimization part of the project.

4. Code file Turning Torso (visualization, emulator, optimization).ipynb
This Jupyter Notebook file contains the code developed for:
  1.Visualizing and analyzing the dataset
  2.Creating an emulator to approximate surface behavior
  3.Performing the optimization task based on the emulator results

The code is written in Python and must be run in a Jupyter Notebook environment.
Important: The dataset.xlsx file must be placed in the same directory as the Notebook file for proper execution.

5. Report Turning Torso.pdf
This is the final report of the project, documenting all steps of the work—starting from the initial modeling in Grasshopper through to the final optimization and conclusions.
