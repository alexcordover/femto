# femto

Femto is a novel image compression methodology and related suite of tools designed at MHacks: Refactor. It was created to allow machine learning algorithms to run more efficiently on images by compressing them using pre-computed features. Further, the femto methodology can be reduced smaller than the size of a jpeg without sacrificing information and is transmissable by text, making it both lightweight and low overhead.

The femto suite includes an automated setup tool for Apache Spark (PySpark) and the SciPy stack on Linode servers, allowing distributed scientific computing using master and slave configurations on multiple machines.

Compressed text files are saved with the extension .laff in honor of John Lafferty, our machine learning professor at the University of Chicago.

# The Intuition

Femto treats images as an array of pixels and performs singular value decomposition to isolate important features. The singular values are encoded using a collection of performance optimizations (including multi-stage clustering to increase redundancy, indexing using k-strings, and standard text compression) on the server side. A pre-chosen amount of encoded data is then sent to the client where image reconstruction or data analysis takes place.

# Performance

The femto protocol manages to compress large TIF images by up to 8 times without significant loss in quality or information. Additionally, femto is between 40% and 50% of the size of JPEG encoding (when converting from large TIF or Raw files).

# Linode Auto-Setup Tool Usage

1) Obtain a Linode server with a fresh Ubuntu 14.04+ install.

2) In terminal, run ```$ wget https://raw.githubusercontent.com/alexcordover/femto/master/spark_setup.sh```

3) ```$ chmod 755 spark_setup.sh```

4) ```$ source ./spark_setup.sh``` - this downloads Spark, the SciPy stack, and other essential machine learning libraries.

At this point, the Linode server can be used as normal. If you would like to set up master/slave configuration between multiple Linode servers, for the master server, run the following:

5) ```$ startmaster <linode public IP address>```

For each slave server, run steps 1-4 and the following:

6) ```$ startslave <master Spark URL>```

The master Spark URL can be found by visiting ```http://<linode master public IP address>:8080``` on a browser. At this point, setup is complete.

To stop the master server, run ```$ stopmaster```. To stop slave servers, run ```$ stopslave```.

# Jupyter and PySpark

To increase usability, we set up Apache Spark (PySpark) to run through a Jupyter notebook. To start a Jupyter notebook, run ```$ ./pyspark.sh``` on the master server. The notebook can be accessed at ```http://<master public IP address>:1337``` in a browser. For further information and docpython ImageDraw line thicknessumentation for PySpark and Jupyter, visit Spark's documentation.  

# Running The Femto Image Compression Protocol

You will need an image to compress on the master server - either download it or use file transfer. For color image compression, open the colorImageCompression.ipynb, set your chosen constants, and target an image and an output location. YOU MUST HAVE A FOLDER CALLED 'images' THAT CONTAINS TARGET PHOTOS AND A FOLDER CALLED 'images_out'.  A gzip file of the data will be present in images_out.

To use grayscale compression, do the exact same thing as above except run grayscale_compression.ipynb. Like with above, a gzip file  containing the compressed data will be available in images_out.

# Reconstructing From GZIP-ed JSON

The data for image reconstruction is saved as a JSON (in a text file) that has been GZIP-ed. This is the output of using either grayscale or color compression. To reconstruct the image from text, simply type ```python3 decompressor.py <name of compressed archive>```. A reconstruction of the compressed file will appear in the images_out folder.
