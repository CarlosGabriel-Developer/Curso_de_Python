import math 

angulo = float(input("Quantos angulos :"))

rad = math.radians(angulo) 

seno = math.sin(rad)
coseno = math.cos(rad)
tang = math.tan(rad)

print(f"O seu seno é {seno:.2f} O seu cosseno é {coseno:.2f} e sua a tangente é {tang:.2f}")