all:
	python rst2html.py ../README.rst > site-src/pages/README.html
	cd ..; git log --pretty=format:'%ci;%h;%s' | grep -v Merge > gh-pages/changelog.csv
	md5sum *.deb > md5sum
	#build after any site-src modification
	cd site-src; cactus build; cd ..
	cp -r site-src/.build/* .

serve: all
	cd site-src/; cactus serve
