# RaPro
Useful Raster Processing Routines

## TiSeRa

Routine which creates a time series in .csv format based on arbitrary numbers of raster files.
It can be used, for example, to generate the average precipitation or temperature profile within a specific region of interest.

### Input data
Tab separated raster files in .txt format. Current code extracts the date and time for each raster file from its name. Format: yyyymmdd_hhh (e.g.20171115_019)
The separator can be easily adjusted in the code.

### Output
Comma separated (easy to adapt) result table which provides you the timestamp and the respective value (e.g. precipitation)
