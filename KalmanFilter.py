
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['figure.pencereboyutu'] = (10, 8)

# Başlangıç Parametreleri
n_iterasyon = 20
dizi_boyut = (n_iterasyon,) # dizinin boyutu
x = 0 # Robotun x eksenindeki yolu
z = np.random.normal(x,1,size=20) # (1) birim aralık değeri ve rastegele üretilecek gürültülü veri miktarı

Q = 1e-55 # süreç farkı

# Ölçüm ve Zaman güncelleme formüllerinde kullanılacak matrisler dizi bıyutunda sıfır matris olacak şekilde oluşturuluyor.
xhat=np.zeros(dizi_boyut)      # x'in tahmini
P=np.zeros(dizi_boyut)         # hata tahmini
xhatminus=np.zeros(dizi_boyut) #  x'in ön tahmini
Pminus=np.zeros(dizi_boyut)    # ön hata tahmini
K=np.zeros(dizi_boyut)         # kazanç faktörü

R = 0.1**2 #tahmini ölçüm farkı/değişim etkisi

# ilk tahminler
xhat[0] = 0.0
P[0] = 0.1

for k in range(1,n_iterasyon):
    # zaman güncelleme
    xhatminus[k] = xhat[k-1]
    Pminus[k] = P[k-1]+Q

    # ölçüm güncelleme
    K[k] = Pminus[k]/( Pminus[k]+R )
    xhat[k] = xhatminus[k]+K[k]*(z[k]-xhatminus[k])
    P[k] = (1-K[k])*Pminus[k]

plt.figure()
plt.plot(z, '-s', label='gürültülü değerler')
plt.plot(xhat,'r-',label='tahmini rota')
plt.axhline(x,color='g',label='gerçek rota')
plt.legend()
plt.title('Tahmini vs Gerçek Rota', fontweight='bold')
plt.xlabel('İterasyon')
plt.ylabel('Konum')
plt.show()
