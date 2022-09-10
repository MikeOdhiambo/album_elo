# album_elo
Rate albums based on the ELO rating system and store on a simple json file.

## Usage
Clone this [repository](https://github.com/MikeOdhiambo/album_elo.git) and run the executable [elo-calc.py](./elo-calc.py) 

## Calculations
Each new album is assigned a standard arbitrary rating of 2500 and then compared against existing records. The respective ELOs are calculated and, finally, a new entry is done and the json file updated.

I use a k-factor of $k=24$.

Given two ratings *r1* and *r2*

1. 	Compute the transformed ratings $$R1={10^{r1\over400}}$$ and $$R2={10^{r2\over400}}$$
2.  Calculate the expected scores $$E1={{R1}\over{R1+R2}}$$ and $$E2={{R2}\over{R1+R2}}$$
3.  Obtain the actual scores $S1$ and $S2$. Here the preferred album is assigned a value of $1$ while the other gets $0$
4.  Finally, we put everything together and calculate the new ELO ratings $$O1={{r1}+{K(S1-E1)}}$$ and $$O2={{r2}+{K(S2-E2)}}$$