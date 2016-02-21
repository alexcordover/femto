# femto

Femto is a novel image compression methodology and related suite of tools designed at MHacks: Refactor. It was created to allow machine learning algorithms to run more efficiently on images by compressing them using pre-computed features. Further, the femto methodology can be reduced smaller than the size of a jpeg without sacrificing information and is transmissable by text, making it both lightweight and low overhead.

The femto suite includes an automated setup tool for Apache Spark (PySpark) and the SciPy stack on Linode servers, allowing distributed scientific computing using master and slave configurations on multiple machines.

Compressed text files are saved with the extension .laff in honor of John Lafferty, our machine learning professor at the University of Chicago.

# The Intuition

Femto treats images as an array of pixels and performs singular value decomposition to isolate important features. The singular values are encoded using a collection of performance optimizations (including multi-stage clustering to increase redundancy, indexing using k-strings, and standard text compression) on the server side. A pre-chosen amount of encoded data is then sent to the client where image reconstruction or data analysis takes place.

# Performance

The femto protocol manages to compress large TIF images by up to 8 times without significant loss in quality or information. Additionally, femto is between 40% and 50% of the size of JPEG encoding (when converting from large TIF or Raw files).

# Linode Auto-Setup Tool Usage

1) Obtain a Linode server with a fresh Ubuntu 14.04 install.
2) In terminal, run "$ wget https://raw.githubusercontent.com/alexcordover/femto/master/spark_setup.sh"
3) "$ chmod 755 spark_setup.sh"
4) "$ ./spark_setup.sh" - this downloads Spark, the SciPy stack, and other essential machine learning libraries.

At this point, the Linode server can be used as normal. If you would like to set up master/slave configuartion between multiple Linode servers, for the master server, run the following:
5) "$ startmaster <linode public IP address>"

For each slave server, run steps 1-4 and the following:
6) "$ startslave <master Spark URL>"

The master Spark URL can be found by visiting "http://<master server public IP address>:8080" on a browser. At this point, setup is complete.
# Jupyter and PySpark

To increase usability, Apache Spark (PySpark) will run through a Jupyter notebook. To start a Jupyter notebook, run:
"$ ./pyspark.sh" 
on the master server. The notebook can be accessed at:
"http://<master public IP address>:1337"
in a browser. For further information and documentation for PySpark and Jupyter, visit Spark's documentation.  
