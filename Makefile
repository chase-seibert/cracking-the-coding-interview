FILE := $(shell ls -t *.py | head -1)

default:
	python3 $(FILE)
	pep8 $(FILE)
new:
	@echo "Enter a slug for your new question like '01-01-str-unique-chars' and hit [ENTER]: "
	@read slug; cp template.py ctci-$$slug.py
	git status
ls:
	@ls -1 |grep ctci |sed -e 's/\..*//' |uniq
count:
	@ls -1 |grep ctci |sed -e 's/\..*//' |uniq |wc -l
