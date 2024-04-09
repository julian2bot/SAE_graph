dicoTest = [{
    "title": "Actrius",
    "cast": [
        "[[Núria Espert]]",
        "[[Rosa Maria Sardà]]",
        "[[Anna Lizaran]]",
        "[[Mercè Pons]]"
    ],
    "directors": [
        "[[Ventura Pons]]"
    ],
    "producers": [
        "[[Ventura Pons]]"
    ],
    "companies": [
        "[[Buena Vista International]]"
    ],
    "year": 1997
},
{
    "title": "Army of Darkness",
    "cast": [
        "[[Bruce Campbell]]",
        "[[Embeth Davidtz]]",
        "[[Marcus Gilbert (actor)|Marcus Gilbert]]",
        "[[Ian Abercrombie]]",
        "Richard Grove",
        "Timothy Patrick Quill",
        "Michael Earl Reid",
        "[[Bridget Fonda]]",
        "[[Bill Moseley]]",
        "[[Patricia Tallman]]",
        "[[Ted Raimi]]",
        "[[Angela Featherstone]]"
    ],
    "directors": [
        "[[Sam Raimi]]"
    ],
    "producers": [
        "[[Robert Tapert]]"
    ],
    "companies": [
        "[[Dino De Laurentiis|Dino De Laurentiis Communications]]",
        "[[Renaissance Pictures]]",
        "[[Introvision International]]",
        "[[Universal Pictures]]"
    ],
    "year": 1992
}]

import donneeTest

for i in range(len(donneeTest.dicoTest)):
    print(donneeTest.dicoTest[i]["year"])