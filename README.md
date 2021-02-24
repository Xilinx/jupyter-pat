# jupyter-pat: Versal Power Tool

This repo contains the Jupyter Python Notebook as well as the Python Library for the Versal Power Tool.

## Background

Customers typically do not need to install this code as it normally comes pre-installed for both the Versal System Controller as part of the BEAM Tool, and comes pre-installed for Versal in the PetaLinux Board Support Package. However, any users that are porting to an unsupported software stack on a supported evaluation board can follow the instructions below. 

User should have installed Python3 version >=3.7 has been tested along with Jupyter Notebook.

### Installing the poweradvantage.py Library:

The Power Tool Python library is poweradvantage.py. The jupyter-pat directory contains the poweradvantage folder which contains the Python code poweradvantage.py and other support files. This is installed to the target System Controller Linux by an SSH file copy of the entire folder to the Python library folder. The name of this Python library folder will depend on the current version of Python. For Python 3.7 the copy path would be /usr/lib/python3.7/site-packages.

### Installing the Power_Advantage_Tool.ipynb Notebook:

The Power Tool Jupyter Notebook is Power_Advantage_Tool.ipynb. The jupyter-pat directory contains the Jupyter Notebook named Power_Advantage_Tool.ipynb and its artwork folder img. This notebook is installed to the target System Controller Linux by an SSH file copy of Power_Advantage_Tool.ipynb with its artwork folder img to the folder where Jupyter Notebooks are found. The path of the Jupyter Notebooks folder is commonly /home/root. You may choose to use a sub-folder if you wish to organize your Jupyter Notebooks.

### Versal Power Tool Testing

The full Versal Power Tool instructions are available at https://xilinx-wiki.atlassian.net/wiki/spaces/XWUC/pages/1299251214/Versal+ACAP+Power+Tool+part+1+-+Introduction+to+the+Power+Tool. And the appropriate instructions how to run the Versal Power Tool are at https://xilinx-wiki.atlassian.net/wiki/display/A/Versal+ACAP+Power+Tool+part+3+-+Running+the+Pre-Built+Power+Tool section 1.2 "Jupyter Notebook Running Instructions".

In short:

- Launch Jupyter Notebook on your system, then open Power_Advantage_Tool.ipynb
- Edit the "pa = poweradvantage("Tenzing", "SC") line to your appropriate environment. The first argument will be your evaluation board type. The second  argument is either "SC" for running on the System Controller or "" for  Versal. Repeat the edit for each code cell.
- Click to select the last code cell and click "Run".  This will install any supporting Python libraries that you may not have installed yet.
- Then starting from the top, try running each of the remaining code cells. The expected behavior is described in the text associated with each cell.  