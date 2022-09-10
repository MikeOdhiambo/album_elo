# album_elo
Rate albums based on the ELO rating system and store on a simple json file.

## Calculations
Each new album is assigned a standard arbitrary rating of 2500 and then compared against existing records. The respective ELOs are calculated and, finally, a new entry is done and the json file updated.

I use a k-factor of 24.

Given two ratings *r1* and *r2*

1. 	Compute the transformed rating $R1=(10^r1\over400)$