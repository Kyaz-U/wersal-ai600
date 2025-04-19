import random

def run_dynamic_predictions():
    aviator = round(random.uniform(1.7, 2.0), 2)
    crash = round(random.uniform(2.0, 2.5), 2)
    luckyjet = round(random.uniform(1.5, 1.9), 2)
    safe_cells = random.sample(range(1, 26), 3)
    dice = random.choice(["1", "2", "3"])
    hilo = random.choice(["katta", "kichik"])

    return f"""Wersal AI Signallari:
1. Aviator: {random.randint(89, 95)}% ehtimol bilan {aviator} martadan oshadi
2. Crash: {random.randint(85, 92)}% ehtimol bilan {crash} martadan pastga tushadi
3. LuckyJet: {random.randint(90, 96)}% ehtimol bilan {luckyjet} martadan oshadi
4. Mines: Xavfsiz kataklar: {safe_cells}
5. Dice: {random.randint(80, 90)}% ehtimol bilan {dice} soni chiqadi
6. HiLo: {random.randint(80, 90)}% ehtimol bilan navbatdagi karta {hilo} bo‘ladi"""
