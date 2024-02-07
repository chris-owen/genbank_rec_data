# genbank_rec_data

## Installing Miniconda for macOS
1. Please visit this [website](https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html) and follow the directions to install Miniconda.

## Use Miniconda to install Python and the dependent packages to run the script.
1. First open the Terminal your Mac
  - If you are not sure where the Terminal is located on your Mac, you can press <kbd>Cmd</kbd>+<kbd>Space</kbd> to open spotlight, then search for *Terminal*
2. Once in the Terminal, issue the following command followed by <kbd>Return</kbd>: ```conda create --name <env_name> python==3.12.1 pandas biopython```.
  - Please replace ```<env_name>``` with any name you would like to use for your environment.
  - You may be prompted for <kbd>Y</kbd> or <kbd>N</kbd> to update and/or add dependencies for pandas and biopython. Please press <kbd>Y</kbd>.

## Activate your Miniconda environment and execute the script
1. Now open the terminal in the directory where your Excel file that contains the list of GenBank accessions that you want to obtain data for.
  - If you are unfamiliar with changing directories in the Terminal please see [this tutorial](https://www.macworld.com/article/221277/command-line-navigating-files-folders-mac-terminal.html).
  - An example Excel file on how to structure your GenBank accessions is in the same directory as the script.
2. Once in the desired directory, initiate your Miniconda environment by typing ```conda activate <env_name>```
  - Please replace ```<env_name>``` with the name you gave your environment
  - If by chance you don't remember the name, you can view ALL conda environment names by typing ```conda info --envs```
3. Now that loaded your Miniconda environment, we will execute the script in the terminal by typing: ```python get_gb_rec_data.py <excel_file_name> <email_address>```.
  - Please replace ```<excel_file_name>``` with the actual name of the Excel file that contains your GenBank accessions
  - Please replace ```<email_address>``` with your email address (I think it is required for searching GenBank via the api)
  
## Output files
1. I have chosen not to include any output to the terminal (this may change in the future)
2. The file with the extension *.gb* contains all of the GenBank records from those GenBank accessions listed in the Excel file.
3. The file with the extension *.tsv* contains all of the metadata obtained from the GenBank records
