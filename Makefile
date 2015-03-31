HTML = index.html specification.html showcase_2048.html showcase_noriteo.html testimonials.html developers.html


#TODO: markdown


all: $(HTML)
	$(foreach html, $(HTML), \
		python3 build.py $(html) ; \
	)
