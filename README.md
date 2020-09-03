## Clusterbootstraps

Clusterbootstraps is a Python library for dealing with cluster bootstraps.

There are two kinds of clusterbootstraps:pair and wild.Detailed introduction in Cameron, A. Colin; Miller, Douglas L.; Gelbach, Jonah B. , Working Paper , Bootstrap-based improvements for inference with clustered errors


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install clusterbootstraps.

```bash
pip install clusterbootstraps
```
## Package Homepage
https://github.com/Bank1999/clusterbootstraps

## Usage
1.Introduction
  
Pairs Cluster Bootstrap-T

![](https://github.com/Bank1999/clusterbootstraps/blob/master/pictures/pair.png)
  
Wild Cluster Bootstrap-T

![](https://github.com/Bank1999/clusterbootstraps/blob/master/pictures/wild.png)
  
2.Syntax
```python
import clusterbootstraps.pair as cbp
import clusterbootstraps.wild as cbw

result = cbp.Pair(Y,X,cluster_var,*args)  # input matrices or dataframes
result.table()                      # return the table
result = cbw.Wild(Y,X,cluster_var,*args)  # input matrices or dataframes
result.table()                      # return the table
```         

3.Arguments

Y: the dependent variable

X: the independent variables

cluster_var:the cluster variable you choose

iter[optional]:iterations,default = 10000

seed[optional]:random seed number,default = 2020

alpha[optional]:(1-alpha)% confidence level,default = 5

constant[optional]:whether to add a constant term,default = True

4.Saved Variables

self.mean:Mean of wald coefficient(s) of bootstrap sample

self.upper_bound:Upper bound of the wald statistic

self.lower_bound:lower bound of the wald statistic

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Authors and Contact
Bingkun Lin , an undergraduate of Jinan University, China

Shiyue Shen , an undergraduate of Jinan University, China

Ziyi Zhan , an undergraduate of Jinan University, China

Zizhong Yan , an assistant professor of Jinan University, China

Code Maintainer:Bingkun Lin

Email:linbingkun.iesr18u@outlook.com

## Reference
Cameron, A. Colin; Miller, Douglas L.; Gelbach, Jonah B. , Working Paper , Bootstrap-based improvements for inference with clustered errors
