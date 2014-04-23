download:
	echo "Downloading..."
	wget -nv -r -nH --cut-dirs=2 --no-parent --reject="index.html*" http://trashtube.it/~askz/dsk/pub/


clean:
	rm -rf *~ 


