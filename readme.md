# paperNamer

A tool to automate the naming of paper files and update your read paper in the database

## How to use

- Args
  - --isCreate
  - --data_dir
  - -y or --year
  - -s or --source
  - -n or --name
  - -k or --Keywords

- run the command

```python
python .\paperNamer.py -y paper_year -s pub_source -n "long name" -k Keyword1,keyword2
```

- return 
  - paper_name: NO1_2018_arXiv_A_Tutorial_on_Bayesian_Optimization
    - (Remove all special characters, punctuation and spaces from paper name and substitute with '_')
  - update your paper in your database
    - Index,Year,Source,Name,Keywords,Time

## Example

1. Run

```python
python .\paperNamer.py -y 2018 -s arXiv -n "A Tutorial on Bayesian Optimization" -k BO,Survey
```

2.Output

```python
paper name: NO1_2018_arXiv_A_Tutorial_on_Bayesian_Optimization
```
