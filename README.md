## Clusterbootstraps

Clusterbootstraps is a Python library for dealing with cluster bootstraps.

There are two kinds of clusterbootstraps:pair and wild.Detailed introduction in reference(Cameron, A. Colin; Miller, Douglas L.; Gelbach, Jonah B. , Working Paper , Bootstrap-based improvements for inference with clustered errors)


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

Arguments|Introduction
:---:|:---:
Y|the dependent variable
X|the independent variables
cluster_var|the cluster variable you choose
iter[optional]|iterations,default = 10000
seed[optional]|random seed number,default = 2020
alpha[optional]|(1-alpha)% confidence level,default = 5
constant[optional]|whether to add a constant term,default = True

4.Saved Variables

Saved Variables|Introduction
:---:|:---:
self.coef|Original Coefficient(s)
self.mean|Mean of wald coefficient(s) of bootstrap sample
self.upper_bound|Upper bound of the wald statistic
self.lower_bound|Lower bound of the wald statistic

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Authors and Contact
Bingkun Lin , an undergraduate of Jinan University, China

Shiyue Shen , an undergraduate of Jinan University, China

Ziyi Zhan , an undergraduate of Jinan University, China

Zizhong Yan , an assistant professor of Jinan University, China

Code Maintainer:Bingkun Lin

Email:linbingkun.iesr18u@outlook.com

## Reference
Cameron, A. Colin; Miller, Douglas L.; Gelbach, Jonah B. , Working Paper , Bootstrap-based improvements for inference with clustered errors
