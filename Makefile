default:
	pyinstaller --onefile entrypoint.py

with_virtualenv:
	pyinstaller --onefile --paths `python -m site --user-site` entrypoint.py

clean:
	rm -rf *.spec build dist __pycache__
