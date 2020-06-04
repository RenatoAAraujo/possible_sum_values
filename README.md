# Possible combinations of a sum
>This tutorial assumes that your on Unix like OS. If not make the necessary adjustments.

#### Requirement
* [Python3](https://www.python.org/)
* clone the project and go the chosen directory, for example:
```
cd ~/projects/possible_sum_values
```
* lib `virtualenv`, in the terminal execute:
>A virtualenv guarantees that your python environment is not influenced by other projects.
 ```
python3 -m venv venv
source venv/bin/activate
 ``` 

#### Project Dependencies
>All python packages to be installed are in [requirements.txt](requirements.txt), to install them run:
```
pip install -r requirements.txt
``` 

#### Generate Combinations
>Run the file [export_data.py](export_data.py) and tweak the the variables ```targets```, ```total_numbers_to_be_used```, ```numbers_to_be_used``` and ```replace_numbers```.
>Multiple combinations target can be used, change the target range accordingly.
