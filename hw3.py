import pandas as pd
import numpy as np
import pystan



data = pd.read_csv("https://raw.githubusercontent.com/carlson9/KocPython2020/master/homework/trend2.csv") 
data.columns = data.columns.map(str.strip)
data = data.dropna() 
data.country = data.country.map(str.strip)
countries = data.country.unique()
n = len(countries)
country_lookup = dict(zip(countries, range(n)))
country = data['country_code'] = data.country.replace(country_lookup).values
religiousness = data.church2
inequality = data.gini_net.values
rgdpl = data.rgdpl.values


random_intercepts_model = """
data {
  int<lower=0> J; 
  int<lower=0> N; 
  int<lower=1,upper=J> country[N]; 
  vector[N] x1; //inequality
  vector[N] x2; //rgdpl
  vector[N] y; //religiousness
}
parameters {
  vector[J] a;
  real b1;
  real b2;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;
}
transformed parameters {
  vector[N] y_hat;
  for (i in 1:N)
    y_hat[i] = a[country[i]] + x1[i] * b1 + x2[i] * b2;
}
model {
  sigma_a ~ uniform(0, 100);
  a ~ normal(mu_a, sigma_a);
  b1 ~ normal(0,1);
  b2 ~ normal(0,1);
  sigma_y ~ uniform(0, 100);
  y ~ normal(y_hat, sigma_y);
}
"""

df_random_intercepts_model = {'N': len(religiousness),'J': len(countries),'country': country+1,'x1': inequality,'x2': rgdpl,'y': religiousness}

random_intercepts_model_fit = pystan.stan(model_code=random_intercepts_model, data=df_random_intercepts_model, iter=1000, chains=2)

a_sample = pd.DataFrame(random_intercepts_model_fit['a'])

print(a_sample)

"""
Initially I used the generic generic weakly informative prior: normal(0, 1);

I used beta distribution specifically b1~beta(500,500) for the main explanatory variable to be highly informative but relatively far away.

When prior distribution is noninformative, the posterior distribution was highly determined by the data. 

However, when prior distribution is informative, the dependence of the posterior distribution to the data is decreased and dependence to prior is increased.

"""