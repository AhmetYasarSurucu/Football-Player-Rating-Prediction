1. DEĞİŞKENLER VE VERİ SETİ
1.1 ÖZET İSTATİSTİKLER
![image](https://github.com/user-attachments/assets/81c26e85-4605-4f12-9412-60619978653c)

1.2 DEĞİŞKENLER HAKKINDA GENEL BİLGİ
Overall Rating (Genel Derecelendirme): Oyuncunun genel yetenek seviyesi ve performansını gösteren bir değer.
Potential (Potansiyel): Oyuncunun gelecekte ulaşabileceği maksimum yetenek seviyesi.
Crossing (Orta Yapma): Oyuncunun topu kanattan doğru bir şekilde orta yapma kabiliyeti.
Finishing (Bitiricilik): Oyuncunun gol pozisyonlarındaki son vuruş yeteneği.
Heading Accuracy (Kafa Vuruşu Doğruluğu): Oyuncunun hava toplarındaki isabet oranı.
Short Passing (Kısa Pas): Oyuncunun kısa mesafede isabetli pas yapma becerisi.
Volleys (Vole): Oyuncunun havadan gelen toplara doğru şekilde vurma yeteneği.
Dribbling (Top Sürme): Oyuncunun topu kontrol ederek rakip oyuncuları geçme becerisi.
Curve (Kavis): Oyuncunun topa falso vererek şut veya pas yapma yeteneği.
Freekick Accuracy (Frikik Doğruluğu): Oyuncunun duran toplarda isabetli şut çekme kabiliyeti.
Long Passing (Uzun Pas): Oyuncunun uzun mesafede isabetli pas yapma becerisi.
Ball Control (Top Kontrolü): Oyuncunun topu ilk dokunuşta kontrol etme yeteneği.
Acceleration (Hızlanma): Oyuncunun kısa sürede maksimum hıza ulaşma kapasitesi.
Sprint Speed (Sprint Hızı): Oyuncunun düz bir koşuda ulaştığı maksimum hız.
Agility (Çeviklik): Oyuncunun yön değiştirme ve hızlı hareket etme yeteneği.
Reactions (Tepkiler): Oyuncunun ani durumlara hızlı yanıt verme kapasitesi.
Balance (Denge): Oyuncunun fiziksel dengeyi koruma yeteneği.
Shot Power (Şut Gücü): Oyuncunun şutlarının gücü ve sertliği.
Jumping (Sıçrama): Oyuncunun yükseğe zıplama yeteneği.
Stamina (Dayanıklılık): Oyuncunun maç boyunca yorulmadan performans sergileme kapasitesi.
Strength (Güç): Oyuncunun fiziksel mücadelelerdeki dayanıklılığı ve kuvveti.
Long Shots (Uzaktan Şut): Oyuncunun ceza sahası dışından isabetli şut atma kabiliyeti.
Aggression (Agresiflik): Oyuncunun saha içindeki mücadeleci ve hırslı oyun tarzı.
Interceptions (Araya Girme): Oyuncunun rakip paslarını kesme ve müdahale etme becerisi.
Positioning (Pozisyon Alma): Oyuncunun saha içinde doğru pozisyonda bulunma yeteneği.
Vision (Vizyon): Oyuncunun sahadaki takım arkadaşlarını görme ve pas seçeneklerini değerlendirme becerisi.
Penalties (Penaltı): Oyuncunun penaltı atışlarını isabetli şekilde yapma kabiliyeti.
Composure (Soğukkanlılık): Oyuncunun stresli durumlarda sakin kalabilme yeteneği.
Marking (Markaj): Oyuncunun rakibini savunmada etkili şekilde takip etme becerisi.
Standing Tackle (Ayakta Müdahale): Oyuncunun rakipten topu düzgün bir şekilde kazanma yeteneği.
Sliding Tackle (Kayarak Müdahale): Oyuncunun kayarak topa müdahale etme becerisi.

3. VERİ ÖN İŞLEME 
2.1 EKSİK VE AYKIRI GÖZLEMLER
   
![image](https://github.com/user-attachments/assets/ce0ad404-9e29-4a42-8a06-1fdcfd7d3ede)


Aykırı değerler, veri analizi sürecinde sonuçları yanıltabilecek uç gözlemlerdir. Bu nedenle, her bir sayısal sütun için IQR (Interquartile Range) yöntemi kullanılarak alt ve üst sınırlar belirlenmiştir. Alt sınırın altındaki ve üst sınırın üstündeki değerler sırasıyla alt ve üst sınıra sabitlenmiştir. Bu işlem, verinin genel yapısını koruyarak aşırı uçların etkisini minimize etmeyi ve modelin daha dengeli sonuçlar üretmesi amaçlanmıştır.

2.2 STANDARTLAŞTIRMA
Standartlaştırma, veri setindeki sayısal değişkenlerin farklı ölçeklerden kaynaklanan etkilerini ortadan kaldırmak için kullanılan bir yöntemdir. Bu süreçte, her bir değişkenin ortalaması sıfır ve standart sapması bir olacak şekilde dönüştürülmüştür. Verilerin aynı ölçekte olması farklı değişkenlerin model üzerindeki etkilerini dengelenmesi amaçlanmıştır. Bu işlem, StandardScaler kullanılarak gerçekleştirilmiştir.


3. VERİ ANALİZİ VE GÖRSELLEŞTİRME 
3.1. TEK DEĞİŞKENLİ VE DAĞILIM ANALİZ
![image](https://github.com/user-attachments/assets/c1c7ebe9-dc60-4b43-be84-ecff7bc62bde)
Bu grafikte futbolcuların genel derecelendirme (overall rating) dağılımını görüyoruz. Ortalama dereceler (60-70 aralığı), futbolcuların büyük bir kısmının ortalama performans sergilediğini gösteriyor. 80 ve üzeri derecelendirme alan futbolcuların azlığı ise elit düzeydeki oyuncuların nadir olduğunu vurguluyor. Düşük dereceler (50-60 arası) genellikle genç, yaşlı veya deneyimsiz oyunculara işaret etmektedir.
![image](https://github.com/user-attachments/assets/b752b10a-2002-4058-af22-19f139add1ef) 
Futbolcuların genel derecelendirmeleri (overall rating) ile potansiyel dereceleri (potential) arasındaki ilişkiyi göstermektedir. Grafik, genel olarak pozitif bir korelasyon olduğunu ortaya koyuyor; yani bir futbolcunun potansiyeli yükseldikçe mevcut performansının da artma eğiliminde olduğu görülüyor. 
Bazı futbolcuların mevcut derecelerinin beklenenden düşük olduğu dikkat çekiyor. Bu durum, potansiyelini tam olarak gerçekleştiremeyen oyuncuları işaret etmekte. Grafikteki sıkı ve düzenli yapı, futbolcuların büyük bir kısmının potansiyellerine yakın performans sergilediğini, ancak istisnalarımda olduğunu gösteriyor.

3.2. ÇOK DEĞİŞKENLİ ANALİZ: KORELASYON MATRİSİNİN İNCELENMESİ
![image](https://github.com/user-attachments/assets/95909c8e-2e4c-4caf-9b66-f284b1230b52)
Futbolcuların özellikleri arasındaki korelasyon ilişkilerini görselleştiren bir ısı haritasıdır. Pozitif korelasyonlar (kırmızı tonlar), özelliklerin birlikte artma eğiliminde olduğunu, negatif korelasyonlar (mavi tonlar) ise ters yönde bir ilişki olduğunu göstermektedir. 
"overall_rating" ile "reactions" arasında güçlü bir pozitif ilişki (+0.86) vardır, bu da yüksek performanslı oyuncuların genelde hızlı tepki yeteneklerine sahip olduğunu işaret etmketedir. 
"standing_tackle" ile "sliding_tackle" arasında neredeyse mükemmel bir pozitif ilişki (+0.98) bulunmaktadır, bu da savunma becerilerinin bir bütün olarak değerlendirildiğini göstermketedir.

3.3. ÖZELLİKLER ARASI İLİŞKİLERİN GÖRSELLEŞTİRİLMESİ
![image](https://github.com/user-attachments/assets/87f4bb12-140e-434c-8009-241f9924aba3)
Futbolcuların her agresiflik seviyesi için oyuncuların güç dağılımı box plot ile görselleştirilmiştir. Genel olarak agresiflik seviyesi arttıkça oyuncuların güç değerlerinin de yükseldiğini işaret etmektedir. 
Daha düşük agresiflik seviyelerinde (20-50 arası), güç değerlerinde daha geniş bir aralığa sahiptir. Bu durum, agresif olmayan oyuncuların fiziksel güç açısından iyi olduklarını göstermketedir. 
Grafikte belirli agresiflik seviyelerinde yüksek olup güç değerleri düşük olan oyuncuları aykırı değerler olarak göstermektedir.

![image](https://github.com/user-attachments/assets/05ba9d56-932f-4d44-a940-35a6e6408a31)
Futbolcuların shot power (şut gücü) ve penalties (penaltı) özellikleri arasındaki ilişkiyi gösterilmiştir. Grafik, şut gücü ile penaltı yeteneği arasında pozitif bir ilişki vardır. Penaltı yeteneği yüksek olan oyuncuların şut gücü de daha yüksektir.
Düşük penaltı skorlarında (10-30 arası), şut gücü değerleri oldukça değişkendir ve medyan değerleri düşüktür. Penaltı skorları arttıkça şut gücü değerlerinin ortalaması ve medyanı da belirgin bir şekilde yükselmekte ve bu artış 30'in üzerinde daha da dikkat çekici hale gelmektedir.
Grafikte görülen aykırı değerler, düşük penaltı skoruna sahip bazı oyuncuların yüksek şut gücüne sahip olabileceğini göstermektedir.

![image](https://github.com/user-attachments/assets/5f82bbb7-b674-4885-9cc5-588fc9334b67) 
Futbolcuların agility (çeviklik) ve stamina (dayanıklılık) özellikleri arasındaki ilişkiyi göstermektedir. Grafikte genel olarak pozitif bir ilişki görülmektedir.
Çeviklik seviyesi arttıkça dayanıklılık seviyesinin de artma eğiliminde olduğu görülmektedir. Fakat bu ilişki yüksek bir korelasyona sahip değildir, dağılımda belirli bir genişlik bulunmaktadır.

4. MODEL SEÇİMİ
4.1. YÖNTEM
Bu çalışmada, Overall Rating (Genel Derecelendirme) tahmini için farklı makine öğrenmesi yöntemlerinin karşılaştırmalı analizi gerçekleştirilmiştir. Kullanılan yöntemler arasında Doğrusal Regresyon (Linear Regression), XGBoost, Rastgele Orman (Random Forest), Yapay Sinir Ağları (YSA) ve Ensemble modelleri bulunmaktadır. Çalışma, her bir modelin tahmin performansını değerlendirerek hangi yöntemin daha etkili olduğunu belirlemeyi amaçlamaktadır.

4.2 KULLANILAN YÖNTEMLER VE MODELLER
4.2.1. DOĞRUSAL REGRESYON (LR):
Doğrusal Regresyon, bağımsız değişkenler ile bağımlı değişken arasındaki doğrusal ilişkilerin modellenmesinde kullanılan temel bir yöntemdir. 

4.2.2. XGBOOST:
Gradient boosting algoritmalarının bir varyantı olan XGBoost, yüksek doğruluk oranı ve hızı ile bilinir. 

4.2.3. RASTGELE ORMAN (RANDOM FOREST):
Rastgele Orman, birden fazla karar ağacının birleşiminden oluşur ve bu ağacın çıktılarının ortalamasını alarak daha kararlı tahminler sağlar.

4.2.4. YAPAY SİNİR AĞLARI (YSA):
Yapay Sinir Ağları, çok katmanlı yapıları sayesinde doğrusal olmayan ilişkileri anlamakta ve modellemekte üstün performans gösterir. Büyük veri setlerinde ve karmaşık problemlerde güçlü bir tahmin kapasitesine sahiptir.

4.2.5. ENSEMBLE MODEL:
Ensemble yöntemi, yukarıda belirtilen modellerin tahminlerini birleştirerek daha yüksek doğruluk oranlarına ulaşmayı hedefler. Çalışmada kullanılan Ensemble model, Yapay Sinir Ağları, Rastgele Orman ve XGBoost gibi güçlü modellerin çıktılarının ortalamasını alarak tahmin performansını artırmayı amaçlamaktadır.

4.3 KULLANILAN MODELLER VE PARAMETRELERİ:
Her bir model için hiperparametre optimizasyonu gerçekleştirilmiş ve en iyi parametreler belirlenmiştir.
4.3.1. RANDOM FOREST
•	Hiperparametre Aralıkları:
	n_estimators: [50, 100, 200] (Ağaç sayısı)
	max_depth: [10, 20, None] (Ağaçların maksimum derinliği)
	max_features: ['sqrt', 'log2', None] (Her ağaç için seçilecek özellik sayısı)
	min_samples_split: [2, 5, 10] (Bir düğümün bölünmesi için gereken minimum örnek sayısı)
	min_samples_leaf: [1, 2, 4] (Bir yaprak düğümünde olması gereken minimum örnek sayısı)
•	En İyi Parametreler:
 
	n_estimators: 200
	max_depth: None
	max_features: 'sqrt'
	min_samples_split: 5
	min_samples_leaf: 1
 

4.3.2. YAPAY SİNİR AĞLARI 
•	Model Yapısı:
	Katmanlar: 
	Giriş katmanı (30 düğüm) 
	1. gizli katman (64 düğüm)
	2. gizli katman (32 düğüm)
	Çıkış katmanı (1 düğüm)
	Aktivasyon Fonksiyonu: ReLU (Rectified Linear Unit)
•	Optimizasyon Süreci:
	Kayıp Fonksiyonu: Mean Squared Error (MSELoss)
	Optimizasyon Algoritması: Adam
	Öğrenme Oranı (Learning Rate): 0.01
	Epoch Sayısı: 1000
•	En İyi Parametreler:
 
	Learning Rate: 0.01
	Epochs: 1000
	Optimizer: Adam
	Loss Function: MSELoss
	Layer Sizes: [30, 64, 32, 1]
 

4.3.3. XGBOOST
•	Hiperparametre Aralıkları:
	n_estimators: [50, 100, 200] (Ağaç sayısı)
	max_depth: [3, 6, 10] (Ağaçların maksimum derinliği)
	learning_rate: [0.01, 0.1, 0.2] (Aşamalı öğrenme oranı)
	subsample: [0.8, 1.0] (Eğitimde kullanılacak örnek oranı)
	colsample_bytree: [0.8, 1.0] (Her ağaç için kullanılacak özellik oranı)
•	En İyi Parametreler:
 
	n_estimators: 200
	max_depth: 6
	learning_rate: 0.1
	subsample: 1.0
	colsample_bytree: 0.8
 


Random Forest, optimum ağaç sayısı ve derinlik parametreleriyle genelleme başarısını artırmıştır.
Yapay Sinir Ağları, karmaşık veri yapılarını öğrenmede üstün performans göstermiştir.
XGBoost, hızlı çalışması ve optimize edilmiş hiperparametreleriyle dengeli bir model sunmuştur.




5. MODEL METRİKLER VE TEST HATASI
5.1 ÇALIŞMADA KULLANILAN PERFORMANS METRİKLERİ:
RMSE (Kök Ortalama Kare Hatası):
•	Gerçek ve tahmin edilen değerler arasındaki hata büyüklüğünü ölçer.
•	Yorum: Daha düşük RMSE, modelin tahmin doğruluğunun yüksek olduğunu gösterir.
RRMSE:
•	RMSE değerinin gerçek değerlerin ortalamasına oranıdır.
•	Yorum: Modelin hata oranını nispi olarak değerlendirmek için kullanılır.
SDR (Standard Deviation Ratio):
•	Tahmin edilen değerlerin standart sapmasının, gerçek değerlerin standart sapmasına oranıdır.
•	Yorum: Modelin değişkenlik düzeyini analiz eder.
CV (Varyasyon Katsayısı):
•	Gerçek değerlerin standart sapmasının ortalamaya oranıdır.
•	Yorum: Değişkenlik düzeyini yüzdelik olarak değerlendirir.
MAPE (Ortalama Mutlak Yüzde Hatası):
•	Gerçek ve tahmin edilen değerler arasındaki ortalama yüzde hatasını ölçer.
•	Yorum: Tahmin hatasının yüzdelik olarak ne kadar büyük olduğunu gösterir.
MAD (Ortalama Mutlak Sapma):
•	Gerçek ve tahmin edilen değerler arasındaki mutlak hatanın ortalamasıdır.
•	Yorum: Model hatasının ortalama büyüklüğünü ölçer.
R² (R-Kare):
•	Modelin açıklayabildiği varyansın toplam varyansa oranıdır.
•	Yorum: Modelin ne kadar iyi bir uyum sağladığını ölçer. Yüksek R², modelin daha iyi performans gösterdiğini belirtir.
Adjusted R² (Düzeltilmiş R-Kare):
•	R² değerinin değişken sayısı göz önünde bulundurularak düzeltilmiş halidir.
•	Yorum: Özellikle çoklu değişken içeren modellerde, aşırı uyumun (overfitting) etkisini azaltmak için kullanılır.
AIC (Akaike Bilgi Kriteri):
•	Modelin uyumu ile karmaşıklığı arasındaki dengeyi ölçer. Daha düşük AIC değeri, daha iyi bir model seçimini işaret eder.
•	Yorum: Model performansını ve parsimoni (sadelik) düzeyini değerlendirir.
CAIC:
•	AIC’nin düzeltilmiş bir versiyonudur ve daha büyük veri setleri için uygundur.
•	Yorum: Model seçiminde cezalandırma faktörünü artırarak karmaşık modelleri sınırlamayı amaçlar.



5.2 EĞİTİM
![image](https://github.com/user-attachments/assets/3421f8df-618b-4d46-86d0-87a4fd94e071)

5.3 TEST 
![image](https://github.com/user-attachments/assets/c3f14d98-9524-43e2-beb0-aea955be0e7f)
5.3 PERFORMANS DEĞERLENDİRMESİ VE SONUÇLAR
RMSE:
Yapay Sinir Ağlarının eğitim setindeki RMSE değeri (0.1451), Random Forest ve Ensemble'den biraz daha yüksek olmasına rağmen test setindeki RMSE değeri (0.1738), Ensemble (0.1815) ve XGBoost (0.1926) gibi modellerden daha düşük olup, genelleme performansının güçlü olduğunu kanıtlamaktadır. 
Yapay Sinir Ağlarının hem eğitim hem de test setinde tutarlı bir hata oranı sergilediğini göstermektedir.

R²:
Eğitim setinde Yapay Sinir Ağlarının eğitim R² (0.9788) değeri Random Forest (0.9912) ve Ensemble (0.9869) daha daha düşüktür. Test setinde ise Yapay Sinir Ağlarının R² değeri (0.9705) en yüksek açıklama gücüne sahiptir.
Random Forest eğitim setinde R² (0.9912) sonucu elde ederken test setinde (0.9591) elde edilmiştir. Eğitim ve test seti arasındaki R² farkı diğer modellerden daha fazla çıkmaktadır. Bu durum az da olsa overfitting riskine işaret edebilir.
Linear Regression(LR) modeli ise hem eğitim setinde R² (0.8499) hem de test setinde R²(0.8571) diğer modellere kıyasla en düşük açıklama gücüne sahiptir. 

MAPE:
Eğitim setinde Yapay Sinir Ağlarının yüzde hata oranı (30.63), Random Forest ve Ensemble modellerine kıyasla biraz daha yüksektir. Test setinde ise Yapay Sinir Ağlarının MAPE değeri (39.99), Ensemble (45.35) ve diğer modellere kıyasla daha düşüktür. Bu durum, Yapay Sinir Ağlarının test setinde diğer modellere kıyasla öne çıktığını göstermektedir.

AIC ve CAIC:
Eğitim setinde Yapay Sinir Ağlarının AIC (-55391) ve CAIC (-55125) değerleri, veri setine uyum sağlama açısından tatmin edici olsa da Ensemble ve Random Forest modelleri kadar güçlü değildir. 
Test setinde de benzer şekilde Yapay Sinir Ağlarının AIC (-12505) ve CAIC (-12282) değerleri, genelleme başarısının güçlü olduğunu ancak uygunluk açısından diğer modellerin gerisinde kalmaktadır.



En iyi eğitim ve test setinde dengeli ve yüksek sonuç veren model Yapay Sinir Ağlarıdır. Bağımlı değişken üzerindeki etkileri iyi öğrenip genelleme yapabildiğini göstermektedir.
En düşük genelleme yeteneğine sahip model ise geleneksel yöntemlerden biri olan Linear Regression(LR) modelidir.

6. YAPAY SİNİR AĞLARI DETAYLI DEĞERLENDİRME
6.1 STANDARTLAŞTIRILMIŞ VE STANDARTLAŞTIRILMAMIŞ VERİ TEST PERFORMANSLARINI KARŞILAŞTIRILMASI
Yapay Sinir Ağlarının standartlaştırılmış ve standartlaştırılmamış veri kullanılarak eğitim ve test performanslarını karşılaştırdık.
![image](https://github.com/user-attachments/assets/7532b979-7201-4bfb-9cb0-bf88c7e754c1)
	Standartlaştırılmış veri ile model hem eğitim hem de test setlerinde daha düşük RMSE değerleri (Eğitim: 0.1451, Test: 0.1738) ve daha yüksek R² değerleri (Eğitim: 0.9788, Test: 0.9705) elde ederek daha iyi bir performans sergilemiştir. 

	Standartlaştırılmamış veri ile modelin hata oranları (RMSE: Eğitim: 1.8148, Test: 1.8291) ve MAPE değerleri (Eğitim: 2.0861, Test: 2.1093) oldukça yüksektir, bu da modelin genelleme yeteneğinin zayıfladığına işaret etmektedir. AIC ve CAIC değerleri de standartlaştırılmamış veri kullanıldığında daha yüksektir, bu durum model uygunluğunun düştüğünü göstermektedir.
Standartlaştırmanın modelin doğrusal olmayan ilişkileri öğrenme kapasitesini artırdığını göstermektedir.



6.2 STANDARTLAŞTIRILMIŞ VE STANDARTLAŞTIRILMAMIŞ VERİ TEST GERÇEK VE TAHMİN DEĞERLERİ

Yapay Sinir Ağlarının standartlaştırılmamış veri ile elde edilen grafikler:
![image](https://github.com/user-attachments/assets/3931fbc9-c892-4eeb-bc8e-f8194c63b742) ![image](https://github.com/user-attachments/assets/dd2e785f-19a4-44bf-9e3c-c849241fe4e2)

Yapay Sinir Ağlarının standartlaştırılmış veri ile elde edilen grafikler:
![image](https://github.com/user-attachments/assets/fa87f18d-7427-4f4a-842e-f3916d3239ce) ![image](https://github.com/user-attachments/assets/2fa10eab-e341-405e-99f5-7c5977f875f0)

	Standartlaştırma ile tahminler daha dar bir dağılım sergilemiş ve gerçek değerlerle daha iyi örtüşmüştür.
	İkinci grafikte, tahminler doğrusal çizgiye çok daha yakın bir dağılım göstermiştir.
Standartlaştırılmış veri kullanımı, Yapay Sinir Ağlarının tahmin doğruluğunu ve genelleme kapasitesini önemli ölçüde artırmıştır.



