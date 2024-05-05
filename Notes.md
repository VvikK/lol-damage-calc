## Prototype 1 Notes
- Assuming static damage
- Assuming all abilities + x aa are hit
- Accounts for items and runes -> This is going to be tricky, especially the runes

## Some Notes on getting data
- One possibility is to individually calculate the stat changes, damage numbers of each ability for each champion and manually input them into a spreadsheet. However this can get really tedious when balance changes occur.
- We could develop some sort of a web scraper, etc. to pull this information. But the problem is each champion will have unique calculation methods fpr each damage + statchange
-Figure out somethign with riot api
