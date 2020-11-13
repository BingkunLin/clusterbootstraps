## 🏆 Overview

`clusterbootstraps` is a Python library for **estimating a linear regression model and carrying accurate inference with clustered errors using the (i) Pairs Cluster Bootstrap-T and (ii) Wild Cluster Bootstrap-T procedures.**

Detailed introduction of the bootstrap methodology are in reference: Cameron, A. Colin, Jonah B. Gelbach, and Douglas L. Miller. "Bootstrap-based improvements for inference with clustered errors." The Review of Economics and Statistics 90.3 (2008): 414-427.

The method is also programmed in Stata and namely wcbregress.

Last edited on 21st Sep 2020. Comments are welcome. 

## 💿 Installations

This Python package can be installed via the **pip package manager** [pip](https://pip.pypa.io/en/stable/), i.e.:

```bash
pip install clusterbootstraps
```


## 🎷 Usages

### 🎷 Install Requires
`numpy` `pandas`  `statsmodels` `prettytable`

### 🎷 Syntax
```python
import clusterbootstraps.pair as cbp  # For Pairs Cluster Bootstrap-T
import clusterbootstraps.wild as cbw  # For Wild Cluster Bootstrap-T

result = cbp.Pair(Y,X,cluster_var,*args)  # input matrices or dataframes
result.table()                      # return the table
result = cbw.Wild(Y,X,cluster_var,*args)  # input matrices or dataframes
result.table()                      # return the table
```         
### 🎷 Arguments/Options
`clusterbootstraps`

Arguments|Introduction
:---:|:---:
`Y`|the dependent variable
`X`|the independent variables
`cluster_var`|the cluster variable you choose
`iter`[integer]|number of iterations,default = 10000 (optional)
`seed`[integer]|set random seed number,default = 2020 (optional)
`alpha`[float]|set the (1-alpha)% confidence level,default = 5 (optional)
`constant`[boolean]|set whether to add a constant term,default = True (optional)

### 🎷 Saved Variables
`clusterbootstraps` stores the following:

Saved Variables|Introduction
:---:|:---:
self.coef|Original Coefficient(s) of Sample
self.mean_coef|Average Coefficient(s) of n Iterations
self.mean|Mean of Bootstrap Sample Wald Statistic
self.upper_bound|Upper Bound of the Wald Statistic
self.lower_bound|Lower Bound of the Wald Statistic

### 🎷 Examples

#### Example 1: Pairs Cluster Bootstrap-T
Here, we run the linear regression of `logprice` on a set of covariates stored in the the matrix `X.matrix` and use the Pairs Cluster Bootstrap-T method to cluster the standard errors on level of five categories of variable `rep78`. 

In Python, we code:

```python
import clusterbootstraps.pair as cbp
result = cbp.Pair(Y = logprice,X = X.matrix,cluster_var = 'rep78')
result.table() 
```
Variables  | Original Coefs | Average Coefs | Pair Bootstrap Wald mean | Cluster Standard Error | Confidence Interval 
:---:|:---:|:---:|:---:|:---:|:---:
Constant|8.6109|8.5175|-0.1287|7.3002|[-2.2901,0.5436] 
mpg|-0.0029|-0.0035|0.1010|2.4323|[-2.5909,1.3779]   
headroom|-0.0571|-0.0667|-0.0127|25.8132|[-1.2115,1.0439]  
trunk|0.0134|0.0168|0.0645|2.7486|[-0.4213,1.1609]   
weight|0.0007|0.0006|-0.0247|0.0257|[-1.6886,2.6269]   
length|-0.0097|-0.0083|0.1133|1.0446|[-0.4850,0.8579]   
gear_ratio|-0.0976|-0.1123|-0.2112|31.7415|[-1.0551,0.6560]   
Foreign|0.5785|0.5624|0.2108|43.4689|[-0.5486,1.3473]

#### Example 2: Wild Cluster Bootstrap-T
We run the same regression and use the Wild Cluster Bootstrap-T to cluster the standard errors.

```python
import clusterbootstraps.wild as cbw
result = cbw.Wild(Y = logprice,X = X.matrix,cluster_var = 'rep78')
result.table() 
```
Variables  | Original Coefs | Average Coefs | Wild Bootstrap Wald mean | Cluster Standard Error | Confidence Interval 
:---:|:---:|:---:|:---:|:---:|:---:
Constant|8.5856|9.9176|-0.0005|4.4025|[-0.4649, 0.4647] 
mpg|0.0375|0.0191|-0.0010|0.1773|[-0.4189, 0.4291]  
headroom|-0.0564|0.0985|0.0016|0.1365|[-0.3862, 0.3843]  
trunk|0.0119|-0.0211|-0.0017|0.0600|[-0.3365, 0.3335]   
weight|0.0007|0.0003|0.0027|0.0009|[-0.4297, 0.4361]  
length|-0.0101|-0.0105|-0.0013|0.0292|[-0.4131, 0.4112]  
gear_ratio|-0.0827|0.1363|0.0003|0.6816|[-0.4283, 0.4262]  
Foreign|0.5241|-0.3451|0.0008|0.6512|[-0.3800, 0.3930]  


## Reference
Cameron, A. Colin, Jonah B. Gelbach, and Douglas L. Miller. "Bootstrap-based improvements for inference with clustered errors." The Review of Economics and Statistics 90.3


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Authors and Contact
Bingkun Lin (Coder maintainer, email: linbingkun.iesr18u@outlook.com)

Shiyue Shen 

Ziyi Zhan 

Zizhong Yan

Authors are from the IESR, Jinan University, Guangzhou, China.

## Package Homepage
https://github.com/BingkunLin/clusterbootstraps


## License
[MIT License](https://choosealicense.com/licenses/mit/)

Copyright (c) 2020 

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

