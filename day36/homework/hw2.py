# 2) უკვე შექმნილ scores dictionary-ში დაამატე ახალი სტუდენტები update()-ით




scores = {
    "Ana": 95,
    "Giorgi": 88,
    "Luka": 76
}

scores.update({
    "Nino": 82,
    "Dato": 91
})

for name, score in scores.items():
    print("სტუდენტი:", name, "- ქულა:", score)