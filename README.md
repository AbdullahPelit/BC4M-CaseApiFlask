# BC4M-CaseApiFlask

#DOCKERFILE anlatımı

Hangi sistemden kuracağımızı söylüyoruz. kullanılan sisteme göre ubuntu şeklinde de girdiler olabiliyor.\
FROM python:3.9.7\
// mkdir yeni bir dizin oluşturmaya yarar // -p (parents) yoksa gerekli dizinleri oluşturur varsa hata döndürmez.\
RUN mkdir -p /usr/src/app\
/mevcut çalışma dizinini tanımlıyor \
WORKDIR /usr/src/app\
//  /usr/src/app/ dizinindeki app.py ı kopyalıyor\
COPY app.py /usr/src/app/\
//  /usr/src/app/ dizinindeki requirements.txt i kopyalıyor\
COPY requirements.txt /usr/src/app/\
// dizindeki her şeyi kopyalıyor\
COPY . ./\
// requirements.txt içinde belirttiğimiz gereksinimleri yüklememize yarıyor(flask,request gibi) // requirements.txt proje başlamadan ihtiyacımız olan gereksinimleride kolaylıkla yüklememize yardımcı olur.\
RUN pip install -r requirements.txt\
// Belirli bir yürütülebilir dosya olduğundan dolayı Entrypoint tercih ettik. Docker runa parametra ve ya komut girerek entrypoint i geçersiz kılamayız.\
ENTRYPOINT [ "python3", "app.py" ] (Exec Form tipinde bir yazım.)\
/portu belirtiyoruz.\
EXPOSE 5000\

#KONTEYNIRLASTIRMA SURECI

1)Öncelikle CMD de Uygulamanın bulundugu klasöre geliyoruz.\
2)image oluşturmak için "docker build -t test_bestcloud ." yazıyoruz. // t nin anlamı tag yani bir isim veriyoruz imageimize // sonda koydugumuz . ise yerel lokasyonda çalıştırmak istediğimiz anlamına geliyor.\
3)docker images yazarak image'imizi kontrol ediyoruz.\
4)"docker run -d -p 5000:5000 --name test_bestcloud_container test_bestcloud" ile imageimizi konteynırlaştırıyoruz. \
//-d =>  detached mode anlamına geliyor. Arka planda çalıştırır ve kimliği yazdırır.\
//-p => --publish konyetnırın portunu hostta yayınlar. \
//5000:5000 ilk 5000 target(hedefi) yani konteynırın içindeki port ikincisi ise yayınlacak portu veriyor\
//--name konteynıra isim verir.\
// son parametre ise imageimizin tagi.\

#docker hub

1)docker hubda repo oluştur\
2)docker tag komutuyla repodaki ismi eşle\
3)docker push username/reponame:tag(lastest gibi)\
