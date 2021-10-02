default:
#	pyinstaller --onefile entrypoint.py

#with_virtualenv:
	pyinstaller --paths /home/martin/.virtualenvs/ng/lib/python3.7/site-packages \
		--hiddenimport sklearn.neighbors._typedefs \
		--hiddenimport sklearn.neighbors._partition_nodes \
		--hiddenimport sklearn.neighbors._quad_tree \
		--hiddenimport scipy.special.cython_special \
		--hiddenimport skimage.filters.rank.core_cy_3d \
		--add-data 'ng_whistles/model:.' \
		--noconfirm \
		--onefile \
		entrypoint.py

clean:
	rm -rf build dist __pycache__ *.spec ng_whistles/__pycache__
