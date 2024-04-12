tex_files := $(wildcard Lesson*/lesson*.tex)
pdf_files := $(patsubst %.tex,%.pdf,$(tex_files)) ad/ad.pdf rop/rop.pdf
lesson_names := $(notdir $(tex_files))
lesson_names := $(patsubst %.tex,%,$(lesson_names))
clean_targets := $(patsubst %,clean-%,$(lesson_names))

LATEX=pdflatex
LATEXOPT=--shell-escape
NONSTOP=--interaction=batchmode

LATEXMK=latexmk
LATEXMKOPT=-pdf

$(info $$lesson_names is [${lesson_names}])

ifneq (,$(wildcard ./.run_locally))
# lol, don't put any indented commands here (https://stackoverflow.com/a/32022883)
	RUN := ./run_locally.sh
else
 	RUN := ./run_docker.sh
endif

.PHONY: all clean clean-archive build_container archive $(lesson_names) $(clean_targets)
.SECONDEXPANSION: # see below; this applies to the entire file

all: $(pdf_files)

# syntactic sugar, e.g. "make lesson3"
# this is Make black magic of the highest degree!
# .SECONDEXPANSION means prerequisites are expanded twice, where "$*" (and "$@") are defined in the second round of expansion
# because you can't use the '%' sign twice on the right-hand side of a subsitution 🙄
# TODO (maybe?): account for cases like 'lesson5_bis'
$(lesson_names): lesson% : Lesson$$*/lesson$$*.pdf

ad: ad/ad.pdf

$(pdf_files): %.pdf : %.tex theme/*
	$(RUN) $$(dirname $@) $(LATEXMK) $(LATEXMKOPT) -pdflatex="$(LATEX) $(LATEXOPT) $(NONSTOP) %O %S" $$(basename $(patsubst %.pdf,%.tex,$@))

clean: $(clean_targets) clean-archive

$(clean_targets):
	LESSON_DIR="$(patsubst clean-lesson%,Lesson%,$@)" && \
	$(RUN) "$$LESSON_DIR" $(LATEXMK) -C $(patsubst clean-%,%.tex,$@) && \
	$(RM) -rf "$$LESSON_DIR"/_minted-*

build_container:
	docker build -t ctf-lessons-latex --no-cache .

archive: lessons.zip

clean-archive:
	$(RM) lessons.zip

lessons.zip: $(pdf_files)
	$(MAKE) clean-archive # lol DRY (it's not a prerequisite so the zip file can stay unchanged if the PDFs don't change)
	zip -D -j $@ $^

