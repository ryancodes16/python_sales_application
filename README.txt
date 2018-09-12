sales.py currently is hardcoded to read the XLS file in the 2016_11_30
directory. We can generalize it to point to a different directory
specified by an argument, once we figure out a standard way to make the 
derived plots that works the same for different directories.

To run, on server03, type:
  ipython2.7
  execfile('sales.py')
(this can be made to work on other machines with pandas and numerous other
python packages installed).

/mnt/storage/business/product_sales is a clone of /mnt/storage/gitrepo/business.git.
The specific directories that contain spreadsheets are NOT checked into the repo.

