# FBÜ BİTİRME PROJESİ
## GNS3 ALTYAPILLI AĞ SİMÜLASYONU İLE AĞ İZLEME-YÖNETME ÜRÜNÜ

Projenin amacı, kurumsal firmaların ağ altyapılarını daha etkin bir şekilde yönetmelerini ve izlemelerini sağlayan bir çözüm geliştirmektir. Mevcut ağ yönetim araçlarının karmaşıklığını ve maliyetlerini azaltmak için, GNS3 yazılımı ile sanal ağ modellemesi yapılmakta ve SNMP ve SSH protokolleri ile izleme ve yönetim sağlanmaktadır. Python ve Django kullanılarak geliştirilen arayüz, ağ yöneticilerine ağ cihazlarının durumunu ve performansını kolayca izleme ve yönetme imkânı sunmaktadır. Bu proje, firmaların ağ altyapılarını daha güvenilir ve verimli bir şekilde yönetmelerine yardımcı olmayı hedeflemektedir. 

## Projenin Adımları
1. **GNS3 ile VMware Entegrasyonu**: GNS3 ve VMware kullanılarak ağ simülasyonu yapılması.
2. **Ağ Modelleme ve Simülasyon**: Ağ cihazlarının modellenmesi ve simülasyonu.
3. **Ağ Cihazlarının Konfigürasyonu**: Ağ cihazlarının yapılandırılması.
4. **Ağ İzleme ve Yönetim Geliştirme**: Ağ izleme ve yönetim süreçlerinin geliştirilmesi.
5. **Veri Toplama Süreci**: Veri toplama süreçlerinin uygulanması.
6. **Veritabanı Entegrasyonu**: Veritabanı ile entegrasyonun sağlanması.
7. **Veri İşleme ve Analiz**: Verilerin işlenmesi ve analiz edilmesi.
8. **Veri Görselleştirme (Arayüz Tasarımı)**: Veri görselleştirme ve kullanıcı arayüzü tasarımı.

## Geliştirilen Ağ Modeli

<img width="604" alt="image" src="https://github.com/yaseminaslann/NETWORK-MONITORING-AND-MANAGEMENT-WITH-GNS3/assets/96794119/3338e0b5-1bd8-4bc7-9d56-52766fb82927">

## Uygulama Çıktıları

**Giriş Sayfası ve Kullanıcı Giriş Sayfası**:
Giriş sayfası, kullanıcıların sisteme erişim sağladığı ilk arayüzdür.
Kullanıcı giriş sayfası, sistemin güvenliğini sağlamak ve sadece yetkili kullanıcıların sisteme erişimini temin etmek amacıyla tasarlanmış bir arayüzdür. Bu sayfa, kullanıcı adı ve şifre bilgilerini girerek doğrulama işlemi yapılmasını sağlar.

<img width="412" alt="image" src="https://github.com/yaseminaslann/NETWORK-MONITORING-AND-MANAGEMENT-WITH-GNS3/assets/96794119/0c638b4d-fb85-46c8-8a4f-9f583fdec344">
<img width="454" alt="image" src="https://github.com/yaseminaslann/NETWORK-MONITORING-AND-MANAGEMENT-WITH-GNS3/assets/96794119/45b7007a-0c6c-48aa-9890-4253d098fef7">

**Ağ İzleme Ana Sayfası**:
Ana sayfa, kullanıcıların ağın genel durumunu izleyebileceği ve yönetim görevlerini gerçekleştirebileceği merkezi bir noktadır. SNMP ve SSH protokolleri kullanılarak çekilen veriler, ağ yöneticilerine anlık bilgi sağlar ve sorunların hızlı bir şekilde tespit edilmesine yardımcı olur. Kullanıcı dostu arayüz ve grafiksel veri gösterimi, sistemin etkin bir şekilde yönetilmesini ve izlenmesini sağlar.

<img width="454" alt="image" src="https://github.com/yaseminaslann/NETWORK-MONITORING-AND-MANAGEMENT-WITH-GNS3/assets/96794119/bee5d635-513a-4cf1-9920-840953b65494">

**Cihaz Yönetim Sayfası**:
Cihaz yönetim sayfası, kullanıcıların ağ üzerindeki cihazları yönetebildiği ve izleyebildiği bir arayüzdür. Bu sayfa, cihaz ekleme, komut gönderme ve cihazları seçme gibi işlevleri içerir. Kullanıcılar, bu sayfa üzerinden ağdaki cihazlarla etkileşime geçebilir ve yönetim görevlerini gerçekleştirebilir. Komut gönderildikten sonra yeni bir sayfada istenilen veriler gösterilir.

<img width="454" alt="image" src="https://github.com/yaseminaslann/NETWORK-MONITORING-AND-MANAGEMENT-WITH-GNS3/assets/96794119/19763085-490c-47be-882a-b53f37b66df0">

**Kayıt OL Syafası**:
Bu sayfa, kullanıcıların sisteme eklenmesi gerektiğinde kullanılır ve yalnızca URL üzerinden erişilebilir. Herhangi bir yönlendirme bağlantısı bulunmamaktadır ve doğrudan erişim gerektirir.

<img width="454" alt="image" src="https://github.com/yaseminaslann/NETWORK-MONITORING-AND-MANAGEMENT-WITH-GNS3/assets/96794119/0198c423-879c-4231-b2ae-fa326b874bb6">











