
# Required Courses

Some sample output:

```
AR307 Meta-Capitalist Ethicism
HI507 Psychologist Fundamentalism
PH369 The Humanization Of The Human And The De-Radicalization Of Capital
HI485 The Psychology of The Ethic
AN307 Post-Aestheticist Structuralism
AN505 The Post-Post-Third Wave-Philosophy of Post-Machinist Genderization
PH384 Technologist Femininism
AR441 Ethicist Positivism
PH443 Neo-Philosophist Machinism
HI457 Structuralist Radicalism
PH584 Positivist Ethicism of Structuralist Archeologies
```

# Running and developing

If running from docker, then

```
docker run -p 80:80 brightredchilli/required-courses
```

If testing locally, the python version is 2.7.14. In new environments, people
should create an environment with 2.7.14, and do:

```
cd flask-app
pip install -r requirements.txt
python required_courses.py
```
