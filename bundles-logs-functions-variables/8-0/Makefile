TXTDIR=modified
HTMLS=$(wildcard *.html)
MDS=$(patsubst %.html,$(TXTDIR)/%.markdown, $(HTMLS))

.PHONY : all

all : $(MDS)

$(TXTDIR) :
	mkdir $(TXTDIR)

$(TXTDIR)/%.markdown : %.html $(TXTDIR)
	pandoc -f html -t markdown -s $< -o $@
